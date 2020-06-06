from django.test import TestCase

from ..tasks import parse_bulldog
from .jobs import JOBS


class BulldogParseTests(TestCase):
    def setUp(self):
        self.parsed = parse_bulldog(JOBS)

    def test_includes_scrum_master(self):
        result = {'name': 'Scrum Master', 'company': 'Luxoft'}

        self.assertDictEqual(self.parsed[0], result)
