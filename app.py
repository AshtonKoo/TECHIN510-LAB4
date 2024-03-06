import time
from datetime import datetime
import pytz
import streamlit as st

placeholder = st.empty()

timezones = {
    "Tokyo": "Asia/Tokyo",
    "London": "Europe/London",
    "New York": "America/New_York",
    "Sydney": "Australia/Sydney",
}

while True:
    with placeholder.container():
        st.title("World Clock")
        for city, tz in timezones.items():
            now = datetime.now(pytz.timezone(tz))
            st.write(f"{city}: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(1)
