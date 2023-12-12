from django.contrib import admin
from address.models import Address
# Register your models here.

class AddressAdmin(admin.ModelAdmin):

    # 관리자 사이트에 표시할 내용을 기술(등록)
    # 등록할 필드목록은 튜플로 지정
    list_display = ('name', 'tel', 'email', 'address')

admin.site.register(Address, AddressAdmin)
