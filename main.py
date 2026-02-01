import streamlit as st
import random
import requests
import user_agent
from user_agent import generate_user_agent
import time
import os

# --- إعدادات الواجهة الرسومية ---
st.set_page_config(page_title="علـش GX1GX1", layout="centered")

# CSS لإخفاء بصمات ستريم ليت وتنسيق الإطار الذهبي والواجهة
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background-color: #000000; }
    .gold-border {
        border: 4px solid #D4AF37;
        padding: 5px;
        border-radius: 15px;
        box-shadow: 0px 0px 20px #D4AF37;
        margin-bottom: 20px;
        display: inline-block;
    }
    .telegram-link {
        display: block;
        text-align: center;
        background-color: #D4AF37;
        color: black !important;
        font-weight: bold;
        padding: 10px;
        border-radius: 10px;
        text-decoration: none;
        margin-bottom: 20px;
        font-size: 20px;
    }
    .stButton>button {
        background-color: #D4AF37 !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        width: 100%;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- عرض الصورة بالإطار الذهبي ---
st.markdown('<div style="text-align: center;"><div class="gold-border">', unsafe_allow_html=True)
st.image("https://www.raed.net/img?id=1507882", width=350)
st.markdown('</div></div>', unsafe_allow_html=True)

# --- رابط التليجرام المطلوب ---
st.markdown('<a href="https://t.me/gx1gx1" class="telegram-link">علـش GX1GX1</a>', unsafe_allow_html=True)

# --- واجهة الخيارات ---
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>اختر الخدمة المطلوبة:</h3>", unsafe_allow_html=True)
D = st.selectbox("", ["1 – رشق مشاهدات ستوري", "2 – رشق مشاركـات ريــلــز", "3 – رشـق مشاهـدات ريـلـز"])

# --- حقول الإدخال ---
if "1" in D:
    user = st.text_input("حط يوزر حسابك :", key="user_field")
elif "2" in D:
    crl1 = st.text_input("رابط الريلز حقك :", key="link_field1")
else:
    crl = st.text_input("رابط الريلز :", key="link_field2")

start_btn = st.button("بدء الرشق الآن")

# --- دالة توليد IP وهمي لكل طلب ---
def get_random_ip():
    return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

# --- التنفيذ (كودك الأصلي بالكامل) ---
if start_btn:
    status_area = st.empty()
    
    # تحويل الاختيار إلى رقم ليتوافق مع شروط كودك الأصلي
    D_val = D[0] 

    if D_val == '1' and user:
        while True:
            fake_ip = get_random_ip()
            cookies = {
                'token': '65f7a4063b76f95104fb7e13228e9e13',
                'ci_session': 'ccf763e6a521d0ddef1aa5572d1641b99ea39e62',
                'cfzs_google-analytics_v4': '%7B%22mHFS_pageviewCounter%22%3A%7B%22v%22%3A%223%22%7D%7D',
                'cfz_google-analytics_v4': '%7B%22mHFS_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1797026685127%7D%2C%22mHFS_engagementStart%22%3A%7B%22v%22%3A1765490695876%2C%22e%22%3A1797026691204%7D%2C%22mHFS_counter%22%3A%7B%22v%22%3A%2215%22%2C%22e%22%3A1797026685127%7D%2C%22mHFS_session_counter%22%3A%7B%22v%22%3A%223%22%2C%22e%22%3A1797026685127%7D%2C%22mHFS_ga4%22%3A%7B%22v%22%3A%22d62377ee-ab11-44f2-a93b-6c2cb64cee65%22%2C%22e%22%3A1797026685127%7D%2C%22mHFS_let%22%3A%7B%22v%22%3A%221765490685127%22%2C%22e%22%3A1797026685127%7D%2C%22mHFS_ga4sid%22%3A%7B%22v%22%3A%221006956886%22%2C%22e%22%3A1765492485127%7D%7D',
            }
            headers = {
                'accept': '*/*',
                'accept-language': 'ar-EG',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://leofame.com',
                'priority': 'u=1, i',
                'referer': 'https://leofame.com/ar/free-instagram-story-views',
                'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': str(generate_user_agent()),
                'X-Forwarded-For': fake_ip, # IP وهمي جديد
            }
            params = {'api': '1'}
            data = {'token': '65f7a4063b76f95104fb7e13228e9e13', 'timezone_offset': 'Asia/Amman', 'free_link': user}
            try:
                response = requests.post('https://leofame.com/ar/free-instagram-story-views', params=params, cookies=cookies, headers=headers, data=data).text
                if "Please wait hours" in response:
                    status_area.success(' تم رشـق ')
                else:
                    status_area.error(' فشـل بالرشق ')
            except: pass
            time.sleep(0.5)

    if D_val == '2' and crl1:
        while True:
            fake_ip = get_random_ip()
            cookies = {
                'ci_session': 'ccf763e6a521d0ddef1aa5572d1641b99ea39e62',
                'token': 'f99fa6c5a4df2792c19643c30cc5290c',
                'cfzs_google-analytics_v4': '%7B%22mHFS_pageviewCounter%22%3A%7B%22v%22%3A%222%22%7D%7D',
                'cfz_google-analytics_v4': '%7B%22mHFS_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_engagementStart%22%3A%7B%22v%22%3A1765632466422%2C%22e%22%3A1797168466703%7D%2C%22mHFS_counter%22%3A%7B%22v%22%3A%2233%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_session_counter%22%3A%7B%22v%22%3A%226%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_ga4%22%3A%7B%22v%22%3A%22d62377ee-ab11-44f2-ab11-44f2-a93b-6c2cb64cee65%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_let%22%3A%7B%22v%22%3A%221765632459976%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_ga4sid%22%3A%7B%22v%22%3A%22156770422%22%2C%22e%22%3A1765634259976%7D%7D',
            }
            headers = {
                'accept': '*/*',
                'accept-language': 'ar-EG',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://leofame.com',
                'priority': 'u=1, i',
                'referer': 'https://leofame.com/ar/free-instagram-shares',
                'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': str(generate_user_agent()),
                'X-Forwarded-For': fake_ip,
            }
            params = {'api': '1'}
            data = {'token': 'f99fa6c5a4df2792c19643c30cc5290c', 'timezone_offset': 'Asia/Amman', 'free_link': crl1, 'quantity': '100', 'speed': '-1'}
            try:
                response = requests.post('https://leofame.com/ar/free-instagram-shares', params=params, cookies=cookies, headers=headers, data=data).text
                if "Please wait hours" in response:
                    status_area.success(' تم رشـق ')
                else:
                    status_area.error(' فشـل بالرشق ')
            except: pass
            time.sleep(0.5)

    if D_val == '3' and crl:
        while True:
            fake_ip = get_random_ip()
            cookies = {
                'ci_session': 'ccf763e6a521d0ddef1aa5572d1641b99ea39e62',
                'token': 'e7ef36edf9d31e133ffcf756c462210b',
                'cfzs_google-analytics_v4': '%7B%22mHFS_pageviewCounter%22%3A%7B%22v%22%3A%221%22%7D%7D',
                'cfz_google-analytics_v4': '%7B%22mHFS_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1797155143320%7D%2C%22mHFS_engagementStart%22%3A%7B%22v%22%3A1765619149120%2C%22e%22%3A1797155149365%7D%2C%22mHFS_counter%22%3A%7B%22v%22%3A%2226%22%2C%22e%22%3A1797155143320%7D%2C%22mHFS_session_counter%22%3A%7B%22v%22%3A%225%22%2C%22e%22%3A1797155143320%7D%2C%22mHFS_ga4%22%3A%7B%22v%22%3A%22d62377ee-ab11-44f2-a93b-6c2cb64cee65%22%2C%22e%22%3A1797155143320%7D%2C%22mHFS_let%22%3A%7B%22v%22%3A%221765619143320%22%2C%22e%22%3A1797155143320%7D%2C%22mHFS_ga4sid%22%3A%7B%22v%22%3A%22692995886%22%2C%22e%22%3A1765620943320%7D%7D',
            }
            headers = {
                'accept': '*/*',
                'accept-language': 'ar-EG',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://leofame.com',
                'priority': 'u=1, i',
                'referer': 'https://leofame.com/ar/free-instagram-views',
                'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': str(generate_user_agent()),
                'X-Forwarded-For': fake_ip,
            }
            params = {'api': '1'}
            data = {'token': 'e7ef36edf9d31e133ffcf756c462210b', 'timezone_offset': 'Asia/Amman', 'free_link': crl, 'quantity': '200', 'speed': '-1'}
            try:
                response = requests.post('https://leofame.com/ar/free-instagram-views', params=params, cookies=cookies, headers=headers, data=data).text
                if "Please wait hours" in response:
                    status_area.success(' تم رشـق ')
                else:
                    status_area.error(' فشـل بالرشق ')
            except: pass
            time.sleep(0.5)
