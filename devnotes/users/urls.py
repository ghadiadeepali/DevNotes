from rest_framework.authtoken import views as authtoken_view
from django.urls import path
from users import views

urlpatterns = [
    path('auth-token/', authtoken_view.obtain_auth_token),
    path('register/', views.user_registration_view)
]