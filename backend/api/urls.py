from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('job-posts/', views.JobPostList.as_view()),
    path('job-posts/<int:pk>/', views.JobPostDetail.as_view()),
    path('companies/', views.CompanyList.as_view()),
    path('companies/<int:pk>/', views.CompanyDetail.as_view()),
    path('locations/', views.LocationList.as_view()),
    path('locations/<int:pk>/', views.LocationDetail.as_view()),
    path('technologies/', views.TechnologyList.as_view()),
    path('technologies/<int:pk>/', views.TechnologyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
