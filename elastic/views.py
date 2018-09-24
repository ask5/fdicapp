from elasticsearch import Elasticsearch
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from common.decorators import subscription_required

@login_required
@subscription_required
@csrf_exempt
def Institution(request):
    response = {}
    if request.method == "POST":
        host = settings.ELASTICSEARCH_DSL['default']['hosts']
        t = settings.ELASTICSEARCH_DSL['default']['timeout']
        client = Elasticsearch(hosts=[host], timeout=t)
        response = client.search(
            index="institutions",
            body=request.body
        )
    return HttpResponse(json.dumps(response), content_type="application/json")


@login_required
@subscription_required
@csrf_exempt
def Office(request):
    response = {}
    if request.method == "POST":
        host = settings.ELASTICSEARCH_DSL['default']['hosts']
        t = settings.ELASTICSEARCH_DSL['default']['timeout']
        client = Elasticsearch(hosts=[host], timeout=t)
        response = client.search(
            index="offices",
            body=request.body
        )
    return HttpResponse(json.dumps(response), content_type="application/json")
