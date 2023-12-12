from django.urls import path
from member import views

urlpatterns = [
    path('', views.home),
    path('join', views.join),
    path('login', views.login_check),
    path('logout', views.logout),
]