import streamlit as st
import time
import numpy as np
import datetime
import pandas as pd

st.set_page_config(page_title="Prediksi Tahunan", page_icon="📈")

st.markdown("# Grafik Curah Hujan Tahunan")
st.write(
    """Grafik dibawah memperlihatkan hasil forecast curah hujan dalam rentang satu tahun."""
)
selected_year = st.selectbox("Pilih Tahun", [datetime.datetime.now().year, datetime.datetime.now().year + 1])
date = np.load('./assets/date_index.npy')
val = np.load('./assets/rainfall_rate.npy')


if st.button("Prediksi!"):

    st.header(f"Grafik Curah Hujan {selected_year}")
    
    start_date = np.datetime64(datetime.datetime(selected_year, 1, 1))
    end_date = np.datetime64(datetime.datetime(selected_year, 12, 31))
    days = (end_date - start_date).astype('timedelta64[D]').astype(int)
    masks = (date >= start_date) & (date <= end_date)
    indexes = date[masks]
    values = val[masks]
    last_rows = np.array([[values[0]]])
    chart_data = pd.DataFrame({'date': [indexes[0]], 'rainfall': [values[0]]})
    chart = st.line_chart(chart_data.set_index('date'),color='#A8C4BA')

    progress_bar = st.progress(0)

    for i in range(1, values.size):
        new_data = pd.DataFrame({'date': [date[i]], 'rainfall': [values[i]]})
        chart.add_rows(new_data.set_index('date'))
        progress_percentage = int((i / days) * 100)
        progress_bar.progress(progress_percentage)

        time.sleep(0.02)  
    progress_bar.empty()
    total_rainfall = sum(values)
    formatted_rainfall = f"{total_rainfall:.2f}"
    markdown_text = f"<h4 style='color: black;'>Total curah hujan pada tahun {selected_year} adalah {formatted_rainfall} mm.</h4>"
    st.markdown(markdown_text, unsafe_allow_html=True)

