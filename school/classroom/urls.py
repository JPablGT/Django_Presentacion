from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.ContactFormView.as_view(), name='contact_form'),
    path('teacher/', views.TeacherCreateView.as_view(), name='create_teacher'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
]
