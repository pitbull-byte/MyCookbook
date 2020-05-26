# Perform a HTTP HEAD request to see if a site is up and return a 200 OK response
# Push to GIT
import datetime

from django.contrib.sites import requests
from sitechecker.models import Site, Check
from django.core.management.base import BaseCommand, CommandError
import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('[*] Checking all sites.....')

        # Perform HTTP request on all sites
        for site in Site.objects.all():
            # site_url = 'https://www.tesla.com'
            response = requests.head(site.url)
            # TODO follow redirects
            # TODO multi-thread
            # TODO fix timezone
            self.stdout.write('Response for %s: %s' % (site.url, response.status_code))
            site.last_response_code = str(response.status_code)
            site.last_time_checked = datetime.datetime.now()

            try:
                site.save()
            except Exception as e:
                raise CommandError("Error updating site: %s - %s." % (e, site))

            try:
                new_check_entry = Check(site=site, response_code=str(response.status_code))
                new_check_entry.save()
            except Exception as e:
                raise CommandError("Error adding check: %s - %s." % (e, site))
