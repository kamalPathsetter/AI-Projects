import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

def get_model_client():
    gemini_model_client = OpenAIChatCompletionClient(
        model="gemini-2.0-flash",
        api_key=os.getenv("GEMINI_API_KEY")
    )
    return gemini_model_client