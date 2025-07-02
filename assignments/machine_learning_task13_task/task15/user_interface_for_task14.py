import salary_basedOn_Experience as sbe
import gradio as gr

def predict (x):
  return float (sbe.model.predict ([[x]]))
input_field = gr.Number (label = "Years of Experience")
demo = gr.Interface (fn= predict, inputs = input_field, outputs = "number", title = "Salary Prediction")
demo.launch ()