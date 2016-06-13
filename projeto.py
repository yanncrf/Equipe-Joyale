

import joyale

#exibirPacientes = joyale.listarPacientes("CriançasCadastradas.txt")
#print (exibirPacientes)

opcao = ""
print("Bem vindo ao Sistema!")
while opcao != "x":
    joyale.menu()
    opcao = input("Digite sua opção: ")
    if opcao == "1":
        joyale.cadastrar_paciente()
    elif opcao == "2":
        ler = joyale.listarPacientes2("CriançasCadastradas.txt")

    elif opcao == "x":
        print("Obrigado por usar nosso sistema\nSaindo...")
    else:
        print ("Opção inválida!")


