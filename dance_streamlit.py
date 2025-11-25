import streamlit as st
from src.dance_fsm import DanceFSM
from src.utils import add_step_name_to_image
import random
import time

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
if "current_image" not in st.session_state:
    st.session_state.current_image = fsm.state.image

st.sidebar.header("Configurações")
if st.sidebar.button("Reiniciar Sequência"):
    fsm = DanceFSM()
    st.session_state.sequence = []
    st.session_state.current_state = fsm.state
    st.session_state.current_image = fsm.state.image
    st.rerun()
    # Add a tab for the step catalog

tab1, tab2 = st.tabs(["Gerador de Sequências", "Catálogo de Passos"])

with tab1:
    # Display current state
    color = st.session_state.current_state.color
    st.markdown(f"<h3>Estado Atual: <span style='color:{color}'>{st.session_state.current_state.name}</span></h3>", unsafe_allow_html=True)

    # Display current state image and available steps in two columns
    col1, col2 = st.columns([1, 2])

    with col1:
        imageholder = st.empty()
        imageholder.image(st.session_state.current_image, width="content")
        #st.image(imageholder, width="content")
        captions = st.session_state.current_state.image_caption.split("+")
        if len(captions) > 1:
            st.markdown(f"<span style='color:red'>{captions[0]}</span> <span style='color:blue'>{captions[1]}</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color:red'>{captions[0]}</span>", unsafe_allow_html=True)
    with col2:
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
        add_step_name_to_image(step)
        imageholder.image("img/basico_step.png", width="content")
        time.sleep(1.3)  # Simulate processing delay
        st.success(f"Passo '{step}' executado com sucesso!")
        st.rerun()

    # Display the sequence
    if st.session_state.sequence:
        st.subheader("Sequência Completa:")
        st.write(" → ".join(st.session_state.sequence))
        if st.button("Executar sequência Completa!"):
            sequenceholder = st.empty()
            temp_fsm = DanceFSM()
            sequenceholder.image(temp_fsm.state.image, width=400)
            for step in st.session_state.sequence:
                time.sleep(0.8)
                add_step_name_to_image(step)
                sequenceholder.image("img/basico_step.png", width=400)
                time.sleep(0.8)  # Simulate processing delay
                temp_fsm.transition(step)
                sequenceholder.image(temp_fsm.state.image, width=400)
                

with tab2:
    st.header("Catálogo de Passos")
    st.write("Aqui estão todos os passos disponíveis no sistema:")
    steps_catalog = fsm.get_all_step_set()
    st.write(steps_catalog)