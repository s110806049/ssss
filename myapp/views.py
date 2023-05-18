from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 時間函數
from datetime import datetime

import random

def students(request):
    #宣告學生資料
	std1 = {"name": "佳翰", "sid": "110806004", "age": 22}
	std2 = {"name": "睿彬", "sid": "110806001", "age": 22}
	std3 = {"name": "郭郭", "sid": "110806037", "age": 21}
	stds = [std1, std2, std3]
    #LIST包上面的變數
   
	return render(request, "std.html", locals())

def hello(request):
	# return HttpResponse("Hello World")
	return render(request, 'hello.html')

def hello1(request, username):
	now = datetime.now()
	#                                     傳遞的資料
	return render(request, 'hello1.html', locals())

# global全域變數
times = 0

def hello2(request, username):
	global times
	times = times + 1
	local_times = times
  #local區域變數 - 離開函數就沒用了
	now = datetime.now()
	dicenum1 = random.randint(1,6)
	dicenum2 = random.randint(1,6)
	dicenum3 = random.randint(1,6)
	dict1 = {"dice1": dicenum1, "dice2": dicenum2, "dice3": dicenum3}
    #將score的數值傳到後面做判斷做判斷
	score = random.randint(0,100) 
	#                                     傳遞的資料
	return render(request, 'hello2.html', locals())
  #  return render(request, 'hello2.html',{"username": "test123", "now": now, "dice1":dicenum1, "dice2": dicenum2, "dice3": dicenum3}) 
   
    #return render(request, 'hello2.html', {"username": "test123", "now": now, "dict1":dict1 }) 
    
    
	# 字典型式 
	# {"username": username, "now": datetime.now(), "dicenum1": random.randint(1,6), 
	#  "dicenum2": random.randint(1,6), "dicenum3": random.randint(1,6), 
	#  "dict1": {"dice1": dicenum1, "dice2": dicenum2, "dice3": dicenum3}}
    
    