import gradio as gr

from utils import generate_response

with gr.Blocks() as demo:

    chatbot = gr.Chatbot(label='Openai Chatbot', height=750)
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])
    
    msg.submit(generate_response, [msg, chatbot], [msg, chatbot])

demo.launch()
