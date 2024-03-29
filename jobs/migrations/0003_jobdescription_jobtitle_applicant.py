# Generated by Django 4.1.7 on 2023-03-27 16:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0002_djangodb"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobDescription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("role", models.CharField(default="", max_length=250)),
                ("description_text", models.CharField(max_length=250)),
                ("pub_date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="JobTitle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                (
                    "last_updated",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "job_description",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jobs.jobdescription",
                    ),
                ),
                (
                    "portal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jobs.portal"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Applicant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("cover_letter", models.CharField(max_length=250)),
                (
                    "applied_for",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jobs.jobtitle"
                    ),
                ),
            ],
        ),
    ]
