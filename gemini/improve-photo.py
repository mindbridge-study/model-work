import google.generativeai as genai
import os
from dotenv import dotenv_values

os.chdir('..')
config = dotenv_values(".env")  # (format) config = {"USER": "foo", "EMAIL": "foo@example.org"}

genai.configure(api_key=config["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-1.0-pro-latest')
response = model.generate_content("The opposite of hot is")
print(response.text)
