import json

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Applicant


class ApplicantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
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
        breakpoint()
        applicants = request.data
        name = applicants.get('name')[0]
        applied_for = int(applicants.get('applied_for')[0])
        cover_letter = applicants.get('cover_letter')[0]
        applicants = Applicant.objects.create(name=name, applied_for=applied_for,cover_letter=cover_letter)
        applicants.save()

        resp = {"message": "success", "records": ""}
        return Response(resp)

    def delete(self, request):
        # TODO - write logic to take json input from `request.body`
        # TODO - write ORM query to delete record from database.
        pass
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
