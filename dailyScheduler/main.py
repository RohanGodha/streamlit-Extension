import streamlit as st
import random

# Title of the app
st.title("Daily Schedule")

# Define the schedule
schedule = [
    ("05:00 - 06:00", "Wake Up, Warm Water, Brush, Bath, Drink 500mL Milk+Dryfruits+Amla, YT(Playlist)"),
    ("06:00 AM - 08:30 AM", "Study"),
    ("08:30 AM - 05:00 PM", "College/Lunch/Self Study"),
    ("05:00 PM - 06:00 PM", "1 Hour of Sleep (Yoga Nindra 3rd Eye Opener)"),
    ("06:00 PM - 08:30 PM", "Milk Buying, Dinner, Home Conversation"),
    ("08:30 PM - 11:30 PM", "Study (Preferred: DSA)"),
    ("11:30 PM - 01:30 AM", "Study + 250 mL Milk with Haldi/Plain/Coffee/Chai"),
    ("01:30 AM - 05:00 AM", "Sleep (Yoga Nindra 3rd Eye Opener)")
]

# Custom CSS styles
css = """
    <style>
        .schedule {
            font-weight: bold;
            font-style: italic;
            color: #ffffff;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            background-size: cover;
            background-position: center;
        }

        .schedule-image {
            background-repeat: no-repeat;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# List of background images
background_images = ["https://github.com/RohanGodha/streamlit-Extension/blob/main/dailyScheduler/image1.jpg", 
                     "https://github.com/RohanGodha/streamlit-Extension/blob/main/dailyScheduler/image2.jpg",
                     "https://github.com/RohanGodha/streamlit-Extension/blob/main/dailyScheduler/image3.jpg",
                     "https://github.com/RohanGodha/streamlit-Extension/blob/main/dailyScheduler/image4.jpg"
                    ]

# Create checkboxes for each activity
for time_slot, activity in schedule:
    activity_checked = st.checkbox(label=f"{time_slot}: {activity}")
    if activity_checked:
        edited_activity = st.text_input(label="Edit activity:", value=activity)
        if edited_activity:
            activity = edited_activity
    random_image = random.choice(background_images)
    activity_style = f'<div class="schedule schedule-image" style="background-image: url(\'{random_image}\');">{time_slot}: {activity}</div>'
    st.markdown(activity_style, unsafe_allow_html=True)
