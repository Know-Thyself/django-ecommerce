from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    # Reset password
    # 1. Submit email form
    path(
        'password-reset',
        auth_views.PasswordResetView.as_view(
            template_name='verification/password/password-reset.html'
        ),
        name='reset_password',
    ),
    # 2. Sending password reset email
    path(
        'password-reset-sent',
        auth_views.PasswordResetDoneView.as_view(
            template_name='verification/password/password-reset-sent.html'
        ),
        name='password_reset_done',
    ),
    # 3. Password reset link
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='verification/password/password-reset-form.html'
        ),
        name='password_reset_confirm',
    ),
    # 4. Password reset success message
    path(
        'password-reset-complete',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='verification/password/password-reset-complete.html'
        ),
        name='password_reset_complete',
    ),
]
