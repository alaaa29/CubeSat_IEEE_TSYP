CubeSat EPS Temperature Prediction

This project simulates and predicts the temperature behavior of a 3U CubeSat Electrical Power System (EPS) using real-like telemetry data. The model is trained to detect temperature fluctuations and handle sensor failures over time.

📈 Features

Simulated dataset of CubeSat temperature readings over one month

Automatic insertion of sensor failure periods (NaN values)

Machine learning model to predict missing or future temperature data

Visualization comparing actual vs predicted temperatures

🧠 Objective

To develop a model capable of learning thermal dynamics within a CubeSat EPS and maintaining accurate temperature predictions even during data loss events.

⚙️ Requirements

Python 3.x

pandas, numpy, matplotlib, scikit-learn

Jupyter Notebook (for training and plotting)

🚀 Usage

Generate or load the temperature dataset

Train the model on the available data

Run predictions and visualize results using the provided notebook

Optionally deploy the trained model on the Raspberry Pi Pico (MicroPython) via Wokwi

📂 Output Example

The output plot shows actual vs predicted EPS temperatures for a random day, highlighting the model’s performance and stability under simulated failure conditions.
