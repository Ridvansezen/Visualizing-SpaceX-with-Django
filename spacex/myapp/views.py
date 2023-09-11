from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import requests

def index(request):
    launches = categorize_launches(fetch_spacex_launches())
    return render(request, "index.html", {"launches": launches})

def date_only_filter(s):
    date_object = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date_object.date()

def fetch_spacex_launches():
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def categorize_launches(launches):
    successful = list(filter(lambda x: x["success"] and not x["upcoming"], launches))
    failed = list(filter(lambda x: not x["success"] and not x["upcoming"], launches))
    upcoming = list(filter(lambda x: x["upcoming"], launches))

    return {
        "successful": successful,
        "failed": failed,
        "upcoming": upcoming
    }
