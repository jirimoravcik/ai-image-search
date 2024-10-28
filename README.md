# ai-image-search
AI image search using Apify, CLIP, and Streamlit

## How to run
Create a virtual environment and install the required dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Rename `.env.example` to `.env` and add your `APIFY_TOKEN`, which can be obtained for free from [here](https://console.apify.com/sign-up).

First, run the script to create the database:
```bash
python create_image_db.py
```

Then, run the image search app via `streamlit`:
```bash
streamlit run image_search.py
```