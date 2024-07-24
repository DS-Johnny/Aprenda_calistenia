import streamlit as st

st.sidebar.title("Home")

st.title("Aprenda Calistenia")

st.write("Fonte do conteúdo: https://www.barzclub.net/")
st.markdown("---")
st.title("O que é Calistenia?")
st.write("""Calistenia é o treino que utiliza apenas o peso do próprio corpo para fortalecer os músculos. Como por exemplo repetições de flexão, barra fixa e agachamentos.

Pode ser feita em praticamente qualquer local, mas principalmente em praças, parques públicos e até em casa. E sua grande característica é que você pode treinar de graça e ter resultados incríveis.

Essa modalidade de treino vem desde a antiguidade e tem sido por milênios a base do fortalecimento de exércitos, atletas e acrobatas.

A palavra Calistenia vem da junção das palavras gregas kallos (beleza) e sthenos (força), sendo portanto o método de treino pra deixar o seu corpo belo, perfeito e ao mesmo tempo forte, como você deve perceber nos vídeos de Calistenia no Youtube.""")

st.markdown("### Treinos:")

basico, iniciante = st.tabs(['Treino Básico', 'Treino Iniciante'])

with basico:

    col1, col2 = st.columns(2)
    with col1:
        st.write("Treino de Flexão")
        st.image("images/basico/treino-flexao-calistenia-iniciante-basico.png")
        st.markdown("---")
        st.write("Treino de Core e Pernas")
        st.image("images/basico/treino-core-pernas-calistenia-iniciante-basico.png")
        

    with col2:
        st.write("Treino de Barra")
        st.image("images/basico/treino-barra-calistenia-iniciante-basico.png")
        st.markdown("---")
        st.write("Grade")
        st.image("images/basico/grade-treinos-calistenia-iniciante-basico.png")

    st.page_link("pages/2_Treino_Basico.py", label="Clique aqui para ir para o treino")