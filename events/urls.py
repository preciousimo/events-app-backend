from events import views
from django.urls import path

urlpatterns = [
    path('events/', views.EventListView.as_view()),
]
