import requests

url = 'https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image'
api_key = 'sk-q4uoFqg4J5qLWrriHWNIMUNCBKddtY6ZqngrsmXYybjZK3I2'
prompt = 'A red flying dog'
accept_header = 'image/*' 

headers = {
    'Authorization': f'Bearer {api_key}',
    'Accept': accept_header,
}

data = {
    'prompt': prompt,   
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    if accept_header == 'image/*':       
        with open('generated_image.jpg', 'wb') as f:
            f.write(response.content)
    elif accept_header == 'application/json':
        json_data = response.json()
        image_base64 = json_data.get('image', '')
else:
    print(f"Request failed with status code: {response.status_code}")
    print(f"Error message: {response.text}")
