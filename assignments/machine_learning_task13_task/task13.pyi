import pandas as pd
df = pd.read_csv('Iris.csv')
df['Species'] = df['Species'].replace('Iris_setosa',0)
df['Species'] = df['Species'].replace('Iris_versicolor',1)
df['Species'] = df['Species'].replace('Iris_virginica',2)
df.isna().sum()
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test =train_test_split(df.drop('Species',axis=1),df['Species'],test_size=0.2,random_state=42)
from sklearn.svm import SVC 
model =SVC(kernel="linear")
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
from sklearn.metrics import classification_report, accuracy_score
accuracy=accuracy_score(y_test,y_pred)
report=classification_report(y_test,y_pred)
print('Accuracy:',accuracy)
print('Classification Report:\n',report)