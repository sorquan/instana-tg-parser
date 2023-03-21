#!/usr/bin/env python3

from flask import Flask, request
import requests
import os
import json
from datetime import datetime

app = Flask(__name__)

TG_TOKEN = os.getenv('TG_TOKEN')
TG_CHAT = os.getenv('TG_CHAT')


def tg_send(chat, text):
    url = "https://api.telegram.org/bot" + TG_TOKEN + "/sendMessage?chat_id=" + chat
    headers = {"Content-Type": "application/json"}
    data = {"text": text}
    response = requests.get(url, headers=headers, json=data)
    return response.json()


@app.route('/',methods = ['POST'])
def parse():
    log = {}
    event = request.json['issue']
    log['Recieved'] = event
    if event['type'] in ['issue', 'incident']:
        message = (
            f"id: {event['id']}\n"
            f"state: {event['state']}\n"
            f"start: {datetime.fromtimestamp(event['start'] / 1000)}\n"
            f"end: {datetime.fromtimestamp(event['end'] / 1000) if 'end' in event.keys() else 'Not resolved' }\n"
            f"text: {event['text']}\n"
            f"zone: {event['zone']}\n"
            f"entity: {event['entity']}\n"
            f"entityLabel: {event['entityLabel']}\n"
            f"service: {event['service']}\n"
            f"link: {event['link']}"
        )
        log['Sent'] = tg_send(TG_CHAT, message)
    else:
        log['Sent'] = "Presence events parsing is not implemented"

    return json.dumps(log)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
