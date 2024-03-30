from django import forms
from .models import Author, Post, Comment


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['full_name']
        labels = {'first_name': 'Имя',
                  'last_name': 'Фамилия',
                  'email': 'Почта',
                  'bio': 'О себе',
                  'birthdate': 'Дата рождения'
                  }

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    pub_date = forms.DateField()
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField()
    views_count = forms.IntegerField(initial=0)
    is_public = forms.BooleanField(required=False)

class EditPostForm(forms.Form):
    def __init__(self, post_id, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)
        post = Post.objects.filter(pk=post_id).first()
        self.fields['title'] = forms.CharField(initial=post.title)


class CommentForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    content = forms.CharField(widget=forms.Textarea)