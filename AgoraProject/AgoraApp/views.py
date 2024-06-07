from rest_framework import generics,status
from .models import DebateUser
from .serializers import DebateUserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from .AduioToTextFunction.audioToText import transcribe_audio_file
from .AIFunction.generateResponse import generateResponse
from rest_framework.decorators import api_view

class TranscribeAudio(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        print("im posting--------------")
        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        try:
            transcription = transcribe_audio_file(file_name)
            print("result of transcription: ", transcription)
            aiResponse = generateResponse(transcription)
            print("ai response: ",aiResponse)
        finally:
            default_storage.delete(file_name)
        return Response({"transcription": aiResponse})

# Create your views here.
class DebateUserListCreate(generics.ListCreateAPIView):
    queryset = DebateUser.objects.all()
    serializer_class = DebateUserSerializer

class DebateUserDetail(generics.RetrieveDestroyAPIView):
    queryset = DebateUser.objects.all()
    serializer_class = DebateUserSerializer

@api_view(['GET'])
def get_user_by_username(request, username):
    try:
        user = DebateUser.objects.get(username=username)
    except DebateUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = DebateUserSerializer(user)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_user_by_username(request, username):
    try:
        user = DebateUser.objects.get(username=username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except DebateUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)