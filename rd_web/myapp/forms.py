from django import forms
from .models import UploadFileList

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileList
        fields = ['file_name', 'url', 'file_description', 'key']
        widgets = {
            'file_name': forms.ClearableFileInput(attrs={'required': False}),
            'url': forms.URLInput(attrs={'required': False}),
        }

    def clean(self):
        cleaned_data = super().clean()
        file_name = cleaned_data.get('file_name')
        url = cleaned_data.get('url')

        if file_name and url:
            raise forms.ValidationError('只能選擇上傳檔案或提供網址，不能同時選擇。')
        if not file_name and not url:
            raise forms.ValidationError('請選擇上傳檔案或提供網址。')
        return cleaned_data
