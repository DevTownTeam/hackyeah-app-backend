from django.db import models

from .job_categories import JOB_CATEGORIES_CHOICES


class Technology(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Technologies'


class JobCategory(models.Model):
    name = models.CharField(choices=JOB_CATEGORIES_CHOICES, max_length=50)


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

    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    technologies = models.ManyToManyField(Technology)
    salary = models.IntegerField(default=0)

    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date', 'name']
