import g4f
from g4f.Provider import (
    Bing,
    ChatgptAi,
    Liaobots
)
from flask import Flask, request,  Response
from flask_compress import Compress
from flask_talisman import Talisman
from flask_cors import CORS
import traceback
from bson.json_util import dumps
import time
import asyncio
from ast import literal_eval


app = Flask(__name__)
CORS(app)
Compress(app)
Talisman(app)


@app.route("/ask/Bing")
def bing():
    prompt = request.args.get(
        'prompt', default="[{'role': 'user', 'content': 'hi'}]", type=str)

    try:
        # change string prompt to list
        listPrompt = literal_eval(prompt)

        response = g4f.ChatCompletion.create(
            model=g4f.Model.gpt_4, provider=Bing, messages=listPrompt)

        return Response(dumps({"content": response}), mimetype='application/json; charset=utf-8')
    except Exception as ee:
        print("--- error --- >>>", ee)
        traceback.print_exc()
        return Response(dumps({"error": repr(ee)}), mimetype='application/json; charset=utf-8')


@app.route("/ask/ChatgptAi")
def chatgptai():
    prompt = request.args.get(
        'prompt', default="[{'role': 'user', 'content': 'hi'}]", type=str)

    try:
        # change string prompt to list
        listPrompt = literal_eval(prompt)

        response = g4f.ChatCompletion.create(
            model=g4f.Model.gpt_4, provider=ChatgptAi, messages=listPrompt)

        return Response(dumps({"content": response}), mimetype='application/json; charset=utf-8')
    except Exception as ee:
        print("--- error --- >>>", ee)
        traceback.print_exc()
        return Response(dumps({"error": repr(ee)}), mimetype='application/json; charset=utf-8')


@app.route("/ask/Liaobots")
def liaobots():
    prompt = request.args.get(
        'prompt', default="[{'role': 'user', 'content': 'hi'}]", type=str)

    try:
        # change string prompt to list
        listPrompt = literal_eval(prompt)

        response = g4f.ChatCompletion.create(
            model=g4f.Model.gpt_4, provider=Liaobots, messages=listPrompt)

        return Response(dumps({"content": response}), mimetype='application/json; charset=utf-8')
    except Exception as ee:
        print("--- error --- >>>", ee)
        traceback.print_exc()
        return Response(dumps({"error": repr(ee)}), mimetype='application/json; charset=utf-8')
