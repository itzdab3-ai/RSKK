import streamlit as st
import random
import requests
from user_agent import generate_user_agent
import time

# --- إعداد الصفحة (يجب أن يكون أول سطر) ---
st.set_page_config(page_title="علـش GX1GX1", layout="centered")

# --- التنسيق (خلفية سوداء وإطار ذهبي) ---
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
    /* جعل الأزرار ذهبية */
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

# --- قائمة Device IDs (كاملة كما طلبت) ---
DEVICE_LIST = [
    "7569686276958406176:7569686357842675489:SO-51A:sony:58a9c9ab3a0e5b1f:625e1351-a2ba-4576-b421-2d3825d7fdc5",
    "7569686186635347488:7569686353766041376:SO-51A:sony:b9dddea1d47783ea:24ff104a-e595-48df-8731-724949a542da",
    "7569686276958455328:7569686376536098593:SO-51A:sony:c219ba7a200a81e9:b1c95edb-4b32-4bd6-8423-56b589e8fc94",
    "7569686276958504480:7569686412186912544:SO-51A:sony:737b632f6a7725a4:8896aef6-cdf1-4619-b089-c492edc624ad",
    "7569686164372178465:7569686376536049441:SO-51A:sony:c87b365e7a2ad487:3594c6c1-275c-4ac5-bfcf-3b0bd14c3f76",
    "7569686273640990241:7569686357842855713:SO-51A:sony:94ad416dd6598687:740ce665-a1dc-4dad-99f2-a47da2fb6a26",
    "7569686273640924705:7569686376536196897:SO-51A:sony:f2b3634c4864341f:e0d14804-06fc-4863-841c-a84186670011",
    "7569686186635494944:7569686357842872097:SO-51A:sony:82ed2da06c95e6c1:53a173ee-bb6a-4665-b9f2-e8a99fa0705b",
    "7569686276958635552:7569686381229688608:SO-51A:sony:f2298e84d2bd60ef:1180772d-f4c3-4ce3-abb3-51af3f508ac2",
    "7569686273640859169:7569686376536033057:SO-51A:sony:d2fdac30dfbc1ce7:a0de57cc-25b7-4f4f-a93c-f2661bd35447",
    "7569686276958537248:7569686357842708257:SO-51A:sony:8837d6053040f9cf:8956c30e-eb8e-4a3c-9f67-bad30f79ea62",
    "7569686276958668320:7569686412187060000:SO-51A:sony:c8cc0827278ec4d6:a4538591-2d12-4aae-a9fd-794709e1b773",
    "7569686164372194849:7569686381229557536:SO-51A:sony:5ea1798d8f96fc61:8f5c1a38-c9e5-45d7-9df9-5de7011f4e41",
    "7569686164372244001:7569686412186994464:SO-51A:sony:317a74ac677f2b7d:9087bbb1-919a-48c0-9dd9-99d8b048cd83",
    "7569686186635413024:7569686381229623072:SO-51A:sony:c344616f5cd35874:388cb2db-7fa0-405e-8759-6ce7fe98600f",
    "7569686276958422560:7569686381229524768:SO-51A:sony:16c4776b70c10dee:cedc9ff3-f4d9-4ec7-a939-b4d713019aec",
    "7569686276958553632:7569686381229590304:SO-51A:sony:82c85a60095825c5:c740e93a-2aa2-4719-9740-61ce8c5f169f",
    "7569686186635511328:7569686412187043616:SO-51A:sony:118201aeff30b8c3:e41f9d58-baec-430f-a0a9-5bcfb1ce63f5",
    "7569686273640842785:7569686412186879776:SO-51A:sony:e84b6f397bab4f45:23e7981b-4a00-4834-8ae3-2be224b56ee5",
    "7569686273640826401:7569686381229541152:SO-51A:sony:912010c6c191dbf5:d82f058b-e00f-4444-80a4-c3282941e635",
    "7569686276958619168:7569686376536229665:SO-51A:sony:40b5bed0dbd58da3:f84f5d56-8657-4b63-b8e2-b89ee1621926",
    "7569686276958602784:7569686357842790177:SO-51A:sony:aaf5c35835bd19f6:2787acc0-a6a9-4ce8-bc2e-1120eb97c841",
    "7569686276958471712:7569686376536131361:SO-51A:sony:4fdc2e1e4c7a5cfe:68c9ab74-affd-4152-8580-f8936176db79",
    "7569686276958438944:7569686412186896160:SO-51A:sony:5ebd50580a592b2a:232455ec-c905-44fb-8f12-d0b90b10aee8",
    "7569686186635462176:7569686381229672224:SO-51A:sony:0039768235912241:5e8a1b61-cddb-48c3-a06e-ff0121a4bc5f",
    "7569686273641006625:7569686381229737760:SO-51A:sony:01e923c6a8aa7760:aad27f8f-1958-4a48-acf5-e938652569bd",
    "7569686273640875553:7569686376536082209:SO-51A:sony:7de1415419fa5f22:03dbf997-7e8a-4917-97c6-e99b6e071743",
    "7569686273640891937:7569686376536114977:SO-51A:sony:9f529882e539263a:f59bed87-2572-429c-b760-484ade469ea5",
    "7569686275754559008:7569686357842757409:SO-51A:sony:240189d9531e09a8:47ea91f9-1915-4419-bbb9-d62a9cd57f80",
    "7569686276958586400:7569686381229655840:SO-51A:sony:a0904cdd01793d31:5a832bc3-172e-4805-a5ec-496ec43c0ecb",
    "7569686273640908321:7569686376536180513:SO-51A:sony:409e322c74116c8a:4bc76aee-3827-43b7-9c2f-8abfa1d62faa",
    "7569686186635478560:7569686381229721376:SO-51A:sony:1c25a04de94c7c75:aa7d013a-1716-41d4-a2d3-43d8fc079c48",
    "7569686186635544096:7569686376536262433:SO-51A:sony:e7a4a853afd1a6af:c8872b4b-bc26-459d-9c6d-1f292778af86",
    "7569686186635527712:7569686357842904865:SO-51A:sony:ffa18d16a88bb959:545ecfc7-ef61-4313-8878-652fc2f3409e"
]

# --- عرض الصورة والواجهة ---
st.markdown('<div class="gold-border">', unsafe_allow_html=True)
st.image("https://www.raed.net/img?id=1507882", width=300)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<a href="https://t.me/gx1gx1" class="telegram-link">علـش GX1GX1</a>', unsafe_allow_html=True)

option = st.selectbox("اختر الخدمة:", ["1 – رشق مشاهدات ستوري", "2 – رشق مشاركـات ريــلــز", "3 – رشـق مشاهـدات ريـلـز"])
target_val = st.text_input("اليوزر أو الرابط:")

start_button = st.button("بدء الرشق")

# --- المنطق البرمجي (يبدأ فقط عند الضغط) ---
if start_button:
    if not target_val:
        st.warning("الرجاء كتابة اليوزر أو الرابط")
    else:
        st.success("جاري الرشق... (لا تغلق الصفحة)")
        status_box = st.empty()
        
        # حلقة لانهائية (داخل الزر لتجنب تعليق الصفحة)
        while True:
            # توليد بيانات وهمية جديدة
            fake_ip = f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
            fake_device = random.choice(DEVICE_LIST)
            ua = str(generate_user_agent())
            
            # --- تجهيز البيانات بناءً على كودك الأصلي حرفياً ---
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

            # --- الهيدر (الثابت + المتغير) ---
            hd = {
                'accept': '*/*',
                'accept-language': 'ar-EG',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://leofame.com',
                'priority': 'u=1, i',
                'referer': req_url,
                'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': ua,               # متغير
                'X-Forwarded-For': fake_ip,     # متغير
                'X-Device-ID': fake_device      # متغير
            }

            try:
                # محاولة الإرسال
                req = requests.post(req_url, params={'api': '1'}, cookies=ck, headers=hd, data=dt, timeout=10).text
                
                # فحص النتيجة
                if "Please wait hours" in req or "successfully" in req.lower():
                    status_box.success("✅ تم الرشق بنجاح")
                else:
                    status_box.error("❌ فشل الرشق.. جاري المحاولة")
            except:
                status_box.warning("⚠️ خطأ في الاتصال.. جاري المحاولة")
            
            # انتظار بسيط لتجنب انهيار الصفحة
            time.sleep(0.5)
