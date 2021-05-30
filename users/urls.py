from django.urls import path, include
from users.views import UserCreationView, UserCreationDoneView, EmailConfirmView

urlpatterns = [
    # User registration urls
    path('signup/', UserCreationView.as_view(), name='sign_up'),
    path('signup/done/', UserCreationDoneView.as_view(), name='sign_up_done'),
    path('verification/<uidb64>/<token>/', EmailConfirmView.as_view(),
         name='email_confirm'),
    # Default Django auth urls
    # https://github.com/django/django/blob/main/django/contrib/auth/urls.py
    path('', include('django.contrib.auth.urls')),
]