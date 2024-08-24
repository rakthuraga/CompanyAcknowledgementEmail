import os
from openai import OpenAI
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 2: Upload the Existing Dataset
response = client.files.create(
    file=open("mydata.jsonl", "rb"),
    purpose="fine-tune"
)
training_file_id = response.id
print(f"Uploaded file ID: {training_file_id}")

# Step 3: Create a Fine-Tuning Job with gpt-4o
fine_tuning_job = client.fine_tuning.jobs.create(
    training_file=training_file_id,
    model="gpt-4o-2024-08-06"
)
fine_tuned_model_name = fine_tuning_job.fine_tuned_model
print(f"Fine-tuned model name: {fine_tuned_model_name}")

# Step 4: Monitor and Manage Fine-Tuning Jobs
# List all fine-tuning jobs
jobs = client.fine_tuning.jobs.list(limit=10)
print(jobs)

# Retrieve details of a specific fine-tuning job
job_details = client.fine_tuning.jobs.retrieve(fine_tuning_job.id)
print(job_details)

#include json file
# Load user input from the JSON file
with open('user_input.json', 'r') as file:
    user_data = json.load(file)

# Extract relevant information from the JSON file
name = user_data.get("name")
job_title = user_data.get("job_title")
company_name = user_data.get("company_name")
prompt = user_data.get("prompt")

system_message = (
    "You are an Application Acknowledgment Email sender. "
    "You include the info that the user put in their application "
    "in the application acknowledgment email to make the user feel "
    "like the company genuinely cares about what they have to say."
)
user_message = f"Write a personalized acknowledgment email for {name} who applied for the {job_title} role at {company_name}."

# Step 5: Use the Fine-Tuned gpt-4o Model
if fine_tuned_model_name:
    completion = client.chat.completions.create(
        model=fine_tuned_model_name,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
            {"role": "user", "content": prompt}
        ]
    )
    print(completion.choices[0].message['content'])
else:
    print("The fine-tuning job is still running or failed. Please check the status again later.")

# Step 6: Iterate on Data and Hyperparameters (if necessary)
# Example of creating a fine-tuning job with custom hyperparameters
fine_tuning_job = client.fine_tuning.jobs.create(
    training_file=training_file_id,
    model="gpt-4o-2024-08-06",
    hyperparameters={
        "n_epochs": 3
    }
)

# Step 7: Evaluate the Fine-Tuned Model
# At this point, you'd run tests or real-world evaluations to see how well the fine-tuned model performs.

# Step 8: Integrate the Fine-Tuned Model into Your Application
# Once satisfied, replace the base model with the fine-tuned model in your production environment.
