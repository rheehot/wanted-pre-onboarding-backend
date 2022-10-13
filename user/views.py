import json

from django.views import View
from django.http import JsonResponse
from django.db.models import Q

from company.models import Apply, Job
from .models import User


class ApplyView(View):
    def post(self, request):
        try:
            apply_data = json.loads(request.body)
            user       = User.objects.get(id = apply_data["user_id"])
            job        = Job.objects.get(id = apply_data["job_id"])
            q          = Q(user_id=user.id) & Q(job_id=job.id)
            apply      = Apply.objects.filter(q)

            if not apply:
                Apply.objects.create(user_id=user.id, job_id=job.id)
                return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

            return JsonResponse({"MESSAGE": "ALREADY_APPLY"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"MESSAGE": "USER_NOT_EXIST"}, status=400)
        except Job.DoesNotExist:
            return JsonResponse({"MESSAGE": "JOB_NOT_EXIST"}, status=400)