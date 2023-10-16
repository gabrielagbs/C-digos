import streamlit as st
import pandas as pd
from views import View

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterClienteUI.listar()
        with tab2:
            ManterClienteUI.inserir()
        with tab3:
            st.write("Atualizar")
        with tab4:
            st.write("Excluir")
    def listar():
        clientes = View.cliente_listar()
        dic = []
        for c in clientes:
            dic.append(c.__dict__)
        df = pd.DataFrame(dic)
        st.dataframe(df)   
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone)
    def atualizar():
        clientes = View.cliente_atualizar()
        dic = []
        for c in clientes:
            dic.append(c.__dict__)
        cliente = st.text_input("Atualização de Clientes")
        nome = st.text_input("Informe o novo nome")
        email = st.text_input("Informe o novo e-mail")
        fone = st.text_input("Informe o novo fone")
        if st.button("Atualizar"):
            View.cliente_inserir(nome, email, fone)
    def excluir():
        clientes = View.cliente_excluir()
        dic = []
        for c in clientes:
            dic.delete(c.__dict__)

