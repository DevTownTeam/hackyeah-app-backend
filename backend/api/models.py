from django.db import models

from .job_categories import JOB_CATEGORIES_CHOICES


class Technology(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Technologies'


class Location(models.Model):
    location = models.TextField()


class Company(models.Model):
    name = models.CharField(max_length=255)
    technologies = models.ManyToManyField(Technology)
    size = models.IntegerField(default=1)  # how many employees

    class Meta:
        verbose_name_plural = 'Companies'


class JobPost(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    job_category = models.CharField(choices=JOB_CATEGORIES_CHOICES, default='UN', max_length=50)
    technologies = models.ManyToManyField(Technology)
    salary = models.IntegerField(default=0)

    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date', 'name']
