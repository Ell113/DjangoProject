from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
            views.PostDetailView.as_view(),
            name='post_detail'),
    path('createNews/', views.PostCreateView.as_view(), name='createPost'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$update/', views.PostUpdateView.as_view(), name='post_update'),
]