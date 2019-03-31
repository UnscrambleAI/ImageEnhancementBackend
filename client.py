import requests
import base64
from io import BytesIO
from PIL import Image

image = Image.open('./IMG_0420.jpg')
buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue())

url  = "http://127.0.0.1:5000/enhance"
params = {
    "userId":"2TAP7EZO",
"accessToken":"ULCPAWBMDRXR42FS",
"imageString": str(img_str)
}

r = requests.post(url, json=params)
print (r.content)