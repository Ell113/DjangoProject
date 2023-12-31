from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('profile/<user>', views.PostProfile.as_view(), name='profile'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
            views.PostDetailView.as_view(),
            name='post_detail'),
    path('createNews/', views.PostCreateView.as_view(), name='post_create'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('logout/', auth_views.LogoutView.as_view(next_page='signup'), name='logout'),
]