from django.contrib import admin
from django.db import models
from itertools import chain
from django.urls import reverse
# Create your models here.

#Courses Table Create

class Courses(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses-list")
    



class Steps(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)

    class  Meta:
        abstract = True
        ordering = ["order"]
    

    def __str__(self):
        return self.title

class Text(Steps):
    content = models.TextField(blank=True,default="")

    def get_absolute_url(self):
        return reverse("text_detail", kwargs={
            'course_id': self.course_id,
            'step_id' : self.id
            })
    


class Quizs(Steps):
    total_question = models.IntegerField(default=4)

    def get_absolute_url(self):
        return reverse("quiz_detail", kwargs={
            'course_id': self.course_id,
            'step_id' : self.id
            })
    


    class  Meta:
        verbose_name_plural = 'Quizess'