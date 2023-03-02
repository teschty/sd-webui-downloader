import gradio as gr
from modules import script_callbacks


def add_tab():
    with gr.Blocks(analytics_enabled=False) as ui:
        with gr.Row().style(equal_height=False):
            with gr.Column(variant='panel'):
                gr.HTML(value="<p>Hello world</p>")

            with gr.Column(variant='panel'):
                gr.HTML(value="I'm over here too!")

    return [(ui, "Model Downloader", "model_downloader")]

script_callbacks.on_ui_tabs(add_tab)
