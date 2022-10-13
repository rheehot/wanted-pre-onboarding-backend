from django.urls import path
from company.views import PostJobView

urlpatterns = [
    path("/job/post", PostJobView.as_view()),

]