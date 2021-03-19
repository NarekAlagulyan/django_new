from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),

    # Post handling
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/detail/<str:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/update/<str:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<str:pk>/', PostDeleteView.as_view(), name='post-delete'),

]