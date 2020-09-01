from django.urls import path
#from .import views
from .views import Homeview, Articledetailview, Addpostview, Updatepostview, Deletepostview, \
    Addcategoryview, CategoryView, CategoryListView,LikeView, AddCommentView

urlpatterns = [
    #path('',views.home,name='home'),
    path('', Homeview.as_view(),name="home"),
    path('article/<int:pk>', Articledetailview.as_view(),name="article_detail"),
    path('add_post/', Addpostview.as_view(),name='add_post'),
    path('add_category/', Addcategoryview.as_view(),name='add_category'),
    path('article/edit/<int:pk>', Updatepostview.as_view(),name="update_post"),
    path('article/<int:pk>/remove', Deletepostview.as_view(),name="delete_post"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name="add_comment"),
]