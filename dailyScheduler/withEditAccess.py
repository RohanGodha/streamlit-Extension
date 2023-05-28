import streamlit as st

# Title of the app
st.title("Daily Schedule")

# Define the schedule
schedule = [
    ("05:00 - 06:00", "Wake Up, Warm Water, Brush, Bath, Drink 500mL Milk+Badaam+Akhroat+Amla, YT(Playlist)"),
    ("06:00 - 08:30", "Study"),
    ("08:30 - 05:00", "College/Lunch/Self Study"),
    ("05:00 - 06:00", "1 Hour of Sleep (Yoga Nindra 3rd Eye Opener)"),
    ("06:00 - 08:30", "Milk Buying, Dinner, Home Conversation"),
    ("08:30 - 11:30", "Study (Preferred: DSA)"),
    ("11:30 - 01:30", "Study + 250 mL Milk with Haldi/Plain/Coffee/Chai"),
    ("01:30 - 05:00", "Sleep (Yoga Nindra 3rd Eye Opener)")
]

# Custom CSS styles
css = """
    <style>
        .schedule {
            font-weight: bold;
            font-style: italic;
            background-color: #f1f1f1;
            color: #333333;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# Create checkboxes for each activity
for time_slot, activity in schedule:
    activity_checked = st.checkbox(label=f"{time_slot}: {activity}")
    if activity_checked:
        edited_activity = st.text_input(label="Edit activity:", value=activity)
        if edited_activity:
            activity = edited_activity
    st.markdown(f'<div class="schedule">{time_slot}: {activity}</div>', unsafe_allow_html=True)
