from django.urls import path

from members.views import SiteLoginView, SiteLogoutView, ProfileView, SiteRegisterView, SitePasswordChangeView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', SiteLoginView.as_view(), name='login'),
    path('register/', SiteRegisterView.as_view(), name='register'),
    path('logout/', SiteLogoutView.as_view(), name='logout'),

    path('password-change/', SitePasswordChangeView.as_view(), name='password-change'),
]
