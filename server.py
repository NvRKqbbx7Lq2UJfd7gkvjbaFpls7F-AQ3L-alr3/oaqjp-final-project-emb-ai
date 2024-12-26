#!/usr/bin/env python3
"""
Emotion Detection API
"""
from flask import Flask, make_response, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
@app.route('/')
def render_index_page() -> str:
    """
    Renders the index page.
    """
    return render_template('index.html')

@app.route('/emotion-detector', methods=['GET'])
def emotion_detector_api() -> str:
    """
    Analyzes the provided text and returns the detected emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze is None:
        return "Invalid input! Please provide a text."
    result = emotion_detector(text_to_analyze)
    dominant_emotion = result.get('dominant_emotion')
    if dominant_emotion is None:
        return "Invalid input! Please try again."
    response = f"For the given statement, the system response is \
    {result.get('response', '[Unknown]')} The dominant emotion is {dominant_emotion}."
    return make_response(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    