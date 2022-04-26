from dataclasses import field
from rest_framework import serializers
from jobs.models import JobOffer

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = ('company_name', 'company_email', 'job_title', 'job_description', 'salary', 'prefectures',  'city', 'create_at')