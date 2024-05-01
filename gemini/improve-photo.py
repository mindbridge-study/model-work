import google.generativeai as genai
import os
from dotenv import dotenv_values

os.chdir('..')
config = dotenv_values(".env")  # (format) config = {"USER": "foo", "EMAIL": "foo@example.org"}

genai.configure(api_key=config["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-1.0-pro-latest')
response = model.generate_content("The opposite of hot is")
print(response.text)



#Tuned Example
"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import hashlib
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

uploaded_files = []
def upload_if_needed(pathname: str) -> list[str]:
  path = Path(pathname)
  hash_id = hashlib.sha256(path.read_bytes()).hexdigest()
  try:
    existing_file = genai.get_file(name=hash_id)
    return [existing_file]
  except:
    pass
  uploaded_files.append(genai.upload_file(path=path, display_name=hash_id))
  return [uploaded_files[-1]]

prompt_parts = [
  "input: Indoor, low light, cluttered background",
  "output: Increase ISO to 800; suggest decluttering the background",
  "input: Outdoor, bright sunlight, portrait",
  "output: Adjust exposure to -1; recommend using a reflector",
  "input: Selfie, evening, indoor lighting",
  "output: Switch to portrait mode; increase ambient light if possible",
  "input: Group photo, night, outdoors",
  "output: Use flash; increase ISO to 1600\"",
  "input: Landscape, sunset, vibrant colors",
  "output: Set white balance to shade; enhance color saturation",
  "input: Real estate, wide interior shot, dim lighting",
  "output: Turn on HDR; increase exposure slightly",
  "input: Car photo, showroom, bright lights",
  "output: Reduce ISO to 100; adjust angles to avoid reflection",
  "input: Product shot, studio lighting, white background",
  "output: Ensure even lighting; use a tripod for stabilit",
  "input: Food photography, natural light, close-up",
  "output: Use macro mode; soften background with wide aperture",
  "input: Street photography, overcast day, urban scene",
  "output: Increase contrast; capture candid moments",
  "input: Concert, low light, dynamic scene",
  "output: Use a high ISO setting; try a slower shutter for motion blur",
  "input: Wildlife, bright day, distant subjects",
  "output: Use telephoto lens; set focus to continuous",
  "input: Pet photography, indoor, playful subject",
  "output: Use burst mode; keep the background simple",
  "input: Wedding, indoor, low light, lots of guests",
  "output: Activate low-light mode; advise on organizing groups for clarity",
  "input: Travel, landmark, busy surroundings",
  "output: Recommend best time for fewer crowds; increase depth of field",
  "input: Underwater photography, clear water",
  "output: Use underwater preset; adjust white balance for blue tones",
  "input: Baby portrait, soft lighting, serene background",
  "output: Advise on using soft light; recommend gentle tones for a calm mood",
  "input: Fashion shoot, mixed lighting, multiple models",
  "output: Balance the lighting; direct models to create dynamic pose",
  "input: Documentary, indoor, historical artifacts",
  "output: Use a polarizing filter to reduce glare; enhance details in post-processing",
  "input: Sports, outdoor, fast action",
  "output: Set shutter speed to 1/1000s or faster; use continuous shooting mode",
  "input: ",
  *upload_if_needed("<path>/image0.png"),
  "output: ",
]

response = model.generate_content(prompt_parts)
print(response.text)
for uploaded_file in uploaded_files:
  genai.delete_file(name=uploaded_file.name)