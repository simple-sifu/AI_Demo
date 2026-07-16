from openai import OpenAI
import base64
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.images.generate(
    model="gpt-image-1",
    prompt="A beautiful sunset over a calm ocean",
    n=1,
    size="1024x1024",
    quality="high",
)

image_bytes = base64.b64decode(response.data[0].b64_json)
out_path = "sunset.png"
with open(out_path, "wb") as f:
    f.write(image_bytes)

print(f"Saved {out_path}")
