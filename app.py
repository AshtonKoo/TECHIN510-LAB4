import streamlit as st
from datetime import datetime
import pytz

def get_current_time_in_zone(zone):
    timezone = pytz.timezone(zone)
    return datetime.now(timezone)

st.title('World Clock')

locations = ['Asia/Tokyo', 'Europe/London', 'America/New_York', 'Australia/Sydney']
selected_locations = st.multiselect('Select up to four locations:', locations, default=locations[0])

time_container = st.empty()

st_autorefresh_interval = st.experimental_get_query_params().get("autorefresh", [1000])[0]  # 设置自动刷新间隔为1000毫秒（1秒）
st.experimental_set_query_params(autorefresh=st_autorefresh_interval)  # 为URL设置自动刷新查询参数

for location in selected_locations:
    current_time = get_current_time_in_zone(location)
    time_container.write(f"{location} Current Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
