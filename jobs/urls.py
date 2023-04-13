"""minidjango_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobs.views import (
    welcome,
    get_portal_details,
    get_job_description,
    get_name_applicants,
    get_jobtitles,
    job_titles,
)
from . import views_2, views_3, views_4

urlpatterns = [
    path("admin/", admin.site.urls),
    path("welcome/", welcome, name="welcome"),

    # keyword argument `name` is passed to path function
    # these are called as named URLs
    path("portals/", get_portal_details, name="portal_details"),
    path("jobtitles/<int:job_id>", get_job_description, name="jd"),
    path("applicants/<int:applicant_id>", get_name_applicants, name="applicants"),
    path("jobtitles/", get_jobtitles, name="jt"),
    path("postjob/", job_titles, name="jobtitle"),

    # class-based views using django generic views.
    path("v2/applicants/", views_2.ApplicantList.as_view(), name="v2-applicant-list"),
    path("v2/applicants/detail/<int:pk>", views_2.ApplicantDetailView.as_view(), name="v2-applicant-detail-view"),
    path("v2/applicants/create/", views_2.ApplicantCreate.as_view(), name="v2-applicant-create"),
    path("v2/applicants/update/<int:pk>/", views_2.ApplicantUpdate.as_view(), name="v2-applicant-update"),
    path("v2/applicants/delete/<int:pk>/", views_2.ApplicantDelete.as_view(), name="v2-applicant-delete"),

    # V3 URLs (created for django-rest-framework using APIView)
    path(
        "v3/applicants/",
        views_3.Applicants.as_view(),
        name="v3_applicants_list"
    ),

    path("v3/users/",
         views_3.UserList.as_view(),
         name="v3_users_list"),

    # V4 URLs (created for job titles using DRF and serializers)
    path(
        "v4/jobtitles",
        views_4.jobtitle_list,
        name="v4_jobtitles_list"
    ),
    path(
        "v4/portals",
        views_4.portal_list,
        name="v4_portals_list"
    ),

]
