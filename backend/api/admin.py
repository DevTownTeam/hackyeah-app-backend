from django.contrib import admin

from . import models


admin.site.register(
    [
        models.Company,
        models.JobPost,
        models.Technology,
        models.Location,
    ]
)
