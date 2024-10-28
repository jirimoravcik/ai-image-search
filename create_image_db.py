from apify_client import ApifyClient
import requests
import os

from dotenv import load_dotenv

# Needed to load APIFY_TOKEN from .env file
load_dotenv()

if __name__ == '__main__':
    print('Creating image database, please wait...')
    # Make sure the directory exists
    os.makedirs('images', exist_ok=True)
    client = ApifyClient(token=os.environ['APIFY_TOKEN'])
    # Run the Google Maps extractor to get images of restaurants in Prague
    run_info = client.actor('compass/google-maps-extractor').call(run_input={
        'countryCode': 'cz',
        'deeperCityScrape': True,
        'language': 'en',
        'locationQuery': 'Prague, Czechia',
        'maxCrawledPlacesPerSearch': 100,
        'searchStringsArray': [
            'restaurant'
        ],
        'skipClosedPlaces': False
    })
    # Download the images, skip if the image is not available
    for item in client.dataset(run_info['defaultDatasetId']).iterate_items():
        if 'imageUrl' not in item:
            continue
        image = requests.get(item['imageUrl'])
        with open(f'images/{item["cid"]}.jpg', 'wb') as f:
            f.write(image.content)
