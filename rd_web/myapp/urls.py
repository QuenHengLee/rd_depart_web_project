# myapp/urls.py
from django.urls import path
from . import views

# 定義應用程式的URL模式
urlpatterns = [
    
    # 父標題列表頁面的URL模式
    path('parent_titles/', views.parent_title_list, name='parent_title_list'),
    
    # 父標題詳細頁面的URL模式，包含動態父標題ID參數
    path('parent_titles/<int:parent_id>/', views.parent_title_detail, name='parent_title_detail'),
    
    # 刪除上傳文件功能的URL模式，包含動態文件ID參數
    path('delete_upload_file/<int:file_id>/', views.delete_upload_file, name='delete_upload_file'),

    # 編輯上傳文件功能的URL模式，包含動態文件ID參數
    path('edit_upload_file/<int:file_id>/', views.edit_upload_file, name='edit_upload_file'),

]
