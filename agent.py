from groq import Groq
from dotenv import load_dotenv
import os
import base64

# Load API key
load_dotenv()

# Connect to Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load and encode the image
with open("product.jpg", "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

# Generate listings for all platforms
response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_data}"
                    }
                },
                {
                    "type": "text",
                    "text": """You are an expert e-commerce copywriter.
                    
Look at this product image and write optimized listings for 3 platforms:

--- AMAZON LISTING ---
Title: (max 200 chars, keyword rich)
Bullet Points:
- 
- 
- 
- 
- 
Description: (150-200 words, SEO optimized)

--- SHOPIFY LISTING ---
Title: (catchy, brand focused)
Description: (conversational, 100-150 words)
Tags: (comma separated keywords)

--- EBAY LISTING ---
Title: (max 80 chars)
Description: (short and direct, 80-100 words)
Condition Notes:

Write all 3 listings now. Be specific about the product features you can see."""
                }
            ]
        }
    ]
)

# Print the listings
print(response.choices[0].message.content)