from django.urls import path
from .views import HomeView,mail_me

app_name = "home"

urlpatterns = [ 
    path("",HomeView.as_view(),name="home"),
    path("/mail",mail_me,name='mail')
]