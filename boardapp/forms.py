from django.db import models
from captcha.fields import CaptchaField
# Create your models here. 對應資料表
class PostForm(forms.form):
    
    
    bname = models.CharField(max_length=20, null=False)
    #bgender= models.BooleanField()
    bgender= models.BooleanField(max_length=2, default='F',null=False)
    btittle = models.CharFirld(max_length=100,null=False)
    bcontent = models.TextField(null=False)
    btime = models.DateTimeField(auto_now=True)
    bemail = models.EmailFied(max_length=100,blank=True,default='')
    # 網站回覆內容
    bresponse = models.TextField(blank=True,default='')
    captcha= CaptchaField()


    def __str__(self):
        return self.btitle
