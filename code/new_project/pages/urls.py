
from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('account_settings', views.account_settings, name="account_settings"),

]
