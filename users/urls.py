from django.contrib.auth import views as auth
from django.urls import path
from users.views import UserCreationView, UserCreationDoneView, EmailConfirmView

urlpatterns = [
    # User creation urls
    path('signup/', UserCreationView.as_view(), name='sign_up'),
    path('signup/done/', UserCreationDoneView.as_view(), name='sign_up_done'),
    path('verification/<uidb64>/<token>/', EmailConfirmView.as_view(),
         name='email_confirm'),
    # Login and logout urls
    path('login/', auth.LoginView.as_view(), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),
    # Password change urls
    path('password-change/', auth.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/', auth.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    # Password reset urls
    path('password-reset/', auth.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]