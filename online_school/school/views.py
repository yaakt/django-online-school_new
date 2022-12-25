from .serializers import *
from .models import *
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherListCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, serializer):
        users = Teacher.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class TeacherLookView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LogSerializer

    def create(self, request, *args, **kwargs):
        serializer = LogSerializer(data=request.data)
        serializer.is_valid()

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        try:
            user = Teacher.objects.get(username=username)
        except Exception as e:
            raise ValidationError({"400": f'Account does not exist'})
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({'user': user.username})
        else:
            raise ValidationError({"400": f'Can not find information'})


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
