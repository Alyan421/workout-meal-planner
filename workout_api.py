import requests
import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()
EXERCISE_KEY = os.getenv("EXERCISE_API_KEY")


def get_exercises(muscle="biceps"):
    """
    Fetch workout exercises from API Ninjas
    
    Args:
        muscle (str): Muscle group to target (e.g., biceps, chest, legs)
    
    Returns:
        list of dict
    """
    url = f"https://api.api-ninjas.com/v1/exercises?muscle={muscle}"
    headers = {"X-Api-Key": EXERCISE_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("❌ API Ninjas error:", response.text)
        return []


def format_exercises(exercises, limit=5):
    """
    Format exercise data for easy display
    
    Args:
        exercises (list): List of exercises (API response)
        limit (int): Number of exercises to return
    
    Returns:
        list of dict
    """
    formatted = []
    for ex in exercises[:limit]:
        formatted.append({
            "name": ex["name"],
            "type": ex["type"],
            "difficulty": ex["difficulty"],
            "instructions": ex["instructions"]
        })
    return formatted
