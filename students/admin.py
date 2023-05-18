from django.contrib import admin

#從students.models裡面有個class叫student import近來
from students.models import student

# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ("id", "stdName", "stdID", "stdSex", "stdBirth")
    # 過濾器
    list_filter = ("stdName", "stdSex")
    # 查詢功能 只能查兩種
    search_fields = ("stdName", "stdID")
    # 排序方式 用id進行排序 記得加逗號
    ordering = ("id",)

admin.site.register(student,studentAdmin)