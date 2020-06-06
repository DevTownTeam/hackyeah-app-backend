from .serializers import JobPostSerializer, CompanySerializer, LocationSerializer, TechnologySerializer
from .models import JobPost, Company, Location, Technology
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class JobPostList(APIView):
    """
    List all job posts, or create a new job post.
    """

    def get(self, request, format=None):
        job_posts = JobPost.objects.all()
        serializer = JobPostSerializer(job_posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JobPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobPostDetail(APIView):
    """
    Retrieve, update or delete a job post instance.
    """

    def get_object(self, pk):
        try:
            return JobPost.objects.get(pk=pk)
        except JobPost.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        job_post = self.get_object(pk)
        serializer = JobPostSerializer(job_post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        job_post = self.get_object(pk)
        serializer = JobPostSerializer(job_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        job_post = self.get_object(pk)
        job_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompanyList(APIView):
    """
    List all companies, or create a new company.
    """

    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
    """
    Retrieve, update or delete a companies instance.
    """

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LocationList(APIView):
    """
    List all locations, or create a new location.
    """

    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationDetail(APIView):
    """
    Retrieve, update or delete a locations instance.
    """

    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TechnologyList(APIView):
    """
    List all technologies, or create a new technology.
    """

    def get(self, request, format=None):
        technologies = Technology.objects.all()
        serializer = TechnologySerializer(technologies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TechnologySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TechnologyDetail(APIView):
    """
    Retrieve, update or delete a technologies instance.
    """

    def get_object(self, pk):
        try:
            return Technology.objects.get(pk=pk)
        except Technology.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        technology = self.get_object(pk)
        serializer = TechnologySerializer(technology)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        technology = self.get_object(pk)
        serializer = TechnologySerializer(technology, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        technology = self.get_object(pk)
        technology.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
