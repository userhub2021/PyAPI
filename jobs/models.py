from venv import create
from django.db import models

# Create your models here.


class JobOffer(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=60)
    job_description = models.TextField()
    salary = models.PositiveIntegerField()
    prefectures = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return super.company_name