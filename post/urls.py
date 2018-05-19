from django.conf.urls import url
from django.urls import path
from post.views import moderation, post_edit, post_detail, add_comment

app_name = 'post'

urlpatterns = [
    path(r'moderation/', moderation, name='moderation'),
    path(r'<int:pk>/', post_detail, name='post_detail'),
    path(r'<int:pk>/edit/', post_edit, name='post_edit'),
    path(r'comment/<int:article_id>/', add_comment, name='add_comment'),
]