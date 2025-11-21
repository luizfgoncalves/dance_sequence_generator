import streamlit as st
from dance_fsm import DanceFSM
import random
from colorama import Fore, Style

# Define colors for each state
STATE_COLORS = {
    "Dança Fechada - Esquerda livre": "blue",
    "Dança Fechada - Direita livre": "cyan",
    "Dança Aberta - Esquerda livre - Mão Esquerda": "green",
    "Dança Aberta - Esquerda livre - Mão Direita": "yellow",
    "Dança Aberta - Direita livre - Mão Esquerda": "magenta",
    "Dança Aberta - Direita livre - Mão Direita": "red",
}

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

# Display current state
color = STATE_COLORS.get(st.session_state.current_state, "black")
st.markdown(f"<h3 style='color:{color}'>Estado Atual: {st.session_state.current_state}</h3>", unsafe_allow_html=True)

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