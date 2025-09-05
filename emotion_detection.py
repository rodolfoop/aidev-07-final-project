import requests

def emotion_detector(text_to_analyze):
    host = 'https://sn-watson-emotion.labs.skills.network'
    URL= f'{host}/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input= { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=Input, headers=Headers)

    return response.text
