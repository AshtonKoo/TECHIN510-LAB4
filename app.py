import streamlit as st
from datetime import datetime
import pytz

def get_current_time_in_zone(zone):
    timezone = pytz.timezone(zone)
    return datetime.now(timezone)

st.title('World Clock')

locations = ['Asia/Tokyo', 'Europe/London', 'America/New_York', 'Australia/Sydney']
selected_locations = st.multiselect('Select up to four locations:', locations, default=locations[0])

for location in selected_locations:
    current_time = get_current_time_in_zone(location)
    st.write(f"{location}Current Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
