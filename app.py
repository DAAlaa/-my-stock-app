import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# عنوان التطبيق
st.title("تحليل أسعار الأسهم وتنبؤاتها")

# إدخال رمز السهم والمدى الزمني
ticker = st.text_input("أدخل رمز السهم:", "AAPL")  # رمز السهم الافتراضي
start_date = st.date_input("اختر تاريخ البداية:", value=pd.to_datetime("2020-01-01"))
end_date = st.date_input("اختر تاريخ النهاية:", value=pd.to_datetime("2024-01-01"))

# زر لتنفيذ العملية
if st.button("جلب البيانات"):
    # جلب البيانات من Yahoo Finance
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        st.error("لا توجد بيانات للرمز المدخل. يرجى التحقق من الرمز.")
    else:
        st.success(f"تم جلب البيانات بنجاح لرمز السهم: {ticker}")
        st.write(data.head())

        # عرض الأسعار على شكل رسم بياني
        st.line_chart(data['Close'])

        # حساب المتوسطات المتحركة
        data['SMA_20'] = data['Close'].rolling(window=20).mean()
        data['SMA_50'] = data['Close'].rolling(window=50).mean()

        # رسم المتوسطات المتحركة
        plt.figure(figsize=(10, 5))
        plt.plot(data['Close'], label='Close Price')
        plt.plot(data['SMA_20'], label='SMA 20 يوم')
        plt.plot(data['SMA_50'], label='SMA 50 يوم')
        plt.title("أسعار الإغلاق مع المتوسطات المتحركة")
        plt.xlabel("التاريخ")
        plt.ylabel("السعر")
        plt.legend()
        st.pyplot(plt)

