import os
import random
import time

import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_completion(messages: list) -> str:
    try:
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages
        )
        return completion['choices'][0]['message']['content']
    except:
        return 'We are facing a technical issue at this moment.'

def generate_messages(messages: list, query: str) -> list:
    formated_messages = [
        {
            'role': 'system',
            'content': 'You are a helpful assistant.'
        }
    ]
    for m in messages:
        formated_messages.append({
            'role': 'user',
            'content': m[0]
        })
        formated_messages.append({
            'role': 'assistant',
            'content': m[1]
        })
    formated_messages.append(
        {
            'role': 'user',
            'content': query
        }
    )
    return formated_messages

def generate_response(query: str, chat_history: list) -> tuple:
        messages = generate_messages(chat_history, query)
        bot_message = chat_completion(messages)
        chat_history.append((query, bot_message))
        time.sleep(random.randint(0, 5))
        return '', chat_history
