# Evaluating-Language-NLP-Capabilities-Across-Models

# 🤖 LLM Integration — Multilingual Evaluation Report

> A comparative study testing three LLMs across **English**, **Arabic**, and **Mixed-language** prompts, evaluating Fluency, Accuracy, and Language Mixing capabilities.

**Author:** Mohammad Aljabali

---

## 📋 Table of Contents

- [Overview](#overview)
- [Models Tested](#models-tested)
- [Project Structure](#project-structure)
- [Test Categories](#test-categories)
- [Results Summary](#results-summary)
- [Reflection & Key Findings](#reflection--key-findings)
- [Setup & Usage](#setup--usage)

---

## 🔍 Overview

This project evaluates the real-world performance of three large language models across challenging multilingual scenarios. Each model is tested on three dimensions:

| Dimension | Description |
|-----------|-------------|
| **Fluency** | Can the model follow stylistic or constraint-based instructions? |
| **Accuracy** | Does the model reason correctly, or does it hallucinate? |
| **Language Mixing** | Can the model handle cross-lingual or script-switching tasks? |

---

## 🧠 Models Tested

### 1. 🇺🇸 English Model — `Granite-3.0-8b-Instruct` (IBM)
- **Source:** `hf.co/Bartowski/granite-3.0-8b-instruct-GGUF:latest`
- **API:** Local Ollama (`http://localhost:11434`)
- **Strengths:** Strong logic, excellent instruction following
- **Weakness:** Blind to character-level constraints due to tokenization limits

### 2. 🇸🇦 Arabic Model — `ALLaM-7B-Instruct` (Saudi)
- **Source:** `hf.co/tensorblock/ALLaM-7B-Instruct-preview-GGUF:latest`
- **API:** Local Ollama (`http://localhost:11434`)
- **Strengths:** High proficiency in Modern Standard Arabic (MSA)
- **Weakness:** Rigid to dialects, hallucinates on logic traps, fails Arabizi

### 3. 🌐 Mixed Model — `Qwen2.5-7B-Instruct` (Alibaba)
- **Source:** `Qwen/Qwen2.5-7B-Instruct`
- **API:** HuggingFace Inference Router
- **Strengths:** Best cross-lingual reasoning, semantic translation, grammar analysis
- **Weakness:** Struggles with strict mechanical language-switching rules

---

## 📁 Project Structure

```
📁 LLM-Integration/
├── Arabic.PY                    ← Tests ALLaM-7B on Arabic prompts
├── English.PY                   ← Tests Granite-3.0 on English prompts
├── Mixed.PY                     ← Tests Qwen2.5 on mixed-language prompts
└── LLM_Integration_Report.pdf  ← Full report with results & analysis
```

---

## 🧪 Test Categories

### 🇺🇸 English Prompts (`English.PY`)

| Category | Prompt |
|----------|--------|
| Fluency (Constraint) | Write about 'War' without using the letter 'e' |
| Accuracy (Trick Question) | Which is heavier: a pound of feathers or a pound of lead? |
| Language Mixing (Instruction) | Translate 'مدرسة' to French, then explain in English only |

### 🇸🇦 Arabic Prompts (`Arabic.PY`)

| Category | Prompt |
|----------|--------|
| Fluency (Dialect Challenge) | Write a formal letter to your manager in Egyptian slang |
| Accuracy (Logic Trap) | "I was born 3 years before my father" — explain scientifically |
| Language Mixing (Arabizi) | Write "الجو اليوم جميل جداً" using English letters and numbers |

### 🌐 Mixed Prompts (`Mixed.PY`)

| Category | Prompt |
|----------|--------|
| Fluency (Chaos) | Explain how to make tea, switching Arabic/English every 3 words |
| Accuracy (Idioms) | Translate 'Break a leg' to Arabic literally — no meaning |
| Language Mixing (Grammar) | Analyze 'The boy eats' using Arabic grammar (Mubtada & Khabar) |

---

## 📊 Results Summary

| Model | Fluency | Accuracy | Language Mixing | Verdict |
|-------|---------|----------|-----------------|---------|
| **Granite-3.0** (English) | ❌ Failed — couldn't exclude letter 'e' | ✅ Solved feathers vs. lead correctly | ✅ French word + English explanation perfectly | Strong logic; blind to character-level rules |
| **ALLaM-7B** (Arabic) | ❌ Refused Egyptian dialect | ❌ Hallucinated fake science | ❌ Failed to generate Arabizi | Best for formal MSA only |
| **Qwen2.5** (Mixed) | ⚠️ Good flow, preferred translating over strict mixing | ✅ Applied Arabic grammar to English correctly | ⚠️ Failed 3-word rule; excelled at semantic switching | Best for cross-lingual & reasoning tasks |

---

## 💡 Reflection & Key Findings

**1. Which model performed best overall?**
The **English model (Granite-3.0)** performed best on reasoning — it correctly solved the trick question, while ALLaM hallucinated a fake scientific justification.

**2. Did Arabic output feel natural?**
It felt natural but **too formal**. ALLaM wrote good MSA but failed completely when asked for Egyptian dialect, making responses sound robotic and unusable for casual conversation.

**3. How were mixed-language prompts handled?**
Qwen handled **meaning well but failed strict mechanical rules**. It could not switch languages every 3 words exactly, but it excelled at cross-lingual grammar analysis.

**4. Is ALLaM suitable for an Arabic chatbot?**
**No.** It hallucinates on simple logic questions and cannot understand or produce dialects — which are essential for a real conversational Arabic chatbot.

**5. Best model for Arabic + English social media analysis?**
**Qwen2.5** — it demonstrated the strongest ability to understand and reason across both languages simultaneously.

---

## ⚙️ Setup & Usage

### Prerequisites

```bash
pip install requests
```

### English & Arabic scripts (requires Ollama running locally)

```bash
# Start Ollama
ollama serve

# Pull the models
ollama pull hf.co/Bartowski/granite-3.0-8b-instruct-GGUF:latest
ollama pull hf.co/tensorblock/ALLaM-7B-Instruct-preview-GGUF:latest

# Run
python English.PY
python Arabic.PY
```

### Mixed script (requires HuggingFace API token)

```bash
# Add your HuggingFace Bearer token in Mixed.PY, then run:
python Mixed.PY
```

> ⚠️ **Security Note:** Never hardcode API tokens in source files. Use environment variables instead:
> ```python
> import os
> headers = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"}
> ```

---

## 📦 Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Inference_API-yellow?logo=huggingface)
![IBM Granite](https://img.shields.io/badge/IBM-Granite_3.0-054ada)
![ALLaM](https://img.shields.io/badge/SDAIA-ALLaM_7B-green)
![Qwen](https://img.shields.io/badge/Alibaba-Qwen2.5-orange)
