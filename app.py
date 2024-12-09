import streamlit as st
import joblib
import numpy as np

# Memuat model yang disimpan
model = joblib.load('gradient_boosting_model.pkl')

# Fungsi untuk melakukan prediksi
def predict_species(features):
    # Pastikan input features berbentuk array 2D (misalnya [0, 1, 0, ...])
    prediction = model.predict([features])
    return prediction[0]

# Fungsi untuk mengonversi kode kelas ke nama spesies
def get_species_name(class_code):
    species_dict = {
        1: 'Mammal',
        2: 'Bird',
        3: 'Reptile',
        4: 'Fish',
        5: 'Amphibian',
        6: 'Bug',
        7: 'Invertebrate'
    }
    return species_dict.get(class_code, 'Unknown')

# Fungsi untuk mengonversi 'Ya'/'Tidak' menjadi 1/0
def yes_no_to_int(value):
    if value == 'Ya':
        return 1
    else:
        return 0

# Membuat antarmuka input di Streamlit
st.title('Prediksi Tipe Kelas Hewan Berdasarkan Karakteristik')

# Menampilkan form input untuk setiap kolom dengan pilihan 'Ya' dan 'Tidak'
hair = st.selectbox('Apakah hewan ini memiliki rambut?', ['Tidak', 'Ya'])
feathers = st.selectbox('Apakah hewan ini memiliki bulu?', ['Tidak', 'Ya'])
eggs = st.selectbox('Apakah hewan ini bertelur?', ['Tidak', 'Ya'])
milk = st.selectbox('Apakah hewan ini menghasilkan susu?', ['Tidak', 'Ya'])
airborne = st.selectbox('Apakah hewan ini bisa terbang?', ['Tidak', 'Ya'])
aquatic = st.selectbox('Apakah hewan ini hidup di air?', ['Tidak', 'Ya'])
predator = st.selectbox('Apakah hewan ini pemangsa?', ['Tidak', 'Ya'])
toothed = st.selectbox('Apakah hewan ini memiliki gigi?', ['Tidak', 'Ya'])
backbone = st.selectbox('Apakah hewan ini memiliki tulang belakang?', ['Tidak', 'Ya'])
breathes = st.selectbox('Apakah hewan ini bernapas?', ['Tidak', 'Ya'])
venomous = st.selectbox('Apakah hewan ini berbisa?', ['Tidak', 'Ya'])
fins = st.selectbox('Apakah hewan ini memiliki sirip?', ['Tidak', 'Ya'])
legs = st.selectbox('Jumlah kaki hewan ini (pilih dari 0, 2, 4, 5, 6, 8):', ['0', '2', '4', '5', '6', '8'])
tail = st.selectbox('Apakah hewan ini memiliki ekor?', ['Tidak', 'Ya'])
domestic = st.selectbox('Apakah hewan ini adalah hewan peliharaan?', ['Tidak', 'Ya'])
catsize = st.selectbox('Apakah ukuran hewan ini besar seperti kucing?', ['Tidak', 'Ya'])

# Membuat array fitur dari input pengguna, konversi 'Ya'/'Tidak' menjadi 1/0
features = np.array([yes_no_to_int(hair), yes_no_to_int(feathers), yes_no_to_int(eggs),
                     yes_no_to_int(milk), yes_no_to_int(airborne), yes_no_to_int(aquatic),
                     yes_no_to_int(predator), yes_no_to_int(toothed), yes_no_to_int(backbone),
                     yes_no_to_int(breathes), yes_no_to_int(venomous), yes_no_to_int(fins),
                     int(legs), yes_no_to_int(tail), yes_no_to_int(domestic), yes_no_to_int(catsize)])

# Tombol prediksi
if st.button('Prediksi'):
    # Lakukan prediksi
    prediction = predict_species(features)
    
    # Menampilkan nama spesies berdasarkan prediksi
    species_name = get_species_name(prediction)
    st.write(f"Hewan ini kemungkinan adalah: **{species_name}**")
