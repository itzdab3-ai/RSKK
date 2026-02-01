import streamlit as st
import random
import requests
import user_agent
from user_agent import generate_user_agent
import time

# --- إعدادات الواجهة الاحترافية ---
st.set_page_config(page_title="Instagram Booster", layout="centered")

# CSS لإخفاء شعارات ستريم ليت وتصميم الإطار الذهبي والواجهة
st.markdown("""
    <style>
    /* إخفاء شريط ستريم ليت العلوي والقائمة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* تنسيق الخلفية العامة */
    .stApp {
        background-color: #000000;
    }
    
    /* تصميم الإطار الذهبي للصورة */
    .gold-border {
        border: 4px solid #D4AF37;
        padding: 5px;
        border-radius: 15px;
        box-shadow: 0px 0px 20px #D4AF37;
        margin-bottom: 20px;
        display: inline-block;
    }
    
    /* تنسيق النصوص */
    h1, h2, h3, p {
        color: #F - #D4AF37 !important;
        text-align: center;
    }
    
    /* تنسيق الأزرار */
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

st.markdown("<h1 style='color: #D4AF37;'>مرحباً بك في أداة ملهم السرحاني</h1>", unsafe_allow_html=True)

# --- قائمة الخيارات ---
st.markdown("<h3 style='text-align: right;'>اختر الخدمة المطلوبة:</h3>", unsafe_allow_html=True)
choice = st.radio("", ["1 – رشق مشاهدات ستوري", "2 – رشق مشاركـات ريــلــز", "3 – رشـق مشاهـدات ريـلـز"])

# --- حقول الإدخال ---
if "1" in choice:
    user_input = st.text_input("حط يوزر حسابك :", placeholder="مثال: m_sarhani")
elif "2" in choice:
    user_input = st.text_input("رابط الريلز حقك :", placeholder="ضع الرابط هنا...")
else:
    user_input = st.text_input("رابط الريلز :", placeholder="ضع الرابط هنا...")

start_btn = st.button("بدء عملية الرشق الآن")

# --- التنفيذ (بدون حذف أي حرف من الكوكيز أو الهيدرز) ---
if start_btn and user_input:
    status_box = st.empty()
    log_area = st.empty()
    
    if "1" in choice:
        # --- كود رشق الستوري (Copy-Paste من كودك الأصلي) ---
        while True:
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
            }
            params = {'api': '1'}
            data = {'token': '65f7a4063b76f95104fb7e13228e9e13', 'timezone_offset': 'Asia/Amman', 'free_link': user_input}
            
            response = requests.post('https://leofame.com/ar/free-instagram-story-views', params=params, cookies=cookies, headers=headers, data=data).text
            if "Please wait hours" in response:
                status_box.success("✅ تم رشـق مشاهدات الستوري")
            else:
                status_box.error("❌ فشـل بالرشق")
            time.sleep(2)

    elif "2" in choice:
        # --- كود رشق المشاركات (بدون أي تعديل) ---
        while True:
            cookies = {
                'ci_session': 'ccf763e6a521d0ddef1aa5572d1641b99ea39e62',
                'token': 'f99fa6c5a4df2792c19643c30cc5290c',
                'cfzs_google-analytics_v4': '%7B%22mHFS_pageviewCounter%22%3A%7B%22v%22%3A%222%22%7D%7D',
                'cfz_google-analytics_v4': '%7B%22mHFS_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_engagementStart%22%3A%7B%22v%22%3A1765632466422%2C%22e%22%3A1797168466703%7D%2C%22mHFS_counter%22%3A%7B%22v%22%3A%2233%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_session_counter%22%3A%7B%22v%22%3A%226%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_ga4%22%3A%7B%22v%22%3A%22d62377ee-ab11-44f2-a93b-6c2cb64cee65%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_let%22%3A%7B%22v%22%3A%221765632459976%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_ga4sid%22%3A%7B%22v%22%3A%22156770422%22%2C%22e%22%3A1765634259976%7D%7D',
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
            }
            params = {'api': '1'}
            data = {'token': 'f99fa6c5a4df2792c19643c30cc5290c', 'timezone_offset': 'Asia/Amman', 'free_link': user_input, 'quantity': '100', 'speed': '-1'}
            
            response = requests.post('https://leofame.com/ar/free-instagram-shares', params=params, cookies=cookies, headers=headers, data=data).text
            if "Please wait hours" in response:
                status_box.success("✅ تم رشـق مشاركات الريلز")
            else:
                status_box.error("❌ فشـل بالرشق")
            time.sleep(2)

    elif "3" in choice:
        # --- كود رشق المشاهدات (كامل كما هو) ---
        while True:
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
            }
            params = {'api': '1'}
            data = {'token': 'e7ef36edf9d31e133ffcf756c462210b', 'timezone_offset': 'Asia/Amman', 'free_link': user_input, 'quantity': '200', 'speed': '-1'}
            
            response = requests.post('https://leofame.com/ar/free-instagram-views', params=params, cookies=cookies, headers=headers, data=data).text
            if "Please wait hours" in response:
                status_box.success("✅ تم رشـق مشاهدات الريلز")
            else:
                status_box.error("❌ فشـل بالرشق")
            time.sleep(2)
elif start_btn and not user_input:
    st.warning("يرجى إدخال اليوزر أو الرابط أولاً!")
