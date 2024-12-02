from django.shortcuts import render 

# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        
    #     # list.append({'name':name,'username':username,'password':password,'email':email})
    

    #     print(list)
#     return render(request,'index.html')  
# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         for i in list:
#             if username==i[1] and password==i[2]:
#                 print(i[0])
        
#     return render(request,'login.html')  