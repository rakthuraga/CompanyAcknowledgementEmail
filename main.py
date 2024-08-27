from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key from the .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load user input from the JSON file
with open('user_input_ten.json', 'r') as file:
    user_data = json.load(file)

# Extract relevant information from the JSON file
name = user_data.get("name")
job_title = user_data.get("job_title")
company_name = user_data.get("company_name")
prompt = user_data.get("prompt")

# Create the prompt using the extracted information
system_message = (
    "You are an Application Acknowledgment Email sender. "
    "You include the info that the user put in their application "
    "in the application acknowledgment email to make the user feel "
    "like the company genuinely cares about what they have to say."
)
user_message = f"Write a personalized acknowledgment email for {name} who applied for the {job_title} role at {company_name}."

# Create a completion using the extracted data
completion = client.chat.completions.create(model="gpt-4o",
messages=[
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_message},
    {"role": "user", "content": prompt}
])

# Print the response
print(completion.choices[0].message.content)
