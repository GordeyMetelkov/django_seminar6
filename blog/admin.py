from django.contrib import admin

from .models import Author, Post, Comment

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'birthdate',]
    list_display_links = ('first_name', 'last_name')
    list_filter = ['birthdate']
    fieldsets = (('Основная информация', {'fields': ['first_name', 'last_name', 'birthdate'],
                                          'description': 'Данные пользователя',
                                          'classes': ['collapse']}),
                 ('Дополнительная информация', {'fields': ['email',]}))

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'author', 'category', 'views_count', 'is_public']
    list_display_links = ('title', 'category')
    list_filter = ['views_count', 'pub_date']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post']