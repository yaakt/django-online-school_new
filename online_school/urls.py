from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from online_school.school.views import *


router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
# router.register(r'teacher', TeacherViewSet)
router.register(r'group', GroupViewSet)
router.register(r'course', CourseViewSet)
router.register(r'sales', SalesViewSet)
router.register(r'goods', GoodsViewSet)

school_urls = [
    path('api/', include(router.urls))
]

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(school_urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('all-profiles/', TeacherListCreateView.as_view(), name='all-profiles'),
    path('log/', TeacherLookView.as_view(), name='log'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
