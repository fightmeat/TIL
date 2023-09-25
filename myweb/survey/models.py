from django.db import models

# 설문문제 table
class Survey(models.Model):
    survey_idx = models.AutoField(primary_key=True)
    # 문제
    question = models.TextField(null=False)
    # 답문항1~4
    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    ans4 = models.TextField(null=True)
    # 설문진행상태(y=진행중, n=종료)
    status = models.CharField(max_length=1, default='y')

# 응답한 내용을 저장할 table
class Answer(models.Model):
    # 응답식별값
    answer_idx = models.AutoField(primary_key=True)
    # 설문식별값, 외래키(foreign key)
    survey_idx = models.IntegerField()
    # 응답번호값
    num = models.IntegerField()