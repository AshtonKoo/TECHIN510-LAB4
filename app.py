"""
Change this to a world clock app
"""
import streamlit as st
from datetime import datetime
import pytz

import time
def get_current_time_in_zone(zone):
    timezone = pytz.timezone(zone)
    return datetime.now(timezone)

import streamlit as st
st.title('World Clock')

placeholder = st.empty()
locations = ['Asia/Tokyo', 'Europe/London', 'America/New_York', 'Australia/Sydney']
selected_locations = st.multiselect('Select up to four locations:', locations, default=locations[0])

cnt = 0
while True:
    with placeholder.container():
        placeholder.metric("Seconds since you arrived this page", cnt)
        cnt += 1
    time.sleep(1)
for location in selected_locations:
    current_time = get_current_time_in_zone(location)
    st.write(f"{location}Current Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
