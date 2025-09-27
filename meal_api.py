import requests
import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()
SPOON_KEY = os.getenv("SPOONACULAR_API_KEY")


def get_meal_plan(calories=2000, timeframe="day"):
    """
    Fetch meal plan from Spoonacular API.
    
    Args:
        calories (int): Target calories per day
        timeframe (str): "day" or "week"
    
    Returns:
        dict or None
    """
    url = (
        f"https://api.spoonacular.com/mealplanner/generate"
        f"?timeFrame={timeframe}&targetCalories={calories}&apiKey={SPOON_KEY}"
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("❌ Spoonacular error:", response.text)
        return None


def format_meal_plan(meal_plan):
    """
    Format meal plan into a printable string/list for display.
    
    Args:
        meal_plan (dict): JSON response from API
    
    Returns:
        list of dict
    """
    if not meal_plan or "meals" not in meal_plan:
        return []

    meals = []
    for meal in meal_plan["meals"]:
        meals.append({
            "title": meal["title"],
            "ready_in": meal["readyInMinutes"],
            "servings": meal["servings"],
            "url": meal["sourceUrl"]
        })
    return meals
