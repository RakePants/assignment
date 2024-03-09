import gradio as gr

from src.examples.examples import example_csv
from src.utils.pipelines import process_csv

interface = gr.Interface(
    fn=process_csv,
    inputs=gr.File(
        label="Upload CSV File",
        file_count="single",
        file_types=["csv"],
    ),
    outputs=[gr.File(label="Download File"), gr.DataFrame(label="Predictions")],
    title="VK Intership Assignment Classifier Interface",
    description="Upload a CSV file to get predictions. An example is given below.",
    examples=[example_csv],
    allow_flagging="never",
)
