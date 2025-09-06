""" Startup python file """
from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """ Default route that will invoke index.html """

    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    """ Main route for calling library emotion_detection """

    text = request.args.get('textToAnalyze')
    output_text = 'For the given statement, the system response is '

    result = emotion_detector(text)

    if result['dominant_emotion'] == 'none':
        output_text = 'Invalid text! Please try again!'
    else:
        dominant = ''
        for k,v in result.items():
            if k != 'dominant_emotion':
                output_text += f"'{k}':, {v}"
            else:
                dominant = v

        output_text += f'. The dominant emotion is {dominant}.'

    return output_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
