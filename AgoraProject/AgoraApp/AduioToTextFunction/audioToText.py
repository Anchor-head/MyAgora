import whisper

# Load the model
model = whisper.load_model("base")

# Transcribe an audio file
result = model.transcribe("AgoraProject/TestingResources/AudioTest1.wav")

# Print the transcription
print(result["text"])