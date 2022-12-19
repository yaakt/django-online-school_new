from online_school.school.serializers import *
from online_school.school.models import *
from rest_framework import viewsets
from django import http
import re
from django.db import DatabaseError
from django.shortcuts import render


from django.shortcuts import redirect
from django.urls import reverse



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

class RegisterView(viewsets.ModelViewSet):
    "" "Интерфейс регистрации отображает бизнес-логику" ""
    # 1. Получить параметры
    # 2. Проверьте параметры
    # 3. Получить данные из базы данных или хранить данные
    # 4. Вернуть данные ответа, такие как JSON

    def get(self, request):
        """
                 Вернуться в интерфейс регистрации
        :param request:
        :return:
        """
        return render(request, 'register.html')

    def post(self, request):
        """
                 1 Получить параметры
                 2 Параметры проверки
                 3 Добавить базу данных
                 4 Возврат данных
        :param request:
        :return:
        """
        # 1. Получить параметры
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        allow = request.POST.get('allow')

        if not all([username, password, password2, mobile, allow]):
            return http.HttpResponseBadRequest('Отсутствует обязательный параметр')
            # Определить, является ли имя пользователя 5-20 символов
        if not re.match(r'^[a-zA-Z0-9_]{5,20}$', username):
            return http.HttpResponseBadRequest('Пожалуйста, введите имя пользователя из 5 - 20 символов')
            # Определить, является ли пароль 8-20 цифрами
        if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
                return http.HttpResponseBadRequest('Пожалуйста, введите 8 - 20 - значный пароль')
            # Определить, соответствуют ли два пароля
        if password != password2:
                return http.HttpResponseBadRequest('Пароли, введенные дважды, противоречивы')
            # Определить, является ли номер мобильного телефона законным
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return http.HttpResponseBadRequest('Пожалуйста, введите правильный номер телефона')
            # Определить, проверять ли пользовательское соглашение
        if allow != 'on':
            return http.HttpResponseBadRequest('Пожалуйста, отметьте пользовательское соглашение')