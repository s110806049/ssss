from django.shortcuts import render,redirect
from students.form import PostForm

# Create your views here.
from students.models import student


    #嘗試做.... 如果得到AAA就沒問題  不然會例外處理
def listone(request): 
    try: 
        unit = student.objects.get(stdName="郭") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "students/listone.html", locals())

def listall(request):  
    allStudents = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "students/listall.html", locals())
    
def post(request):
    #利用if
    # 判斷表單資料傳送方式
    if request.method == "POST":
        # 接收傳送資料
        mess = request.POST['stdName']
    else:
        mess = "表單資料尚未送出!"
    return render(request, "students/addstudent.html", locals())

def post1(request):
    if request.method == "POST":      #如果是以POST方式才處理
        stdName = request.POST['stdName'] #取得表單輸入資料
        stdID = request.POST['stdID']
        stdSex =  request.POST['stdSex']
        stdBirth =  request.POST['stdBirth']
        stdEmail = request.POST['stdEmail']
        stdPhone =  request.POST['stdPhone']
        stdAddress =  request.POST['stdAddress']
        #新增一筆記錄  所有資料庫物件 用creat把物件丟入
        unit = student.objects.create(stdName=stdName, stdID=stdID, stdSex=stdSex, stdBirth=stdBirth, stdEmail=stdEmail, stdPhone=stdPhone, stdAddress=stdAddress) 
        unit.save()  #寫入資料庫
        return redirect('/post1')  
    else:
        mess = '請輸入資料(資料不作驗證)'
    return render(request, "students/addstudent1.html", locals())
  
def postform(request):
    # 新增PostForm表單物件
    stdform = PostForm()
    if request.method == "POST":
        stdName = request.POST['stdName']
        stdID = request.POST['stdID']
        stdSex = request.POST['stdSex']
        stdBirth = request.POST['stdBirth']
        stdEmail = request.POST['stdEmail']
        stdPhone = request.POST['stdPhone']
        stdAddress =  request.POST['stdAddress']
        #新增一筆記錄
        unit = student.objects.create(stdName = stdName, stdID = stdID, stdSex = stdSex, stdBirth = stdBirth, stdPhone = stdPhone)
        unit.save() #寫入資料庫    
    return render(request,"students/stdform.html", locals())

#                     沒給初始值，呼叫時要給ID，有給則不用呼叫
def delete(request, stdID=None):
    if stdID!= None:
        if request.method == "POST":
            stdID = request.POST["stdID"]
        #如果發生錯誤或例外則執行except
        #嘗試try區塊程式碼，
        try:
            unit = student.objects.get(stdID=stdID)
            #刪除資料
            unit.delete()
            return redirect('/hello')
        except:
            mess = "查無資料"
    return render(request,"students/delete.html",locals())

def edit(request, stdID=None, mode=None):
    if mode == "edit":
        unit = student.objects.get(stdID=stdID)
        unit.stdName = request.GET["stdName"]
        unit.stdID = request.GET["stdID"]
        unit.stdSex = request.GET["stdSex"]
        unit.stdBirth = request.GET["stdBirth"]
        unit.stdEmail = request.GET["stdEmail"]
        unit.stdPhone = request.GET["stdPhone"]
        unit.stdAddress = request.GET["stdAddress"]
        unit.save()
        mess = "已修改完成"
        return redirect('/')
    else:
        try:
            unit = student.objects.get(stdID=stdID)
            strDate = str(unit.stdBirth)
            strDate2 = strDate.replace(" 年 ", "-")
            strDate2 = strDate.replace(" 月 ", "-")
            strDate2 = strDate.replace(" 日 ", "-")
            unit.stdBirth = strDate2
        except:
            mess = "此學號不存在"
        return render(request, "students/edit.html", locals())
