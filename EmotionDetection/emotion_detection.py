import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    maxval = "anger"
    if response.status_code == 200:
        formatted_response = json.loads(response.text)["emotionPredictions"][0]["emotion"]
        for y in formatted_response:
            if formatted_response[y] > formatted_response[maxval]:
                maxval = y
        formatted_response["dominant_emotion"] = maxval
        anger = formatted_response['anger']
        disgust = formatted_response['disgust']
        fear = formatted_response['fear']
        joy = formatted_response['joy'] 
        sadness = formatted_response['sadness']
        dominant_emotion = formatted_response['dominant_emotion']
    elif response.status_code == 400:
        anger = disgust = fear = joy = sadness = dominant_emotion = None
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}