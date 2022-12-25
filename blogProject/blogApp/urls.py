
from django.urls import path
#from . import views
from .views import home_View
urlpatterns = [
    #path('', views.home, name="home"),
    path('', home_View.as_view(), name="home"),

]