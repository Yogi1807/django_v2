import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Applicant, JobTitle
from .serializers import JobDescriptionSerializer, PortalSerializer, JobTitleSerializer

class ApplicantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    applied_for = JobTitleSerializer(required=True)
    cover_letter = serializers.CharField(
        max_length=250,
        required=False,
        help_text="cover letter is brief description of your interests in particular job role")


class Applicants(APIView):
    def get(self, request):
        applicants_ = Applicant.objects.all()
        applicants = [applicant.name for applicant in applicants_]
        return Response(applicants)

    def post(self, request):
        # TODO - write logic to take JSON input from `request.body`
        # TODO - write ORM query to insert record in the database
        global portal_obj, jd_obj

        applicants = request.body
        data = json.loads(applicants)
        applied_for = data.get("applied_for")
        job_d = applied_for.get("job_description")
        job_d_serializer = JobDescriptionSerializer(data=job_d)
        if job_d_serializer.is_valid():
            jd_obj = job_d_serializer.save()
        else:
            return Response({"message": job_d_serializer.errors})

        portal = applied_for.get("portal")
        portal_serializer = PortalSerializer(data=portal)
        if portal_serializer.is_valid():
            portal_obj = portal_serializer.save()
        else:
            return Response({"message": portal_serializer.errors})

        jt_serializer = JobTitleSerializer(data=applied_for)
        if jt_serializer.is_valid():
            applied_for["job_description"] = jd_obj
            applied_for["portal"] = portal_obj
            jt = JobTitle.objects.create(**applied_for)
        else:
            return Response({"Error": jt_serializer.errors})

        data["applied_for"] = jt_serializer.data
        applicant_serializer = ApplicantSerializer(data=data)
        if applicant_serializer.is_valid():
            data["applied_for"] = jt
            appli_obj = Applicant.objects.create(**data)
            return Response({"messeage": "Success"})
        else:
            return Response({"Error": applicant_serializer.errors})

        # def delete(self, request):
        #     # TODO - write logic to take json input from `request.body`
        #     # TODO - write ORM query to delete record from database.
        #     pass
###############################################
# django default authentication system        #
###############################################


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        final = dict()
        for user in users:
            final[user.id] = {"first_name": user.username,
                              "email": user.email}

        return Response(final)

