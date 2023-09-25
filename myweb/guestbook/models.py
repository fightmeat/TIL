from django.db import models
from datetime import datetime
# Create your models here.

class Guestbook(models.Model):
    # 글번호
    idx = models.AutoField(primary_key=True)
    # 작성자
    name = models.CharField(null=False, max_length=50)
    # 이메일
    email = models.CharField(null=False, max_length=50)
    # 수정과 삭제를 위한 비밀번호
    passwd = models.CharField(null=False, max_length=50)
    # 내용
    content = models.TextField(null=False)
    # 작성일
    post_date = models.DateTimeField(default=datetime.now, blank=True)