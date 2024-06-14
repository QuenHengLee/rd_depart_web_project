from django.db import models
from django.contrib.auth.models import User

class ParentTitle(models.Model):
    id = models.AutoField(primary_key=True)
    parent_no = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class SubTitle(models.Model):
    id = models.AutoField(primary_key=True)
    sub_no = models.IntegerField()
    title = models.CharField(max_length=255)
    parent_id = models.ForeignKey(ParentTitle, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ChildTitle(models.Model):
    id = models.AutoField(primary_key=True)
    child_no = models.IntegerField()
    title = models.CharField(max_length=255)
    sub_id = models.ForeignKey(SubTitle, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UploadFileList(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=255, default="0.0")
    file_name = models.FileField(upload_to='uploads/')
    url = models.URLField(blank=True, null=True)
    file_description = models.TextField()
    child_id = models.ForeignKey(ChildTitle, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name.name if self.file_name else self.url