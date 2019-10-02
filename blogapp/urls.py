#custom created

from django.contrib import admin,messages
from django.urls import path
from . import views
from .views import PostListView,CategoryDetailView,PostCreateView,PostDetailView
# from django.views.generic import list_detail
from django.contrib.auth import views as auth_views 
# . means current directory
urlpatterns = [
	# pattern with home route
# 6.    path('', views.home,name='blogapp-home'),
#5.    path('myblog/',views.myblog,name="blogapp-myblog"),
    # pattern with about route
    path('about/',views.about,name='blogapp-about'),
    ####
    # path('', views.newhome,name='blogapp-newhome'),
     # path('newhome/',views.newhome,name="blogapp-newhome"), For the method based view.
    path('',views.PostListView.as_view(),name="blogapp-newhome"),
    path('newhome/',views.PostListView.as_view(),name="blogapp-newhome"),
    # path('/',views.PostListView.as_view(),name="blogapp-newhome"),
    ###
    # path('newhome/',list_detail.object_list,all_model_dict),
    path('newhome/admin/',admin.site.urls,name="blogapp-newhome-admin"),
##ROUTES FOR CLASS BASE VIEWS
    path('newhome/new/',PostCreateView.as_view(),name='post-create'),
    # path('newhome/',views.PostListView.as_view(),name="blogapp-newhome"),
    path('newhome/<int:pk>',views.CategoryDetailView.as_view(),name="Categories-newhome"),
    path('newhome/<int:pk>/comment/',views.CommentView,name="post-comment"),
    path('newhome/<int:pk>/reply/',views.CommentView,name="comment-reply"),
    path('newhome/posts/<str:author_name>',views.AuthorPostListView.as_view(),name="author-posts-newhome"),
    path('newhome/post/<slug:slug>',views.PostDetailView.as_view(),name="post-detail-newhome"), 
    # path('newhome/<int:pk>',views.CategoryDetailView.as_view(),name="Categories-newhome"),
    

    path('newhome/search',views.search_posts,name="newhome-search-post"),
#8.    path('cookie_test',views.cookie_test,name="cookie_test"),
]