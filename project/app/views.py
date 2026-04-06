from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# from django.http import JsonResponse
# from .models import Internship
# from django.views.decorators.csrf import csrf_exempt
# import json

# def home(request):
#     return HttpResponse("app is running") 


# @csrf_exempt
# def internship_list(request):
#     if request.method == 'GET':
#         data = list(Internship.objects.values())
#         return JsonResponse(data, safe=False)

#     if request.method == 'POST':
#         body = json.loads(request.body)
#         internship = Internship.objects.create(
#             company=body['company'],
#             role=body['role'],
#             status=body['status'],
#             notes=body.get('notes', '')
#         )
#         return JsonResponse({"message": "Created", "id": internship.id})
# @csrf_exempt
# def internship_detail(request, id):
#     try:
#         internship = Internship.objects.get(id=id)
#     except Internship.DoesNotExist:
#         return JsonResponse({'error': 'Not found'}, status=404)

#     if request.method == 'PUT':
#         body = json.loads(request.body)
#         internship.company = body.get('company', internship.company)
#         internship.role = body.get('role', internship.role)
#         internship.status = body.get('status', internship.status)
#         internship.notes = body.get('notes', internship.notes)
#         internship.save()
#         return JsonResponse({'message': 'Updated'})

#     if request.method == 'DELETE':
#         internship.delete()
#         return JsonResponse({'message': 'Deleted'})


# shifting to rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Internship
from .serializers import InternshipSerializer

@api_view(['GET', 'POST'])
def internship_list(request):
    if request.method == 'GET':
        internships = Internship.objects.all()
        serializer = InternshipSerializer(internships, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InternshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def internship_detail(request, id):
    try:
        internship = Internship.objects.get(id=id)
    except Internship.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InternshipSerializer(internship)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InternshipSerializer(internship, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        internship.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)