import streamlit as st
from meal_api import get_meal_plan, format_meal_plan
from workout_api import get_exercises, format_exercises

# ---------------------------
# Streamlit UI
# ---------------------------

st.set_page_config(page_title="AI Fitness & Meal Planner", page_icon="💪", layout="wide")

st.title("💪 Workout + 🍽️ Meal Planner")
st.markdown("Generate a personalized **daily workout & meal plan** with free APIs!")

# Sidebar controls
st.sidebar.header("⚙️ Customize Your Plan")
muscle = st.sidebar.selectbox(
    "Choose muscle group:",
    ["biceps", "triceps", "chest", "back", "legs", "shoulders", "abs"]
)

calories = st.sidebar.slider("Daily Calories:", 1200, 3500, 2000, 100)

if st.sidebar.button("Generate Plan 🚀"):
    # Workout Plan
    st.subheader(f"🏋️ Workout Plan for {muscle.capitalize()}")
    exercises = get_exercises(muscle)
    if exercises:
        workout_list = format_exercises(exercises)
        for ex in workout_list:
            with st.expander(ex['name']):
                st.write(f"**Type:** {ex['type']}")
                st.write(f"**Difficulty:** {ex['difficulty']}")
                st.write("**Instructions:**")
                st.info(ex['instructions'])
    else:
        st.warning("No exercises found (API limit might be reached).")

    # Meal Plan
    st.subheader("🍴 Daily Meal Plan")
    meal_plan = get_meal_plan(calories)
    if meal_plan:
        meals = format_meal_plan(meal_plan)
        cols = st.columns(len(meals)) if meals else []
        for i, meal in enumerate(meals):
            with cols[i]:
                st.markdown(f"**{meal['title']}**")
                st.write(f"⏱ {meal['ready_in']} mins | 🍽 Servings: {meal['servings']}")
                st.write(f"[View Recipe]({meal['url']})")
    else:
        st.warning("Meal plan not available (API limit might be reached).")
