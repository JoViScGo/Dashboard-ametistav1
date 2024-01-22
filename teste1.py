
# Com apenas o python
# with open('Dados Ametista.csv' , 'r') as da: 
#     da_csv = csv.reader(da , delimiter=',')

# for i , linha in enumerate(da_csv):
#     if i == 0:
#         print('Cabeçalho: '+ str(linha))
#     else:
#         print('Valor: ' + str(linha))
# Com o pandas
# da = pd.read_csv('Dados Ametista.csv' , sep = ',')
# print(da)
# da['Coluna']
import pandas as pd
import streamlit as st

df0 = pd.read_csv('DadosSimples.csv' , header = None)
df0.columns=['Nome da Estação' , 'Data' , 'Hora' , 'Tensão da bateria' , 'temperatura interna da pcd' , 
             'Temperatura do ar instantânea' , 'Temperatuda máxima do ar de 1h' , 
             'Temperatura mínima do ar de 1h' , 'Umidade relativa do ar instantânea' , 
             'Umidade relativa do ar máxima de 1h' , 'Umidade relativa do ar mínima de 1h' , 
             'Ponto de orvalho instantâneo' , 'ponto de orvalho máximo de 1h' , 
             'Ponto de orvalho mínimo de 1h' , 'Pressão atmosférica do ar instantânea' , 
             'Pressão atmosférica do ar máxima de 1h' , 'Pressão atmosférica mínima de 1h' , 
             'Direção do vento média de 10min' , 'Velocidade do vento média de 10min' , 
             'Velocidade do vento máxima de 1h' , 'vecolidade do vento mínima de 1h' , 
             'Somatório de radiação solar de 1h' , 'Soma da precipitação de 1h' , '/' , '/' , '/']
df0.to_csv('df2.csv')
df = pd.read_csv('df2.csv' , header = 0)
#Título do dashboard 
st.title("Dados Meteorológicos")

# definindo todas as colunas
columns=['Nome da Estação' , 'Data' , 'Hora' , 'Tensão da bateria' , 'temperatura interna da pcd' , 
             'Temperatura do ar instantânea' , 'Temperatuda máxima do ar de 1h' , 
             'Temperatura mínima do ar de 1h' , 'Umidade relativa do ar instantânea' , 
             'Umidade relativa do ar máxima de 1h' , 'Umidade relativa do ar mínima de 1h' , 
             'Ponto de orvalho instantâneo' , 'ponto de orvalho máximo de 1h' , 
             'Ponto de orvalho mínimo de 1h' , 'Pressão atmosférica do ar instantânea' , 
             'Pressão atmosférica do ar máxima de 1h' , 'Pressão atmosférica mínima de 1h' , 
             'Direção do vento média de 10min' , 'Velocidade do vento média de 10min' , 
             'Velocidade do vento máxima de 1h' , 'vecolidade do vento mínima de 1h' , 
             'Somatório de radiação solar de 1h' , 'Soma da precipitação de 1h' , '/' , '/' , '/']

# Exibir o df (Opção está na barra lateral)
dafr = st.sidebar.checkbox('Dados Brutos')
if dafr:
    st.dataframe(df)

# Gráficos de temperatura(col 7, 8 e 9)
st.subheader('Temperaturas')

temp = st.selectbox(
    'Selecione o tema desejado',
    ('Temperatura do ar instantânea', 'Temperatuda máxima do ar de 1h', 'Temperatura mínima do ar de 1h'))

if temp == 'Temperatura do ar instantânea':
    st.line_chart(df[columns], x='Hora', y='Temperatura do ar instantânea')
elif temp == 'Temperatuda máxima do ar de 1h':

    st.line_chart(df[columns], x='Hora', y='Temperatura do ar máxima de 1h')

elif temp == 'Temperatura mínima do ar de 1h':
    st.line_chart(df[columns], x='Hora', y='Temperatura do ar mínima de 1h')

# Gráfico de umidade(col 10, 11 e 12)
st.subheader('Umidade')

umd = st.selectbox(
    'Selecione o tema desejado',
    ('Umidade relativa do ar instantânea','Umidade relativa do ar máxima de 1h','Umidade relativa do ar mínima de 1h'))
if umd == 'Umidade relativa do ar instantânea':
    st.line_chart(df[columns], x='Hora' , y='Umidade relativa do ar instantânea')

elif umd == 'Umidade relativa do ar máxima de 1h': 
    st.line_chart(df[columns],x='Hora' ,y='Umidade relativa do ar máxima de 1h')

elif umd == 'Umidade relativa do ar mínima de 1h':
    st.line_chart(df[columns], x='Hora', y='Umidade relativa do ar mínima de 1h')
