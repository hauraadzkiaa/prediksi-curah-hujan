import streamlit as st
import pandas as pd
import altair as alt
import datetime
import numpy as np

st.set_page_config(page_title="Prediksi Bulanan", page_icon="📊")

st.markdown("# Grafik Curah Hujan Bulanan")
st.write(
    """Grafik dibawah memperlihatkan hasil forecast curah hujan dalam rentang satu bulan."""
)

months = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
date = np.load('dashboard/assets/date_index.npy')
val = np.load('dashboard/assets/rainfall_rate.npy')
df = pd.DataFrame({'Date': date, 'Value': val})
crop_cutoff = {
    'Padi': (125, 167),
    'Teh': (166, 209),
    'Cabai': (100, 200),
    'Lada': (166, 209),
    'Jagung': (85, 200),
    'Kelapa Sawit': (150, 167)
}
selected_year = st.selectbox("Pilih Tahun", \
                                [datetime.datetime.now().year, datetime.datetime.now().year + 1])
def recommend(value, min_val, max_val):
    return "Direkomendasikan" if min_val < value < max_val else "Tidak Direkomendasikan"
selection = st.multiselect(
    "Pilih Bulan", months, ["Januari"]
)
if not selection:
    st.error("Pilih setidaknya satu bulan.")
else:
    numeric_selection = [months.index(month)+1 for month in selection]

    df['Date'] = pd.to_datetime(df['Date'])

    df['Month'] = df['Date'].dt.month
    df['DayOfMonth'] = df['Date'].dt.day

    df_2024 = df[df['Date'].dt.year == 2024]
    df_2025 = df[df['Date'].dt.year == 2025]
  
    selected_months_df_2024 = df_2024[df_2024['Month'].isin(numeric_selection)]
    selected_months_df_2025 = df_2025[df_2025['Month'].isin(numeric_selection)]

    month_mapping = {
        1: 'Januari',
        2: 'Februari',
        3: 'Maret',
        4: 'April',
        5: 'Mei',
        6: 'Juni',
        7: 'Juli',
        8: 'Agustus',
        9: 'September',
        10: 'Oktober',
        11: 'November',
        12: 'Desember'
    }

    selected_months_df_2024['Month'] = selected_months_df_2024['Month'].map(month_mapping)
    selected_months_df_2025['Month'] = selected_months_df_2025['Month'].map(month_mapping)

    pivot_2024 = selected_months_df_2024.pivot(index='Month', columns='DayOfMonth', values='Value').reset_index()
    pivot_2025 = selected_months_df_2025.pivot(index='Month', columns='DayOfMonth', values='Value').reset_index()

    sum_by_month = pivot_2025.groupby('Month').sum()

    melted_2024 = pd.melt(pivot_2024, id_vars=['Month'], var_name='DayOfMonth', value_name='Value')
    melted_2025 = pd.melt(pivot_2025, id_vars=['Month'], var_name='DayOfMonth', value_name='Value')

    chart_2024 = alt.Chart(melted_2024).mark_area(opacity=0.8).encode(
        x=alt.X('DayOfMonth:O', title='Hari ke-', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Value:Q', stack=None, title='Curah Hujan (mm)'),
        color=alt.Color('Month:N', title='Bulan')
    ).properties(
    title={
        "text": 'Curah Hujan di 2024',
        "anchor": 'middle'
    }
    )
    chart_2025 = alt.Chart(melted_2025).mark_area(opacity=0.8).encode(
        x=alt.X('DayOfMonth:O', title='Hari ke-', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('Value:Q', stack=None, title='Curah Hujan (mm)'),
        color=alt.Color('Month:N', title='Bulan')
    ).properties(
    title={
        "text": 'Curah Hujan di 2025',
        "anchor": 'middle'
    }
    )
    if selected_year == 2024:
        st.altair_chart(chart_2024, use_container_width=True)
        pivot_df = pd.pivot_table(selected_months_df_2024, values='Value', index='Month', aggfunc='sum')
    elif selected_year == 2025:
        st.altair_chart(chart_2025, use_container_width=True)
        pivot_df = pd.pivot_table(selected_months_df_2025, values='Value', index='Month', aggfunc='sum')

    tanaman = ["Padi", "Teh", "Cabai","Lada", "Kelapa Sawit", "Jagung"]

    pivot_df.rename(columns={'Value': 'Total Curah Hujan'}, inplace=True)
    pivot_df.index.name = 'Bulan'
    pivot_df = pivot_df._append(pd.DataFrame(columns=tanaman))
   
    for index, row in pivot_df.iterrows():
        for crop, (min_val, max_val) in crop_cutoff.items():
            column_name = f"{crop}"
            pivot_df.loc[index, column_name] = recommend(row["Total Curah Hujan"], min_val, max_val)
   
    pivot_df = pivot_df.transpose()
    st.write("### Rekomendasi Waktu Tanam")
    st.write(pivot_df.sort_index(),wide_mode=True)
