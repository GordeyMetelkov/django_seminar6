from django.core.management.base import BaseCommand
from ...models import Author, Post
from django.utils import lorem_ipsum
from random import randint, choice


class Command(BaseCommand):
    help = "Create new post"

    def handle(self, *args, **options):
        authors = Author.objects.all()
        for i in range(10):
            post = Post(
                title=lorem_ipsum.words(5, common=False).capitalize(),
                content='\n'.join(lorem_ipsum.paragraphs(7, common=False)),
                pub_date=f'2000-03-{randint(10, 31)}',
                author = choice(authors),
                category = choice(lorem_ipsum.WORDS).capitalize(),
            )
            post.save()
            self.stdout.write(f'{post.title}')

