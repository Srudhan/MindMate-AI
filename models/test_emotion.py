print("File Started")

from models.emotion_detector import detect_emotion

print("Model Imported")

emotion = detect_emotion(
    "I am stressed about my exams"
)

print("Detected:", emotion)