from django.urls import path
from api.views import (user_login, create_user, create_job, get_job)
urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', create_user, name='register'),
    path('post_job/', create_job, name='post_job'),
    path('get_job/', get_job, name='get_job')
]
