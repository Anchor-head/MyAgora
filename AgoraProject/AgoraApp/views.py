from rest_framework import generics,status
from .models import DebateUser,SpeechHistory
from .serializers import DebateUserSerializer,SpeechHistorySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from .AduioToTextFunction.audioToText import transcribe_audio_file
from .AIFunction.generateResponse import generateResponse
from rest_framework.decorators import api_view
from .models import *

#------helper methods------
def ensure_speech_history_for_user(username):
    try:
        user = DebateUser.objects.get(username=username)
    except DebateUser.DoesNotExist:
        return f"User {username} does not exist."

    try:
        speech_history = SpeechHistory.objects.get(user=user)
    except SpeechHistory.DoesNotExist:
        speech_history = SpeechHistory(user=user)
        speech_history.save()
        return f"Created new speech history for user {username}."
    
    return f"User {username} already has an associated speech history."

#------Controllers--------
class TranscribeAudio(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        print("im posting--------------")
        file = request.FILES['file']
        username = request.data.get('username')
        #general chat memory list
        ensure_speech_history_for_user(username=username)
        user = DebateUser.objects.get(username=username)
        speech_history = SpeechHistory.objects.get(user=user)

        print(f"Received username: {username}")  # Print the received username for debugging
        #trancribe file
        file_name = default_storage.save(file.name, file)
        try:
            transcription = transcribe_audio_file(file_name)
            speech_history.content.append({'role': 'user', 'content':transcription})
            speech_history.save()
            print(f"User: {username}, Transcription: {transcription}")
            aiResponse = generateResponse(speech_history.content)
            #store data into history
            speech_history.content.append({'role': 'assistant', 'content':aiResponse})
            speech_history.save()
            print("AI response: ", aiResponse)

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

class SpeechHistoryListCreate(generics.ListCreateAPIView):
    queryset = SpeechHistory.objects.all()
    serializer_class = SpeechHistorySerializer

class SpeechHistoryDetail(generics.RetrieveDestroyAPIView):
    queryset = SpeechHistory.objects.all()
    serializer_class = SpeechHistorySerializer

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