"""
State classes for the Dance FSM.
Each state represents a specific dance position.
"""

class DanceState:
    """Base class for all dance states."""
    
    def __init__(self, name: str, description: str = "", color: str = "black"):
        self.name = name
        self.description = description
        self.color = color
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"DanceState('{self.name}')"
    
    def __eq__(self, other):
        if isinstance(other, DanceState):
            return self.name == other.name
        return False
    
    def __hash__(self):
        return hash(self.name)

# Define all available states
DANCA_FECHADA_ESQUERDA_LIVRE = DanceState(
    "Dança Fechada - Esquerda livre",
    "Posição fechada com a perna esquerda livre",
    "blue"
)

DANCA_FECHADA_DIREITA_LIVRE = DanceState(
    "Dança Fechada - Direita livre",
    "Posição fechada com a perna direita livre",
    "cyan"
)

DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA = DanceState(
    "Dança Aberta - Esquerda livre - Mão Esquerda",
    "Posição aberta, perna esquerda livre, segurando com a mão esquerda",
    "green"
)

DANCA_ABERTA_DIREITA_LIVRE_MAO_ESQUERDA = DanceState(
    "Dança Aberta - Direita livre - Mão Esquerda",
    "Posição aberta, perna direita livre, segurando com a mão esquerda",
    "orange"
)

DANCA_ABERTA_ESQUERDA_LIVRE_MAO_DIREITA = DanceState(
    "Dança Aberta - Esquerda livre - Mão Direita",
    "Posição aberta, perna esquerda livre, segurando com a mão direita",
    "violet"
)

DANCA_ABERTA_DIREITA_LIVRE_MAO_DIREITA = DanceState(
    "Dança Aberta - Direita livre - Mão Direita",
    "Posição aberta, perna direita livre, segurando com a mão direita",
    "red"
)

# Dictionary mapping state names to state objects
ALL_STATES = {
    "Dança Fechada - Esquerda livre": DANCA_FECHADA_ESQUERDA_LIVRE,
    "Dança Fechada - Direita livre": DANCA_FECHADA_DIREITA_LIVRE,
    "Dança Aberta - Esquerda livre - Mão Esquerda": DANCA_ABERTA_ESQUERDA_LIVRE_MAO_ESQUERDA,
    "Dança Aberta - Direita livre - Mão Esquerda": DANCA_ABERTA_DIREITA_LIVRE_MAO_ESQUERDA,
    "Dança Aberta - Esquerda livre - Mão Direita": DANCA_ABERTA_ESQUERDA_LIVRE_MAO_DIREITA,
    "Dança Aberta - Direita livre - Mão Direita": DANCA_ABERTA_DIREITA_LIVRE_MAO_DIREITA,
}
