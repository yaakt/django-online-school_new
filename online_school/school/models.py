from django.db import models
from .services import calc_discount
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Student(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField("password", max_length=128, blank=True)
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE,
        related_name='students',
    )  # группа в которой учится студент


class SchoolManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("You forgot to enter email")
        if not username:
            raise ValueError("You forgot to enter username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_teacher(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, is_staff=True, is_superuser=True)


class Teacher(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    surname = models.CharField(blank=True, max_length=50, null=True)
    name = models.CharField(blank=True, max_length=50, null=True)
    salary = models.IntegerField(null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = SchoolManager()

    def __str__(self):
        return self.username


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

    def __str__(self):
        return self.name

    def discount(self):
        return calc_discount(self.price, 0.15)
