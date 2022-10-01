import whisper
from datetime import datetime, timedelta

print(datetime.now())

model = whisper.load_model("small")
options = whisper.DecodingOptions(without_timestamps=False)
result = model.transcribe("airbnb.mp3")

segments = result['segments']
final_transcript = ''

for segment in segments:
    startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
    endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
    text = segment['text']
    segmentId = segment['id']+1
    segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"
    final_transcript += segment

print(result["text"])
print(final_transcript)
print(datetime.now())
