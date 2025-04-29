import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Conectar com Google Sheets
def conectar():
    escopo = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credenciais = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", escopo)
    cliente = gspread.authorize(credenciais)
    planilha = cliente.open("Planilha_Producao")  # Substitua pelo nome real da sua planilha
    return planilha.sheet1

st.title("📋 Cadastro de Produção")

data = st.date_input("Data")
dia_semana = st.selectbox("Dia da Semana", ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"])
vol_total = st.number_input("Volume Total de Produção", min_value=0)
receitas = st.number_input("Nº de receitas esperadas", min_value=0)
pacotes = st.number_input("Nº de pacotes", min_value=0)
hora_inicio = st.text_input("Hora início Produção (ex: 16/09/2024 03:00)")
hora_fim = st.text_input("Hora fim Produção (ex: 17/09/2024 00:00)")
tempo_total = st.text_input("Tempo Total Produção (ex: 21:00:00)")
produtividade = st.number_input("Produtividade", min_value=0)
faltas = st.number_input("Nº Falta", min_value=0)
tempo_max = st.text_input("Tempo máx. exposição produto (ex: 03:00:00)")
ocorrencia = st.text_input("Ocorrência")

if st.button("Salvar na Planilha"):
    aba = conectar()
    aba.append_row([str(data), dia_semana, vol_total, receitas, pacotes,
                    hora_inicio, hora_fim, tempo_total, produtividade,
                    faltas, tempo_max, ocorrencia])
    st.success("✅ Dados salvos com sucesso!")
