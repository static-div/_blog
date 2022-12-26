
from django.urls import path
#from . import views
from .views import home_View, detail_View, post_Add, update_View
urlpatterns = [
    #path('', views.home, name="home"),
    path('', home_View.as_view(), name="home"),
    path('blog/<int:pk>', detail_View.as_view(), name="post_Detail"),
    path('create_post/', post_Add.as_view(), name="post_Create"),
   path('article/edit/<int:pk>', update_View.as_view(), name="post_Update" )
    #path('edit_post/')
]   