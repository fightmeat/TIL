# Flask vs Django
- 몇가지의 기능은 Flask 방대한 기능은 Django
- IDE : Pycharm, atom, Vscode, sublinetext... 많다
- Anaconda : 포함(python), numpy, pandas, matplotlib...

# Pycharm 다운로드 및 설치
- 2022.3.3 버전 다운로드
https://www.jetbrains.com/ko-kr/pycharm/download/other.html

# MVC  VS  MTV

MVC
```
model : ntt는 데이터만 담는  데이터베이스에 전달하는 모델로 사용되는 클래스
view : 보여주는 역할
controller : 제어하는 역할
```

MTV
```
model : crud 명령어를 안쓰고 직접접근하지않고 db만 건들인다. 우리는 그걸 orm 스타일 이라고 한다.
        db에 직접 접근하지 않고 create 명령어 delete... 그런거 이용하지 않고 class화 함수를 이용해서 데이터를 처리할 때
        우리는 **모델**이라는것을 사용한다.

template : 보여주는거 html파일존재 css존재 javascript존재 혹은 이미지들이 들어가는게 템플릿

view : 요청에 해당하는 거 보여주는거
```

# import 에러가 뜨면 
- window powershell을 관리자 권한으로 실행
- get-help Set-ExecutionPolicy
- Y 선택
- Set-ExecutionPolicy RemoteSigned
- A
- 하면 해결된다.
  
## 이후에  teminal 누르고
- django-admin startproject config .
- 여기서 config 띄우고 .을 찍어야 한다. 안그러면 config 안쪽에 config가 생긴다.

## 주소록 application
- 슈퍼 유저 : 관리자 계정
```
# 그 다음부터는
python manage.py makemigrations # 변경된 내용을 수집하는 명령
# 처음 실행할 때만
python manage.py migrate # DB에 반영(commit)
# 슈퍼유저 생성
python manage.py createsuperuser
# 아이디(admin)와 이메일주소(생략) 그리고 비밀번호(1234) 너무짧아서 y입력 
python manage.py runserver localhost:80
# 그리고 http://localhost:80/admin/ 에 들어가면 로그인창이 뜬다.
# 터미널에 ctrl + c를 누르면 서버 닫기
```
## 어플리케이션 생성
```
python manage.py startapp address
# config에서 settings.py에 INSTALLED_APPS에 address 추가
# LANGUAGE_CODE를 ko 로
# TIME_ZOME을 Asia/Seoul 로
# ctrl + s 누르면 저장
