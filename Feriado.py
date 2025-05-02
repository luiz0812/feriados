import requests
from datetime import datetime
import streamlit as st


def consultar_api(ano):
    url = f'https://brasilapi.com.br/api/feriados/v1/{ano}'
    resposta = requests.get(url)
    feriados = resposta.json()
    return feriados

dias = {
    0: 'segunda',
    1: 'terça',
    2: 'quarta',
    3: 'quinta',
    4: 'sexta',
    5: 'sábado',
    6: 'domingo',
}

st.title('Feriados !!')

tab_1, tab_2 = st.tabs(
    [
        'Pesquisa',
        'Lista',
    ]
)

with tab_1:
    st.header('Quando Vai Ser?')

    ano = st.number_input(
        label='**Qual ano você quer ver?**',
        value=datetime.now().year,
        min_value=1900,
        max_value=2199,
    )

    feriado = consultar_api(ano)[st.number_input(
        label='**Qual feriado te interessa? Digite o número para ver os detalhes (de 1 a 13)**',
        min_value=1,
        max_value=len(consultar_api(ano)),
    ) - 1]
    
    data_feriado = datetime.strptime(feriado['date'], '%Y-%m-%d')
    nome_feriado = feriado['name']
    data_formatada = data_feriado.strftime('%d/%m/%Y')
    dia_da_semana = dias[data_feriado.weekday()]
    tipo_feriado = feriado['type'].replace('t','c')

    st.write(f'###### O feriado {nome_feriado} será no dia {data_formatada}, é de abrangência {tipo_feriado} e cai no(a) {dia_da_semana}.')

with tab_2:
    st.header('Lista dos  Feriados Nacionais')

    numero = 1
    for feriado in consultar_api(ano):
        nome = feriado['name']
        st.markdown(f' {numero} . **{nome}** ' )
        numero+=1
