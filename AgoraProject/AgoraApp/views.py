from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from .AduioToTextFunction.audioToText import transcribe_audio_file
from .AIFunction.generateResponse import generateResponse
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
