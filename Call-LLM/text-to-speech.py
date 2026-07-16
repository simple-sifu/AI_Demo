import os
from openai import OpenAI

from pathlib import Path

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

input_speech = """
**Hey Future AI Developer!** 🌟
As you embark on this exciting journey into the world of AI development, remember that every great innovation starts with a spark of curiosity and the courage to learn. The field of artificial intelligence is like an endless ocean of possibilities—vast and filled with opportunities to explore, create, and impact the world.
Embrace the challenges you encounter; they are stepping stones to mastery. Each problem you solve and each line of code you write is a contribution to the future of technology. Stay curious, keep experimenting, and never hesitate to push the boundaries of what’s possible.
Surround yourself with a community of like-minded individuals. Share your ideas, ask questions, and collaborate. Together, you will elevate each other's skills and foster creativity. Remember, every expert was once a beginner!
Believe in your potential, and remember that persistence is key. The path of a developer can be winding, but with every setback, you are learning and growing. The tools you gain in AI development will not only empower you but also enable you to shape the future in ways we can only begin to imagine.
So, take a deep breath, dive in, and enjoy the ride! The world is waiting for your ideas and innovations. Keep pushing forward, and you'll not only become a proficient developer but also a pioneer in shaping the future of AI. You've got this!
"""

speech_file_path = Path(__file__).parent / "motivation_message.mp3"

with client.audio.speech.with_streaming_response.create(
    model="tts-1",
    input=input_speech,
    voice="alloy"
) as response:
    response.stream_to_file(speech_file_path)

print(f"Saved {speech_file_path}")