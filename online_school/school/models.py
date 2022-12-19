from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin


class Student(AbstractUser):
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        related_name='students',
    )  # группа в которой учится студент


class Teacher(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField("password", max_length=128)
    salary = models.IntegerField(blank=True)


class Group(models.Model):
    name = models.CharField(max_length=50, blank=True)
    course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name='groups',
    )
    timetable = models.DateTimeField(blank=True)

    @property
    def amount(self):
        return self.students.count()


class Course(models.Model):
    name_c = models.CharField(max_length=50)
    created_c = models.DateTimeField(blank=True)
    teacher = models.ForeignKey(
        'Teacher',
        on_delete=models.CASCADE,
        null=True,
        related_name='courses',
    )


class Sales(models.Model):
    good = models.ForeignKey(
        'Goods',
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE,
    )


class Goods(models.Model):
    name_g = models.CharField(max_length=50)
    name_manufacture = models.CharField(max_length=60)
    price = models.IntegerField(blank=True)
