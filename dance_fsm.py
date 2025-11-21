class DanceFSM:
    def __init__(self, state="Dança Fechada - Esquerda livre"):
        self.state = state
        self.transitions = {
            "Dança Fechada - Esquerda livre": {
                "Básico": "Dança Fechada - Direita livre",
                "Caminhada": "Dança Fechada - Direita livre",
                "Chapéu": "Dança Fechada - Esquerda livre",
                "Abertura": "Dança Aberta - Direita livre - Mão Esquerda",
            },
            "Dança Fechada - Direita livre": {
                "Básico": "Dança Fechada - Esquerda livre",
                "Giro junto": "Dança Fechada - Esquerda livre",
                "Giro junto com Paulista": "Dança Aberta - Direita livre - Mão Esquerda",
                "Facão": "Dança Fechada - Esquerda livre",
            },
            "Dança Aberta - Esquerda livre - Mão Esquerda": {
                "Abertura": "Dança Aberta - Direita livre - Mão Esquerda",
                "Giro conduzido": "Dança Aberta - Direita livre - Mão Esquerda",
                "Giro conduzido 5": "Dança Aberta - Direita livre - Mão Esquerda",
                "Quebra de braço": "Dança Aberta - Esquerda livre - Mão Esquerda",
                "Chuveirinho": "Dança Aberta - Esquerda livre - Mão Esquerda",
                "Meio Costas": "Dança Aberta - Esquerda livre - Mão Esquerda",
                "Costas com Costas": "Dança Aberta - Direita livre - Mão Esquerda",
                "Costas com Costas 1 Mão": "Dança Aberta - Direita livre - Mão Esquerda",
            },
            "Dança Aberta - Direita livre - Mão Esquerda": {
                "Abertura": "Dança Aberta - Esquerda livre - Mão Esquerda",
                "Giro condutor": "Dança Aberta - Esquerda livre - Mão Esquerda",
                "Fechamento": "Dança Fechada - Esquerda livre",
                "Giro por trás": "Dança Aberta - Esquerda livre - Mão Esquerda",
                "Avião Giro por trás": "Dança Aberta - Esquerda livre - Mão Direita",
                "Debaixo da portinha": "Dança Aberta - Direita livre - Mão Esquerda",
                "Manivela": "Dança Aberta - Esquerda livre - Mão Esquerda",
                "Manivela 1 Mão": "Dança Aberta - Esquerda livre - Mão Esquerda",
                "Giro Ninja": "Dança Aberta - Esquerda livre - Mão Esquerda",
                "Panamericano": "Dança Aberta - Esquerda livre - Mão Esquerda",
                "Panamericano Troca Mão": "Dança Aberta - Esquerda livre - Mão Direita",
            },
            "Dança Aberta - Esquerda livre - Mão Direita": {
                "Giro conduzido": "Dança Aberta - Direita livre - Mão Direita",
                "Quebra de braço": "Dança Aberta - Esquerda livre - Mão Direita",
            },
            "Dança Aberta - Direita livre - Mão Direita": {
                "Giro condutor": "Dança Aberta - Esquerda livre - Mão Direita",
                "Giro por trás": "Dança Aberta - Esquerda livre - Mão Direita",
                "Avião": "Dança Aberta - Esquerda livre - Mão Esquerda",
            },
        }
    def get_valid_step_set(self):
        return self.transitions[self.state]
    
    def get_all_steps(self):
        all_steps = dict()
        for state_transitions in self.transitions.items():
            all_steps[state_transitions[0]] = [x for x in state_transitions[1]]
        return all_steps

    def transition(self, step):
        if step in self.transitions[self.state]:
            self.state = self.transitions[self.state][step]
            return self.state
        else:
            raise ValueError(f"Invalid step '{step}' for state '{self.state}'")