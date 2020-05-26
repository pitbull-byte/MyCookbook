from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Test command that says hello'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        # to make the name argument optional use --name
        # parser.add_argument('--name', type=str)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Hello, %s ' % options['name']))
        self.stdout.write(self.style.ERROR('Hello, %s ' % options['name']))
