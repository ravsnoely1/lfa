from multi_tape_turing_machine import *
def main():
    # Carregar a especificação da máquina de Turing a partir de um arquivo JSON
    with open('maquina_turing.json', 'r') as file:
        json_data = file.read()

    # Carregar a palavra de entrada a partir dos argumentos de linha de comando
    palavra = input("Digite a palavra de entrada: ")

    # Inicializar a máquina de Turing
    mt = MultiTapeTuringMachine(json_data)

    # Executar a máquina de Turing com a palavra de entrada
    resultado = mt.run(palavra)

    # Exibir o resultado
    if resultado:
        print(f"A palavra '{palavra_exemplo}' pertence à linguagem.")
    else:
        print(f"A palavra '{palavra_exemplo}' não pertence à linguagem.")

if __name__ == "__main__":
    main()
