import logging

from django.http import JsonResponse

from .models import Counter


def get_all_counters(request):
    logging.info("Requesting all counters...")

    result = {
        "counters": [
            {"id": counter.id, "count": counter.count}
            for counter in Counter.objects.all()
        ]
    }

    return JsonResponse(result)


def get_counter(request, id):
    try:
        counter = Counter.objects.get(id=id)
        return JsonResponse({"id": counter.id, "count": counter.count})
    except Counter.DoesNotExist:
        return JsonResponse({}, status=404)


def health(request):
    logging.debug("Checking health...")
    return JsonResponse({"message": "ok"})
