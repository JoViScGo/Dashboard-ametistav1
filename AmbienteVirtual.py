# python -m venv 'nome do ambiente virtual' = cria o ambiente virtual
# .\test\Scripts\Activate.ps1 = ativa o ambiente virtual

# https://grizzly-amaranthus-f6a.notion.site/Streamlit-3f599bdfbb584cd1b581e748b5291c36
# streamlit run (nome do arquivo) = ativar o dashboard
# import streamlit as st

# # Elementos Textuais

# # texto maior(header)
# st.header("Texto maior")

# # texto menor(text)
# st.text("Subtítulo")

# # texto na barra lateral
# st.sidebar.text("Barra lateral")

# # forma diferente do texto(#=negrito ~~=riscado)
# st.markdown('# Meu texto')

# # Criar uma legenda
# st.caption('Balloons. Hundreds of them...')

# # Serve para printar, estruturas de dados, markdown etc
# st.write("# Ola", ['Caio', 'Sampaio'])

# # ----------------------------------------------------------------

# # Tabelas
# import pandas as pd 
# import numpy as np

# # Criando um dataframe com o pandas
# df = pd.DataFrame(
# # Nem ideia(olhar documentação dps)
#     #  10= Eixo y, 4=eixo x
#     np.random.rand(10, 4), 
#     # Nome do que vai estar no eixo X
#     columns = ["Preço" , "Taxa de ocupação " , "Taxa de inadimplência" , "Pessoas por casa"]
#     ) 

# # tabela que exibe os dados
# st.table(df)

# # tabela que exibe os dados com maior maleabilidade
# st.dataframe(df)

# # gráfico de linhas
# st.line_chart(df)

# # gráfico de barras 
# st.bar_chart(df)

# # ---------------------------------------

# # Criar botões

# # se o botão for apertado uma ação será tomada
# if st.button("Nome do Botão"):
#     st.bar_chart(df)

# # criando checkbox(enquanto marcada exibe algo)
# check = st.checkbox("Nome da checkbox")
# if check:
#     st.line_chart(df)

# # Escolha de opção
# opcao = st.radio(
#  "Selecione uma opção",
#  ('Linhas', 'Barras'))

# if opcao == 'Linhas':
#     st.line_chart(df)
# else:
#     st.bar_chart(df)

# # caixa de seleção(mais bonito que o radio)
# option = st.selectbox(
#     'Selecione',
#     ('Op 1', 'Op 2', 'Op 3'))

# st.write('Você selecionou:', option)

# # Caixa de seleção com a possibilidade de se escolher mais de um ao mesmo tempo
# options = st.multiselect(
#      'Cor favorita',
#      ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
#      ['Vermelho', 'Verde'])
# # as 2 cores acima já virão selecionado

# # Cria uma barra com um intervalo
# values = st.slider(
# 'Intervalo',
# 0.0, 100.0, (25.0, 75.0))

# # Aberto para o usuário digitar algo
# title = st.text_input('Nome', 'Caio')

# # 
# number = st.number_input('Número')

# # 
# d = st.date_input(
#  "Digite uma data",
# datetime.date(2022, 2, 2))