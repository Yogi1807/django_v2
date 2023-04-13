import json
from django.shortcuts import render, get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.views import View

from jobs.models import Portal, JobDescription, Applicant, JobTitle
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError


# Create your views here.
def welcome(request):

    cricketers = ["virat", "dhoni", "Rohit", "sachin"]

    return render(
        request,
        "jobs/welcome.html",
        {"message": "Good morning", "cricketers": cricketers}

    )


def get_portal_details(request):
    """


    """
    ####################################
    # how to get url associated with django view?
    ####################################

    from django.urls import reverse

    print(reverse("portal_details"))

    objs = Portal.objects.order_by("id")
    portals = []
    for obj in objs:
        portals.append(obj.name)

    return JsonResponse(portals, safe=False)


def get_job_description(request, job_id):
    jd = get_object_or_404(JobDescription, pk=job_id)
    return render(request, "jobs/job_description.html", {"job_desc": jd})


def get_name_applicants(request,applicant_id):
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    return render(request, "jobs/registrator.html", {'applicants': applicant})


def get_jobtitles(request):
    jobtitle = JobTitle.objects.order_by("id")
    breakpoint()

    jobs = []
    for job in jobtitle:
        jobs.append(job.title)

    return JsonResponse(jobs, safe=False)


@csrf_exempt
def job_titles(request):
    """plural endpoint to get all job titles"""
    if request.method == "POST":
        data = json.loads(request.body)
        # TODO - add validation for the request data.

        portal_data = data.get("portal")
        portal_name = portal_data.get("name")
        portal = Portal.objects.filter(name=portal_name)

        if not portal:
            portal = Portal.objects.create(**portal_data)
            portal.save()
        else:
            portal = portal[0]

        jd = data.get("job_description")
        jd_role = jd.get("role")
        jd_obj = JobDescription.objects.filter(role=jd_role)

        if not jd_obj:
            jd = JobDescription.objects.create(**jd)
            jd.save()
        else:
            jd = jd_obj[0]

        data["job_description"] = jd
        data["portal"] = portal

        try:
            jt = JobTitle.objects.create(**data)
            jt.save()

        except IntegrityError:
            return JsonResponse({"ERROR": "DATA ALREADY EXIST"})

        job_titles = JobTitle.objects.all()
        return render(
            request,
            "jobs/job_titles.html",
            {"objects": job_titles})

    elif request.method == "PATCH":
        data = json.loads(request.body)
        # TODO - add validation for the request data.

        portal_data = data.get("portal")
        portal_name = portal_data.get("name")
        portal = Portal.objects.filter(name=portal_name)

        if not portal:
            portal = Portal.objects.create(**portal_data)
            portal.save()
            return HttpResponse("DATA INSERT SUCCESSFULLY")
        else:
            portal = portal.update(**portal_data)
            return HttpResponse("DATA UPDATED")

    elif request.method == "DELETE":
        data = json.loads(request.body)
        # TODO - add validation for the request data.

        portal_data = data.get("portal")
        portal_name = portal_data.get("name")
        portal = Portal.objects.filter(name=portal_name)
        breakpoint()
        if portal:
            portal.delete()
            return HttpResponse("DATA DELETED")


from django.utils.decorators import method_decorator


# Create your class based view like following -
@method_decorator(csrf_exempt, name='dispatch')
class WelcomeView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('welcome to first class based view')

    def post(self, request):

        breakpoint()

        # write your post view logic here
        return HttpResponse("welcome to POST request using class based view")

    def patch(self, request):
        # write your PATCH request logic here
        return HttpResponse("welcome to PATCH request using class based view")
