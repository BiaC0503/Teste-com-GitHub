import streamlit as st
st.title('Calculadora de Reembolso de combustível')
st.subheader('Escolha o combustível ')
#Quanto vale a pena escolher etanol ao invés de gasolina?
etanol = 0.36
gasolina = 0.25
opcoes = ['Gasolina', 'Etanol']
#vEtanol = 0.0
#vGasolina = 0.0
#totalKm = 0.0
escolha = st.selectbox('Escolha o combustível\n', opcoes)

if escolha == 'Etanol':
    vEtanol = st.number_input('Digite o valor do etanol', min_value=0.0)
    totalKm = st.number_input('Quantos Km você rodou no total?', min_value=0.0)
    vKm = vEtanol * etanol
    #gasolina = st.number_input('Digite o valor da gasolina', min_value=0.0)
else: 
    vGasolina = st.number_input('Digite o valor da gasolina', min_value=0.0)
    totalKm = st.number_input('Quantos Km você rodou no total?', min_value=0.0)
    vKm = vGasolina * gasolina

reembolso = vKm * totalKm
if st.button('Resolver'):
    st.write(f'Valor do reembolso:\n R$ {reembolso:.2f}')