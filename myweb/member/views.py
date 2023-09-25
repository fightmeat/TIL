from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as dlogin, logout as dlogout
from member.models import UserForm, LoginForm

# Create your views here.
## 시작페이지
def home(request):
    # 로그인을 하지 않은 상태
    if not request.user.is_authenticated:
        data = {'username':request.user, 'is_authenticated':request.user.is_authenticated}
    else: # 로그인을 한 상태
        data = {'last_login':request.user.last_login,
                'username':request.user.username,
                'password':request.user.password,
                'is_authenticated':request.user.is_authenticated}
    return render(request, 'member/index.html', {'data':data})

## 회원가입페이지
def join(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        # 입력값에 문제가 없다면(모든 유효성검사규칙을 통과했다면)
        if form.is_valid():
            # 새로운 사용자 객체를 생성한다.
            new_user = User.objects.create_user(**form.cleaned_data)
            # 로그인 처리
            dlogin(request, new_user)
            # 시작페이지로 이동
            return redirect('/member')
        else:
            return render(request, 'member/index.html', {'msg':'회원가입 실패..다시 시도해주세요'})

    else:
        # post 방식이 아닌 경우 회원가입페이지로 이동
        form = UserForm()
        return render(request, 'member/join.html', {'form':form})

# 로그인 처리
def login_check(request):
    if request.method == "POST":
        name = request.POST['username']
        pwd = request.POST['password']

        # 인증
        user = authenticate(username=name, password=pwd)
        if user is not None: # 로그인 성공
            dlogin(request, user)
            # session에 저장하는 작업
            request.session['userid'] = name
            return redirect('/member')
        else: # 로그인에 실패
            return render(request, 'member/index.html', {'msg':'로그인 실패...다시 시도하세요'})
    else: # get 방식으로 넘어온 경우 로그인 페이지로 이동
        form = LoginForm()
        return render(request, 'member/login.html', {'form':form})

def logout(request):
    # 로그아웃 처리
    dlogout(request)
    return redirect('/member')
