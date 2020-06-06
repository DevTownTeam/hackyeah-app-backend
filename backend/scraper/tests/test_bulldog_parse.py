from django.test import TestCase

from ..tasks import parse_bulldog
from .jobs import JOBS


class BulldogParseTests(TestCase):
    def setUp(self):
        self.parsed = parse_bulldog(JOBS)

    def test_includes_scrum_master(self):
        true_result = {'name': 'Scrum Master', 'company': 'Luxoft'}
        false_result = {'name': 'Master of Puppets', 'company': 'Metallica'}

        superset = set(self.parsed[0].items())

        self.assertTrue(set(true_result.items()).issubset(superset))
        self.assertFalse(set(false_result.items()).issubset(superset))
