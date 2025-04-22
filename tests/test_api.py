import requests
import json

# Replace with your actual API URL
url = "http://127.0.0.1:5000"

# Example data with all features
# Replace these with actual values from your dataset
data = {
    "Hair quality": 1,
    "Hair texture": 1, 
    "Hair fall": 1,
    "Hair growth speed": 1,
    "Weather preference": 1,
    "Skin moisture": 2,
    "Thirst": 2,
    "Hunger": 2,
    "Face glow": 2,
    "Bowel movement": 2,
    "Travel sickness": 2,
    "Sleep quality": 2,
    "Night water requirement": 2,  
    "Money spending habit": 2,
    "Learning ability": 2,
    "Memory strength": 2,
    "Patience": 2,
    "Decision making": 2,
    "Faith": 1,
    "Cleanliness": 1,
    "Communicaion skill": 1,
    "Speech style": 2,
    "Speech speed": 2,
    "Nature of competition": 2,
    "Stamina": 2,
    "Body weight": 2,
    "Sweating": 2,
    "Urine smell": 2,
    "Voice": 2,
    "Attitude": 2,
    "Response to problems": 2,
    "Weather dislike": 2,
    "Body temperature": 2,
    "Fat distribution": 2,
    "Digestion strength": 2,
    "Eye size": 2,
    "Weight gain": 2,
    "Urine color": 2,
    "Menstrual cycle (for females only)": 2,
    "Skin complexion": 2,
    "Body structure": 1,
    "Food habits": 1,
    "Food behavior": 1,
    "Trust level": 1
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())