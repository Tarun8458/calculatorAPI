from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.

class CalcController(APIView):

    def get(self, request):
        value1 = request.GET['value1']
        value2 = request.GET['value2']
        operation = request.GET['operation']
        if(operation == " "):
            operation = "+"
            
        value = eval(value1 + operation + value2)

        response = {
            "Output" : value
        }

        return JsonResponse(response)

    def post(self, request):
        data = request.data
        value1 = data["value1"]
        value2 = data["value2"]
        operation = data["operation"]

        value = eval(str(value1) + operation + str(value2))

        response = {
            "Output" : value
        } 

        return JsonResponse(response)
