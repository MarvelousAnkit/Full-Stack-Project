from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate ,login
from .models import Data,details,url1

def visit(request):
    return render (request,'index99.html')
def home(request):
    return render (request,'index.html')
def testimonial(request):
    if request.method=='POST':
        fname = request.POST.get('name')
        fid = request.POST.get('ids')
        furl = request.POST.get('url')
        fcountry = request.POST.get('country')
        freview = request.POST.get('review')
        tea = details(name=fname,image=furl,country=fcountry,review=freview,ids=fid)
        tea.save()
    datas = details.objects.all()
    return render (request,'admin.html',{'data':datas})
def delete(request):
    
    dels = request.GET['id']
    print(dels)
    details.objects.filter(ids=dels).delete()
    return redirect('testimonial')
def send(request):
    dels = request.GET['id']
    countryy = imagee = 'Not_Available'
    for data in details.objects.filter(ids=dels):
        countryy= data.image
        imagee = data.country
        print(imagee)
    return render(request,'changes.html',{'name':dels,'country':countryy,'image':imagee})
def update(request):
    if request.method == 'POST':
        
        idss = request.POST.get('named')
        
        eimage = request.POST.get('url')
        ename = request.POST.get('names')
        ecountry = request.POST.get('country')
        ereview = request.POST.get('review')
        print(idss,'id hai re')
        
        # Check if the ID is not None before updating the object
        if idss is not None:
            details.objects.filter(ids=idss).update(image=eimage, country=ecountry, review=ereview,name=ename)
            return redirect('testimonial')
    
    # Handle the case where the request method is not POST or the ID is None
    return render(request, 'changes.html')
# def pic(request):

#     if request.method=="POST":
#         try:
#             action_type = request.POST.get('type')
#             if action_type == 'pay':
#             # Handle testimonial logic
#                 print('i')
#             # ...
                

    
#             furls=request.POST.get('urls')
#             tea = url1(urls=furls)
#             tea.save()
#         except Exception as e:
#             print(e)
    
    
#     data = url1.objects.all()
#     return render (request,'admin.html',{'data':data})



def about(request):
    return render (request,'about.html')
def Myaccount(request):
    return render (request,'indexcopy.html')
def travel(request):
    return redirect('https://www.makemytrip.com/flights/')
def signup(request):
    
    if request.method=='POST':
        femail = request.POST.get('email')
        fpass = request.POST.get('password')
        coffee = Data(email=femail,password=fpass)
        coffee.save()
        return render (request , 'index.html')


    return render (request , 'signup.html')
def login(request):
    if request.method == "POST":
        femail = request.POST.get('email')
        fpass = request.POST.get('password')
        users = Data.objects.filter(email=femail, password=fpass)

        
        
        if users.exists():
            user = users.first()
    # login with user object directly
            return redirect('myaccount')
        else:
            return HttpResponse("not found")
    return render(request, 'login.html')
# Create your views here.
