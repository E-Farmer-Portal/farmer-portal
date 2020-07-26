from . import views
from django.urls import path

app_name = 'forum'
urlpatterns = [
    path('login/dashboard/forum/', views.forum, name='forum'),
]

