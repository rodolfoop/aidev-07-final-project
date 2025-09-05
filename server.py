from emotion_detection.emotion_detection import emotion_detector
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    text = request.args.get('textToAnalyze')
    outputText = 'For the given statement, the system response is '

    result = emotion_detector(text)
    dominant = ''
    for k,v in result.items():
        if k != 'dominant_emotion':
            outputText += f"'{k}':, {v}"
        else:
            dominant = v

    outputText += f'. The dominant emotion is {dominant}.'

    return outputText

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
