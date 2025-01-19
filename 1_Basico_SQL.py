# Importar bibliotecas
import streamlit as st
import pandas as pd
import time
from sqlalchemy import create_engine
import plotly.express as px
from dash import Dash, html, dash_table, dcc

engine = create_engine('postgresql://cabral:ml05lc12@localhost:5434/dsadb')

# Configuração do Streamlit
st.set_page_config(page_title=" Portfolio de Analises de dados", layout="wide")

# importando a logogmarca
#st.image('logomarca.png')

# Interface do Streamlit
#st.write('# Fundamentos Básicos da linguagem SQL')
st.write('<h1 style="color: #141444;">SQL Para Análise de Dados e Data Science</h1>', unsafe_allow_html=True)

# Criando o schema, tabela e inserindo registro
st.markdown('<h2 style="color: #141444;">Criação de Schema, Tabela e Inserindo registros</h2>', unsafe_allow_html=True)
# Criando schema
schema = st.checkbox('1 - Criação de Schema')
if schema:
    st.code('''CREATE SCHEMA cap03 AUTHORIZATION cabral''',language='sql')
# Criando tabela
tabela = st.checkbox('2 - Criação de Tabela Funcionario')
if tabela:
    st.code(
    '''CREATE TABLE cap04.funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    sobrenome VARCHAR(50),
    salario DECIMAL(10, 2),
    departamento VARCHAR(50),
    data_contratacao DATE
);''',language='sql')

# Inserindo Registro na Tabela
registro = st.checkbox('3 - Inserindo Registro')
if registro:
    st.code('''
    INSERT INTO cap03.estudantes_dsa (nome, sobrenome, nota_exame1, nota_exame2, tipo_sistema_operacional) VALUES
('Xavier', 'Murphy', 86.0, 89.0, 'Linux'),
('Yara', 'Bailey', 80.5, 81.0, 'Windows'),
('Alice', 'Smith', 80.5, 85.0, 'Windows'),
('Quincy', 'Roberts', 86.5, 90.0, 'Mac'),
('Bob', 'Johnson', 75.0, 88.0, 'Linux'),
('Carol', 'Williams', 90.0, 90.5, 'Mac'),
('Grace', 'Miller', 95.5, 93.0, 'Windows'),
('Nina', 'Carter', 80.5, 81.0, 'Windows'),
('Ursula', 'Kim', 80.0, 82.5, 'Linux'),
('Eve', 'Jones', 90.0, 88.0, 'Mac'),
('Frank', 'Garcia', 79.0, 82.0, 'Linux'),
('Helen', 'Davis', 90.0, 89.5, 'Mac'),
('Grace', 'Rodriguez', 89.0, 88.0, 'Windows'),
('Jack', 'Martinez', 90.0, 80.0, 'Linux'),
('Karen', 'Hernandez', 93.5, 91.0, 'Windows'),
('Leo', 'Lewis', 82.0, 85.5, 'Mac'),
('Mallory', 'Nelson', 91.0, 89.0, 'Linux'),
('Oscar', 'Mitchell', 88.0, 87.5, 'Linux'),
('Paul', 'Perez', 94.0, 92.0, 'Windows'),
('Rita', 'Gomez', 77.0, 80.0, 'Linux'),
('Steve', 'Freeman', 89.5, 88.5, 'Windows'),
('Troy', 'Reed', 90.0, 92.0, 'Mac'),
('Victor', 'Morgan', 90.0, 85.0, 'Windows'),
('Oscar', 'Bell', 85.5, 87.0, 'Mac'),
('Zane', 'Rivera', 89.0, 90.5, 'Mac'),
('Aria', 'Wright', 75.0, 76.5, 'Linux'),
('Bruce', 'Cooper', 90.0, 84.0, 'Windows'),
('Karen', 'Peterson', 90.0, 92.5, 'Mac'),
('Dave', 'Brown', 88.5, 89.0, 'Windows'),
('Derek', 'Wood', 86.0, 87.5, 'Linux');
''')
  
# Respondendo perguntas
st.markdown('<h2 style="color: #141444;">Respondendo Perguntas</h2>', unsafe_allow_html=True)

# Pergunta 1
consulta_select = st.checkbox('1 - Query SELECT - Consultado Tabela')
consulta_select_df = pd.read_sql('SELECT * FROM cap03.estudantes_dsa',engine)
if consulta_select:
    st.write('**Query**')
    st.code('SELECT * FROM cap03.estudantes_dsa')
    st.write('**Tabela**')
    st.dataframe(consulta_select_df.head())

# Pergunta 2
consulta_order_by = st.checkbox('2 - Query ORDER BY - Ordenando Tabela por nome')
consulta_order_by_df = pd.read_sql('''SELECT * FROM cap03.estudantes_dsa
                                   ORDER BY nome;''',engine)
if consulta_order_by:
    st.write('**Query**')
    st.code('SELECT * FROM cap03.estudantes_dsa ORDER BY nome')
    st.write('**Tabela**')
    st.dataframe(consulta_order_by_df.head())

# Pergunta 3
consulta_where = st.checkbox('3 - Query WHERE - Filtrando por Sistema Operacional')
consulta_where_df = pd.read_sql('''SELECT * FROM cap03.estudantes_dsa 
                                   WHERE tipo_sistema_operacional = 'Linux'
                                   ORDER BY nome;''',engine)
if consulta_where:
    st.write('**Query**')
    st.code('''SELECT * FROM cap03.estudantes_dsa 
            WHERE tipo_sistema_operacional = 'Linux'
            ORDER BY nome''')
    st.write('**Tabela**')
    st.dataframe(consulta_where_df.head())
    st.write('**Gráfico de Usuários por Sistema Operacional**')
    grafico3 = pd.read_sql('''  SELECT COUNT(nome) AS nome,tipo_sistema_operacional
                                FROM cap03.estudantes_dsa
                                GROUP BY tipo_sistema_operacional''',engine)
    st.bar_chart(grafico3,x='tipo_sistema_operacional',y='nome',color='#141444',horizontal=False)
    fig = px.pie(grafico3, values='nome', names='tipo_sistema_operacional')
    st.plotly_chart(fig)

# Pergunta 4
consulta_qtd_usuario = st.checkbox('4 - Quantidade de Usuario por Sistema Operacional')
consulta_qtd_usuario_df = pd.read_sql('''  SELECT COUNT(nome) AS nome,tipo_sistema_operacional
                                FROM cap03.estudantes_dsa
                                GROUP BY tipo_sistema_operacional''',engine)
if consulta_qtd_usuario:
    st.write('**Gráfico do Streamlit**')
    st.bar_chart(consulta_qtd_usuario_df,x='tipo_sistema_operacional',y='nome',color='#141444',horizontal=False)
    st.write('**Gráfico do plotly express**')
    fig = px.pie(consulta_qtd_usuario_df, values='nome', names='tipo_sistema_operacional')
    st.plotly_chart(fig)
    st.write('**Gráfico do plotly express**')
    fig1 = px.funnel(consulta_qtd_usuario_df, x='nome', y='tipo_sistema_operacional')
    st.plotly_chart(fig1)
    st.write('**Gráfico do plotly express**')
    fig2 = px.histogram(consulta_qtd_usuario_df, x='nome', y='tipo_sistema_operacional')
    st.plotly_chart(fig2)
#while True:
#    time.sleep(60)  # Espera 5 minutos
#    st.rerun()  # Recarrega a aplicação

