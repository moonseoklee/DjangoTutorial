from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse,Http404

from .models import Item,Comment
from .forms import ItemForm,CommentsForm
from django.core.paginator import Paginator
# Create your views here.

def list(request):
    items = Item.objects.all()
    pagingItems = Paginator(items,10)
    pageNumber = request.GET.get('page')
    pagedItems = pagingItems.get_page(pageNumber)

    context =  {'items':pagedItems}
    
    return render(request,'dashboard/list.html',context)

def upload(request):
    
    if request.method == 'POST':
        itemForm = ItemForm(request.POST)
        
        if itemForm.is_valid():
            
            item = Item(title=itemForm.data['title'],contents=itemForm.data['contents'],author=request.user)
            item.save()
        
        return HttpResponseRedirect("/dashboard")

    return render(request,"dashboard/upload.html")

def detail(request,itemId):    
    if request.method == 'POST':
        commentsForm = CommentsForm(request.POST)         
        
        comments = Comment(item_id=itemId,comment=commentsForm.data['comment'],author=request.user)
        
        comments.save()

        
        return HttpResponseRedirect("/dashboard/"+str(itemId))
    
    item = get_object_or_404(Item,pk=itemId)
    return render(request,'dashboard/detail.html',context={'item':item,'comments':item.comment_set.all()})


def deleteComment(request,itemId,commentId):
    
    comment = get_object_or_404(Comment,pk=commentId)

    item = get_object_or_404(Item,pk=itemId)
    if request.method=='POST':
        comment.delete()
        return HttpResponseRedirect("/dashboard/"+str(itemId))

    return render(request,'dashboard/detail.html',context={'item':item,'comments':item.comment_set.all()})
