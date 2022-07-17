from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_view, name="login"),
    path('loginpage/', loginpage, name="login"),
    path('register/', register_view, name="register"),
    path('blog/', add_blog, name="blog"),
    path('blogdetail/<slug:url>', blogdetail, name="blogdetail"),
    path('deleteBlog/<slug:url>', deleteblog, name="blogdetail"),
    path('viewBlogs', viewBlogs, name="blogdetail"),
    path('logout/', logoutuser, name="logout"),
    path('search/', search, name="search"),
]

