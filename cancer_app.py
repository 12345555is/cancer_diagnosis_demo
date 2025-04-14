import streamlit as st
from PIL import Image

st.set_page_config(page_title="סרטן - זיהוי דיגיטלי", layout="centered")

# 🎨 עיצוב עמוד
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #1e90ff;
    }
    .title {
        font-size: 32px;
        color: #1e90ff;
        text-align: center;
    }
    .footer {
        text-align: center;
        font-size: 12px;
        color: gray;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">🔬 זיהוי סוג סרטן - אבחון ראשוני</div>', unsafe_allow_html=True)

# תמונה של מדע
st.image("https://cdn.pixabay.com/photo/2021/10/19/07/43/microscope-6723003_1280.jpg", use_column_width=True)

# 🧪 שאלות
st.write("ענו על השאלות הבאות כדי לקבל אבחון ראשוני:")

age = st.slider("מה הגיל שלך?", 1, 100, 30)
gender = st.radio("מין", ["זכר", "נקבה"])
symptoms = st.multiselect(
    "בחר את הסימפטומים שאתה חווה:",
    ["עייפות קבועה", "כאבים באיבר מסוים", "ירידה במשקל", "נפיחות", "קשיי נשימה", "דם בצואה", "שיעול כרוני", "כאבי ראש קבועים"]
)
history = st.selectbox("האם יש היסטוריה משפחתית של סרטן?", ["לא", "כן - סרטן ריאות", "כן - סרטן מעי", "כן - סרטן שד", "כן - אחר"])

# 🔍 ניתוח ראשוני
if st.button("🔍 נתח את התשובות שלי"):
    result = "סרטן לא מזוהה במדויק, התייעץ עם רופא. 😐"
    color = "gray"

    if "שיעול כרוני" in symptoms or "קשיי נשימה" in symptoms:
        result = "יתכן ומדובר בסרטן ריאות. 🫁"
        color = "red"

    elif "דם בצואה" in symptoms or "ירידה במשקל" in symptoms:
        result = "יתכן ומדובר בסרטן מעי. 🧻"
        color = "orange"

    elif "כאבים באיבר מסוים" in symptoms and gender == "נקבה" and age > 30:
        result = "יתכן ומדובר בסרטן שד. 🎗️"
        color = "pink"

    elif "כאבי ראש קבועים" in symptoms:
        result = "יתכן ומדובר בגידול מוחי. 🧠"
        color = "purple"

    st.markdown(f"<h3 style='color:{color};text-align:center;'>{result}</h3>", unsafe_allow_html=True)

    st.success("🔔 זוהי הערכה ראשונית בלבד. יש לפנות לרופא מוסמך לבדיקות נוספות!")

st.markdown('<div class="footer">נבנה באהבה ע״י צוות מומחים • כל הזכויות שמורות © 2025</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
