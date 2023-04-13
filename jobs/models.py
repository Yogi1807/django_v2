from django.db import models
from django.utils import timezone


# Create your models here.
class Portal(models.Model):
    # TODO - refer
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id) + " portal - " + self.name


class JobTitle(models.Model):
    """
    JobTitle will have association with multiple portals
    `JobTitle` <--> `Portal`  (one-to-many relationship)
    `JobDescription`  <--> `JobTitle` (one-to-one relationship)
    # TODO
    # refer
    # https://docs.djangoproject.com/en/4.1/topics/db/examples/#examples-of-model-relationship-api-usage
    """

    title = models.CharField(max_length=250)
    last_updated = models.DateTimeField(default=timezone.now)

    # one-to-one relationship
    job_description = models.OneToOneField("JobDescription", on_delete=models.CASCADE)

    # one-to-many relationship
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + f"( {self.portal} )"


class JobDescription(models.Model):
    """ """

    role = models.CharField(max_length=250, default="")
    description_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.role + f"( {self.pub_date} )"


class Applicant(models.Model):
    name = models.CharField(max_length=250)

    # one-to-many relationship
    applied_for = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    cover_letter = models.CharField(max_length=250)

    def __str__(self):
        return self.name
