from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from .forms import Bookform

def book_list(request):
  books=Book.objects.all()
  return render(request,'book_list.html',{'books':books})

def book_detail(request,pk):
  book=get_object_or_404(Book,pk=pk)
  return render(request,'book_list.html',{'book':book})

def book_create(request):
  if request.method=="POST":
    form=Bookform(request.POST)
    if form.is_valid():
      book=form.save()
      return redirect('book_detail',pk=book.pk)
  else:
    form=Bookform()
  return render(request,'book_list.html',{'form':form})

def book_delete(request,pk):
  book=get_object_or_404(Book,pk=pk)
  book.delete()
  return redirect('book_list')
