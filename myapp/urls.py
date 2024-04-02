from django.urls import path, include
from .views import SignUpView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("myapp/", views.myapp, name='myapp'),
    path('signup/', SignUpView.as_view(), name='signup'),
]