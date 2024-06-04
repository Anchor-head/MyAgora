from django.test import TestCase
import whisper

# Create your tests here.
class ExampleTestCase(TestCase):
    def test_example(self):
        x = 1+1
        self.assertEqual(x,2)
    
class AudioToTextConverterTestCase(TestCase):
    def test_audioToTestExampleOne(self):
        model = whisper.load_model("base")

        # Transcribe an audio file
        result = model.transcribe("../AgoraProject/TestingResources/AudioTest1.wav")

        # Print the transcription
        print(result["text"])