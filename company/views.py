import json

from django.views import View
from django.http import JsonResponse
from django.db.models import Q

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


class JobListView(View):
    def get(self, request):
        search = request.GET.get('search')
        q = Q()

        if search:
            q &= Q(position__contains=search)
            q |= Q(company_id__name__contains=search)

        jobs = Job.objects.filter(q)

        job_list = [
            {
                "id": job.id,
                "company": job.company.name,
                "country": job.company.region.country.name,
                "region": job.company.region.name,
                "position": job.position,
                "incentive": job.incentive,
                "stack": job.stack
            }
            for job in jobs
        ]

        return JsonResponse({'results': job_list}, status=200)


class JobDetailView(View):
    def get(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
            company_jobs = [
                company_jobs.id for company_jobs in job.company.job_set.all()
            ]
            job_detail = {
                "id": job.id,
                "company": job.company.name,
                "country": job.company.region.country.name,
                "region": job.company.region.name,
                "position": job.position,
                "incentive": job.incentive,
                "stack": job.stack,
                "detail": job.detail,
                "company_jobs": company_jobs
            }

            return JsonResponse({"results": job_detail}, status=200)

        except Job.DoesNotExist:
            return JsonResponse({"MESSAGE": "NOT_EXIST"}, status=400)
