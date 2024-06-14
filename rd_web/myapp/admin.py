from django.contrib import admin

from .models import ParentTitle, SubTitle, ChildTitle, UploadFileList

admin.site.register(ParentTitle)
admin.site.register(SubTitle)
admin.site.register(ChildTitle)
admin.site.register(UploadFileList)