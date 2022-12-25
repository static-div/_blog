
from django.urls import path
#from . import views
from .views import home_View, detail_View
urlpatterns = [
    #path('', views.home, name="home"),
    path('', home_View.as_view(), name="home"),
    path('blog/<int:pk>', detail_View.as_view(), name="post_Detail"),

]