import streamlit as st
from datetime import datetime
import pytz
import time

def display_time():
    # 创建一个空的容器
    placeholder = st.empty()

    # 获取用户选择的时区
    locations = ['Asia/Tokyo', 'Europe/London', 'America/New_York', 'Australia/Sydney']
    selected_locations = st.multiselect('Select up to 4 locations:', locations, default=locations[0])
    
    # 每秒更新一次时间
    while True:
        with placeholder.container():
            # 对于每个选定的位置，显示当前时间
            for location in selected_locations:
                timezone = pytz.timezone(location)
                current_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
                st.metric(label=f"Time in {location}", value=current_time)
        
        # 暂停一秒再次更新时间
        time.sleep(1)

# 确保这个函数只在应用第一次运行时被调用
if 'time_initialized' not in st.session_state:
    st.session_state['time_initialized'] = True
    display_time()
