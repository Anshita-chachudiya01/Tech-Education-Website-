from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import UserForm
from service.models import Service
from News.models import news
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.core.exceptions import ValidationError
import numpy as np
import joblib
import pickle


#MODEL_PATH = os.path.join(settings.BASE_DIR, "mytask", "statics", "placement_model.pk1")


model = joblib.load('statics/CS_students_career_predictor.pkl')
# Create a mapping for the predicted values
pred_mapping ={
    0: "Web Developer",                 
    1: "Information Security Analyst",    
    2: "Mobile App Developer",            
    3: "Database Administrator",          
    4: "Cloud Solutions Architect",       
    5: "Software Engineer ",              
    6: "Machine Learning Engineer",       
    7: "NLP Research Scientist "   ,      
    8: "Graphics Programmer"   ,           
    9: "Data Scientist" ,                  
    10:"AI Researcher" ,                   
    11:"Data Analyst ",                    
    12:"Game Developer ",                  
    13:"UX Designer ",                     
    14:"Bioinformatician ",                
    15:"Healthcare IT Specialist ",        
    16:"Quantum Computing Researcher",     
    17:"Geospatial Analyst ",             
    18:"Data Privacy Specialist",          
    19:"SEO Specialist ",                  
    20:"Distributed Systems Engineer",     
    21:"Blockchain Engineer",              
    22:"VR Developer ",                    
    23:"Digital Forensics Specialist ",    
    24:"Machine Learning Researcher",      
    25:"NLP Engineer",                    
    26:"IoT Developer",                   
    27:"DevOps Engineer ",                 
    28:"Computer Vision Engineer",         
    29:"Robotics Engineer ",              
    30:"Embedded Software Engineer",       
    31:"Security Analyst",                 
    32:"Ethical Hacker",              
    
}





def homePage(request):
   NewsData=news.objects.all();
   ServicesData=Service.objects.all().order_by('-service_title')[2:3]

   if request.method=="POST":
        st=request.POST.get('search_box')
        if st!=None:
            ServicesData=Service.objects.filter(service_title__icontains=st)

   for a in ServicesData:
       print(a.service_icon)

       print(Service);
       print(news);
   data={
        'ServiceData':ServicesData,
        'NewsData': NewsData
        }
   return render(request,"index1.html",data)
    

 



def newsDetails(request,newsid):
    newsDetails=news.objects.get(id=newsid)
    data={
        'newsDetails':newsDetails
    }
    return render(request,"newsDetails.html",data)


def about(request):
    return render(request,"about.html")

def Course(request):
   
        

    return render(request,"Course.html")


    r

def calculator(request):
    c=''
    data={}
    try:
        if request.method == "POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            operation=request.POST.get('operation')
            if operation=="+":
                c=n1+n2
            elif operation=="-":
                c=n1-n2
            elif operation=="*":
                c=n1*n2
            elif operation=="/":
                c=n1/n2
            data={
                'n1':n2,
                'n2':n2,
                'operation':operation,
                'c':c
            }
            
    except:
        c="Invalid operation ...."




    return render(request,"calculator.html",data)

def UserForm(request):
    finalans=0
    try:    
        #n1=int(request.GET['num1'])
        #n2=int(request.GET['num2'])
    

        if request.method == "GET" :
            n1=int(request.GET.get['num1'])
            n2=int(request.GET.get['num2'])
            Finalans=n1+n2
    except:
        pass

        return render(request,"Form.html",{'output':Finalans})
    
def Submitform(request):
    return HttpResponse(request)
    


def evenodd(request):
    c=''
    
    if request.method == "POST" :
        #(manual form validattion)if request.POST.get('num1')=="":
                #return render(request,"evenodd.html",{'error':True})
        
        n=int(request.POST.get('num1'))
        if n%2==0:
           c="even"
        else:
            c="odd"


    return render(request,"evenodd.html",{'c':c})
    
    


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('homepage')  
        else:
            
            context = {'error': 'Username or password is incorrect'}
            return render(request, 'login.html', context)

    return render(request, 'login.html')
    

def registration(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'registration.html')

        
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'registration.html')

        
        if not uname.isalnum() or uname.isnumeric():
            messages.error(request, "Username must contain both letters and numbers, and it can't be purely numeric.")
            return render(request, 'registration.html')

        
        try:
            user = User.objects.create_user(username=uname, email=email, password=pass1)
            user.save()
            messages.success(request, "Account created successfully.")
            return redirect('placement')  # Redirect to login page after successful signup
        except ValidationError as e:
            messages.error(request, str(e))
            return render(request, 'registration.html')

    return render(request, "registration.html")


def placement(request):
    output = None 

    if request.method=="POST":
        try:
            Gender=int(request.POST.get("Gender",0))
            Age=int(request.POST.get("Age",0))
            GPA=float(request.POST.get("GPA",0))
            Interested_Domain=int(request.POST.get("Interested Domain",0))
            Java=int(request.POST.get("Java",0))
            Python=int(request.POST.get("Python",0))
            SQL=int(request.POST.get("SQL",0))
            

            input_Data=np.array([[Gender,Age,GPA,Interested_Domain,Java,Python,SQL]])
            

             # Ensure model is loaded before calling predict
            if "model" not in globals():
                raise ValueError("Model is not loaded")


            pred = model.predict(input_Data)

            print("prediction:",pred)

            #return render(request,'placement.html')
        
        
           # output={"output":pred}

            decoded_pred = pred_mapping.get(pred[0], "Unknown")

           
            output = f"Prediction result: {decoded_pred}"
            #output=f"output : {pred}"

        except Exception as e:
            output = f"Error: {str(e)}"  # Handle any errors

    return render(request,'placement.html',{'output':output})
#else:
#return render(request,'placement.html')



    