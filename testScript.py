import json

def validate_jsonl(file_path):
    with open(file_path, 'r') as f:
        for i, line in enumerate(f, 1):
            try:
                json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Error on line {i}: {e}")
                return False
    print("File is valid.")
    return True

# Replace 'your_file.jsonl' with your actual file path
validate_jsonl('mydata.jsonl')