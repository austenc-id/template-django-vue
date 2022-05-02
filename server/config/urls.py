from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.models import UserViewSet
from users.auth import LoginView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('user/login/', LoginView.as_view())
]
