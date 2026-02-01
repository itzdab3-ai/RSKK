import streamlit as st
import requests
import random
from user_agent import generate_user_agent
import time

# --- إعدادات الواجهة الاحترافية ---
st.set_page_config(page_title="Instagram Tools", layout="centered")

# CSS لتجميل الواجهة وإخفاء شعارات ستريم ليت
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

# دالة لتوليد IP وهمي عشوائي لكل طلب
def generate_fake_ip():
    return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

# --- عرض الصورة بالإطار الذهبي ---
st.markdown('<div style="text-align: center;"><div class="gold-border">', unsafe_allow_html=True)
st.image("https://www.raed.net/img?id=1507882", width=350)
st.markdown('</div></div>', unsafe_allow_html=True)

# --- رابط التليجرام المطلوب ---
st.markdown('<a href="https://t.me/gx1gx1" class="telegram-link">علـش GX1GX1</a>', unsafe_allow_html=True)

# --- قائمة الخيارات ---
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>اختر الخدمة:</h3>", unsafe_allow_html=True)
choice = st.selectbox("", ["1 – رشق مشاهدات ستوري", "2 – رشق مشاركـات ريــلــز", "3 – رشـق مشاهـدات ريـلـز"])

# --- حقول الإدخال ---
if "1" in choice:
    user_input = st.text_input("حط يوزر حسابك :", key="u1")
else:
    user_input = st.text_input("رابط الريلز :", key="u2")

start_btn = st.button("بدء الرشق")

if start_btn and user_input:
    status_area = st.empty()
    
    # حلقة لانهائية لمحاولة الرشق حتى النجاح
    while True:
        # توليد معلومات وهمية جديدة لكل محاولة
        fake_ip = generate_fake_ip()
        new_ua = generate_user_agent()
        
        # اختيار البيانات بناءً على النوع (مع الحفاظ على الكوكيز والتوكنز الأصلية)
        if "1" in choice:
            url = 'https://leofame.com/ar/free-instagram-story-views'
            token = '65f7a4063b76f95104fb7e13228e9e13'
            post_data = {'token': token, 'timezone_offset': 'Asia/Amman', 'free_link': user_input}
        elif "2" in choice:
            url = 'https://leofame.com/ar/free-instagram-shares'
            token = 'f99fa6c5a4df2792c19643c30cc5290c'
            post_data = {'token': token, 'timezone_offset': 'Asia/Amman', 'free_link': user_input, 'quantity': '100', 'speed': '-1'}
        else:
            url = 'https://leofame.com/ar/free-instagram-views'
            token = 'e7ef36edf9d31e133ffcf756c462210b'
            post_data = {'token': token, 'timezone_offset': 'Asia/Amman', 'free_link': user_input, 'quantity': '200', 'speed': '-1'}

        # إضافة الـ IP الوهمي والـ User-Agent الجديد للهيدرز
        headers = {
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'x-forwarded-for': fake_ip,
            'x-real-ip': fake_ip,
            'user-agent': new_ua,
            'referer': url
        }

        try:
            response = requests.post(url, params={'api': '1'}, data=post_data, headers=headers, timeout=10).text
            
            if "Please wait hours" in response or "successfully" in response.lower():
                status_area.success('✅ تم رشـق')
                # نتوقف عند أول نجاح أو نستمر (حسب رغبتك)، الكود هنا سيستمر لضمان أقصى رشق
            else:
                status_area.error('❌ فشـل بالرشق')
        
        except:
            status_area.error('❌ خطأ في الاتصال.. محاولة جديدة')
        
        # سرعة المحاولات (تأخير بسيط جداً لتجنب تجميد الصفحة)
        time.sleep(0.5)

