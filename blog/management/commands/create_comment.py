from django.core.management.base import BaseCommand
from ...models import Author, Post, Comment
from django.utils import lorem_ipsum
from random import randint, choice


class Command(BaseCommand):
    help = "Create new comment"

    def handle(self, *args, **options):
        authors = Author.objects.all()
        posts = Post.objects.all()
        for i in range(10):
            comment = Comment(
                author=choice(authors),
                post=choice(posts),
                content='\n'.join(lorem_ipsum.paragraphs(3, common=False)),
                create_date=f'2000-01-{randint(10, 31)}',
                edite_date=f'2000-02-{randint(10, 28)}',
            )
            comment.save()
