from django.contrib import admin
from memo.models import Memo
# Register your models here.

class MemoAdmin(admin.ModelAdmin):
    list_display = ('writer', 'memo')

admin.site.register(Memo, MemoAdmin)