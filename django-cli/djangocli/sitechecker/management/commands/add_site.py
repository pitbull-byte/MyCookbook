from sitechecker.models import Site
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Add a new site to the database'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)
        parser.add_argument('description', type=str)
        # to make the name argument optional use --name
        # parser.add_argument('--name', type=str)

    def handle(self, *args, **options):
        new_site = Site(url=options['url'], description=options['description'])

        try:
            new_site.save()
            self.stdout.write(self.style.SUCCESS("Site added: %s - %s" % (options['url'], options['description'])))
        except Exception as e:
            raise CommandError("Error adding site: %s." % e)




