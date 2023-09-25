from django.shortcuts import render, redirect
from survey.models import Survey, Answer

# Create your views here
def main(request):
    # 설문조사 main 페이지 - 한 화면에 하나의 문항만 추출하여 표시
    # 최신 데이터 1개만 추출
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]
    return render(request, 'survey/main.html', {'survey':survey})

def save_survey(request):
    print(request.POST['survey_idx'])
    print(request.POST['num'])

    row = Answer(survey_idx=request.POST['survey_idx'], num=request.POST['num'])
    row.save()
    return render(request, 'survey/success.html')

def show_result(request):
    # 문제번호
    idx = request.GET['survey_idx']
    ans = Survey.objects.get(survey_idx=idx)
    answer = [ans.ans1, ans.ans2, ans.ans3, ans.ans4]
    # 객체명.objects.raw("query문")
    surveyList = Survey.objects.raw("""
    select survey_idx, num, count(num) sum_num, round((select count(*) 
    from survey_answer where survey_idx=a.survey_idx and num=a.num)*100.0/
    (select count(*) from survey_answer where survey_idx = a.survey_idx), 1) rate 
    from survey_answer a
    where survey_idx = %s
    group by survey_idx, num
    order by num""", idx)

    surveyList = zip(surveyList, answer)
    return render(request, 'survey/result.html', {'surveyList':surveyList})