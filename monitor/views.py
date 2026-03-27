from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Keyword, Flag
from .serializers import KeywordSerializer, FlagSerializer
from .services import scan_content_logic

from django.http import HttpResponse

def home(request):
    return HttpResponse("Content Monitor API is running")

@api_view(['POST'])
def create_keyword(request):
    serializer = KeywordSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)


@api_view(['POST'])
def scan_content(request):
    scan_content_logic()
    return Response({"message": "Scan completed"})

@api_view(['GET'])
def get_flags(request):
    flags = Flag.objects.all().order_by('-score')
    serializer = FlagSerializer(flags, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def update_flag(request, id):
    try:
        flag = Flag.objects.get(id=id)
    except Flag.DoesNotExist:
        return Response({"error": "Flag not found"}, status=404)

    serializer = FlagSerializer(flag, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)