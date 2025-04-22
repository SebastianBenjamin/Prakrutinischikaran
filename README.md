# Dosha Prediction API

This API predicts Ayurvedic Dosha (Prakruthi) based on various physiological and psychological features.

## API Endpoints

### GET /
Returns a welcome message and instructions for using the API.

### POST /predict
Predicts the Dosha type based on input features.

#### Request Format
Send a POST request with JSON body containing all required features:

```json
{
  "Hair quality": 1,
  "Hair texture": 2,
  "Hair fall": 3,
  ...and all other required features
}
```

Feature values should be integers 1, 2, or 3, representing:
- 1: Pitta characteristics
- 2: Vata characteristics
- 3: Kapha characteristics

#### Response Format
```json
{
  "prediction": "Pittaj",
  "probabilities": {
    "Pittaj": 0.85,
    "Vataj": 0.10,
    "Kaphaj": 0.03,
    "Pittaj-Kaphaj": 0.01,
    "Pittaj-Vataj": 0.01
  }
}
```

## Example Usage (Python)
```python
import requests
import json

url = "https://your-api-url.onrender.com/predict"
data = {
    "Hair quality": 1,
    "Hair texture": 2,
    "Hair fall": 1,
    # Include all required features here
}

response = requests.post(url, json=data)
result = response.json()
print(f"Predicted Dosha: {result['prediction']}")
print(f"Probabilities: {result['probabilities']}")
```