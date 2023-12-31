from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from tasks.views import RegistrationView , CategoryItemViewSet, LoginView, ContactItemViewSet, TaskItemViewSet

router = routers.DefaultRouter()
router.register(r"categories", CategoryItemViewSet)
router.register(r"contacts", ContactItemViewSet)
router.register(r"tasks", TaskItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', RegistrationView.as_view()),
    path('',include(router.urls))
]