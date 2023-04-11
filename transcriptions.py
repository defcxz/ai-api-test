import whisper

model = whisper.load_model("base")
result = model.transcribe("audios/audio.m4a")
print(result["text"])