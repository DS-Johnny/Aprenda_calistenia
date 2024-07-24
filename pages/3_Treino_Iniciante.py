import streamlit as st


st.sidebar.title("Treino Iniciante")
st.sidebar.image("images/iniciante/grade-treinos-calistenia-iniciante.png")
st.title("Treino Iniciante")

tab1, tab2, tab3 = st.tabs(["Treino de Empurrar", "Treino de Puxar",  "Core e Pernas"])


with tab1:
    st.markdown("### Orientações")
    st.write("""O treino conta com 6 exercícios que vão aumentar o seu número de flexões e te permitir fazer variações mais difíceis no próximo nível. Além disso, vão te preparar para fazer dips nas paralelas e fortalecerão seu peitoral, tríceps e ombros.

*IMPORTANTE: Você deve fazer 3 séries de cada exercício com 2 minutos de descanso entre estas séries e só depois passar para o próximo exercício.
Para que o treino seja eficiente, aí vão algumas recomendações:

- Durante as flexões mantenha sempre o tronco alinhado com as pernas, sem levantar nem abaixar demais a cintura;
- Nos exercícios com hold no nome, significa que você deve segurar aquela posição pelo tempo estipulado.
- Ao descer nas flexões e ao segurar a posição nos últimos exercícios, sempre dobre os cotovelos para trás e nunca para os lados;
- Nas flexões faça o movimento completo, descendo até quase tocar o peitoral no chão e subindo até esticar os braços;
- No bench dips, mantenha as pernas sempre esticadas e desça até o cotovelo passar um pouco do ângulo de 90°""")
    
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Push up")
        st.image("images/iniciante/push_up.png", width=240)

        
    
    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=jWxvty2KROs")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Knee push up")
        st.image("images/iniciante/knee_push_up.png", width=240)

        
    
    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=3WUUeM07i_Q")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Bench dips")
        st.image("images/iniciante/bench_dips.png", width=240)

        
    
    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=16-WWEQNiK0")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Decline push up advanced hold")
        st.image("images/iniciante/decline_push_up_advanced_hold.png", width=240)

        
    
    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=xloazKLlfnw")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Dips advanced hold")
        st.image("images/iniciante/dips_advanced_hold.png", width=240)

        
    
    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=K3YE-tG6kPo&pp=ygUTaG93IHRvIGRvIGRpcHMgaG9sZA%3D%3D")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Pike hold")
        st.image("images/iniciante/pike_hold.png", width=240)

        
    
    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=K3YE-tG6kPo&pp=ygUTaG93IHRvIGRvIGRpcHMgaG9sZA%3D%3D")



with tab2:
    st.markdown("### Orientações")
    st.write("""São 6 exercícios com este foco específico e que de quebra vão deixar suas costas, bíceps e antebraços maiores e mais fortes.

*IMPORTANTE: Você deve fazer 3 séries de cada exercício com 2 minutos de descanso entre estas séries e só depois passar para o próximo exercício.

Durante a execução do treino tome os seguintes cuidados:
- Quando estiver pendurado na barra não deixe o pescoço enterrado entre os ombros;
- Nos exercícios pull up, as palmas das mãos ficam voltadas pra frente;
- Nos exercícios chin up, as palmas das mãos ficam voltadas para você;
- No chin up, suba até o queixo chegar na altura da barra e desça até esticar os braços completamente;
- Na barra negativa, suba com ajuda ou impulso e desça de forma bem lenta até esticar os braços completamente;
- Nas barras inclinadas mantenha o corpo alinhado durante todo o movimento, sem deixar a cintura abaixar;
- Nos exercícios com hold no nome, significa que você deve segurar aquela posição pelo tempo estipulado.""")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Chin up")
        st.image("images/iniciante/chin_up.png", width=240)

    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=mjNHoibfrMo")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Chin up advanced hold")
        st.image("images/iniciante/chin_up_advanced_hold.png", width=240)

    with col2:
        st.write("Video")
        #st.video("https://youtu.be/tkLrUnNZ0SY?si=7vSGXSIQncDNHpK-")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Pull up advanced hold")
        st.image("images/iniciante/pull_up_advanced_hold.png", width=240)

    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=VpeeqGkiDUU")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Negative pull up")
        st.image("images/iniciante/negative_pull_up.png", width=240)

    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=XBsvbpdNiEU&pp=ygUWaG93IHRvIGRvIHB1bGwgdXAgaG9sZA%3D%3D")


    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Australian pull up")
        st.image("images/iniciante/australian_pull_up.png", width=240)

    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=bHO0A4ZF_Zg")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Incline chin up")
        st.image("images/iniciante/incline_chin_up.png", width=240)

    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=Aaxq4ikl8PE")


with tab3:
    st.markdown("### Orientações")
    st.write("""Este é o treino que vai te proporcionar uma shape simétrico, com pernas maiores e mais fortes, mas não é só isso.

Os exercícios de abdômen e lombar vão te preparar para futuros exercícios mais difíceis que requerem bastante estabilização do core.

*IMPORTANTE: Você deve fazer 3 séries de cada exercício com 2 minutos de descanso entre estas séries e só depois passar para o próximo exercício.

Para que o treino seja eficiente e seguro,  basta seguir estas dicas:
- No agachamento mantenha o tronco alinhado e desça até as pernas dobrarem num ângulo um pouco menor que que 90°;
- No hamstring levers, use a força das pernas para levantar o tronco;
- No calf raises desça o calcanhar abaixo do nível da ponta dos pés e suba até a panturrilha contrair ao máximo;
- No knee raises, evite ao máximo balançar o tronco e levante os joelhos até a altura do peito;
- No legs hold, tente manter as pernas sempre esticadas;
- No short bridge, lembre-se de sempre manter a cintura o mais alto possível, contraindo os músculos da lombar.""")

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Squat")
        st.image("images/iniciante/squat.png", width=240)
    
    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=xqvCmoLULNY")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Hamstring levers")
        st.image("images/iniciante/hamstring_levers.png", width=240)

    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=lbV2P9HvY7A&pp=ygUfaG93IHRvIGRvIGhhbXN0cmluZyBzaG9ydCBsZXZlcg%3D%3D")
    
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Calf raises")
        st.image("images/iniciante/calf_raises.png", width=240)
    
    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=c5Kv6-fnTj8&pp=ygUVaG93IHRvIGRvIGNhbGYgcmFpc2Vz")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Hanging knee raises")
        st.image("images/iniciante/hanging_knee_raises.png", width=240)

    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=Wp4BlxcFTkE")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Legs hold")
        st.image("images/iniciante/legs_hold.png", width=240)

    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=fqzMd87uNTI")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Short bridge")
        st.image("images/iniciante/short_bridge.png", width=240)

    with col2:
        st.write("Video")
        #st.video("https://www.youtube.com/watch?v=q4rDeHYMcIg")