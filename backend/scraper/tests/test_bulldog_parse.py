from django.test import TestCase

from ..tasks import parse_bulldog
from .jobs import JOBS


class BulldogParseTests(TestCase):
    def setUp(self):
        self.parsed = parse_bulldog(JOBS)

    def test_includes_scrum_master(self):
        """Check if the example data contains a Scrum Master position"""
        true_result = {'name': 'Scrum Master', 'company': 'Luxoft'}
        false_result = {'name': 'Master of Puppets', 'company': 'Metallica'}

        superset = set(self.parsed[0].items())

        self.assertTrue(set(true_result.items()).issubset(superset))
        self.assertFalse(set(false_result.items()).issubset(superset))

    def test_includes_description(self):
        """Test that description is properly parsed"""
        self.assertIn(
            'We are looking for experienced individual who would be working as Scrum Master.',
            self.parsed[0]['description']
        )
