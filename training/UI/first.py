import gradio as  gr
#? Example 1
# def greet (name):
#     return "Hello " + name + "!"
# demo = gr.Interface (fn = greet, inputs =  "text", outputs = "text")
# demo.launch ()

#? Example 2
# def multi (num1, num2):
#   return num1 * num2
# demo = gr.Interface (fn = multi, inputs = [gr.Number (label = "Num1"), gr.Number (label = "Num2")], outputs = "text")
# demo.launch ()

#? Example 3
## Multi output separate in the function by a colon
# def multi (num1, num2):
#   n1 = num1*2
#   n2 = num2*2
#   return n1, n2
# demo = gr.Interface (fn = multi, inputs = [gr.Number (label = "Num1"), gr.Number (label = "Num2")], outputs = ["text", "text"])
# demo.launch ()

# #? Example 4
# import gradio as gr

# def predict (x):
#   return float (model.predict ([[x]]))
# input_field = gr.Number (label = "Years of Experience")
# demo - gr.Interface (fn= predict, inputs = input_field, outputs = "number", title = "Salary Prediction")
# demo.launch ()