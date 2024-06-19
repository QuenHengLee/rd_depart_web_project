from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ParentTitle, SubTitle, ChildTitle, UploadFileList, CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ['account_type']}),  # 確保這是列表或元組
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ['account_type']}),  # 同樣確保這是列表或元組
    )


admin.site.register(ParentTitle)
admin.site.register(SubTitle)
admin.site.register(ChildTitle)
admin.site.register(UploadFileList)
admin.site.register(CustomUser, CustomUserAdmin)
