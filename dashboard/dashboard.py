import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

st.title("Bike Sharing Data Analysis Dashboard")
st.write("Analisis pola penggunaan sepeda berdasarkan waktu dan faktor lingkungan (2011–2012)")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    return df

df = load_data()

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.header("Filter Data")

season_filter = st.sidebar.multiselect(
    "Pilih Musim",
    options=df['season'].unique(),
    default=df['season'].unique()
)

weather_filter = st.sidebar.multiselect(
    "Pilih Cuaca",
    options=df['weathersit'].unique(),
    default=df['weathersit'].unique()
)

df = df[
    (df['season'].isin(season_filter)) &
    (df['weathersit'].isin(weather_filter))
]

# =========================
# KPI
# =========================
st.subheader("Ringkasan Data")

col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", int(df['cnt'].sum()))
col2.metric("Rata-rata per Jam", int(df['cnt'].mean()))
col3.metric("Penyewaan Maksimum", int(df['cnt'].max()))

# =========================
# 1. POLA PER JAM
# =========================
st.subheader("Pola Penyewaan Berdasarkan Jam")

hourly = df.groupby('hr')['cnt'].mean().reset_index()

fig_hour = px.line(
    hourly,
    x='hr',
    y='cnt',
    markers=True,
    labels={'hr': 'Jam', 'cnt': 'Rata-rata Penyewaan'}
)

st.plotly_chart(fig_hour, use_container_width=True)

st.markdown("""
Insight:
- Puncak penyewaan terjadi pada sekitar jam 08.00 dan 17.00
- Pola ini menunjukkan penggunaan sepeda sebagai sarana transportasi kerja (commuting)
- Disarankan untuk meningkatkan ketersediaan sepeda pada jam sibuk
""")

# =========================
# 2. POLA BERDASARKAN MUSIM
# =========================
st.subheader("Pengaruh Musim terhadap Penyewaan")

season_data = df.groupby('season')['cnt'].mean().reset_index()

fig_season = px.bar(
    season_data,
    x='season',
    y='cnt',
    labels={'season': 'Musim', 'cnt': 'Rata-rata Penyewaan'}
)

st.plotly_chart(fig_season, use_container_width=True)

st.markdown("""
Insight:
- Musim Fall menunjukkan tingkat penyewaan tertinggi
- Musim Spring memiliki penggunaan terendah
- Kondisi cuaca yang nyaman meningkatkan minat penggunaan sepeda
- Disarankan fokus promosi pada musim dengan permintaan rendah
""")

# =========================
# 3. CUACA
# =========================
st.subheader("Pengaruh Cuaca terhadap Penyewaan")

weather_data = df.groupby('weathersit')['cnt'].mean().reset_index()

fig_weather = px.bar(
    weather_data,
    x='weathersit',
    y='cnt',
    labels={'weathersit': 'Kondisi Cuaca', 'cnt': 'Rata-rata Penyewaan'}
)

st.plotly_chart(fig_weather, use_container_width=True)

st.markdown("""
Insight:
- Cuaca cerah menghasilkan penyewaan tertinggi
- Hujan menurunkan jumlah penyewaan secara signifikan
- Pengguna sangat sensitif terhadap kondisi cuaca
- Disarankan memberikan promo atau insentif saat cuaca buruk
""")

# =========================
# 4. WEEKDAY VS WEEKEND
# =========================
st.subheader("Perbandingan Hari Kerja dan Hari Libur")

day_type = df.groupby('day_type')['cnt'].mean().reset_index()

fig_day = px.bar(
    day_type,
    x='day_type',
    y='cnt',
    labels={'day_type': 'Tipe Hari', 'cnt': 'Rata-rata Penyewaan'}
)

st.plotly_chart(fig_day, use_container_width=True)

st.markdown("""
Insight:
- Hari kerja memiliki tingkat penyewaan lebih tinggi dibanding hari libur
- Menunjukkan sepeda digunakan sebagai transportasi utama harian
- Disarankan memperkuat layanan di area perkantoran dan pusat aktivitas
""")

# =========================
# DATA PREVIEW
# =========================
st.subheader("Data Preview")
st.dataframe(df.head())
