from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ParentTitle, UploadFileList,ChildTitle
from .forms import UploadFileForm

# Create your views here.
def book_list(request):
    return render(request, 'books/book_list.html', {})

@login_required
def parent_title_detail(request, parent_id):
    parent_title = get_object_or_404(ParentTitle, id=parent_id)
    parent_titles = ParentTitle.objects.all()
    form = UploadFileForm()  # 創建一個空的表單實例

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        child_id = request.POST.get('child_id')
        if form.is_valid() and child_id:
            upload = form.save(commit=False)
            upload.uploaded_by = request.user
            upload.child_id = get_object_or_404(ChildTitle, id=child_id)
            upload.save()
            return redirect('parent_title_detail', parent_id=parent_id)

    return render(request, 'parent_title_detail.html', {
        'parent_title': parent_title,
        'parent_titles': parent_titles,
        'form': form
    })

@login_required
def parent_title_list(request):
    parent_titles = ParentTitle.objects.all()
    return render(request, 'parent_title_list.html', {'parent_titles': parent_titles})