from django.contrib import admin

from .models import ParentTitle, SubTitle, ChildTitle

admin.site.register(ParentTitle)
admin.site.register(SubTitle)
admin.site.register(ChildTitle)