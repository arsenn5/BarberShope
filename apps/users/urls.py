from django.urls import path

from .views import RegisterView, LoginView, questionnaire_view, service_view, review_view

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', questionnaire_view),
    path('service/', service_view),
    path('review/', review_view)
]
