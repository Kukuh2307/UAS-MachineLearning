import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# sidebar
# opsi 1
with st.sidebar:
    selected = option_menu("Menu Utama", ["Prediksi Penyakit Diabetes", 'Prediksi Penyakit Jantung','Prediksi Kualitas Air'], 
        icons=['hospital', 'clipboard2-pulse','droplet-half'], menu_icon="cast", default_index=0)
    selected
# opsi 2
# with st.sidebar:
#     selected = st.radio(
#         "Menu Utama",
#         ["Prediksi Penyakit Diabetes", 'Prediksi Penyuakit Jantung', 'Prediksi Kualitas Air'],
#         index=0
#     )



if(selected == 'Prediksi Penyakit Diabetes'):
    # Model = '/home/kisawa16/Documents/KULIAH/MACHINE LEARNING/UTS/ID3/diabetes_decision_tree_model.pkl'
    id3Model = pickle.load(open('diabetes_decision_tree_model.pkl', 'rb'))

    st.title('ID3 - Prediksi Penyakit diabetes')

    col1,col2 = st.columns([1,1])

    with col1:
        gender = st.selectbox(
            "Pilih Jenis kelamin",
            ['Female','Male'],
            index=0
        )
        age = st.number_input('Masukkan umur')
        hypertension = st.number_input('Masukkan Hypertension')
        heart = st.number_input('Riwayat Jantung')

    with col2:
        smoking = st.selectbox(
            "Masukkan smoking history",
            ['no info','current','ever','never','former'],
            index=0
        )
        bmi = st.number_input('Masukkan BMI')
        hbaic = st.number_input('Masukkan HbAIc Level')
        blood = st.number_input('Masukkan Bloood glucose level')
    
    # with col3:
    button1 = st.button('Test Prediksi Penyakit Diabetes')
    gender = 0 if gender == "Female" else 1 

    smoking_mapping = {'current': 1, 'never': 4, 'no info': 0, 'former': 3, 'ever':2}
    smoking = smoking_mapping[smoking]

    if smoking == 'current':
            smoking = 1
    if smoking == 'never':
            smoking = 4
    if smoking == 'ever':
            smoking = 2
    if smoking == 'no info':
            smoking = 0
    if smoking == 'former':
            smoking = 3
    input_data = [
            float(gender),float(age),float(hypertension),float(heart),float(smoking),float(bmi),float(hbaic),float(blood)]

    diabetes_diagnosis = ''

    if button1:
            diabetes_predict = id3Model.predict([input_data])

            if diabetes_predict[0] == 1:
                diabetes_diagnosis = 'Pasien terindikasi terkena penyakit diabetes'
            else:
                diabetes_diagnosis = 'Pasien tidak terindikasi terkena penyakit diabetes'

    st.success(diabetes_diagnosis)

if(selected == 'Prediksi Penyakit Jantung'):
    # Model = '/home/kisawa16/Documents/KULIAH/MACHINE LEARNING/UTS/NAIVE BAYES/naive_bayes_model.pkl'
    naiveModel = pickle.load(open('naive_bayes_model.pkl', 'rb'))

    # judul web
    st.title('Naive - Prediksi Penyakit Jantung')

    # input atribut
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input('Masukkan Umur anda')
        sex = st.selectbox(
            "Pilih Jenis kelamin",
            ['Female','Male'],
            index=0
        )
        cp = st.selectbox(
            'Masukkan tipe nyeri dada',
            ['0','1','2','3']
        )
        trtbps = st.number_input('Masukkan tekanan darah')
        chol = st.number_input('Masukkan kolesterol')
        fbs = st.number_input('Masukkan gula darah')
        restecg = st.number_input('Masukkan hasil elektrokardiografi')

    with col2:
        thalach = st.number_input('Masukkan denyut jantung maksimal')
        exng = st.number_input('Masukkan Angina akibat olahraga')
        oldpeak = st.number_input('Depresi disebabkan oleh olahraga')
        slp = st.number_input('Kemiringan puncak latihan segmen')
        caa = st.number_input("Jumlah pembulu darah besar yang diwarnai dengan fluroskopi")
        thall = st.number_input("Hasil test thallium")
    button2 = st.button('Test Prediksi Penyakit Jantung')

    # Convert input values to numeric
    sex = 0 if sex == "Female" else 1 
    input_data = [
            float(age), float(sex), float(cp), float(trtbps), float(chol), float(fbs),
            float(restecg), float(thalach), float(exng), float(oldpeak), float(slp), 
            float(caa), float(thall)
        ]

        # code prediksi
    heart_diagnosis = ''

        # tombol prediksi
    if button2:
            heart_predict = naiveModel.predict([input_data])

            if heart_predict[0] == 1:
                heart_diagnosis = "Pasien terindikasi terkena penyakit jantung"
            else:
                heart_diagnosis = "Pasien tidak terindikasi terkena penyakit jantung"

        # Menampilkan hasil prediksi
    st.success(heart_diagnosis)

if(selected == 'Prediksi Kualitas Air'):
    # Model = '/home/kisawa16/Documents/KULIAH/MACHINE LEARNING/UTS/KNN/knn_model.pkl'
    knnModel = pickle.load(open('knn_model.pkl', 'rb'))

    st.title('KNN - Prediksi Kualitas Air')
    
    col1,col2 = st.columns(2)
    with col1:
        almunium = st.number_input('Masukkan kadar almunium')
        amonia = st.number_input('Masukkan kadar amonia')
        arsenic = st.number_input('Masukkan kadaar arsenic')
        barium = st.number_input('Masukkan kadar barium')
        cadmium = st.number_input('Masukkan kadar cadmium')
        chloramine = st.number_input('Masukkan kadar chloramine')
        chromium = st.number_input('Masukkan kadar chromium')
        copper = st.number_input('Masukkan kadar copper')
        flouride = st.number_input('Masukkan kadar flouride')
        bacteria = st.number_input('Masukkan kadar bacteria')

    with col2:
        viruses = st.number_input('Masukkan kadar viruses')
        lead = st.number_input('Masukkan kadar lead')
        nitrates = st.number_input('Masukkan kadar nitrates')
        nitrites = st.number_input('Masukkan kadar nitrites')
        mercury = st.number_input('Masukkan kadar mercury')
        perchlorate = st.number_input('Masukkan kadar perchlorate')
        radium = st.number_input('Masukkan kadar radium')
        selenium = st.number_input('Masukkan kadar selenium')
        silver = st.number_input('Masukkan kadar silver')
        uranium = st.number_input('Masukkan kadar uranium')

    button3 = st.button('Kalkulasi hasil Prediksi kandungan air')
    input_data = [
            float(almunium),float(amonia),float(arsenic),float(barium),float(cadmium),float(chloramine),float(chromium),float(copper),float(flouride),float(bacteria),float(viruses),float(lead),float(nitrates),float(nitrites),float(mercury),float(perchlorate),float(radium),float(selenium),float(silver),float(uranium)
        ]

    water_status = ''
    if button3:
            water_predict = knnModel.predict([input_data])

            if water_predict[0] == 1:
                water_status = "Kandungan air aman"
            else:
                water_status = "Kandungan air tidak aman"
        
    st.success(water_status)

st.markdown(
    """
    #### Tentang Web
    Web ini di buat untuk memenuhi tugas mata kuliah Machine Learning, kegunaan dari web ini adalah untuk memprediksi beberapa hal seperti prediksi penyakit diabetes,prediksi penyakit jantung dan prediksi kualitas air.

    #### Kelompok 8
    - [Kukhuh Agung]
    - [Miftahul Huda]
    - [Ahmad Firsta]
    """
)