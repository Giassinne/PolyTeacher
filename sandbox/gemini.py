import requests
import google.generativeai as genai
import os

# Set the API key correctly
api_key = "API_KEY"
genai.configure(api_key=api_key)

model = "gpt-4o-mini"
prompt = "hey you how are you doin"
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)
print(response.text)