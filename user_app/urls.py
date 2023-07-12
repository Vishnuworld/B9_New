from django.urls import path
from user_app import views as user_views  # alias
    
# user app urls

urlpatterns = [
    path("signup/", user_views.user_signup, name="user_signup"),
    path("login/", user_views.user_login, name="user_login"),
    path("logout/", user_views.user_logout, name="user_logout")
    ]


# split views
# urls 

# this is url for user_app





