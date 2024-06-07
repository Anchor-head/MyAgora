import whisper
import warnings

# Load the Whisper model once
model = whisper.load_model("base")

def transcribe_audio_file(audio_path):
    # Suppress specific warning
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
        
        # Transcribe the audio file using the preloaded model
        result = model.transcribe(audio_path)
        
    # Return the transcription result
    return result["text"]
