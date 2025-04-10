"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import login_view, logout_view, register_view, home, ArticleDetail, AddPost, UpdatePost, DeletePost, AddCategory, CategoryView, LikeView, AddComment
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article-detail"),
    path('addpost/', AddPost.as_view(), name='add_post'),
    path('update/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('delete/<int:pk>', DeletePost.as_view(), name='delete_post'),
    path('addcategory/', AddCategory.as_view(), name='add_category'),
    path('category/<str:catg>/', CategoryView, name="category"),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('comment/<int:pk>', AddComment.as_view(), name='add_comment'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
