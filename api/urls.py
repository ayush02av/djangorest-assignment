from django.urls import path

from . import views

urlpatterns = [
	path('all/', views.get_all_tasks.as_view()),
	path('new/', views.create_new_task.as_view()),
]