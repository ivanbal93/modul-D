from django.urls import path
from .views import PostList, PostDetail, Search, NewPost, PostUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', Search.as_view(), name='search'),
    path('create', NewPost.as_view(), name='create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='delete'),
]