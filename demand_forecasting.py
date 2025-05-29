import streamlit as st

class DemandForecaster:
    def __init__(self):
        self.model_name = "Demo Forecaster"

    def predict(self):
        return {"peak_hours": [17, 18, 19], "expected_users": 125}

def run():
    st.title("Demand Forecast")
    st.write("Using DemandForecaster to simulate demand prediction.")
    model = DemandForecaster()
    result = model.predict()
    st.json(result)