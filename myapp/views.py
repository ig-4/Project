from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from .forms import PostForm, EditForm, Category, Comment, CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

class home(ListView):
    model = Article
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        catg_menu = Category.objects.all()
        context = super(home, self).get_context_data(*args, **kwargs)
        context["catg_menu"] = catg_menu
        return context

class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        catg_menu = Category.objects.all()
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        context["catg_menu"] = catg_menu
        data = get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes = data.total_likes()
        context["total_likes"] = total_likes
        return context

class AddPost(LoginRequiredMixin, CreateView):
    model = Article
    form_class = PostForm
    template_name = 'createblog.html'


class UpdatePost(UpdateView):
    model = Article
    form_class = EditForm
    template_name = 'updateblog.html'

class DeletePost(DeleteView):
    model = Article
    template_name = 'deleteblog.html' 
    success_url = reverse_lazy('home')

class AddCategory(CreateView):
    model = Category
    template_name = 'addcategory.html' 
    fields = '__all__'

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

def CategoryView(req, catg):
    category_posts = Article.objects.filter(category = catg)
    return render(req, 'categories.html', {'catg': catg, 'category_posts': category_posts})

def LikeView(req, pk):
    article = get_object_or_404(Article,pk=pk)
    article.likes.add(req.user)
    return redirect('article-detail', pk=pk)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})  

@login_required
def logout_view(request):
    logout(request)
    return redirect('home') 

@csrf_protect 
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})  
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})