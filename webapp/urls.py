
from django.contrib import admin
from rest_framework import routers
from . import views
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'heroes',views.HeroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
