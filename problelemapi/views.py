from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from problelemapi.models import Problems
from problelemapi.serializers import ProblemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@csrf_exempt
def Problem_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        problems = Problems.objects.all()
        serializer =ProblemSerializer(problems, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProblemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def add_problem(request):
    print (request)
    print (request.POST)
    problem_serializer = ProblemSerializer(data=request.POST)
    if problem_serializer.is_valid():
        problem_serializer.save()
        return Response({"data": "Problem added successfully"}, status=status.HTTP_201_CREATED)
    else:
        error_details = []
        for key in problem_serializer.errors.keys():
            error_details.append({"field": key, "message": problem_serializer.errors[key][0]})

        data = {
                "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                    }
                }

        return Response(data, status=status.HTTP_400_BAD_REQUEST)