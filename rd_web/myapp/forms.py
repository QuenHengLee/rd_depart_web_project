from django import forms
from .models import UploadFileList

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileList
        # 指定需要包含在表單中的模型字段
        fields = ['file_name', 'url', 'file_description', 'key']
        # 為某些字段設置小部件和屬性
        widgets = {
            'file_name': forms.ClearableFileInput(attrs={'required': False}),
            'url': forms.URLInput(attrs={'required': False}),
        }

    def clean(self):
        # 調用父類的clean方法來獲取清理後的數據
        cleaned_data = super().clean()
        # 獲取清理後的file_name和url數據
        file_name = cleaned_data.get('file_name')
        url = cleaned_data.get('url')

        # 檢查是否同時填寫了file_name和url，如果是，則引發ValidationError
        # if file_name and url:
        #     raise forms.ValidationError('只能選擇上傳檔案或提供網址，不能同時選擇。')
        # # 檢查是否file_name和url都未填寫，如果是，則引發ValidationError
        # if not file_name and not url:
        #     raise forms.ValidationError('請選擇上傳檔案或提供網址。')
        # 返回清理後的數據
        return cleaned_data
