

# 🌿 Prakriti Nishchikaran API

An XGBoost-based Machine Learning API to determine Prakriti (body constitution) based on 40+ bio-behavioral traits from Ayurveda.

> 🔮 **Accuracy**: 88.5%  
> 🚀 **Live API**: [API Link](https://prakruthinischikaran-api.onrender.com)  
> 🧪 **Try API Interface**: [Test Webapp](https://api-prakritinischikaran.netlify.app/)

---

## 📌 Features

- Built using **XGBoost Classifier**  
- Trained on a diverse set of **bio-behavioral traits**  
- Hosted via **Render**  
- Front-end test interface via **Netlify**  
- Accepts JSON payload and returns Prakriti classification (`Vata`, `Pitta`, `Kapha`)

---

## 📂 Model Notebook

The notebook file used for training and evaluation is included in this repository:  
➡️ [`PrakritiNishchikaranModal.ipynb`](./PrakritiNishchikaranModal.ipynb)

---

## 📤 API Usage

### 🔗 Endpoints
```bash
GET / (Root URL)
https://prakruthinischikaran-api.onrender.com
```
```bash
POST / (Root URL)
https://prakruthinischikaran-api.onrender.com/predict
```

### 📥 Sample Input Payload
```json
{
  "Hair quality": 1,
  "Hair texture": 1,
  ...
  "Trust level": 1
}
```

### 📤 Sample Responses

#### For Home page
```json
Status Code: 200
Response: {
  "instructions": "Send a POST request to /predict with feature values to get dosha prediction",
  "message": "Welcome to the Dosha Prediction API"
}
```

#### For /predict page
```json

Status Code: 200
Response: {
  "prediction": "Vataj",
  "probabilities": {
    "Kaphaj": 0.006819805130362511,
    "Kaphaj-Pittaj": 0.006921370979398489,
    "Pittaj": 0.045854952186346054,
    "Pittaj-Kaphaj": 0.08181353658437729,
    "Pittaj-Vataj": 0.007285633124411106,
    "Vataj": 0.701982855796814,
    "Vataj-Pittaj": 0.14932186901569366
  }
}
```

---

## 🧪 Test Script

Use the following script to test locally or modify the URL for live usage:

```python
import requests

url = "https://prakruthinischikaran-api.onrender.com"  # Live URL
data = {
     'Skin color': 1,
        'Skin texture': 1,
        'Details about hair type': 1,
        'Texture of hair ': 1,
        'My hairs are': 1,
        'Hair falling tendency\t': 1,
        'Eyes\t': 1,
        'My eyes  eye balls are': 1,
        'Physique\t': 1,
        'Veins\t': 1,
        'Usual body temperature \t': 1,
        'Teeth \t': 1,
        'Is your lips\t': 2,
        'Hands(Length)': 2,
        'Body hair\t': 2,
        'Joints\t': 2,
        'Chest\t': 2,
        'Tongue\t': 2,
        'Body frame (Length)\t': 2,
        'Body frame (Breadth)\t': 2,
        'Bodyweight changes\t': 2,
        'Style of speaking\t': 2,
        'Voice \t': 2,
        'Walk \t': 2,
        'Appetite \t ': 2,
        'Intensity of hunger\t': 2,
        'Favorite climate\t': 2,
        'Stamina\t': 2,
        'Tastes, I like most': 2,
        'Eagerness about drinking water': 2,
        'Frequency of liquid intake\t': 2,
        'Sleep\t': 2,
        'Quantity of sweat\t': 2,
        'Emotion\t': 2,
        'Intellect\t': 2,
        'Grasping\t': 2,
        'Concentration\t': 2,
        'Memory\t': 2,
        'Temperament\t': 2,
        'Patience\t': 2,
        'Satisfaction/content\t': 2,
        'While making decisions\t': 2,
        'Activities\t': 2,
        'Nature of dreams\t': 2,
        'Friendships & relations\t': 2,
        'Faith in God\t': 2,
        'Self-control\t': 2,
        'Gratefulness\t': 2,
        'Likings\t': 2,
        'Liking- type of food': 2,
        'Politeness/humbleness':2,
        'Biting nails ': 1,
        'Fond of praise ': 1,
        'Brave': 1,
        'Egoistic': 1
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())
```

---

## 📊 Model Evaluation

### 🧠 Important Features
![image](https://github.com/user-attachments/assets/25839d69-fdf3-4d2a-89e0-32e01967b984)

`🔲 Image showing feature importances from the XGBoost model`

---

### 📈 Classification Report
![image](https://github.com/user-attachments/assets/cad84af7-7430-4e97-b292-7b29af5fa3d4)

`🔲 Screenshot or plot of precision, recall, f1-score for each class`

---

### 🔄 Confusion Matrix
![image](https://github.com/user-attachments/assets/e3b82bae-f6b2-4e44-96e6-1c7f8d3f5fb1)

`🔲 Visualization of confusion matrix - heatmap preferred`

---


---

## 🙏 Acknowledgement

Built using inspiration from **Ayurveda Prakriti** concept – integrating technology and tradition for personalized well-being.

