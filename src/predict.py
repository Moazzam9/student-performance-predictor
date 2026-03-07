import pickle
import numpy as np

with open("model.pkl","rb") as f:
    model = pickle.load(f)

input_data = np.array([[5,7,80,70]])

prediction = model.predict(input_data)

print("Predicted Score:",prediction[0])