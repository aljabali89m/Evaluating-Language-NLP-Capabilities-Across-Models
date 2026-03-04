import os
import requests
import json

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"your huggingface api-key",
}
model_name = "Qwen/Qwen2.5-7B-Instruct"

prompts_list = [
    {
        "type": "mixed",
        "category": "Fluency (Chaos)",
        "text": "Explain how to make tea, but switch between English and Arabic every 3 words exactly."
    },
    {
        "type": "mixed",
        "category": "Accuracy (Idioms)",
        "text": "Translate the idiom 'Break a leg' to Arabic literally (word-for-word), do not give the meaning."
    },
    {
        "type": "mixed",
        "category": "Language Mixing (Grammar)",
        "text": "Analyze the English sentence 'The boy eats' using Arabic grammar terminology (Mubtada and Khabar)."
    }
]

for item in prompts_list:
    payload = {
        "messages": [
            {
                "role": "user",
                "content": item["text"]
            }
        ],
        "model": model_name,
        "max_tokens": 300
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    response_json = response.json()
    
    full_response = response_json["choices"][0]["message"]["content"]
    
    output = {
        "language_type": item["type"],
        "prompt": item["text"],
        "model_name": model_name,
        "category": item["category"],
        "model_response": full_response.strip()
    }
    
    print(json.dumps(output, ensure_ascii=False, indent=4))