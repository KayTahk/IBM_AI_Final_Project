'''Server file for Emotion Detection API'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app =  Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''Sends user input to emotion_detection.py and returns formatted result'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['anger'] is None:
        return "Invalid input ! Try again."
    return f"For the given statement, the system response is {str(response)[1:-1]} \
    The dominant emotion is {response.pop('dominant_emotion')}."

@app.route("/")
def render_index_page():
    '''Renders the index page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
