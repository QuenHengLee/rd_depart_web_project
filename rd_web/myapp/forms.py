from django import forms
from .models import UploadFileList, ChildTitle

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileList
        fields = ['file_name', 'file_description']

    def clean_file_name(self):
        file = self.cleaned_data.get('file_name')
        if file:
            if not file.name.endswith('.pdf'):
                raise forms.ValidationError('只允許上傳 PDF 檔案。')
            if file.size > 20 * 1024 * 1024:  # 檔案大小限制為 5MB
                raise forms.ValidationError('檔案大小不能超過 5MB。')
        return file