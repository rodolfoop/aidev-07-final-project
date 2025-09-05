import sys
import requests
import json

def emotion_detector(text_to_analyze):
    host = 'https://sn-watson-emotion.labs.skills.network'
    URL= f'{host}/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input= { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=Input, headers=Headers)

    jsonresponse = json.loads(response.text)
    emotions = jsonresponse['emotionPredictions'][0]['emotion']

    max = -sys.maxsize - 1
    emotion = 'none'
    for k, v in emotions.items():
        if v > max:
            emotion = k
            max = v

    emotions['dominant_emotion'] = emotion

    return emotions
