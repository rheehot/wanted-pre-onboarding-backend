import json

from django.views import View
from django.http import JsonResponse

from .models import Job


class PostJobView(View):
    def post(self, request):
        try:
            job_data = json.loads(request.body)
            id = job_data["id"]
            position = job_data["position"]
            incentive = job_data["incentive"]
            detail = job_data["detail"]
            stack = job_data["stack"]

            Job.objects.create(
                company_id=id,
                position=position,
                incentive=incentive,
                detail=detail,
                stack=stack
            )

            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)


class UpdateJobView(View):
    def post(self, request, job_id):
        try:
            job_data = json.loads(request.body)
            position = job_data["position"]
            incentive = job_data["incentive"]
            detail = job_data["detail"]
            stack = job_data["stack"]

            Job.objects.filter(id=job_id).update(
                position=position,
                incentive=incentive,
                detail=detail,
                stack=stack
            )

            return JsonResponse({"MESSAGE": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)

    def delete(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
            job.delete()

            return JsonResponse({"MESSAGE": "DELETE_SUCCESS"}, status=200)

        except Job.DoesNotExist:
            return JsonResponse({"MESSAGE": "NOT_EXIST"}, status=400)
