from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name='wcclub-home'),
	path('test', views.test, name='wcclub-test'),
	path('channel', views.channel, name='wcclub-music'),
	path('about/', views.about, name='about-club'),
	path('contact', views.contact, name='contact'),
]
