from django.core.management.base import BaseCommand
from ...models import Author
from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = "Create new Author"

    def handle(self, *args, **options):
        for i in range(10):
            author = Author(
                first_name=f'Name{i+1}',
                last_name=f'Secondname{i+1}',
                email=f'Name{i+1}@Secondname.com',
                bio='. '.join(lorem_ipsum.paragraphs(5, common=False)),
                birthdate='1999-05-10'
            )
            author.full_name = author.full_name()
            author.save()
            self.stdout.write(f'{author.full_name}')