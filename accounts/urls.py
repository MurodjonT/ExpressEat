from django.urls import path
from .views import UserSignUpView

urlpatterns = [
	path('signup/',UserSignUpView.as_view(),name='signup'),
	]