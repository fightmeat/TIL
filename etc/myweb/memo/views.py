from django.shortcuts import render,redirect
from memo.models import Memo

# Create your views here.
def home(request):
    # 기존에 등록된 모든 방명록을 읽어와 화면에 출력하는 작업
    memoList = Memo.objects.order_by('-idx')
    return render(request, 'memo/list.html', {'memoList':memoList, 'memoCount':len(memoList)})

def insert_memo(request):
    memo = Memo(writer=request.POST['writer'], memo=request.POST['memo'])
    memo.save()
    return redirect('/memo')

def update_memo(request):
    id = request.POST['idx']
    memo = Memo(idx=id, writer=request.POST['writer'], memo=request.POST['memo'])
    memo.save()
    return redirect('/memo')

def detail_memo(request):
    id = request.GET['idx']
    row = Memo.objects.get(idx=id)
    return render(request, 'memo/detail.html', {'row':row})

def delete_memo(request):
    id = request.POST['idx']
    Memo.objects.get(idx=id).delete()
    return redirect('/memo')