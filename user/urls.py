from django.urls import path

from user.views import ApplyView

urlpatterns = [
    path("/apply", ApplyView.as_view()),
]
