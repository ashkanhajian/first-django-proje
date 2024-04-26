from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<pk>', views.post_detail, name='post_detail'),
    path('posts/<post_id>/comment', views.post_comment, name='post_comment'),
    path('ticket', views.ticket, name='ticket'),
    path('search', views.post_search, name='post_search'),
    path('profile/', views.profile, name='profile'),
    path('profile/creatpost', views.creat_post, name='creat_post'),
    path('profile/delete_post/<post_id>', views.delete_post, name='delete_post', ),
    path('profile/editpost/<post_id>', views.edit_post, name='edit_post'),
    path('login', auth_views.LoginView.as_view(), name="login"),
    path('logout', views.log_out, name="logout")

]
