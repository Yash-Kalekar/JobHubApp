from django.db import models

class job (models.Model):
    job_title = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255)
    salary = models.FloatField(null=True, blank=True)
    job_description = models.TextField()

class Meta:
    db_table = "job"
    fields = "__all__"

   # fields = "__all__"
