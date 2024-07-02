from django.urls import path

from user.views import RegistrationView, RegistrationValidationView

urlpatterns = [
    path('auth/registration/', RegistrationView.as_view()),
    path('auth/registration/validation/', RegistrationValidationView.as_view()),
]
