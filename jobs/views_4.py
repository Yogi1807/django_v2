import json
from jobs.models import JobTitle, Portal
from jobs.serializers import JobTitleSerializer, PortalSerializer, JobDescriptionSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser


def jobtitle_list(request):

    if request.method == "GET":
        job_titles = JobTitle.objects.all()

        #############################################################
        # how to serialize multiple objects using DRF serializer?   #
        #############################################################
        job_titles = JobTitleSerializer(job_titles, many=True)

        # whenever data is in non-dict format we have to set `safe=False`
        return JsonResponse(job_titles.data, safe=False)

    elif request.method == "POST":
        parser = JSONParser()
        data = parser.parse(request)

        # SAVING JOB DESCRIPTION
        # capture job description
        jd_data = data.get("job_description")
        jd_data_serializer = JobDescriptionSerializer(data=jd_data)
        breakpoint()
        # how to save record after validation check has been performed?
        jd_object = None
        if jd_data_serializer.is_valid():
            jd_object = jd_data_serializer.save()

        # SAVING PORTAL
        portal_data = data.get("portal")
        portal_serializer = PortalSerializer(data=portal_data)
        portal_obj = None
        if portal_serializer.is_valid():
            portal_obj = portal_serializer.save()

        job_title_serializer = JobTitleSerializer(data=data)
        if job_title_serializer.is_valid():
            data["job_description"] = jd_object
            data["portal"] = portal_obj
            JobTitle.objects.create(**data)   # ORM query to create job title
        return JsonResponse(job_title_serializer.data)


# TODO portals list
def portal_list(request):
    if request.method == "GET":
        portals = Portal.objects.all()
        portals_data = PortalSerializer(portals, many=True)
        breakpoint()
        ###################################################################
        # how validate serialized object against validation constraints?  #
        ###################################################################

        # SCENARIO 1 :: when you have multiple objects
        obj = PortalSerializer(data=portals_data.data, many=True)
        print(obj.is_valid())

        # To check errors (if any)
        print(obj.errors)

        # SCENARIO 2 :: when you have single object
        portal = portals[0]
        data = {"name": portal.name, "description": portal.description}
        obj = PortalSerializer(data=data)
        print(obj.is_valid())

        # To check errors (if any)
        print(obj.errors)

        return JsonResponse(portals_data.data, safe=False)
