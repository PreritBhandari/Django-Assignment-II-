from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import crud_home, profile, ProfileCreate, PostCreateView, PostUpdateView, PostDeleteView, PostListView

urlpatterns = [
    path('', crud_home.as_view(), name='crudhome'),
    path('profile/', profile.as_view(), name='profile'),
    path('createprofile/', ProfileCreate.as_view(), name='profile-create'),


    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/new/', PostCreateView.as_view(), name='post-create'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
