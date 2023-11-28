import json

class MultiTapeTuringMachine:
    def __init__(self, json_data):
        self.load_from_json(json_data)

    def load_from_json(self, json_data):
        # Implementar lógica para carregar a máquina de Turing a partir do JSON
        mt_data = json.loads(json_data)
        # Extrair dados do JSON e inicializar a máquina

    def run(self, input_word):
        # Implementar a lógica de execução da máquina de Turing com a palavra de entrada
        # Retorna True se a palavra pertencer à linguagem, False caso contrário
