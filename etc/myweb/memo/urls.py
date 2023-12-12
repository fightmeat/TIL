from memo import views
from django.urls import path

# http://localhost/memo
urlpatterns = [
    # path(request, response, name)
    path('', views.home),
    path('insert_memo', views.insert_memo),
    path('detail_memo', views.detail_memo),
    path('update_memo', views.update_memo),
    path('delete_memo', views.delete_memo),
]