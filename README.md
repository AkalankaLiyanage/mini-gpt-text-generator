
# 🧠 Mini GPT Text Generator

A simple and fun web app that generates text using the DistilGPT-2 model (a lightweight version of GPT-2). Built with Hugging Face Transformers and Gradio.

## 🚀 Project Overview

This app lets users enter a short text prompt and generates human-like text based on that prompt using a pre-trained generative AI model. It’s lightweight, easy to run on Google Colab, and designed for education and creative content generation.

## ✨ Features

- Accepts text input from the user
- Generates multiple creative completions
- Adjustable length and randomness (`max_length` & `temperature`)
- Clean, interactive Gradio interface

## 🛠️ Technologies Used

- 🤗 Hugging Face Transformers (`DistilGPT-2`)
- 🔧 Gradio (for the user interface)
- ☁️ Google Colab (no setup required)

## ▶️ How to Run (in Google Colab)

1. Open the Colab notebook [here](https://colab.research.google.com/)
2. Copy and paste the following code:

```python
!pip install transformers gradio
from transformers import pipeline, set_seed
import gradio as gr

generator = pipeline('text-generation', model='distilgpt2')
set_seed(42)

def generate_text(prompt):
    outputs = generator(prompt, max_length=100, num_return_sequences=1, temperature=0.9)
    return outputs[0]['generated_text']

gr.Interface(fn=generate_text, 
             inputs="text", 
             outputs="text", 
             title="Mini GPT Text Generator",
             description="Enter a prompt and let DistilGPT-2 complete your thought!"
             ).launch(share=True)
```

3. Run the code blocks — your app will be live on a public URL 🎉

## 📚 Example Prompts

- "Once upon a time in Tokyo,"
- "The secret to happiness is"
- "AI in the future will be"

## 👨‍💻 Author

Created by [Akalanka Liyanage]  
📅 April 2025

## 📌 Note

The public link generated (`gradio.live`) will expire when Colab shuts down or after ~90 mins of inactivity.
