from django.urls import path

from accounts.views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),
]
