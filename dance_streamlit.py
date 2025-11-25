import streamlit as st
from dance_fsm import DanceFSM
import random
from colorama import Fore, Style

# Streamlit UI
st.title("Gerador de Sequências de Dança 💃")

# Initialize session state
if "sequence" not in st.session_state:
    st.session_state.sequence = []
if "current_state" not in st.session_state:
    # Initialize the FSM
    fsm = DanceFSM()
    st.session_state.current_state = fsm.state
else:
    fsm = DanceFSM(st.session_state.current_state)

st.sidebar.header("Configurações")
if st.sidebar.button("Reiniciar Sequência"):
    fsm = DanceFSM()
    st.session_state.sequence = []
    st.session_state.current_state = fsm.state
    st.rerun()
    # Add a tab for the step catalog

tab1, tab2 = st.tabs(["Gerador de Sequências", "Catálogo de Passos"])

with tab1:
    # Display current state
    color = st.session_state.current_state.color
    st.markdown(f"<h3>Estado Atual: <span style='color:{color}'>{st.session_state.current_state.name}</span></h3>", unsafe_allow_html=True)

    # Get available steps
    available_steps = [x for x in fsm.get_valid_step_set()]
    st.write("Passos disponíveis:", available_steps)

    # User input for the next step
    step = st.selectbox("Selecione o passo desejado (ou deixe a seleção aleatória):", ["Aleatório"] + available_steps)

    # Process the step
    if st.button("Executar Passo"):
        if step == "Aleatório":
            step = random.choice(list(available_steps))
        elif step not in available_steps:
            st.error("Passo inválido! Tente novamente.")
        
        new_state = fsm.transition(step)
        st.session_state.sequence.append(step)
        st.session_state.current_state = new_state
        st.success(f"Passo '{step}' executado com sucesso!")
        st.rerun()

    # Display the sequence
    if st.session_state.sequence:
        st.subheader("Sequência Completa:")
        st.write(" → ".join(st.session_state.sequence))

with tab2:
    st.header("Catálogo de Passos")
    st.write("Aqui estão todos os passos disponíveis no sistema:")
    steps_catalog = fsm.get_all_step_set()
    st.write(steps_catalog)