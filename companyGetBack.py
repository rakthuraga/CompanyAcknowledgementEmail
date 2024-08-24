from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key from the .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Example of making a request using the API key
completion = client.chat.completions.create(model="gpt-4",
messages=[
    {"role": "system", "content": "You are an Application Acknowledgment Email sender but you include the info that the user put in their application in the application acknowledgement email to make the user feel like the company geneuinely cares about what they have to say."},
    {
        "role": "user",
        "content": "Write a haiku about recursion in programming."
    }
])

# Print the response
print(completion.choices[0].message.content)