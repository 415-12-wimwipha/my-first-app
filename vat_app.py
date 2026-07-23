import streamlit as st
st.title("แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
net_price = price - vat
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write("นางสาววิมพ์วิภา ชัยภัทรกุลภรณ์ เลขที่ 12  ม.4/15")
