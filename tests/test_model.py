import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

def test_model_loading():
    """Test if the model and label encoder can be loaded correctly"""
    try:
        model = joblib.load('models/xgb_prakruthi_model.pkl')
        le = joblib.load('models/label_encoder.pkl')
        print("✅ Model and label encoder loaded successfully")
        return model, le
    except Exception as e:
        print(f"❌ Failed to load model or label encoder: {str(e)}")
        return None, None

def create_test_input():
    """Create a test input with various Dosha combinations"""
    # Create test cases - one for each primary Dosha type
    columns = [
        'Hair quality', 'Hair texture', 'Hair fall', 'Hair growth speed',
        'Weather preference', 'Skin moisture', 'Thirst', 'Hunger', 'Face glow',
        'Bowel movement', 'Travel sickness', 'Sleep quality', 'Night water requirement',
        'Money spending habit', 'Learning ability', 'Memory strength',
        'Patience', 'Decision making', 'Faith', 'Cleanliness',
        'Communicaion skill', 'Speech style', 'Speech speed', 'Nature of competition',
        'Stamina', 'Body weight', 'Sweating', 'Urine smell', 'Voice',
        'Attitude', 'Response to problems', 'Weather dislike', 'Body temperature',
        'Fat distribution', 'Digestion strength', 'Eye size', 'Weight gain',
        'Urine color', 'Menstrual cycle (for females only)', 'Skin complexion', 'Body structure',
        'Food habits', 'Food behavior', 'Trust level'
    ]
    
    # Test case 1: Predominantly Pitta (value 1)
    pitta_case = [1] * len(columns)
    
    # Test case 2: Predominantly Vata (value 2)
    vata_case = [2] * len(columns)
    
    # Test case 3: Predominantly Kapha (value 3)
    kapha_case = [3] * len(columns)
    
    # Test case 4: Mixed Pitta-Vata
    pitta_vata_case = []
    for i in range(len(columns)):
        if i % 2 == 0:
            pitta_vata_case.append(1)  # Pitta
        else:
            pitta_vata_case.append(2)  # Vata
    
    # Test case 5: Mixed Pitta-Kapha
    pitta_kapha_case = []
    for i in range(len(columns)):
        if i % 2 == 0:
            pitta_kapha_case.append(1)  # Pitta
        else:
            pitta_kapha_case.append(3)  # Kapha
    
    # Create DataFrame with all test cases
    test_data = pd.DataFrame([
        pitta_case,
        vata_case,
        kapha_case,
        pitta_vata_case,
        pitta_kapha_case
    ], columns=columns)
    
    expected_labels = ['Pittaj', 'Vataj', 'Kaphaj', 'Pittaj-Vataj', 'Pittaj-Kaphaj']
    
    return test_data, expected_labels

def test_model_prediction(model, le, test_data, expected_labels):
    """Test model prediction functionality"""
    if model is None or le is None:
        return
    
    try:
        # Make predictions
        predictions = model.predict(test_data)
        predicted_labels = le.inverse_transform(predictions)
        
        # Get probabilities
        probabilities = model.predict_proba(test_data)
        
        print("\n===== TEST RESULTS =====")
        print("Test Cases:")
        for i, (pred_label, exp_label) in enumerate(zip(predicted_labels, expected_labels)):
            print(f"Case {i+1}:")
            print(f"  Predicted: {pred_label}")
            print(f"  Expected: {exp_label}")
            print(f"  Match: {'✓' if pred_label == exp_label else '✗'}")
            
            # Show top 3 probabilities for this case
            probs = {le.inverse_transform([j])[0]: prob for j, prob in enumerate(probabilities[i])}
            top_probs = sorted(probs.items(), key=lambda x: x[1], reverse=True)[:3]
            print("  Top probabilities:")
            for dosha, prob in top_probs:
                print(f"    {dosha}: {prob:.4f}")
            print()
            
        print("✅ Model prediction test completed")
        
    except Exception as e:
        print(f"❌ Model prediction test failed: {str(e)}")

def test_with_sample_data(model, le):
    """Test model with a sample from the original dataset"""
    try:
        # Try to load a small sample of the original dataset
        sample_url = "https://raw.githubusercontent.com/SebastianBenjamin/MLDataSets/refs/heads/main/Prakriti%20Nishchitikaran%20Questionnaire_data.csv"
        sample_data = pd.read_csv(sample_url)
        
        # Drop the same columns as in the training script
        cols_to_drop = ["Name", "Username", "Age group", "City", "Are you diabetic?",
                        "Do you have high/low BP problem?", "Generosity  ", "Stealing/hiding/plagiarism ",
                        "Jealous/strife ", "Stiff body", "Never surrender ", "Forgiveness\t", "Enmity"]
        sample_data.drop(columns=cols_to_drop, inplace=True)
        sample_data.dropna(inplace=True)
        
        # Take just 5 random samples
        if len(sample_data) > 5:
            sample_data = sample_data.sample(5, random_state=42)
        
        # Make predictions
        predictions = model.predict(sample_data)
        predicted_labels = le.inverse_transform(predictions)
        
        print("\n===== SAMPLE DATA TEST =====")
        print(f"Number of samples: {len(sample_data)}")
        print(f"Predictions: {predicted_labels}")
        print("✅ Sample data test completed")
        
    except Exception as e:
        print(f"❌ Sample data test failed: {str(e)}")
        print("Skipping sample data test. This is not critical if you don't have access to the original dataset.")

def plot_feature_importance(model, columns):
    """Plot feature importance"""
    try:
        importance = model.feature_importances_
        # Sort feature importance in descending order
        sorted_idx = importance.argsort()[::-1]
        
        # Plot top 15 features
        plt.figure(figsize=(10, 8))
        plt.barh(range(15), importance[sorted_idx][:15])
        plt.yticks(range(15), [columns[i] for i in sorted_idx][:15])
        plt.title('Top 15 Feature Importance')
        plt.xlabel('Importance')
        plt.tight_layout()
        plt.savefig('feature_importance_test.png')
        print("✅ Feature importance plot saved as 'feature_importance_test.png'")
    except Exception as e:
        print(f"❌ Feature importance plotting failed: {str(e)}")

def main():
    """Main function to run all tests"""
    print("===== TESTING DOSHA PREDICTION MODEL =====")
    
    # Test model loading
    model, le = test_model_loading()
    
    if model is not None and le is not None:
        # Get test data
        test_data, expected_labels = create_test_input()
        
        # Test model prediction
        test_model_prediction(model, le, test_data, expected_labels)
        
        # Test with sample data from original dataset
        test_with_sample_data(model, le)
        
        # Plot feature importance
        plot_feature_importance(model, test_data.columns)
        
        print("\n===== ALL TESTS COMPLETED =====")
    else:
        print("\n❌ Tests failed: Could not load model or label encoder")

if __name__ == "__main__":
    main()