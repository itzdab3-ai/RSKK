import streamlit as st
import random
import requests
from user_agent import generate_user_agent
import time

# --- إعداد الصفحة ---
st.set_page_config(page_title="علـش GX1GX1", layout="centered")

# --- التنسيق البصري الاحترافي ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .gold-border {
        border: 4px solid #D4AF37;
        padding: 10px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0px 0px 15px #D4AF37;
    }
    .telegram-link {
        display: block;
        text-align: center;
        background-color: #D4AF37;
        color: black !important;
        font-weight: bold;
        padding: 12px;
        border-radius: 10px;
        text-decoration: none;
        margin: 15px 0;
        font-size: 18px;
    }
    .stButton>button {
        background-color: #D4AF37 !important;
        color: black !important;
        font-weight: bold !important;
        width: 100%;
        border-radius: 10px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- دالة لتوليد هوية جهاز عشوائية تماماً ---
def generate_random_device_id():
    part1 = str(random.randint(7000000000000000000, 7999999999999999999))
    part2 = str(random.randint(7000000000000000000, 7999999999999999999))
    models = ["SO-51A", "SM-G998B", "Pixel-6", "RMX3085", "M2101K6G", "iPhone13,4"]
    brands = ["sony", "samsung", "google", "realme", "xiaomi", "apple"]
    idx = random.randint(0, len(models)-1)
    hex_id = "".join(random.choices("0123456789abcdef", k=16))
    uuid_val = f"{random.randint(10000000,99999999)}-{random.randint(1000,9999)}-4bd6-8423-56b589e8fc94"
    return f"{part1}:{part2}:{models[idx]}:{brands[idx]}:{hex_id}:{uuid_val}"

# --- عرض الواجهة ---
st.markdown('<div class="gold-border">', unsafe_allow_html=True)
st.image("https://www.raed.net/img?id=1507882", width=300)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<a href="https://t.me/gx1gx1" class="telegram-link">علـش GX1GX1</a>', unsafe_allow_html=True)

option = st.selectbox("اختر الخدمة:", ["1 – رشق مشاهدات ستوري", "2 – رشق مشاركـات ريــلــز", "3 – رشـق مشاهـدات ريـلـز"])
target_val = st.text_input("اليوزر أو الرابط:")

start_button = st.button("بدء الرشق")

if start_button:
    if not target_val:
        st.warning("الرجاء كتابة اليوزر أو الرابط")
    else:
        st.success("جاري الرشق بتغيير بيانات الجهاز والدولة تلقائياً...")
        status_box = st.empty()
        
        while True:
            # 1. تغيير الدولة (توليد IP عشوائي عالمي)
            fake_ip = f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
            
            # 2. تغيير الجهاز (توليد Device ID جديد كلياً)
            fake_device = generate_random_device_id()
            
            # 3. تغيير المتصفح (User Agent)
            ua = str(generate_user_agent())
            
            # --- الحفاظ على كافة بياناتك الأصلية بدون حذف حرف واحد ---
            if "1" in option:
                req_url = 'https://leofame.com/ar/free-instagram-story-views'
                ck = {
                    'token': '65f7a4063b76f95104fb7e13228e9e13',
                    'ci_session': 'ccf763e6a521d0ddef1aa5572d1641b99ea39e62',
                    'cfzs_google-analytics_v4': '%7B%22mHFS_pageviewCounter%22%3A%7B%22v%22%3A%223%22%7D%7D',
                    'cfz_google-analytics_v4': '%7B%22mHFS_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1797026685127%7D%2C%22mHFS_engagementStart%22%3A%7B%22v%22%3A1765490695876%2C%22e%22%3A1797026691204%7D%2C%22mHFS_counter%22%3A%7B%22v%22%3A%2215%22%2C%22e%22%3A1797026685127%7D%2C%22mHFS_session_counter%22%3A%7B%22v%22%3A%223%22%2C%22e%22%3A1797026685127%7D%2C%22mHFS_ga4%22%3A%7B%22v%22%3A%22d62377ee-ab11-44f2-a93b-6c2cb64cee65%22%2C%22e%22%3A1797026685127%7D%2C%22mHFS_let%22%3A%7B%22v%22%3A%221765490685127%22%2C%22e%22%3A1797026685127%7D%2C%22mHFS_ga4sid%22%3A%7B%22v%22%3A%221006956886%22%2C%22e%22%3A1765492485127%7D%7D',
                }
                dt = {'token': '65f7a4063b76f95104fb7e13228e9e13', 'timezone_offset': 'Asia/Amman', 'free_link': target_val}
            elif "2" in option:
                req_url = 'https://leofame.com/ar/free-instagram-shares'
                ck = {
                    'ci_session': 'ccf763e6a521d0ddef1aa5572d1641b99ea39e62',
                    'token': 'f99fa6c5a4df2792c19643c30cc5290c',
                    'cfzs_google-analytics_v4': '%7B%22mHFS_pageviewCounter%22%3A%7B%22v%22%3A%222%22%7D%7D',
                    'cfz_google-analytics_v4': '%7B%22mHFS_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_engagementStart%22%3A%7B%22v%22%3A1765632466422%2C%22e%22%3A1797168466703%7D%2C%22mHFS_counter%22%3A%7B%22v%22%3A%2233%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_session_counter%22%3A%7B%22v%22%3A%226%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_ga4%22%3A%7B%22v%22%3A%22d62377ee-ab11-44f2-a93b-6c2cb64cee65%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_let%22%3A%7B%22v%22%3A%221765632459976%22%2C%22e%22%3A1797168459976%7D%2C%22mHFS_ga4sid%22%3A%7B%22v%22%3A%22156770422%22%2C%22e%22%3A1765634259976%7D%7D',
                }
                dt = {'token': 'f99fa6c5a4df2792c19643c30cc5290c', 'timezone_offset': 'Asia/Amman', 'free_link': target_val, 'quantity': '100', 'speed': '-1'}
            else:
                req_url = 'https://leofame.com/ar/free-instagram-views'
                ck = {
                    'ci_session': 'ccf763e6a521d0ddef1aa5572d1641b99ea39e62',
                    'token': 'e7ef36edf9d31e133ffcf756c462210b',
                    'cfzs_google-analytics_v4': '%7B%22mHFS_pageviewCounter%22%3A%7B%22v%22%3A%221%22%7D%7D',
                    'cfz_google-analytics_v4': '%7B%22mHFS_engagementDuration%22%3A%7B%22v%22%3A%220%22%2C%22e%22%3A1797155143320%7D%2C%22mHFS_engagementStart%22%3A%7B%22v%22%3A1765619149120%2C%22e%22%3A1797155149365%7D%2C%22mHFS_counter%22%3A%7B%22v%22%3A%2226%22%2C%22e%22%3A1797155143320%7D%2C%22mHFS_session_counter%22%3A%7B%22v%22%3A%225%22%2C%22e%22%3A1797155143320%7D%2C%22mHFS_ga4%22%3A%7B%22v%22%3A%22d62377ee-ab11-44f2-a93b-6c2cb64cee65%22%2C%22e%22%3A1797155143320%7D%2C%22mHFS_let%22%3A%7B%22v%22%3A%221765619143320%22%2C%22e%22%3A1797155143320%7D%2C%22mHFS_ga4sid%22%3A%7B%22v%22%3A%22692995886%22%2C%22e%22%3A1765620943320%7D%7D',
                }
                dt = {'token': 'e7ef36edf9d31e133ffcf756c462210b', 'timezone_offset': 'Asia/Amman', 'free_link': target_val, 'quantity': '200', 'speed': '-1'}

            # الهيدر المدمج (الثابت + المتغيرات الجديدة)
            hd = {
                'accept': '*/*',
                'accept-language': 'ar-EG',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://leofame.com',
                'referer': req_url,
                'user-agent': ua,
                'X-Forwarded-For': fake_ip,
                'X-Device-ID': fake_device
            }

            try:
                response = requests.post(req_url, params={'api': '1'}, cookies=ck, headers=hd, data=dt, timeout=10).text
                if "successfully" in response.lower() or "Please wait" in response:
                    status_box.success(f"✅ تم الرشق | الدولة: عشوائي | الجهاز: {fake_device.split(':')[2]}")
                else:
                    status_box.error("❌ فشل الرشق.. جاري المحاولة ببيانات جديدة")
            except:
                status_box.warning("⚠️ مشكلة في الاتصال.. جاري إعادة المحاولة")
            
            time.sleep(1)
