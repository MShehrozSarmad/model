import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv("heart.csv")

# Features and target
X = data.drop(columns=['target'])
Y = data['target']

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create and train the model
model = LogisticRegression()
model.fit(X_train, Y_train)

def predict_heart_disease():
    # Get user input
    inputs = []
    for entry in entries:
        try:
            value = float(entry.get())
            inputs.append(value)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
            return

    # Make prediction
    input_data = np.array(inputs).reshape(1, -1)
    prediction = model.predict(input_data)

    # Show prediction
    if prediction[0] == 1:
        result_label.config(text="You have a heart disease.")
    else:
        result_label.config(text="You do not have a heart disease.")

# Create the main window
window = tk.Tk()
window.title("Heart Disease Prediction")

# Create labels and entry fields for each input
labels = ['Age:', 'Sex (0 = female, 1 = male):', 'Chest Pain Type:', 'Resting Blood Pressure:', 
          'Cholesterol:', 'Fasting Blood Sugar:', 'Resting Electrocardiographic Results:', 
          'Maximum Heart Rate Achieved:', 'Exercise Induced Angina:', 'ST Depression Induced by Exercise:', 
          'Slope of the Peak Exercise ST Segment:', 'Number of Major Vessels Colored by Fluoroscopy:', 
          'Thalassemia:']

entries = []
for i, label_text in enumerate(labels):
    label = tk.Label(window, text=label_text)
    label.grid(row=i, column=0, padx=5, pady=5)
    entry = tk.Entry(window)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

# Create a button to trigger the prediction
predict_button = tk.Button(window, text="Predict", command=predict_heart_disease)
predict_button.grid(row=len(labels), column=0, columnspan=2, padx=5, pady=5)

# Create a label to show the prediction result
result_label = tk.Label(window, text="")
result_label.grid(row=len(labels)+1, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
window.mainloop()