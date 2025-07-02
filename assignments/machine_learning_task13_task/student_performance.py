import pandas as pd
import gradio as gr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Student_Performance.csv")
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df['Extracurricular Activities'] = df['Extracurricular Activities'].map({'Yes': 1, 'No': 0})

X = df.drop('Performance Index', axis=1)
y = df['Performance Index']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

def predict_performance(hours_studied, previous_scores, activities, sleep_hours, papers_practiced):
    try:
        hours_studied = float(hours_studied)
        previous_scores = float(previous_scores)
        if activities.lower() == "yes":
          activities = 1
        else:
           activities=0
        sleep_hours = float(sleep_hours)
        papers_practiced = float(papers_practiced)

        result = float(model.predict([[hours_studied, previous_scores, activities, sleep_hours, papers_practiced]]))
        return round(min(max(result, 0), 100), 1)
    except:
        return "invalid input try again"

interface = gr.Interface(
    fn=predict_performance,
    inputs=[
        gr.Textbox(label="Hours Studied"),
        gr.Textbox(label="Previous Scores"),
        gr.Textbox(label="Extracurricular Activities (Yes/No)"),
        gr.Textbox(label="Sleep Hours"),
        gr.Textbox(label="Sample Question Papers Practiced")
    ],
    outputs=gr.Number(label="Predicted Performance Index"),
    title="Student Performance Predictor"
)

interface.launch(share=True)