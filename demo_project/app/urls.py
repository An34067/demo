from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.ServicesView.as_view()),
    path('doctor/', views.DoctorView.as_view()),
    path('new-request/', views.NewRequestView.as_view(), name='request-form'),
    path('request/', views.RequestView.as_view(), name='request-list'),
    path('new-comment/', views.AddCommentView.as_view(), name='comment-form'),

]