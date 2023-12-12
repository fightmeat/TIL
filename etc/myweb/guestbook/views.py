from django.shortcuts import render, redirect
from guestbook.models import Guestbook
# Q객체를 이용한 검색기능을 위한 모듈
from django.db.models import Q

# Create your views here.
def list(request):
    # 입력받은 검색어가 포함된 방명록을 읽어오는 작업을 수행
    try:
        searchkey = request.POST['searchkey']
    except:
        searchkey="name"

    try:
        search = request.POST['search']
    except:
        search = ""

    # db에 저장된 모든 방명록을 읽어와 화면에 뿌려주는 작업
    # gbList = Guestbook.objects.order_by('-idx')
    if searchkey == "name_content": # 작성자와 글내용
        gbList = Guestbook.objects.filter(\
            Q(name__contains=search) | Q(content__contains=search)).order_by("-idx")
    elif searchkey == "name":
        gbList = Guestbook.objects.filter(name__contains=search).order_by("-idx")
    elif searchkey == "content":
        gbList = Guestbook.objects.filter(content__contains=search).order_by("-idx")

    try:
        msg = request.GET['msg']
    except:
        msg=""

    return render(request, 'guestbook/list.html',
                  {'gbList':gbList, 'gbCount':len(gbList), 'searchkey':searchkey, 'search':search, 'msg':msg})

def write(request):
    # 방명록 작성 폼으로 이동
    return render(request, 'guestbook/write.html')

def insert(request):
    # 방명록 폼에서 작성한 내용을 db에 저장하는 작업
    # 저장 후 방명록의 목록으로 이동
    row = Guestbook(name=request.POST['name'], email=request.POST['email'],
                    passwd=request.POST['passwd'], content=request.POST['content'])
    row.save()
    return redirect('/guestbook')

def passwd_check(request):
    # 글번호(idx)와 비밀번호가 일치하는지 그렇지 않은지를 판단해서 화면을 이동
    # 글목록에서 특정글(상세보기)을 선택한 후
    id = request.POST['idx']
    pwd = request.POST['passwd']
    row = Guestbook.objects.get(idx=id)
    # 비밀번호가 일치한다면
    if row.passwd == pwd:
        return render(request, 'guestbook/edit.html', {'row':row})
    else: # 비밀번호가 일치하지 않는다면
        return redirect('/guestbook/?msg=error')

def update(request):
    # 수정폼을 통해 넘어온 데이터를 다시 db에 저장하는 작업
    id = request.POST['idx']
    row = Guestbook(idx=id, name=request.POST['name'], email=request.POST['email'],
                    passwd=request.POST['passwd'], content=request.POST['content'])
    row.save()
    return redirect('/guestbook')

def delete(request):
    id = request.POST['idx']
    Guestbook.objects.get(idx=id).delete()
    return redirect('/guestbook')