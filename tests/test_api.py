import requests
import json

# Replace with your actual API URL
url = "https://prakruthinischikaran-api.onrender.com"

# Example data with all features
# Replace these with actual values from your dataset
data = {
    "Hair quality": 1,
    "Hair texture": 1, 
    "Hair fall": 1,
    "Hair growth speed": 1,
    "Weather preference": 1,
    "Skin moisture": 1,
    "Thirst": 1,
    "Hunger": 1,
    "Face glow": 1,
    "Bowel movement": 1,
    "Travel sickness": 1,
    "Sleep quality": 1,
    "Night water requirement": 1,  
    "Money spending habit": 1,
    "Learning ability": 1,
    "Memory strength": 1,
    "Patience": 1,
    "Decision making": 1,
    "Faith": 1,
    "Cleanliness": 1,
    "Communicaion skill": 1,
    "Speech style": 1,
    "Speech speed": 1,
    "Nature of competition": 1,
    "Stamina": 1,
    "Body weight": 1,
    "Sweating": 1,
    "Urine smell": 1,
    "Voice": 1,
    "Attitude": 1,
    "Response to problems": 1,
    "Weather dislike": 1,
    "Body temperature": 1,
    "Fat distribution": 1,
    "Digestion strength": 1,
    "Eye size": 1,
    "Weight gain": 1,
    "Urine color": 1,
    "Menstrual cycle (for females only)": 1,
    "Skin complexion": 1,
    "Body structure": 1,
    "Food habits": 1,
    "Food behavior": 1,
    "Trust level": 1
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())