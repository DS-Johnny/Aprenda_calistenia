import streamlit as st


st.sidebar.title("Treino Básico")
st.title("Treino Básico")

tab1, tab2, tab3 = st.tabs(["Treino de Flexão", "Treino de Barra",  "Core e pernas"])


with tab1:
    st.write("Treino de Flexão")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Knee push up")
        st.image("knee_push_up.png", width=240)

        
    
    with col2:
        st.write("video")
        st.video("https://www.youtube.com/watch?v=jWxvty2KROs")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Incline push up")
        st.image("incline_push_up.png", width=240)

        
    
    with col2:
        st.write("video")
        st.video("https://www.youtube.com/watch?v=3WUUeM07i_Q")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Push up hold")
        st.image("push_up_hold.png", width=240)

        
    
    with col2:
        st.write("video")
        st.video("https://www.youtube.com/watch?v=16-WWEQNiK0")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Decline push up hold")
        st.image("decline_push_up_hold.png", width=240)

        
    
    with col2:
        st.write("video")
        st.video("https://www.youtube.com/watch?v=xloazKLlfnw")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Dips hold")
        st.image("dips_hold.png", width=240)

        
    
    with col2:
        st.write("video")
        st.video("https://www.youtube.com/watch?v=K3YE-tG6kPo&pp=ygUTaG93IHRvIGRvIGRpcHMgaG9sZA%3D%3D")



with tab2:
    st.write("Treino de Barra")

with tab3:
    st.write("Core e pernas")