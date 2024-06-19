from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    account_type = models.CharField(max_length=50, blank=True, null=True)  # 新增帳號類別欄位
    
class ParentTitle(models.Model):
    id = models.AutoField(primary_key=True)
    parent_no = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class SubTitle(models.Model):
    id = models.AutoField(primary_key=True)
    sub_no = models.IntegerField()
    title = models.CharField(max_length=255)
    parent_title = models.ForeignKey(ParentTitle, on_delete=models.CASCADE, related_name='subtitles')

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['parent_title', 'sub_no'], name='unique_subtitle')
        ]

class ChildTitle(models.Model):
    id = models.AutoField(primary_key=True)
    child_no = models.IntegerField()
    title = models.CharField(max_length=255)
    sub_title = models.ForeignKey(SubTitle, on_delete=models.CASCADE, related_name='childtitles', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sub_title', 'child_no'], name='unique_childtitle')
        ]


class UploadFileList(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=255, default="0.0")
    file_name = models.FileField(upload_to='uploads/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    file_description = models.TextField()
    child = models.ForeignKey('ChildTitle', on_delete=models.CASCADE, related_name='uploadfiles')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name.name if self.file_name else self.url

