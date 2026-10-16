from django.contrib import admin
from django.urls import path
from Repository import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/', views.QuestionListCreate.as_view()),
    path('questions/<int:pk>/', views.QuestionRetrieveUpdateDeleteView.as_view()),
]


