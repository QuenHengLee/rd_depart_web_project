from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# 自定義用戶模型，繼承自AbstractUser
class CustomUser(AbstractUser):
    # 新增帳號類別欄位
    account_type = models.CharField(max_length=50, blank=True, null=True)

# 父標題模型
class ParentTitle(models.Model):
    id = models.AutoField(primary_key=True)  # 自動生成的主鍵
    parent_no = models.IntegerField(unique=True)  # 父標題唯一編號
    title = models.CharField(max_length=255)  # 父標題名稱
    description = models.TextField()  # 父標題描述

    def __str__(self):
        return self.title  # 返回父標題名稱

# 子標題模型
class SubTitle(models.Model):
    id = models.AutoField(primary_key=True)  # 自動生成的主鍵
    sub_no = models.IntegerField()  # 子標題編號
    title = models.CharField(max_length=255)  # 子標題名稱
    parent_title = models.ForeignKey(ParentTitle, on_delete=models.CASCADE, related_name='subtitles')  # 外鍵關聯父標題

    def __str__(self):
        return self.title  # 返回子標題名稱

    class Meta:
        # 確保每個父標題下的子標題編號唯一
        constraints = [
            models.UniqueConstraint(fields=['parent_title', 'sub_no'], name='unique_subtitle')
        ]

# 孫標題模型
class ChildTitle(models.Model):
    id = models.AutoField(primary_key=True)  # 自動生成的主鍵
    child_no = models.IntegerField()  # 孫標題編號
    title = models.CharField(max_length=255)  # 孫標題名稱
    sub_title = models.ForeignKey(SubTitle, on_delete=models.CASCADE, related_name='childtitles', null=True, blank=True)  # 外鍵關聯子標題

    def __str__(self):
        return self.title  # 返回孫標題名稱

    class Meta:
        # 確保每個子標題下的孫標題編號唯一
        constraints = [
            models.UniqueConstraint(fields=['sub_title', 'child_no'], name='unique_childtitle')
        ]

# 上傳文件列表模型
class UploadFileList(models.Model):
    id = models.AutoField(primary_key=True)  # 自動生成的主鍵
    key = models.CharField(max_length=255, default="0.0")  # 文件鍵值
    file_name = models.FileField(upload_to='uploads/', blank=True, null=True)  # 文件名（可選）
    url = models.URLField(blank=True, null=True)  # 文件URL（可選）
    file_description = models.TextField()  # 文件描述
    child = models.ForeignKey('ChildTitle', on_delete=models.CASCADE, related_name='uploadfiles')  # 外鍵關聯孫標題
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 外鍵關聯上傳者

    def __str__(self):
        # 返回文件名或URL作為字符串表示
        return self.file_name.name if self.file_name else self.url
