from django.db import models

# Create your models here.

class CoursesStudent(models.Model):
    title = models.CharField(max_length=100, verbose_name="название курса")
    mentor = models.CharField(max_length=50, verbose_name="ментор")
    course_date = models.DateField(verbose_name="старт")

    def __str__(self):
        return self.title

class Student(models.Model):
    firstname = models.CharField(max_length=50, verbose_name="имя")
    lastname = models.CharField(max_length=50, verbose_name="фамилия")
    phone_number = models.IntegerField(verbose_name="номер телефона")
    avatar = models.ImageField(upload_to='media/', verbose_name="аватар")
    student_course = models.ForeignKey(CoursesStudent, verbose_name="группа",
                                       on_delete=models.PROTECT,
                                       related_name='student_course')

