from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ParentTitle, SubTitle, ChildTitle


# Create your views here.
def book_list(request):
    return render(request, 'books/book_list.html', {})

@login_required
def parent_title_detail(request, parent_id):
    parent_title = get_object_or_404(ParentTitle, id=parent_id)
    parent_titles = ParentTitle.objects.all()  # 傳遞所有的 ParentTitle 給模板
    return render(request, 'parent_title_detail.html', {'parent_title': parent_title, 'parent_titles': parent_titles})

@login_required
def parent_title_list(request):
    parent_titles = ParentTitle.objects.all()
    return render(request, 'parent_title_list.html', {'parent_titles': parent_titles})