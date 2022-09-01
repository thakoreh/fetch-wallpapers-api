from fastapi import FastAPI,Response
import requests
from fastapi.responses import FileResponse


app = FastAPI()

CLIENT_ID_KEY = "8858e0b04b1e40f913260fe67fac8a5f94ea24b4f096e251a8a8887812e61443"

from fastapi.responses import HTMLResponse

def generate_html_response(source,alt):
    html_content = f"""
    <html>
        <head>
            <title>Random Image</title>
        </head>
        <body>
            <img src={source} alt={alt}>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/")
def home():
    headers = {'Authorization': f'Client-ID {CLIENT_ID_KEY}'}
    url = f"https://api.unsplash.com/photos/random"
    responsePhotosJSON = requests.get(url, headers=headers).json()
    
    # return generate_html_response(responsePhotosJSON['urls']['raw'],responsePhotosJSON['description'])
    return {'image_url':str(responsePhotosJSON['urls']['raw'])}

@app.get("/{keyword}")
def search_photo_with_keyword(keyword):
    headers = {'Authorization': f'Client-ID {CLIENT_ID_KEY}'}
    url = f"https://api.unsplash.com/search/photos"
    params = {'query':keyword}
    responsePhotosJSON = requests.get(url, headers=headers,params=params).json()
    # from random import randint
    # tempIndex=randint(0,len(responsePhotosJSON['results'])-1)
    results = []
    for result in responsePhotosJSON['results']:
        results.append(result['urls']['raw'])
    # return generate_html_response(responsePhotosJSON['results'][tempIndex]['urls']['raw'],responsePhotosJSON['results'][tempIndex]['description'])
    return {'image_urls':results}
