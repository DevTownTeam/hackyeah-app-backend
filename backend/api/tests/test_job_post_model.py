from django.test import TestCase

from .. import models


class JobPostModelTests(TestCase):
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

        self.job_post = models.JobPost.objects.create(
            name='Junior Front End Developer',
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            company=self.company,
            job_category='FE',
            salary=2000
        )
        self.job_post.technologies.set(technologies)

    def test_job_category(self):
        """Test that the job category is properly assigned"""
        self.assertEqual(self.job_post.job_category, 'FE')

    def test_company(self):
        """Test that the company is properly assigned"""
        self.assertEqual(self.job_post.company, self.company)
        self.assertEqual(self.job_post.company.name, 'Januszex sp. z o.o.')
