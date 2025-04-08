import streamlit as st
from tmdb_api import buscar_filme_id, recomendar_similares

# Configuração da página
st.set_page_config(page_title="Recomendador de Filmes 🎬", layout="wide")

st.markdown("""
    <style>
    /* Força fundo preto em todo o HTML e body */
    html, body, .stApp {
        background-color: #000000 !important;
        color: white !important;
    }

    /* Tira o padding padrão do Streamlit */
    .main, .block-container {
        background-color: #000000 !important;
        padding-top: 2rem;
    }

    header, footer {
        background-color: #000000 !important;
        color: white !important;
    }

    /* Input de texto estilizado */
    .stTextInput > div > div > input {
        background-color: #333333;
        color: white;
        border: 1px solid #555555;
        padding: 10px;
        border-radius: 5px;
    }

    /* Estilo dos títulos e textos */
    h1, h2, h3, h4, h5, h6, p, label, div, span {
        color: white !important;
    }

    /* Linha divisória */
    hr {
        border-color: #333333;
    }

    /* Corrige barra de rolagem branca no canto direito */
    ::-webkit-scrollbar {
        background: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# Título e descrição
st.title("🎥 Recomendador de Filmes")
st.markdown("Descubra filmes parecidos com os que você já curte! 🍿")

# Entrada do usuário
nome_filme = st.text_input("Digite o nome de um filme:")

# Recomendações de filmes
if nome_filme:
    try:
        filme_id, filme_titulo = buscar_filme_id(nome_filme)
        st.subheader(f"🔍 Filmes similares a {filme_titulo}:")

        recomendacoes = recomendar_similares(filme_id)

        for idx, filme in enumerate(recomendacoes, 1):
            with st.container():
                col1, col2 = st.columns([1, 3])
                with col1:
                    if filme.get('poster_url'):
                        st.image(filme['poster_url'], width=150)
                with col2:
                    st.markdown(f"**{idx}. 🎞️ {filme['titulo']}**")
                    st.markdown(f"📝 {filme['descricao']}")
                st.markdown("---")

    except Exception as e:
        st.error(f"Erro ao buscar recomendações: {e}")