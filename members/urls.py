from django.urls import path

from members.views import SiteLoginView, SiteLogoutView, ProfileView, SiteRegisterView, SitePasswordChangeView, \
    SiteVerifyUser, SidebarLoginView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('sidebar-login/', SidebarLoginView.as_view(), name='sidebar-login'),
    path('login/', SiteLoginView.as_view(), name='login'),
    path('register/', SiteRegisterView.as_view(), name='register'),
    path('logout/', SiteLogoutView.as_view(), name='logout'),

    path('verify-user/', SiteVerifyUser.as_view(), name='verified_user'),

    path('password-change/', SitePasswordChangeView.as_view(), name='password-change'),
]
