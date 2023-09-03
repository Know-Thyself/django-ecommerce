from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path(
        'email-verification/<str:uidb64>/<str:token>/',
        views.email_verification,
        name='email-verification',
    ),
    path(
        'email-verification-sent/',
        views.email_verification_sent,
        name='email-verification-sent',
    ),
    path(
        'email-verification-failed/',
        views.email_verification_failed,
        name='email-verification-failed',
    ),
    path(
        'email-verification-success/',
        views.email_verification_success,
        name='email-verification-success',
    ),
    path('user-login/', views.user_login, name='user-login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user-logout/', views.user_logout, name='user-logout'),
    path('manage-profile/', views.manage_profile, name='manage-profile'),
    path('delete-account/', views.delete_account, name='delete-account'),
]
