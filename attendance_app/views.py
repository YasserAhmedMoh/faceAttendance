from email.policy import default
import imp
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
import datetime , calendar
from django.contrib.auth.views import LoginView
from attendance_app.models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage
from django.conf import settings
from attendance_app.forms import *
#from attendance_app.Smart_Attendence_System.add_students import add


# Create your views here.
@login_required
def home(request):
    stu = addStudent.objects.all()
    cou = Courses.objects.all()
    
    n = datetime.datetime.now()
    date = str(n)[0:10] 
    time = str(n)[11:19]
    context = {
        'dat' : date ,
        'tim' : time ,
    }
    
    #custom_model = add(first_time=True)
    

    if request.method == "POST":
        student=request.POST.get('student')
        course=request.POST.get('course')
        
       # week_number=request.POST.get('week_number')
       # student_with_course.objects.filter(student_name=student,course_name=course).save(week1=1)
        #s_w_c_model=student_with_course.objects.get(student_name=student,course_name=course)
        
        #s_w_c_model.date_txt += datetime.datetime.now().strftime("%Y-%m-%d ") + " , " 
        #s_w_c_model.week1 +=1
        #s_w_c_model.save()
        

        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()

        
        #return render(request, "attendance_app/Home.html",{"stu":stu, "cou":cou})
    #return render(request, "attendance_app/Home.html",{"stu":stu, "cou":cou})
    return render(request, "attendance_app/Home.html",{"form":form})



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
            
        else:
            # Return an 'invalid login' error message.
            return render(request, "attendance_app/login.html",{
                        "message":"wrong username or password"
                    })
    context = {}
    return render(request, "attendance_app/login.html", context)
    
@login_required
def attendance(request):
    merge_data = student_with_course.objects.all()
    course_name = Courses.objects.all()
    if request.method!="POST":
        return render(request, "attendance_app/attendance.html",{"merge_data":merge_data,"course_name":course_name })
    else:
        course=request.POST.get("course")
        merge_data = student_with_course.objects.filter(course_name=course)
        return render(request, "attendance_app/attendance.html",{"merge_data":merge_data,"course_name":course_name })

    

#def attendance_save(request):
    

@login_required
def Students(request):
    student_count=addStudent.objects.count()
    course_count=Courses.objects.count()
    student_data = addStudent.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Students')
    else:
        form = DocumentForm()
  #  get_grade=request.POST.get("apear_by_grade")
  #  student_data = addStudent.objects.filter(grade_n=get_grade)
    
    return render(request, "attendance_app/Students.html",{"student_count":student_count ,"course_count":course_count,"student_data":student_data, 'form': form  })


@login_required
def add_course(request):
    return render(request, "attendance_app/add_course.html")

@login_required
def add_course_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        course=request.POST.get("course")
        
        grade=request.POST.get("grade")
        
        try:
            
            course_model=Courses(course_name=course, grade_n=grade)
            course_model.save()
            messages.success(request,"Successfully Added Course")
            return HttpResponseRedirect(reverse("add_course"))
        except Exception as e:
            print(e)
            messages.error(request,"Failed To Add Course")
            return HttpResponseRedirect(reverse("add_course"))

@login_required
def add_student(request):
    return render(request, "attendance_app/add_student.html")

@login_required
def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        student=request.POST.get("student")
        
        grade=request.POST.get("grade")
        
        
        #images = request.FILES.getlist('images')
        try:
            
            student_model=addStudent(student_name=student , grade_n=grade)
            student_model.save()

            #photo_model=photos(File=request.FILES.get('images'))
            #photo_model.save()
            #for f in file_images:
            #    photoname=f.name.rsplit('.', 1)[0]
            #    photos.objects.create(name=student,File=f)
                
                #fss = FileSystemStorage()
                #filename = fss.save(getfile.name, getfile)
                #uploaded_file_url = fss.url(filename)
            
            
            messages.success(request,"Successfully Added Student")
            return HttpResponseRedirect(reverse("add_student"))
        except Exception as e:
            print(e)
            messages.error(request,"Failed To Add Student")
            return HttpResponseRedirect(reverse("add_student"))

@login_required
def merge(request):
    stu = addStudent.objects.all()
    cou = Courses.objects.all()
    s_c = student_with_course.objects.all().order_by("student_name")
    return render(request, "attendance_app/merge.html",{"stu":stu, "cou":cou,"s_c":s_c})
    
@login_required
def merge_save(request):
    #stu = addStudent.objects.all()
    #cou = Courses.objects.all()
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        student=request.POST.get("student")
        course=request.POST.get("course")
        print("******************************************************************************************")
        try:
            merge_model=student_with_course(course_name=course,student_name=student)
            merge_model.save()
            messages.success(request,"Successfully Added merge")
            return HttpResponseRedirect(reverse("merge"))
        except Exception as e:
            print(e)
            messages.error(request,"Failed To Add merge")
            return HttpResponseRedirect(reverse("merge"))


