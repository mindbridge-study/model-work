import google.generativeai as genai
import os
from dotenv import dotenv_values
import PIL.Image

def improve_photo(photo_path = 'gemini/notebooks/pfp.jpeg'):
    os.chdir('..')
    config = dotenv_values(".env")  # (format) config = {"USER": "foo", "EMAIL": "foo@example.org"}

    genai.configure(api_key=config["GOOGLE_API_KEY"])

    model = genai.GenerativeModel('gemini-pro-vision')

    img = PIL.Image.open(photo_path) #NOTE: jpg does not work
    prompt = """
            your goal is to be a robot that helps improve photos. Based on the type of photo, respond ONLY with one of the following options:
            1. Move closer to the subject.
            2. Move further from the subject.
            3. Use the rule of thirds on the subject.
            4. Move the camera up.
            5. Move the camera down.
            6. Move the camera left.
            7. Move the camera right.
            """
    response = model.generate_content([prompt, img])

    print(response.parts)

