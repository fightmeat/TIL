from django.contrib import admin
from guestbook.models import Guestbook
# Register your models here.

class GuestbookAdmin(admin.ModelAdmin):
    # 관리자 화면에 표시할 필드 목록 적의
    list_display = ("name", "email", "passwd", "content")

admin.site.register(Guestbook, GuestbookAdmin)