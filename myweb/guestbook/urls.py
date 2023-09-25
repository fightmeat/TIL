from django.urls import path
from guestbook import views

urlpatterns = [
    # 방명록 시작 : 방명록 목록
    path('', views.list),
    # 방명록 작성 : 폼
    path('write', views.write),
    # 방명록 저장 : db 저장
    path('gb_insert', views.insert),
    # 비밀번호 check
    path('passwd_check', views.passwd_check),
    # 수정
    path('gb_update', views.update),
    # 삭제
    path('gb_delete', views.delete),
]