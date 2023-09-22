import django
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from robot_api.models import Add
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse("Hello Robot API")

# def get_csrf_token(request):
#
#     token = django.middleware.csrf.get_token(request)
#     return JsonResponse({"token": token})

@csrf_exempt
def calculate_add(request):
    if request.method == "POST":
        data = json.loads(request.body)

        _a = data["a"]
        _b = data["b"]
        _res = float(_a) + float(_b)

        new_data = Add(a=_a, b=_b, result=_res)
        new_data.save()

        response = {
            "res_add": _res,
            "success": True,
        }

    else:
        response = {
            "res_add": "",
            "success": False,
        }

    return JsonResponse(response)
