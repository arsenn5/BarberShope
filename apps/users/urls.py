from django.urls import path

from apps.users.views import RegisterView, LoginView, questionnaire_view, service_view

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', questionnaire_view),
    path('service/', service_view)
]
