import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

def create_model(input_dim):
    """ Create a simple neural network model. """
    model = Sequential([
        Dense(64, activation='relu', input_dim=input_dim),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_chain_of_fools(data, labels, chain_length=5):
    """ Train a chain of models, each receiving the output of the previous as input. """
    input_data = data
    models = []

    for i in range(chain_length):
        # Create and train a new model on the current input data
        model = create_model(input_data.shape[1])
        model.fit(input_data, labels, epochs=10, verbose=0)
        models.append(model)

        # Predict with the current model and use predictions as input for the next model
        predictions = model.predict(input_data)
        input_data = np.hstack([input_data, predictions])  # Stack predictions as new features

    return models

def chain_of_fools_predict(models, data):
    """ Use the chain of models to make a prediction. """
    input_data = data

    for model in models:
        predictions = model.predict(input_data)
        input_data = np.hstack([input_data, predictions])  # Use current predictions as input for the next model

    return predictions

# Example usage:
# Generate some synthetic data
np.random.seed(42)
data = np.random.rand(100, 10)
labels = np.random.randint(0, 2, size=(100, 1))

# Train the chain of models
models = train_chain_of_fools(data, labels)

# Make predictions with the chain of models
predictions = chain_of_fools_predict(models, data)
print("Final predictions:", predictions)
