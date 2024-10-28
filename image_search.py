import os
import streamlit as st
from transformers import CLIPProcessor, CLIPModel
from PIL import Image

# Load image database
image_database = [Image.open(os.path.join('./images', image_name)) for image_name in os.listdir('./images')]
# Initialize CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Function to query the database with configurable number of most relevant results
def query_database(query, number_of_results=9):
    # Process the query and the image database
    inputs = processor(text=[query], images=image_database, return_tensors="pt", padding=True)

    # Run the model
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    # Select the top "number_of_results" images and return them
    _, indices = logits_per_image.squeeze().topk(number_of_results)
    return [image_database[i] for i in indices]

def main():
    # Create the Streamlit app
    st.title('AI Image Search')
    # Sidebar with search input and button
    query = st.sidebar.text_input('Enter a search phrase')
    search = st.sidebar.button('Search')
    # Perform search if the button is clicked and display the results
    if search:
        images = query_database(query)
        # Let's display the images in a 3x3 grid
        for i in range(0,3):
            cols = st.columns(3)
            # First column of the ith row
            cols[0].image(images[i*3], use_column_width=True)
            cols[1].image(images[i*3+1], use_column_width=True)
            cols[2].image(images[i*3+2], use_column_width=True)

if __name__ == "__main__":
    main()
