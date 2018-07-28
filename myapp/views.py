from django.http import JsonResponse
from django.shortcuts import render


from .models import Counter


def index(request):

    result = {
        "counters": [
            {"id": counter.id, "count": counter.count}
            for counter in Counter.objects.all()
        ]
    }

    return JsonResponse(result)
