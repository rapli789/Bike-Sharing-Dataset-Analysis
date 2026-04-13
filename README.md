# Bike-Sharing-Dataset-Analysis

## Deskripsi
Proyek ini bertujuan untuk menganalisis pola penggunaan sepeda berdasarkan waktu (jam, hari, musim) serta faktor lingkungan seperti cuaca dan suhu selama periode 2011–2012. Hasil analisis divisualisasikan dalam bentuk dashboard interaktif menggunakan Streamlit.

## Pertanyaan Bisnis
1. Bagaimana pola penggunaan sepeda berdasarkan jam, hari, dan musim selama periode 2011–2012, serta kapan waktu puncak penyewaan terjadi?
2. Bagaimana pengaruh kondisi cuaca, suhu, dan status hari (hari kerja vs hari libur) terhadap jumlah penyewaan sepeda selama periode 2011–2012?

## Dataset
- day.csv (data harian)
- hour.csv (data per jam)
- main_data.csv (data hasil cleaning dan penggabungan)

## Setup Environment - Anaconda
conda create --name main-ds python=3.9  
conda activate main-ds  
pip install -r requirements.txt  

## Setup Environment - Shell/Terminal
mkdir proyek_analisis_data  
cd proyek_analisis_data  
pip install pipenv  
pipenv install  
pipenv shell  
pip install -r requirements.txt  

## Run Streamlit App
streamlit run dashboard.py  

## Struktur Proyek
- dashboard.py
- main_data.csv
- day.csv
- hour.csv
- requirements.txt
- notebook.ipynb
- README.md

## Fitur Dashboard
- Pola penyewaan berdasarkan jam
- Analisis berdasarkan musim
- Analisis pengaruh cuaca
- Perbandingan hari kerja dan hari libur
- Filter interaktif

## Insight Singkat
- Puncak penyewaan terjadi pada jam 08.00 dan 17.00 (jam sibuk)
- Musim Fall memiliki jumlah penyewaan tertinggi
- Cuaca cerah meningkatkan penggunaan sepeda secara signifikan
- Hari kerja menunjukkan aktivitas lebih tinggi dibanding hari libur


## Cara Deploy ke Streamlit Cloud
1. Upload project ke GitHub
2. Buka Streamlit Cloud
3. Pilih repository
4. Tentukan file utama: dashboard.py
5. Klik deploy


## Tools yang Digunakan
- Python
- Pandas
- Plotly
- Streamlit
