import os
import openai
import config

openai.api_key = config.OPENAI_API_KEY
response = openai.Completion.create(
    engine="davinci",
    prompt="Blog topics dealing with daily life living on Mars\n\n1.",
    temperature=0.3,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0)
print(response)
