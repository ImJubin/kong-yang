from django.urls import path
from . import views

app_name="users"
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('account/', views.user_accounts, name='user-accounts'),
    path('calendar/', views.calendar_dates),
]
