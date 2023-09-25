from django.urls import path
from shop import views

urlpatterns = [
    # 상품목록을 보여주는 역할
    path('product_list', views.product_list),
    # 상품 추가하는 폼을 호출하는 역할
    path('product_write', views.product_write),
    # 상품추가 폼에 입력된 값을 db에 저장하는 역할
    path('product_insert', views.product_insert),
    # 상품상세보기 페이지를 호출하는 역할
    path('product_detail', views.product_detail),
    # 상품수정을 위한 폼을 호출하는 역할
    path('product_edit', views.product_edit),
    # 상품 수정을 처리하는 역할
    path('product_update', views.product_update),
    # 상품 삭제를 처리하는 역할
    path('product_delete', views.product_delete),
    # 장바구니에 상품추가하는 역할
    path('cart_insert', views.cart_insert),
    # 장바구니 목록을 보여주는 역할
    path('cart_list', views.cart_list),
    # 장바구니 수정을 하는 역할
    path('cart_update', views.cart_update),
    # 장바구니 삭제를 위한 역할
    path('cart_del', views.cart_del),
    # 장바구니 비우기
    path('cart_del_all', views.cart_del_all),
]