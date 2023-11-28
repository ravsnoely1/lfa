import json
class MultiTapeTuringMachine:
    def __init__(self):
        self.num_tapes = 0
        self.states = []
        self.input_alphabet = []
        self.tape_alphabet = []
        self.start_marker = ""
        self.blank_symbol = ""
        self.transition_function = []
        self.initial_state = ""
        self.final_states = []

    def load_from_json(self, json_data):
        mt_data = json.loads(json_data)
        
        # Extrair dados do JSON
        self.num_tapes = mt_data["mt"][0]
        self.states = mt_data["mt"][1]
        self.input_alphabet = mt_data["mt"][2]
        self.tape_alphabet = mt_data["mt"][3]
        self.start_marker = mt_data["mt"][4]
        self.blank_symbol = mt_data["mt"][5]
        self.transition_function = mt_data["mt"][6]
        self.initial_state = mt_data["mt"][7]
        self.final_states = mt_data["mt"][8]
        
    def run(self, input_word):
        # Inicializar fitas
        tapes = [[self.start_marker] + list(input_word) + [self.blank_symbol] * 1000 for _ in range(self.num_tapes)]

        # Configurar estado inicial
        current_state = self.initial_state
        current_positions = [0] * self.num_tapes

        # Executar a máquina de Turing
        while current_state not in self.final_states:
            # Obter símbolos atuais nas cabeças das fitas
            current_symbols = [tapes[i][current_positions[i]] for i in range(self.num_tapes)]

            # Encontrar a transição correspondente
            transition_found = False
            for transition in self.transition_function:
                if transition[0] == current_state and transition[1:self.num_tapes + 1] == current_symbols:
                    # Aplicar a transição
                    for i in range(self.num_tapes):
                        tapes[i][current_positions[i]] = transition[self.num_tapes + 1][i][0]
                        # Mover a cabeça da fita
                        if transition[self.num_tapes + 1][i][1] == '>':
                            current_positions[i] += 1
                        elif transition[self.num_tapes + 1][i][1] == '<':
                            current_positions[i] -= 1

                    current_state = transition[self.num_tapes + 1][-1]
                    transition_found = True
                    break

            # Se nenhuma transição foi encontrada, a palavra não pertence à linguagem
            if not transition_found:
                return False

        # Se o estado final foi alcançado, a palavra pertence à linguagem
        return True
