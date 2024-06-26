from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import ParentTitle, UploadFileList, ChildTitle
from .forms import UploadFileForm

# 父標題列表視圖
@login_required
def parent_title_list(request):
    # 獲取所有父標題列表
    parent_titles = ParentTitle.objects.all()
    # 渲染父標題列表頁面，並傳遞相關數據
    return render(request, 'parent_title_list.html', {'parent_titles': parent_titles})

# 父標題詳情視圖
@login_required
def parent_title_detail(request, parent_id):
    # 獲取特定父標題對象，如果不存在則返回404錯誤
    parent_title = get_object_or_404(ParentTitle, id=parent_id)
    
    # 獲取所有父標題列表
    parent_titles = ParentTitle.objects.all()
    
    # 創建一個空的上傳文件表單實例
    form = UploadFileForm()

    if request.method == 'POST':
        # 如果請求方法是POST，則創建一個包含POST數據的表單實例
        form = UploadFileForm(request.POST, request.FILES)
        # 獲取POST數據中的child_id
        child_id = request.POST.get('child_id')
        if form.is_valid() and child_id:
            # 如果表單數據有效且存在child_id，則保存表單但不提交到數據庫
            upload = form.save(commit=False)
            # 設置上傳者為當前用戶
            upload.uploaded_by = request.user
            # 設置child為指定ID的ChildTitle對象
            upload.child = get_object_or_404(ChildTitle, id=child_id)
            # 保存上傳文件對象到數據庫
            upload.save()
            # 重新加載父標題詳情頁面
            return redirect('parent_title_detail', parent_id=parent_id)

    # 渲染父標題詳情頁面，並傳遞相關數據
    return render(request, 'parent_title_detail.html', {
        'parent_title': parent_title,
        'parent_titles': parent_titles,
        'form': form
    })

# 刪除上傳文件視圖
@login_required
def delete_upload_file(request, file_id):
    # 獲取特定的上傳文件對象，如果不存在則返回404錯誤
    file = get_object_or_404(UploadFileList, id=file_id)
    
    # 檢查當前用戶是否是文件的上傳者或具有Admin權限
    if file.uploaded_by != request.user and request.user.account_type != 'Admin':
        return HttpResponseForbidden("您沒有權限刪除此文件。")
    
    # 獲取文件所屬的父標題ID
    parent_id = file.child.sub_title.parent_title.id
    # 刪除文件對象
    file.delete()
    
    # 重新加載父標題詳情頁面
    return redirect('parent_title_detail', parent_id=parent_id)


# 編輯上傳文件視圖

@login_required
def edit_upload_file(request, file_id):
    file = get_object_or_404(UploadFileList, id=file_id)
    if file.uploaded_by != request.user and request.user.account_type != 'Admin':
        return HttpResponseForbidden("您沒有權限編輯此文件。")

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            parent_id = file.child.sub_title.parent_title.id
            return redirect('parent_title_detail', parent_id=parent_id)
    else:
        form = UploadFileForm(instance=file)

    return redirect('parent_title_detail', parent_id=file.child.sub_title.parent_title.id)