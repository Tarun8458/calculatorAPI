from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.

class CalcController(APIView):

    def get(self, request):

        evaluatable = True

        value1 = request.GET['value1']
        value2 = request.GET['value2']
        operation = request.GET['operation']
        if(operation == " "):
            operation = "+"

        if(operation != "/"):
            try:
                value = eval(value1 + operation + value2)
                response = {
                 "Output" : value
                }
                res_obj = JsonResponse(response)
            
            except:
                evaluatable = False


            if not evaluatable:
                response = {
                    "Output" : "Provided values are not evaluatable."
                }
                res_obj = JsonResponse(response, status = 400)

        else:
            response = {
                "Output" : "According to test constraints, you are not allowed to perform a division operation in this API."
            }
            res_obj = JsonResponse(response, status = 400)

        return res_obj

    def post(self, request):

        evaluatable = True

        value1 = request.GET.get("value1")
        value2 = request.GET.get("value2")
        operation = request.GET.get("operation")
        if(operation == " "):
            operation = "+"

        if(operation != "/"):
            try:
                value = eval(value1 + operation + value2)
                response = {
                 "Output" : value
                }
                res_obj = JsonResponse(response)
            
            except:
                evaluatable = False


            if not evaluatable:
                response = {
                    "Output" : "Provided values are not evaluatable."
                }
                res_obj = JsonResponse(response, status = 400)

        else:
            response = {
                "Output" : "According to test constraints, you are not allowed to perform a division operation in this API."
            }
            res_obj = JsonResponse(response, status = 400)

        return res_obj