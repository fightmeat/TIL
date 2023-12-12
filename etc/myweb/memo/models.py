from django.db import models
from datetime import datetime
# Create your models here.

class Memo(models.Model):
    # 자동번호, pk, 일련번호
    idx = models.AutoField(primary_key=True)
    # 작성자
    writer = models.TextField(null=False)
    # 메모내용
    memo = models.TextField(null=False)
    # 작성날짜
    post_date=models.DateTimeField(default=datetime.now, blank=True)