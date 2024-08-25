from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key from the .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load user input from the JSON file
with open('user_input.json', 'r') as file:
    user_data = json.load(file)

# Extract relevant information from the JSON file
name = user_data.get("name")
job_title = user_data.get("job_title")
company_name = user_data.get("company_name")
prompt = user_data.get("prompt")

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