from django.db import models

# Create your models here.


class CoursesMentor(models.Model):
    title = models.CharField(max_length=100, verbose_name="название курса")
    mentor = models.CharField(max_length=50, verbose_name="ментор")
    course_date = models.DateField(verbose_name="старт")

    def __str__(self):
        return self.title

class Mentor(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="имя")
    last_name = models.CharField(max_length=50, verbose_name="фамилия")
    phone_number = models.IntegerField(verbose_name="номер телефона")
    avatar = models.ImageField(upload_to='media/', verbose_name="аватар")
    mentor_course = models.ForeignKey(CoursesMentor, verbose_name="группа ментора",
                                      on_delete=models.PROTECT,
                                      related_name='mentor_course')

