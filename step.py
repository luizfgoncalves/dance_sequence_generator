"""
Step classes for the Dance FSM.
Each step represents a specific dance move with its properties.
"""

class DanceStep:
    """Represents a dance step with its properties."""
    
    def __init__(self, name: str, description: str = "", difficulty: int = 1):
        self.name = name
        self.description = description
        self.difficulty = difficulty  # 1 (easy) to 5 (hard)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"DanceStep('{self.name}')"
    
    def __eq__(self, other):
        if isinstance(other, DanceStep):
            return self.name == other.name
        return False
    
    def __hash__(self):
        return hash(self.name)


# Define all available steps
BASICO = DanceStep("Básico", "Passo básico fundamental", difficulty=1)
CAMINHADA = DanceStep("Caminhada", "Movimento de caminhada", difficulty=1)
CHAPEU = DanceStep("Chapéu", "Movimento de chapéu", difficulty=2)
ABERTURA = DanceStep("Abertura", "Abertura da dança", difficulty=1)
GIRO_JUNTO = DanceStep("Giro junto", "Giro em conjunto", difficulty=2)
GIRO_JUNTO_PAULISTA = DanceStep("Giro junto com Paulista", "Giro junto com variação paulista", difficulty=3)
FACAO = DanceStep("Facão", "Movimento de facão", difficulty=2)
GIRO_CONDUZIDO = DanceStep("Giro conduzido", "Giro conduzido pelo condutor", difficulty=2)
GIRO_CONDUZIDO_5 = DanceStep("Giro conduzido 5", "Giro conduzido com 5 tempos", difficulty=3)
QUEBRA_BRACO = DanceStep("Quebra de braço", "Movimento de quebra de braço", difficulty=3)
CHUVEIRINHO = DanceStep("Chuveirinho", "Movimento de chuveirinho", difficulty=2)
MEIO_COSTAS = DanceStep("Meio Costas", "Movimento de meio costas", difficulty=3)
COSTAS_COM_COSTAS = DanceStep("Costas com Costas", "Movimento costas com costas", difficulty=3)
COSTAS_COM_COSTAS_1_MAO = DanceStep("Costas com Costas 1 Mão", "Costas com costas segurando uma mão", difficulty=4)
GIRO_CONDUTOR = DanceStep("Giro condutor", "Giro do condutor", difficulty=2)
GIRO_CONDUTOR_TROCA_MAO = DanceStep("Giro condutor Troca Mão", "Giro do condutor com troca de mão", difficulty=2)
FECHAMENTO = DanceStep("Fechamento", "Fechamento da dança", difficulty=1)
GIRO_POR_TRAS = DanceStep("Giro por trás", "Giro por trás da conduzida", difficulty=3)
AVIAO_GIRO_POR_TRAS = DanceStep("Avião Giro por trás", "Avião com giro por trás", difficulty=4)
DEBAIXO_PORTINHA = DanceStep("Debaixo da portinha", "Movimento debaixo da portinha", difficulty=2)
MANIVELA = DanceStep("Manivela", "Movimento de manivela", difficulty=3)
MANIVELA_1_MAO = DanceStep("Manivela 1 Mão", "Manivela com uma mão", difficulty=4)
GIRO_NINJA = DanceStep("Giro Ninja", "Giro rápido estilo ninja", difficulty=4)
PANAMERICANO = DanceStep("Panamericano", "Movimento panamericano", difficulty=3)
PANAMERICANO_TROCA_MAO = DanceStep("Panamericano Troca Mão", "Panamericano com troca de mão", difficulty=4)
AVIAO = DanceStep("Avião", "Movimento de avião", difficulty=3)

# Dictionary mapping step names to step objects
ALL_STEPS = {
    "Básico": BASICO,
    "Caminhada": CAMINHADA,
    "Chapéu": CHAPEU,
    "Abertura": ABERTURA,
    "Giro junto": GIRO_JUNTO,
    "Giro junto com Paulista": GIRO_JUNTO_PAULISTA,
    "Facão": FACAO,
    "Giro conduzido": GIRO_CONDUZIDO,
    "Giro conduzido 5": GIRO_CONDUZIDO_5,
    "Quebra de braço": QUEBRA_BRACO,
    "Chuveirinho": CHUVEIRINHO,
    "Meio Costas": MEIO_COSTAS,
    "Costas com Costas": COSTAS_COM_COSTAS,
    "Costas com Costas 1 Mão": COSTAS_COM_COSTAS_1_MAO,
    "Giro condutor": GIRO_CONDUTOR,
    "Giro condutor Troca Mão": GIRO_CONDUTOR_TROCA_MAO,
    "Fechamento": FECHAMENTO,
    "Giro por trás": GIRO_POR_TRAS,
    "Avião Giro por trás": AVIAO_GIRO_POR_TRAS,
    "Debaixo da portinha": DEBAIXO_PORTINHA,
    "Manivela": MANIVELA,
    "Manivela 1 Mão": MANIVELA_1_MAO,
    "Giro Ninja": GIRO_NINJA,
    "Panamericano": PANAMERICANO,
    "Panamericano Troca Mão": PANAMERICANO_TROCA_MAO,
    "Avião": AVIAO,
}
