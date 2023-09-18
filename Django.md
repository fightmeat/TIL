# Flask vs Django
- 몇가지의 기능은 Flask 방대한 기능은 Django
- IDE : Pycharm, atom, Vscode, sublinetext... 많다
- Anaconda : 포함(python), numpy, pandas, matplotlib...

# Pycharm 다운로드 및 설치
- 2022.3.3 버전 다운로드
https://www.jetbrains.com/ko-kr/pycharm/download/other.html

# 개발형식 MVC  VS  MTV

MVC pattern (이전의 웹을 개발하는 일련의 절차 또는 과정)
```
Model : 데이터를 관리할 목적으로 생성하는 객체
View : 사용자에게 보여주는 목적으로 구현하는 객체
Controller : Model과 View를 제어할 목적으로 구현하는 객체
```

MTV pattern (python 기반의 웹 개발)
```
Model : DB를 활용하지만 crud 명령어를 안쓰고 직접접근하지않는다. 우리는 그걸 orm 스타일 이라고 한다.
        db에 직접 접근하지 않고 create 명령어 delete... 그런거 이용하지 않고 class화 함수를 이용해서 데이터를 처리할 때
        우리는 모델을 사용한다.
Template : MVC의 View역할(HTML, CSS, Javascript...)
View : MVC의 Controller 역할
```
# Project 개발과정(순서)
- Web Project : myweb
- pycharm 실행후 생성(반드시 관리자 권한으로 실행해야 한다.)
  + Django Project : config
  + pycharm의 터미널에서 실행
  + django-admin  startproject config .
  + 여기서 config 띄우고 .을 찍어야 한다. 안그러면 config 안쪽에 config가 생긴다.
  + 자동으로 생성되는 manage.py : 유틸리티 파일
  + python manage.py makemigrations : 변경내용 수집
  + python manage.py migrate : 수집된 내용을 DB에 반영(commit)
  + python manage.py createsuperuser
  + id(admin), password(1234), email(생략) 등록
  + 관리자 사이트 생성 : superuser - 슈퍼유저 생성
  + 현재까지 작업을 웹에서 확인하는 작업 : 웹서버 실행 후 확인
  + python manage.py runserver localhost:80
  + localhost 대신 127.0.0.1을 써도 된다. 충돌시에는 포트번호를 바꿔준다. 
     * App Project :
     * 주소록을 관리할 목적으로 구현하는 App : address
     * python manage.py startapp address
     * address/models.py
     * 주소록을 관리할 테이블을  클래스로 정의하는 파일
     * 테이블을 새로 만ㄴ들려면 models.py와 admin.py 2개의 파일 수정
     * ORM(오브젝트 릴레이션 매핑)기법을 사용 : 테이블을 클래스로 관리하는 작업
     * 하나의 테이블은 하나의 클래스로 정의하고
     * 테이블의 컬럼은 클래스의 변수로 매핑하고
     * 테이블의 클래스는 django.db.models.Model 클래스를 상속받아 구현
     * 변수의 자료형도 django에서 미리 정의한 자료형을 사용한다.
     * 내부적으로 DB안에 app명-클래스명, address_address라는 테이블
 ```
class AddressAdmin(admin.ModelAdmin):
    # 관리자 화면에 표시할 내용을 튜플로 작성
    list_display = ('name','tel','email','address')

admin.site.register(Address, AddressAdmin)
 ```
# import 에러가 뜨면 
- window powershell을 관리자 권한으로 실행
- get-help Set-ExecutionPolicy
- Y 선택
- Set-ExecutionPolicy RemoteSigned
- A
- 하면 해결된다.

## 주소록 application
- 슈퍼 유저 : 관리자 계정
- 새로운 테이블을 생성하려면 models.py파일과 admin.py 즉, 2개의 파일을 수정해야한다.
- model.py : 테이블 정의
- admin.py : model.py에 등록한 테이블이 admin 사이트에 보이도록 처리한다.
  ```
  from address.models import Address
  class AdressAdmin(admin.ModelAdmin):
  # 관리자 화면에서 표시할 내용을 튜플로 등록
      list_display = ('name','tel','email','address')
  # idx는 등록하는것이 아니다 자동등록된다. 오라클로 치면 시퀀스라 중복처리 안되서 primary키로 동작
  # 두개의 클래스를 등록하고 연결하는 작업
  admin.site.register(Address, AdressAdmin)
  ```
```
# 처음 실행할 때만
python manage.py migrate # DB에 반영(commit)
# 그 다음부터는
python manage.py makemigrations # 변경된 내용을 수집하는 명령
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
```
## 주소록
```
class Address(models.Model):
    idx = models.AutoField(primary_key = True) # 오토필드는 자동으로 입력을 받아서 채우기
    name = models.CharField(max_length=50, black=True, null=True)
    tel = models.CharField(max_length=50, black=True, null=True)
    email = models.CharField(max_length=50, black=True, null=True)
    address = models.CharField(max_length=500, black=True, null=True)
```
- 이러면 db에 자동으로 address_address 테이블이 자동 생성된다.
- 페이지에 들어가서 /admin을 쳐주면 화면으로 들어가진다.

