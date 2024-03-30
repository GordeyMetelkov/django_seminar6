from django.urls import path
from . import views

urlpatterns = [
    path('authors_posts/<int:author_id>/', views.authors_posts, name='authors_posts'),
    path('post/<int:post_id>/', views.read_post, name='read_post'),
    path('author_form/', views.aurhor_form, name='author_form'),
    path('post_form/', views.post_form, name='post_form'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]