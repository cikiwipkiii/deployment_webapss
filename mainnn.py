import streamlit as st
from streamlit_option_menu import option_menu

st.title('Aplikasi Konsep Mol')

with st.sidebar :
    Pilihan = option_menu(menu_title=None,
              options=['Massa ke Mol','Volume Gas ke Mol','Jumlah Partikel ke Mol','Molaritas ke Mol'])
    

#Diketahui Massa
if Pilihan =='Massa ke Mol' :
    Massa = st.number_input('masukkan nilai Massa')
    Mr = st.number_input('masukkan nilai Mr')

    tombol = st.button('hitung nilai Mol')

    if tombol:
        nilai_Mol = Massa/Mr
        st.success(f'Nilai Mol sebesar{nilai_Mol}')
        
    
#Diketahui Volume
elif Pilihan == "Volume Gas ke Mol" :
    Volume = st.number_input('masukkan nilai Volume')
    stp = st.number_input('masukkan nilai stp')

    tombol = st.button('hitung nilai Mol')

    if tombol:
        nilai_Mol = Volume/STP
        st.success(f'Nilai Mol sebesar{nilai_Mol}')
        
        
#Diketahui Jumlah Partikel
elif Pilihan == "Jumlah Partikel ke Mol" :
    JumlahPartikel = st.number_input('masukkan nilai JumlahPartikel')
    BilAvogrado = st.number_input('masukkan nilai BilAvogrado')
    
    tombol = st.button('hitung nilai Mol')
    
    if tombol:
        nilai_Mol = JumlahPartikel/BilAvogrado
        st.success(f'nilai Mol sebesar{nilai_Mol}')
        
        
#Diketahui Molaritas
elif Pilihan == "Molaritas ke Mol" :
    Molaritas = st.number_input('masukkan nilai Molaritas')
    Volume = st.number_input('masukkan nilai volume')
    
    tombol = st.button('hitung nilai mol')
    
    if tombol:
        nilai_Mol = Molaritas*Volume
        st.success(f'nilai Mol sebesar{nilai_Mol}')
        
        
        
else :
    st.write()
       

   