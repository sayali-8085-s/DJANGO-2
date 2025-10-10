from django.shortcuts import render ,redirect
from django.http import HttpResponse

# Create your views here.
def home(request ,pk):
 x =pk*10
 
 return HttpResponse(f'h{x}')

def home1(request ,pk):
 html = "<h1> this is me <h1/>"
 return HttpResponse(f'h{pk}')

def home2(request ,pk):
 return HttpResponse(f'h{pk}')

# def home3(request ):
 
#  data ={"name":"sayali" ,"age":21}
#  jdata = json.dumps(data)
#  return HttpResponse(jdata ,content_type = "application/json")

 
#  html = "<h1> this is html <h1/>"
# #  return HttpResponse("hii" ,content_type = "text/plain")

#  return HttpResponse(html ,content_type = "text/html")

def home4 (req):
 data = {"name":"sayali","age":21}
 return render(req,"home.html" ,{"data":data})
#  return render(req,"home.html" ,data)



#   REDIRECT

def home5(req):
  return redirect('home4')

     
    # return redirect('https://www.facebook.com/username')
    
