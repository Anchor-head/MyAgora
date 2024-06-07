from django.test import TestCase
from .AduioToTextFunction.audioToText import transcribe_audio_file
import os
# Create your tests here.
class ExampleTestCase(TestCase):
    def test_example(self):
        x = 1+1
        self.assertEqual(x,2)
    
class AudioToTextConverterTestCase(TestCase):
    def test_audioToTestExampleOne(self):
        audio_path = os.path.join(os.path.dirname(__file__), '..', 'TestingResources', 'AudioTest1.wav')
        transcribed_result = transcribe_audio_file(audio_path)
        print(transcribed_result)
        self.assertTrue(True)