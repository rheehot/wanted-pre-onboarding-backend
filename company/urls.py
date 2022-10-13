from django.urls import path
from company.views import PostJobView, UpdateJobView

urlpatterns = [
    path("/job/post", PostJobView.as_view()),
    path("/job/<int:job_id>/update", UpdateJobView.as_view()),
    path("/job/<int:job_id>/delete", UpdateJobView.as_view()),
]
