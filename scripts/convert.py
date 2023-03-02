import gradio as gr
from modules import script_callbacks


def add_tab():
    with gr.Blocks(analytics_enabled=False) as ui:
        with gr.Column(variant='panel'):
            gr.HTML(value="<p>Hello world</p>")

    return [(ui, "Model Downloader", "model_downloader")]

script_callbacks.on_ui_tabs(add_tab)
