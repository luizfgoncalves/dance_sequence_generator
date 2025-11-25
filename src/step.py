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
PASSO_BASICO = DanceStep("Passo Básico", "Passo básico do forró universitário.", difficulty=1)
CAMINHADA = DanceStep("Caminhada", "Realiza uma abertura na dança e caminha lado a lado com o par em 3 pisadas. Ao finalizar, fecha a dança novamente.", difficulty=1)
CHAPEU = DanceStep("Chapéu", "Movimento similar a caminhada, porém o condutor toma a frente do conduzido em 3 pisadas. As outras 3 pisadas são utilizadas para o conduzido reencontrar o condutor e fechar a dança ", difficulty=2)
ABERTURA = DanceStep("Abertura", "Abertura da dança fechada para a dança aberta", difficulty=1)
GIRO_JUNTO = DanceStep("Giro junto", "Giro em junto do condutor e conduzido, realizando um angulo de 360° e voltando a mesma posição inicial", difficulty=2)
GIRO_JUNTO_PAULISTA = DanceStep("Giro junto com Paulista", "Giro junto com a adição de um giro paulista para o conduzido, em três pisadas", difficulty=3)
FACAO = DanceStep("Facão", "Movimento de deslocamento em que o condutor abre espaço para o conduzido, e eles realizam uma movimentação de 180° juntos", difficulty=2)
GIRO_CONDUZIDO = DanceStep("Giro conduzido", "Condutor conduz um giro no conduzido em 3 pisadas", difficulty=2)
GIRO_CONDUZIDO_5 = DanceStep("Giro conduzido 5", "Condutor conduz dois giros no conduzido em 5 pisadas", difficulty=3)
QUEBRA_BRACO = DanceStep("Quebra de braço", "Movimento de quebra de braço, em que o condutor troca de lado abaixando uma das mãos do conduzido, que encaixa em suas costas", difficulty=3)
CHUVEIRINHO = DanceStep("Chuveirinho", "Movimento em que o condutor troca de lado com o conduzido levantando as duas mãos do mar, e depois retorna para a posição original.", difficulty=2)
MEIO_COSTAS = DanceStep("Meio Costas", "Movimento em que o condutor abaixa a mão direita do conduzido (como na quebra de braço) e mantém a mão esquerda conectada com sua mão direita. Depois volta para a base original", difficulty=3)
COSTAS_COM_COSTAS = DanceStep("Costas com Costas", "Movimento de três etapas. Consiste no meio costas, seguido de um deslocamento lateral com o conduzido, e depois um giro do conduzido", difficulty=3)
COSTAS_COM_COSTAS_1_MAO = DanceStep("Costas com Costas 1 Mão", "Mesmo movimento de pernas do Costas com Costas, porém mantendo apenas a mão esquerda do condutor conectada a direita do conduzido", difficulty=4)
GIRO_CONDUTOR = DanceStep("Giro condutor", "O condutor se gira, trocando de lado com o conduzido, em 3 pisadas", difficulty=2)
GIRO_CONDUTOR_TROCA_MAO = DanceStep("Giro condutor Troca Mão", "O mesmo do giro condutor, porém trocando a conexão de esquerda com direita, para direita com direita", difficulty=2)
FECHAMENTO = DanceStep("Fechamento", "Sai da dança aberta e volta para a dança fechada", difficulty=1)
GIRO_POR_TRAS = DanceStep("Giro por trás", "O condutor gira no sentido horário, circulando o conduzido em 3 pisadas", difficulty=3)
AVIAO_GIRO_POR_TRAS = DanceStep("Avião Giro por trás", "Mantem o mesmo fluxo do giro por trás, porém deslizando a mão do conduzido e trocando a pegada, de esquerda com direita para direita com direita", difficulty=4)
DEBAIXO_PORTINHA = DanceStep("Debaixo da portinha", "Movimento em que o condutor coloca o braço direito do conduzido em seu ombro direito em 3 pisadas, e depois gira o conduzido em mais 3 pisadas", difficulty=2)
MANIVELA = DanceStep("Manivela", "Movimento em que o condutor propõe um giro em linha do conduzido em 5 pisadas, ficando de costas para o par e lançando a mão direita e logo depois a esquerda (principal para condução)", difficulty=3)
MANIVELA_1_MAO = DanceStep("Manivela 1 Mão", "Mesma movimentação da manivela, porém utilizando apenas a mão esquerda", difficulty=4)
GIRO_NINJA = DanceStep("Giro Ninja", "Movimento em que o condutor propõe um giro em linha de 5 pisadas para o conduzido ao empurrar seu braço direito com a mão direita", difficulty=4)
PANAMERICANO = DanceStep("Panamericano", "Movimento em que o condutor propõe um giro em linha de 5 pisadas para o conduzido ao abrir um espaço em sua frente e circulando a cabeça do conduzido com a mão esquerda", difficulty=3)
PANAMERICANO_TROCA_MAO = DanceStep("Panamericano Troca Mão", "Mesmo movimento do Panamericano, porém trocando a mão utilizada para condução durante o movimento", difficulty=4)
AVIAO = DanceStep("Avião", "Movimento de troca de lado em que o condutor propõe que o conduzido deslize sua mão direita, passando pelo braço até chegar a outra mão do condutor", difficulty=3)

# Dictionary mapping step names to step objects
ALL_STEPS = {
    "Passo Básico": PASSO_BASICO,
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
