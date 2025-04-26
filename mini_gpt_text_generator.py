
# Mini GPT Text Generator - DistilGPT-2 + Gradio
!pip install transformers gradio --quiet

from transformers import pipeline, set_seed
import gradio as gr

generator = pipeline('text-generation', model='distilgpt2')
set_seed(42)

def generate_text(prompt, length=100, temperature=1.0):
    result = generator(prompt, max_length=length, temperature=temperature, num_return_sequences=1)
    return result[0]['generated_text']

interface = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter your prompt here...", label="Prompt"),
        gr.Slider(minimum=50, maximum=200, step=10, value=100, label="Max Length"),
        gr.Slider(minimum=0.5, maximum=1.5, step=0.1, value=1.0, label="Creativity (Temperature)")
    ],
    outputs="text",
    title="Mini GPT Text Generator",
    description="A lightweight text generation app using DistilGPT-2"
)

interface.launch()
