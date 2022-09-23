from. views import Logout_admin, about, home, contact, Login
from django.urls import path 

urlpatterns = [
   
   path('', home, name='home'),
   path('about/', about, name='about'),
   
   path('contact/', contact, name='contact'),
   path('admin_login/', Login, name='admin_login'),
   path('logout_admin/', Logout_admin, name='logout_admin'),
   
]