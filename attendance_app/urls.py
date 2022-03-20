from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.login_page, name="login"),
    
    path('home/', views.home, name="home"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('attendance/', views.attendance, name="attendance"),
    path('Students/', views.Students, name="Students"),
    path('add_course/', views.add_course, name="add_course"),
    path('add_course_save/', views.add_course_save, name="add_course_save"),
    path('merge/', views.merge, name="merge"),
    path('merge_save/', views.merge_save, name="merge_save"),
    path('add_student/', views.add_student, name="add_student"),
    path('add_student_save/', views.add_student_save, name="add_student_save"),
   
   

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

