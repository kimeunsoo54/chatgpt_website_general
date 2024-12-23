import streamlit as st

import langchain
import openai

import os

openai_api_key = "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"
openai.api_key = openai_api_key
os.environ['OPENAI_API_KEY'] = openai_api_key

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

chat = ChatOpenAI(temperature=0.3, openai_api_key=openai_api_key)

chat(
    [
        SystemMessage(content="You are a nice AI bot that helps a user figure out various questions"),
        HumanMessage(content="I like the beaches where should I go?"),
        AIMessage(content="You should go to Nice, France"),
        HumanMessage(content="What else should I do when I'm there?")
    ]
)
