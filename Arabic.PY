import requests, json

url = "http://localhost:11434/api/generate"
model_name = "hf.co/tensorblock/ALLaM-7B-Instruct-preview-GGUF:latest"

prompts_list = [
    {
        "type": "arabic",
        "category": "Fluency (Dialect Challenge)", 
        "text": "اكتب رسالة رسمية لمديرك تطلب فيها إجازة، ولكن استخدم اللهجة المصرية العامية فقط."
    },
    {
        "type": "arabic",
        "category": "Accuracy (Logic Trap)",
        "text": "أنا ولدت قبل والدي بـ 3 سنوات. اشرح كيف يمكن أن يحدث هذا علمياً."
    },
    {
        "type": "arabic",
        "category": "Language Mixing (Arabizi)",
        "text": "اكتب جملة 'الجو اليوم جميل جداً' ولكن باستخدام الحروف الإنجليزية والأرقام."
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
    
    print(json.dumps(output, ensure_ascii=False, indent=4))