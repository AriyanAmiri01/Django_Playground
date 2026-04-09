from django.urls import path
from . import views

# Defining a list of url patterns
urlpatterns = [
    path('' , views.getIndex, name='index'),
    path('Login/' , views.getLogin, name='login'),
    path('Docs/', views.getDocs, name='docs'),
    path('AboutMe/' , views.getAboutMe, name='about'),
    path('index_authenticated/', views.getIndexAuthenticated, name='index_authenticated')
]