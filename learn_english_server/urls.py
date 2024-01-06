from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('get-listen-qsts/', views.get_listen_qsts, name='get_questions'),
    path('get-sent-build-qsts/', views.get_sent_build_qsts, name='get_sent_build_questions'),
    path('get-unseen-qsts/', views.get_unseen_qsts, name='get_unseen_qsts'),
    path('test_version/', views.test_version, name='test_version'),
]
