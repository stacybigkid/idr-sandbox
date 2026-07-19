import requests

# Use the correct IDR domain and JSON API structure
base_url = "https://idr.openmicroscopy.org/api/v0"
image_id = 28662

url = f"{base_url}/m/images/{image_id}/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Access the core attributes dict
    image_meta = data['data']
    print(f"Success! Data Available: {image_meta.keys()}")
    print(f"image name: {image_meta['Name']}")
else:
    print(f"Failed with status code {response.status_code}")
