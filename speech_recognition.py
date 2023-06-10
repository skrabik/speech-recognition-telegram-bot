import whisper

def speech_recognition(file_path, model="base"):
    speech_model = whisper.load_model(model)
    result = speech_model.transcribe(file_path, fp16=False)

    return result['text']



