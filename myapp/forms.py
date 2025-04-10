from django import forms
from .models import Article, Category, Comment

# choices = [('tech', 'Tech'), ('lifestyle', 'Lifestyle'), ('education', 'Education'), ('travel', 'Travel'), ('writing', 'Writing')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for choice in choices:
    choice_list.append(choice)

class PostForm(forms.ModelForm):
    class Meta:
       model = Article
       fields = ('title', 'author', 'category', 'content', 'date')

       widgets = {
           'title' : forms.TextInput(attrs={'class': 'form-control'}),
           'author' : forms.Select(attrs={'class': 'form-control'}),
           'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
           'content' : forms.Textarea(attrs={'class': 'form-control'}),
           'date' : forms.DateInput(attrs={'class': 'form-control'}),
       }

class EditForm(forms.ModelForm):
    class Meta:
       model = Article
       fields = ('title', 'category', 'content', 'date')

       widgets = {
           'title' : forms.TextInput(attrs={'class': 'form-control'}),
           'content' : forms.Textarea(attrs={'class': 'form-control'}),
           'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
           'date' : forms.DateInput(attrs={'class': 'form-control'}),
       }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'content', 'date_added')  
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control'}),
            'date_added' : forms.DateInput(attrs={'class': 'form-control'}),
        }