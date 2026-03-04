import requests, json

url = "http://localhost:11434/api/generate"
model_name = "hf.co/Bartowski/granite-3.0-8b-instruct-GGUF:latest"

prompts_list = [
    {
        "type": "english",
        "category": "Fluency (Constraint)",
        "text": "Write a short paragraph about 'War' without using the letter 'e' at all."
    },
    {
        "type": "english",
        "category": "Accuracy (Trick Question)",
        "text": "Which is heavier: a pound of feathers or a pound of lead? Explain why carefully."
    },
    {
        "type": "english",
        "category": "Language Mixing (Instruction)",
        "text": "Translate the Arabic word 'مدرسة' to French, but explain the meaning to me in English only."
    }
]

for item in prompts_list:
    data = {
        "language_type": item["type"],
        "model": model_name,
        "prompt": item["text"],
        "stream": False
    }

    response = requests.post(url, json=data)
    full_response = response.json().get("response", "")
    
    output = {
        "language_type": item["type"],
        "prompt": item["text"],
        "model_name": model_name,
        "category": item["category"],
        "model_response": full_response.strip()
    }
    
    print(json.dumps(output, indent=4))