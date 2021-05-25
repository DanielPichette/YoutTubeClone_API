from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class AllComments(APIView):

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):

    def get_object(self, pk):  # selecting a song object by the pk id
        try:
                return Comment.objects.get(pk=pk)  # here we returning the song by the id
        except Comment.DoesNotExist:  # if the exception 'song.does.not.exist' occurs, ...
            raise Http404  # then we respond with an HTTP404 response
        # TODO : check on what raise Http404 does exactly. get clarification

    def get(self, request, pk):  # 'get' is getting something fom the database.. in this case a single song
        comment = self.get_object(pk)  # here we are selecting a song by id, and assigning it to the 'song' variable
        serializer = CommentSerializer(comment)  # here we are serializing/reformatting the song variable
        return Response(serializer.data, status=status.HTTP_200_OK)  # here we are returning the selected song, in the serialized/updated format
    # get song by id functionality

    def put(self, request, pk):  # 'put' syntax == update functionality
        comment = self.get_object(pk)  # here we are getting the song by id using the get_object function
        serializer = CommentSerializer(comment, data=request.data)  # here we are reformatting the song using the serializer
        if serializer.is_valid():  # == if the data in the request matches the model ...
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  # save the selected song with the new data from the request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # otherwise give 404 error message
    # update song by id functionality

    def delete(self, request, pk):  # delete functionality
        comment = self.get_object(pk)  # here we are getting the song by id using the get_object function above
        comment.delete()  # deleting the song that has the selected pk id
        return Response(status=status.HTTP_200_OK)  # relaying status info that the the deletion was a success
    # delete song by id functionality
