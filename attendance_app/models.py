from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver





class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    course_code=models.CharField(max_length=255)
    grade_n = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
     return '{} ({})'.format(self.course_name, self.course_code)
     # return self.course_name
    



class addStudent(models.Model):
   # course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
   # session_year_id=models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    student_name=models.CharField(max_length=255, default="")
    student_id=models.CharField(max_length=255, default="")
    grade_n = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    
    def __str__(self):
        return '{} ({})'.format(self.student_name, self.student_id)
        #return self.student_name

   



class student_with_course(models.Model):
    
    course_name=models.CharField(max_length=255, default="")
    student_name=models.CharField(max_length=255, default="")
 #   week = ArrayField( models.IntegerField(), default= [1,1,0,0], blank=False, size = 12)
    week1 = models.IntegerField(default=0)
    date_txt= models.TextField(blank = True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return 'Name:{} Course:{}'.format(self.student_name, self.course_name)



    
  #  if(course_id.grade_n== student_id.grade_n):

    

    











    # python manage.py migrate --run-syncdb





