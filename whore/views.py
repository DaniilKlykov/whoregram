from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import WhoreSerializer
from .models import Whore


@api_view(['POST', 'GET'])
def whore_list(request):
    if request.method == 'POST':
        serializer = WhoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    whores = Whore.objects.all().order_by('id')
    serializer = WhoreSerializer(whores, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def whore_detail(request, pk):
    whore = Whore.objects.get(pk=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = WhoreSerializer(instance=whore, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        whore.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = WhoreSerializer(instance=whore)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


class WhoreListApi(APIView):
    def get(self, request):
        whores = Whore.objects.all().order_by('id')
        serializer = WhoreSerializer(whores, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WhoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
