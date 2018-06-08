from flask import Flask,render_template,request
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
import re
app=Flask(__name__)
with open('Frames-dataset/frames.json') as file:
    data=json.load(file)
train_data=[]
for i in range(0,len(data)):
    train_data.append(((((data[i])['turns'])[0])['text']))
bot=ChatBot("Training Example")
bot.set_trainer(ListTrainer)
bot.train(train_data)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()
