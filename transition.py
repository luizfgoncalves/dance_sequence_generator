"""
Transition mappings for the Dance FSM.
Defines how states transition based on dance steps.
"""

from state import (
    DANCA_FECHADA_ESQUERDA_LIVRE,
    DANCA_FECHADA_DIREITA_LIVRE,
    DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
    DANCA_ABERTA_DIREITA_LIVRE_MAO_ESQUERDA,
    DANCA_ABERTA_ESQUERDA_LIVRE_MAO_DIREITA,
    DANCA_ABERTA_DIREITA_LIVRE_MAO_DIREITA,
    DanceState
)
from step import (
    BASICO,
    CAMINHADA,
    CHAPEU,
    ABERTURA,
    GIRO_JUNTO,
    GIRO_JUNTO_PAULISTA,
    FACAO,
    GIRO_CONDUZIDO,
    GIRO_CONDUZIDO_5,
    QUEBRA_BRACO,
    CHUVEIRINHO,
    MEIO_COSTAS,
    COSTAS_COM_COSTAS,
    COSTAS_COM_COSTAS_1_MAO,
    GIRO_CONDUTOR,
    GIRO_CONDUTOR_TROCA_MAO,
    FECHAMENTO,
    GIRO_POR_TRAS,
    AVIAO_GIRO_POR_TRAS,
    DEBAIXO_PORTINHA,
    MANIVELA,
    MANIVELA_1_MAO,
    GIRO_NINJA,
    PANAMERICANO,
    PANAMERICANO_TROCA_MAO,
    AVIAO,
    DanceStep
)

# Define transitions using objects: {state_object: {step_object: next_state_object}}
TRANSITIONS = {
    DANCA_FECHADA_ESQUERDA_LIVRE: {
        BASICO: DANCA_FECHADA_DIREITA_LIVRE,
        CAMINHADA: DANCA_FECHADA_DIREITA_LIVRE,
        CHAPEU: DANCA_FECHADA_ESQUERDA_LIVRE,
        ABERTURA: DANCA_ABERTA_DIREITA_LIVRE_MAO_ESQUERDA,
    },
    DANCA_FECHADA_DIREITA_LIVRE: {
        BASICO: DANCA_FECHADA_ESQUERDA_LIVRE,
        GIRO_JUNTO: DANCA_FECHADA_ESQUERDA_LIVRE,
        GIRO_JUNTO_PAULISTA: DANCA_ABERTA_DIREITA_LIVRE_MAO_ESQUERDA,
        FACAO: DANCA_FECHADA_ESQUERDA_LIVRE,
    },
    DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA: {
        ABERTURA: DANCA_ABERTA_DIREITA_LIVRE_MAO_ESQUERDA,
        GIRO_CONDUZIDO: DANCA_ABERTA_DIREITA_LIVRE_MAO_ESQUERDA,
        GIRO_CONDUZIDO_5: DANCA_ABERTA_DIREITA_LIVRE_MAO_ESQUERDA,
        QUEBRA_BRACO: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
        CHUVEIRINHO: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
        MEIO_COSTAS: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
        COSTAS_COM_COSTAS: DANCA_ABERTA_DIREITA_LIVRE_MAO_ESQUERDA,
        COSTAS_COM_COSTAS_1_MAO: DANCA_ABERTA_DIREITA_LIVRE_MAO_ESQUERDA,
    },
    DANCA_ABERTA_DIREITA_LIVRE_MAO_ESQUERDA: {
        ABERTURA: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
        GIRO_CONDUTOR: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
        GIRO_CONDUTOR_TROCA_MAO: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_DIREITA,
        FECHAMENTO: DANCA_FECHADA_ESQUERDA_LIVRE,
        GIRO_POR_TRAS: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
        AVIAO_GIRO_POR_TRAS: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_DIREITA,
        DEBAIXO_PORTINHA: DANCA_ABERTA_DIREITA_LIVRE_MAO_ESQUERDA,
        MANIVELA: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
        MANIVELA_1_MAO: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
        GIRO_NINJA: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
        PANAMERICANO: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
        PANAMERICANO_TROCA_MAO: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_DIREITA,
    },
    DANCA_ABERTA_ESQUERDA_LIVRE_MAO_DIREITA: {
        GIRO_CONDUZIDO: DANCA_ABERTA_DIREITA_LIVRE_MAO_DIREITA,
        QUEBRA_BRACO: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_DIREITA,
    },
    DANCA_ABERTA_DIREITA_LIVRE_MAO_DIREITA: {
        GIRO_CONDUTOR: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_DIREITA,
        GIRO_POR_TRAS: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_DIREITA,
        AVIAO: DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
    },
}


def get_next_state(state: DanceState, step: DanceStep) -> DanceState:
    """
    Get the next state given the current state and step.
    
    Args:
        current_state: Name of the current state (or state object)
        step: Name of the step to perform (or step object)
        
    Returns:
        Next state
        
    Raises:
        ValueError: If the transition is invalid
    """
    
    if state not in TRANSITIONS:
        raise ValueError(f"Invalid state: '{state}'")
    
    if step not in TRANSITIONS[state]:
        raise ValueError(f"Invalid step '{step}' for state '{state}'")
    
    next_state = TRANSITIONS[state][step]
    return next_state


def get_valid_transitions(current_state: DanceState) -> dict:
    """
    Get all valid transitions for a given state.
    
    Args:
        current_state: Current state
        
    Returns:
        List of valid transitions
    """
    
    if current_state not in TRANSITIONS:
        raise ValueError(f"Invalid state: '{current_state}'")
    
    # Convert object-based transitions to string-based for backward compatibility
    return TRANSITIONS[current_state]
