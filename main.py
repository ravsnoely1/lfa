from multi_tape_turing_machine import *
import json

# CEFET/LFA/maquina_turing.json "001100001"

def main():
    # Carregar a especificação da máquina de Turing a partir de um arquivo JSON
    entradas = input()
    dados = entradas.split()
    
    if len(dados) != 2:
        print("Usar: python3 main.py [MT] [Palavra]")
    else:
        arquivo, palavra = dados

        with open(arquivo, "r") as arquivo_json:
            # Lendo e desserializando o conteúdo do arquivo JSON
            json_data = json.load(arquivo_json)

        # Inicializar a máquina de Turing
        mt = MultiTapeTuringMachine()
        mt.load_from_json(json_data)

        # Executar a máquina de Turing com a palavra de entrada
        resultado = mt.run(palavra)

        # Exibir o resultado
        print(resultado)

if __name__ == "__main__":
    main()
