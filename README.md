# 🎬 Recomendador de Filmes

Um app simples feito com [Streamlit](https://streamlit.io/) que recomenda filmes parecidos com base em um título que você digita. A busca e as recomendações são feitas usando a [TMDB API](https://www.themoviedb.org/documentation/api).

## 🚀 Demonstração

Digite o nome de um filme e veja recomendações parecidas, com pôster, título e descrição.  
💡 O layout é escuro, com visual moderno e intuitivo.

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/XiloMssj/recomendador-filmes.git
cd recomendador-filmes
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
venv\Scripts\activate  # no Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` com sua chave da API TMDB:

```
TMDB_API_KEY=sua_chave_aqui
```

## 🧠 Como usar

Execute o aplicativo com:

```bash
streamlit run app.py
```

Acesse no navegador (normalmente `http://localhost:8501`) e digite o nome de um filme para receber recomendações!

## 🛠️ Tecnologias utilizadas

- Python
- Streamlit
- TMDB API
- Requests
- dotenv

## 📷 Capturas de tela

Em breve! 😉

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre pra usar, modificar e compartilhar!

---

Feito com ❤️ por [XiloMssj](https://github.com/XiloMssj)
