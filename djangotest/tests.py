import json

import pytest
from django.test import TestCase
from django.urls import reverse

from djangotest.models import Counter


class TestCounterViews(TestCase):
    def test_all_counters_returns_all_counters(self):
        c1 = Counter.objects.create(count=5)
        c2 = Counter.objects.create(count=2)
        expected = {"counters": [{"count": 5, "id": c1.id}, {"count": 2, "id": c2.id}]}

        response = self.client.get(reverse("get_all_counters"))
        content = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected, content)

    def test_get_counter_returns_counter(self):
        c1 = Counter.objects.create(count=5)
        expected = {"count": 5, "id": c1.id}

        response = self.client.get(reverse("counters", args=[c1.id]))
        content = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(expected, content)


# pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_get_counter_with_no_match_gives_404(client):
    # Converted from a xUnit style test to a pytest test to show
    # the usage of the pytest mark, and the client fixture

    response = client.get(reverse("counters", args=[1234]))
    content = json.loads(response.content)

    assert response.status_code == 404
