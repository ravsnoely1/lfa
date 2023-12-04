from multi_tape_turing_machine import *
import json
import sys

# maquina_turing.json "001100001"
def main():
    if len(sys.argv) != 3:
        print("Usar: python3 main.py [MT] [Palavra]")
        sys.exit(1)
  
    arquivo = sys.argv[1]
    palavra = sys.argv[2]

    with open(arquivo, "r") as arquivo:
        # Lendo e desserializando o conteúdo do arquivo JSON
        json_data = json.load(arquivo)

    # Inicializar a máquina de Turing
    mt = MultiTapeTuringMachine()
    mt.load_from_json(json_data)

    # Executar a máquina de Turing com a palavra de entrada
    resultado = mt.run(palavra)

    # Exibir o resultado
    print(resultado)

if __name__ == "__main__":
    main()
