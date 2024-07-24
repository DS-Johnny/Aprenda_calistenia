import streamlit as st


st.sidebar.title("Treino Básico")
st.sidebar.image("images/basico/grade-treinos-calistenia-iniciante-basico.png")
st.title("Treino Básico")

tab1, tab2, tab3 = st.tabs(["Treino de Flexão", "Treino de Barra",  "Core e Pernas"])


with tab1:
    st.markdown("### Orientações")
    st.write("""Começamos o nosso programa com um treino pra você aprender uma das bases da calistenia, a flexão de braço.
Ele é composto por 5 exercícios que vão fortalecer seu peitoral, braços e ombros para que você possa fazer a flexão normal num futuro próximo.

*IMPORTANTE*: Você deve fazer 3 séries de cada exercício com 2 minutos de descanso entre estas séries e só depois passar para o próximo exercício.

Existem alguns cuidados que você deve tomar para garantir a eficiência dos exercícios e evitar lesões:
- Durante as flexões mantenha sempre o tronco alinhado com as pernas, sem levantar nem abaixar demais a cintura;
- Ao descer, sempre dobre os cotovelos para trás e nunca para os lados;
- Faça o movimento completo, descendo até quase tocar o peitoral no chão e subindo até esticar os braços;
- Nos exercícios com hold no nome você deve segurar aquela posição pelo tempo estipulado.""")
    
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Knee push up")
        st.image("images/basico/knee_push_up.png", width=240)

        
    
    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=jWxvty2KROs")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Incline push up")
        st.image("images/basico/incline_push_up.png", width=240)

        
    
    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=3WUUeM07i_Q")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Push up hold")
        st.image("images/basico/push_up_hold.png", width=240)

        
    
    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=16-WWEQNiK0")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Decline push up hold")
        st.image("images/basico/decline_push_up_hold.png", width=240)

        
    
    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=xloazKLlfnw")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Dips hold")
        st.image("images/basico/dips_hold.png", width=240)

        
    
    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=K3YE-tG6kPo&pp=ygUTaG93IHRvIGRvIGRpcHMgaG9sZA%3D%3D")



with tab2:
    st.markdown("### Orientações")
    st.write("""Este treino tem o objetivo de te preparar para outro exercício base da Calistenia, a barra fixa.

Ele é composto por 6 exercícios que fortalecerão seus antebraços, bíceps e costas.

*IMPORTANTE: Você deve fazer 3 séries de cada exercício com 2 minutos de descanso entre estas séries e só depois passar para o próximo exercício.

Alguns cuidados que devem ser tomados são:
- Quando estiver pendurado na barra não deixe o pescoço enterrado entre os ombros;
- Nos exercícios pull up, a palmas das mãos ficam voltadas pra frente;
- Nos exercícios chin up, as palmas das mãos ficam voltadas para você;
- No negative chin up você deve subir com impulso ou ajuda e descer bem devagar;
- Nas barras inclinadas mantenha o corpo alinhado durante todo o movimento, sem deixar a cintura abaixar;
- Nos exercícios com hold no nome você deve segurar aquela posição pelo tempo estipulado.""")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Negative chin up")
        st.image("images/basico/negative_chin_up.png", width=240)

    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=mjNHoibfrMo")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Chin up hold")
        st.image("images/basico/chin_up_hold.png", width=240)

    with col2:
        st.write("Video")
        st.video("https://youtu.be/tkLrUnNZ0SY?si=7vSGXSIQncDNHpK-")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Scapula pull up")
        st.image("images/basico/scapula_pull_up.png", width=240)

    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=VpeeqGkiDUU")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Pull up hold")
        st.image("images/basico/pull_up_hold.png", width=240)

    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=XBsvbpdNiEU&pp=ygUWaG93IHRvIGRvIHB1bGwgdXAgaG9sZA%3D%3D")


    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Australian pull up")
        st.image("images/basico/australian_pull_up.png", width=240)

    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=bHO0A4ZF_Zg")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Incline chin up")
        st.image("images/basico/incline_chin_up.png", width=240)

    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=Aaxq4ikl8PE")


with tab3:
    st.markdown("### Orientações")
    st.write("""Ainda que o grande objetivo deste programa seja que você aprenda barra e flexão, não podemos negligenciar as outras partes do corpo.

Por isso temos este treino de pernas, abdômen e lombar, grupos musculares importantíssimos até mesmo para se desenvolver nas barras, flexões e exercícios mais avançados.

*IMPORTANTE: Você deve fazer 3 séries de cada exercício com 2 minutos de descanso entre estas séries e só depois passar para o próximo exercício.

Para que o treino seja eficiente e seguro, tome os seguintes cuidados:
- No agachamento mantenha o tronco alinhado e desça até as pernas dobrarem num ângulo um pouco menor que que 90°;
- No hamstring levers, use a força das pernas para levantar o tronco;
- No calf raises desça o calcanhar abaixo do nível da ponta dos pés e suba até a panturrilha contrair ao máximo;
- No leg raises e legs hold, tente manter as pernas sempre esticadas;
- No plank mantenha o corpo alinhado, sem levantar nem abaixar demais a cintura.""")

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Squat")
        st.image("images/basico/squat.png", width=240)
    
    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=xqvCmoLULNY")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Hamstring levers")
        st.image("images/basico/hamstring_levers.png", width=240)

    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=lbV2P9HvY7A&pp=ygUfaG93IHRvIGRvIGhhbXN0cmluZyBzaG9ydCBsZXZlcg%3D%3D")
    
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Calf raises")
        st.image("images/basico/calf_raises.png", width=240)
    
    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=c5Kv6-fnTj8&pp=ygUVaG93IHRvIGRvIGNhbGYgcmFpc2Vz")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Lying leg raises")
        st.image("images/basico/lying_leg_raises.png", width=240)

    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=Wp4BlxcFTkE")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Legs hold")
        st.image("images/basico/legs_hold.png", width=240)

    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=fqzMd87uNTI")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Plank")
        st.image("images/basico/plank.png", width=240)

    with col2:
        st.write("Video")
        st.video("https://www.youtube.com/watch?v=q4rDeHYMcIg")