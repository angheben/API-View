from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import HelloSerializer
from rest_framework import status
from rest_framework import viewsets


class HelloApiView(APIView):
    """
    Test API View
    """

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """
        Return a list of APIView features
        """
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete). ',
            "It's similar to a traditional Django View. ",
            "Gives you the most control over your logic. ",
            "It's mapped mannualy to URLs.",
        ]
        return Response({'message': 'Hello World', 'an_apiview': an_apiview})

    def post(self, request):
        """
        Create a hello message with our name
        """
        serializer = HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Handles updating the object
        """
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """
        Patch request, only updates provided in the request
        """
        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """
        Deletes an object
        """
        return Response({"method": "delete"})


class HelloViewSet(viewsets.ViewSet):
    """
    Test API Viewset
    """
    def list(self, request):
        """
        :return: Hello message
        """
        a_viewset = [
            'Uses actions (list, create, retrive, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello', "a_viewset": a_viewset})