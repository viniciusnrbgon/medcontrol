from medicamento import Medicamento
from storage import load, save

def menu():
    print("\n1. Adicionar medicamento")
    print("2. Listar medicamentos")
    print("3. Remover medicamento")
    print("4. Sair")

def adicionar():
    nome = input("Nome: ")
    horario = input("Horário: ")

    med = Medicamento(nome, horario)
    data = load()
    data.append(med.to_dict())
    save(data)

    print("Medicamento adicionado!")

def listar():
    data = load()
    if not data:
        print("Nenhum medicamento cadastrado.")
        return

    for i, med in enumerate(data):
        print(f"{i} - {med['nome']} às {med['horario']}")

def remover():
    data = load()
    listar()
    try:
        index = int(input("Índice para remover: "))
        data.pop(index)
        save(data)
        print("Removido!")
    except:
        print("Erro ao remover.")

def main():
    while True:
        menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            remover()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()