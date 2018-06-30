from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r"^$", views.BlogListView.as_view(), name="blog_list_view"),
    url(r'^post/(?P<post_id>\d+)/$', views.BlogDetailView.as_view(), name='post_detail_view'),
    url(r'^post/new/$', views.NewPostView.as_view(), name='new_post_view'),
    url(r'^post/edit/(?P<post_id>\d+)/$', views.EditPost.as_view(), name='edit_post_view'),
]
