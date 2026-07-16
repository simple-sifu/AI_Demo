from openai import OpenAI

import os

key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a motivational message for a developers learning about AI development."}
    ]
)

# print(completion.choices)
print(completion.choices[0].message.content)