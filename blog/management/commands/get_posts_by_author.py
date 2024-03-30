from django.core.management.base import BaseCommand
from ...models import Author, Post


class Command(BaseCommand):
    help = "Search all posts by Author"

    def add_arguments(self, parser):
        parser.add_argument('author_name', type=str, help='Author name')

    def handle(self, *args, **kwargs):
        author_name = kwargs['author_name']
        posts = Post.objects.filter(author__first_name__icontains=author_name)
        return str(posts)
