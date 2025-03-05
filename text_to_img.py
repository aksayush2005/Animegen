from together import Together
import base64
import time
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=TOGETHER_API_KEY)

def main(myprompt, img_file_name):
    response = client.images.generate(
        prompt=myprompt,
        model="black-forest-labs/FLUX.1-schnell-Free",
        width=1024,
        height=768,
        steps=1,
        n=1,
        response_format="b64_json",
    )
    # print(response.data[0].b64_json)
    imgstring = response.data[0].b64_json
    imgdata = base64.b64decode(imgstring)
    filename = f'{img_file_name}.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    # image = Image.open(filename)
    # image.show()

if __name__=="__main__":
    main("Cat eating burger", "burger-cat")