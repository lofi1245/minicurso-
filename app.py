import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def carregar_dados():
    data = pd.read_csv("Pokemon.csv")
    return data 

def home():
    st.title("Bem-vindo ao projeto pokemoon data vizualization")
    

def grafico_linhas():
    st.title("Gráfico de linhas")
    data = carregar_dados()
    fig= plt.figure(figsize=(10,10))
    
    data.groupby("generation")["hp"].mean().plot(marker="o")
    plt.title("tendência de hp dos pokemons ao longo das gerações")
    plt.xlabel("geração")
    plt.ylabel("Média de HP")
    plt.grid(True)

    st.pyplot(fig)
   
    with st.expander("Código para gerar o gráfico"):
        with st.echo():
                
                data = carregar_dados()
                fig= plt.figure(figsize=(10,10))
                data.groupby("generation")["hp"].mean().plot(marker="o")
                plt.title("tendência de hp dos pokemons ao longo das gerações")
                plt.xlabel("geração")
                plt.ylabel("Média de HP")
                plt.grid(True)
    
def grafico_barras():
    data= carregar_dados()
    
    st.title("Gráfico de barras")
    
    fig=plt.figure(figsize=(10,8))
    
    plt.title("distribuição de pokemon por tipo")
    
    type_counts = pd.concat([data["type1"], data["type2"]]).value_counts()
    
    type_counts.plot(kind="bar")
    plt.title("Distribuição de pokemon por tipo")
    plt.xlabel("tipo")
    plt.ylabel("Numero de pokemon")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    st.pyplot(fig)
    
    with st.expander("Código para gerar o gráfico"):
        with st.echo():
            fig=plt.figure(figsize=(10,8))

            plt.title("distribuição de pokemon por tipo")
            
            type_counts = pd.concat([data["type1"], data["type2"]]).value_counts()
            
            type_counts.plot(kind="bar")
            plt.title("Distribuição de pokemon por tipo")
            plt.xlabel("tipo")
            plt.ylabel("Numero de pokemon")
            plt.xticks(rotation=45)
            plt.grid(axis="y")
            

def grafico_boxplot():
    data= carregar_dados()
    st.title("Gráfico boxplot")
    fig= plt.figure(figsize=(10,8))
    
    stats= data[["hp","attack","defense","sp_attack","sp_defense","speed"]]
    
    stats.boxplot()
    
    plt.title("distribuição das estatisticas dos pokemons")
    plt.ylabel("valores")
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    
    
    st.pyplot(fig)
    
    with st.expander("Código para gerar o gráfico"):
        with st.echo():
            fig= plt.figure(figsize=(10,8))
    
            stats= data[["hp","attack","defense","sp_attack","sp_defense","speed"]]

            stats.boxplot()

            plt.title("distribuição das estatisticas dos pokemons")
            plt.ylabel("valores")
            plt.xticks(rotation=45)
            plt.grid(axis="y")
    
 
 
def grafico_pizza():
    
     st.title("Grafico de pizza")
     dados= carregar_dados()
     lengendary_counts = dados["legendary"].value_counts()
     
     fig= plt.figure(figsize=(10,10))
     
     plt.title("proporção de pokemons lendarios")
     plt.pie(lengendary_counts, labels=["Não lendário", "Lendário"], autopct="%1.1f%%",startangle=140, textprops={'fontsize':14})
     
     st.pyplot(fig)
     
     with st.expander("Código para gerar o gráfico"):
        with st.echo():
            fig= plt.figure(figsize=(10,10))
            plt.title("proporção de pokemons lendarios")
            plt.pie(lengendary_counts, labels=["Não lendário", "Lendário"], autopct="%1.1f%%",startangle=140, textprops={'fontsize':14} )

def main():
    
    st.sidebar.title("Navegação")
    
    pages={
        "Página Inical" : home, 
        "Linhas": grafico_linhas,
        "Barras": grafico_barras,
        "Boxplot":grafico_boxplot,
        "Pizza": grafico_pizza,

    }
    
    selection = st.sidebar.selectbox("Ir para", list(pages.keys()))
    
    st.sidebar.title("Sobre")
    st.sidebar.write("projeto com o intuito de demonstrar algumas funcionalidades básicas da biblioteca matplotlib ")
    
    pages[selection]()
    
    

if __name__ == "__main__":
    main()