import predict_irs_spicies as pis
import gradio as gr

def predict_species(sl, sw, pl, pw):

    pred = pis.model.predict([[sl, sw, pl, pw]])
    return pred

input = [
    gr.Number (label = "Sepal Length (cm)"),
    gr.Number (label = "Sepal Width (cm)"),
    gr.Number (label = "Petal Length (cm)"),
    gr.Number (label = "Petal Width (cm)")
]

demo = gr.Interface (fn= predict_species, inputs = input, outputs = "text", title = "Predicted Iris Species")
demo.launch ()