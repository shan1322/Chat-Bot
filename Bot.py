from flask import Flask,render_template,request
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import json
import re
app=Flask(__name__)
with open('Frames-dataset/frames.json') as file:
    data=json.load(file)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

if __name__ == "__main__":
    app.run()
