import streamlit as st

def cadastrar_produto():
    # leitura das informações do produto
    nome = st.text_input("Digite o nome do produto:")
    preco = st.number_input("Digite o preço do produto:", step=0.01)
    descricao = st.text_area("Digite a descrição do produto:")

    # criação de um dicionário com as informações do produto
    produto = {"nome": nome, "preco": preco, "descricao": descricao}

    # adição do produto à lista de produtos
    produtos.append(produto)

    # exibição da mensagem de sucesso
    st.success("Produto cadastrado com sucesso!")

def exibir_produtos():
    # exibição da lista de produtos cadastrados
    st.write("Produtos cadastrados:")
    for produto in produtos:
        st.write(produto)

# criação da lista de produtos vazia
produtos = []

# título do aplicativo
st.title("Cadastro de Produtos")

# opções do menu
opcao = st.sidebar.selectbox("Selecione uma opção:", ["Cadastrar produto", "Exibir produtos"])

# condições para cada opção do menu
if opcao == "Cadastrar produto":
    cadastrar_produto()
elif opcao == "Exibir produtos":
    exibir_produtos()
