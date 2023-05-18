from django import forms
#目的式產生蘭位並且給限制
class PostForm(forms.Form):                  #初始值    一定要填
    stdName = forms.CharField(max_length=50, initial='',required=True)
    stdID = forms.CharField(max_length=10, initial='',required=True)
    stdSex = forms.CharField(max_length=2, initial="M")
    stdBirth = forms.DateField()
    stdEmail =forms.EmailField(max_length=100, initial='',required=True)
    stdPhone = forms.CharField(max_length=20, initial='',required=False)
    stdAddress = forms.CharField(max_length=255, initial='',required=False)
    
