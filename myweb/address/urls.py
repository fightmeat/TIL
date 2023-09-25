from address import views
from django.urls import path

urlpatterns = [
    # https://localhost/address 주소록목록 표시
    path('', views.home),
    # 주소록관리 : 등록, 수정, 삭제, 상세
    # https://localhost/address/write 등록폼
    path('write', views.write),
    # 등록폼에서 작성된 내용을 DB에 저장하는 작업, 목록
    path('insert', views.insert),
    # 주소록목록에서 내용을 클릭하면 상세주소보기로 이동, 수정과 삭제
    path('detail', views.detail),
    # 수정폼
    path('update', views.update),
    # 삭제 후 목록
    path('delete', views.delete),
]