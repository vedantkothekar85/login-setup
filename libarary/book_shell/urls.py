from django.urls import path
from .import views


urlpatterns = [
    
     path('test/',views.test, name='test'),   
    
    
    # signup urls
    path('',views.signup,name="signup"),
    path('signup_check/',views.signup_checkup,name="signup_check"),
    
    # login urls
    path('login/',views.login, name="login"),
    path('login_check/',views.login_checkup,name="login_check"),
    
    # Dashboard Urls
    path('dashboard/',views.dashboard,name="dashboard")
]
