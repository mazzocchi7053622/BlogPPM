from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, LikeView, AddCommentView, AddCategoryView, CategoryListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('article/edit/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('categories/<str:cats>/', CategoryView, name='categories'),
    path('like/<int:pk>/', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('category_list/', CategoryListView, name='category_list'),

]


