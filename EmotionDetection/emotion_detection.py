import requests
import json
def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # format the request as python dict using json.loads 
    response = json.loads(requests.post(url, json = myobj, headers=header).text)["emotionPredictions"][0]["emotion"]
    maxval="anger"
    for y in response:
        if response[y] > response[maxval]:
            maxval = y
    response["dominant_emotion"] = maxval
    return response