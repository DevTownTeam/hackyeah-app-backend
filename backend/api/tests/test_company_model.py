from django.test import TestCase

from .. import models


class CompanyModelTests(TestCase):
    def setUp(self):
        technologies_list = ['JavaScript', 'React', 'Django', 'Docker']
        technologies = [models.Technology.objects.get_or_create(name=name)[0] for name in technologies_list]
        location = models.Location.objects.get_or_create(location='Pacanowo, ul. Koziołka Matołka 42')[0]
        self.company = models.Company.objects.create(
            name='Januszex sp. z o.o.',
            location=location,
            size=10
        )
        self.company.technologies.set(technologies)

    def test_technologies_included(self):
        """Test that technologies' names are included"""
        technologies = [str(tech) for tech in self.company.technologies.all()]

        self.assertIn('JavaScript', technologies)
        self.assertEqual(len(self.company.technologies.all()), len(technologies))

    def test_null_location(self):
        """Test that setting location to null is allowed"""
        self.company.location = None

        self.assertIsNone(self.company.location)
