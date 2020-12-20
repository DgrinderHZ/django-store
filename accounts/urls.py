from django.urls import path
from django.contrib.auth import views as auth_views

from .views import signup, activate_email, user_detail, edit_profile

urlpatterns = [
    path('accounts/signup/', signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/user_detail/', user_detail, name='user_detail'),
    path('accounts/edit_profile/', edit_profile, name='edit_profile'),

    path('accounts/activate/<uid>/<token>/',
         activate_email, name='activate_email'
         ),

    path('accounts/password/',
         auth_views.PasswordChangeView.as_view(
             template_name='registration/password_change.html'
         ),
         name="password_change"
         ),

    path('accounts/password/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'
         ),

    path('accounts/password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'
         ),

    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'
         ),

    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'
         ),

    path('accounts/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'
         ),
]
