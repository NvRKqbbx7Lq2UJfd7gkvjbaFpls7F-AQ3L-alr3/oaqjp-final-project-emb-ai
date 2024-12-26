#!/usr/bin/env python3
from flask import Flask, make_response, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def no_content():
    textToAnalyze = request.args.get('textToAnalyze')
    emotion_detector(textToAnalyze)
    return (emotion_detector(textToAnalyze), 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)