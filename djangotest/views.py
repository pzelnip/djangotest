import logging

from django.http import JsonResponse

from .models import Counter


def index(request):
    logging.error("Requesting index...")

    result = {
        "counters": [
            {"id": counter.id, "count": counter.count}
            for counter in Counter.objects.all()
        ]
    }

    return JsonResponse(result)


def health(request):
    logging.debug("Checking health...")
    return JsonResponse({"message": "ok"})
