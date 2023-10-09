import time

print('-------------\nsisteme de login\n-------------')
print('1 - registrar\n2 - logar\n-------------')
resposta = input("-->")

def criar_conta():
    rodando = True
    print('\nvamos realizar seu registro:\n')
    while rodando:
        usuario = input("Escolha seu nome de usuario: ")
        with open('bd\\bd.txt', "r") as file:
            linhas = file.readlines()
        usuarios = [linha.strip() for linha in linhas[::2]]  # Obtém os nomes de usuário das linhas pares (0, 2, 4, ...)
        if usuario in usuarios:
            print("\nUsuario ja existe, escolha outro nome.\n")
        else:
            break
    senha = input("Escolha a sua senha: ")
    with open("bd\\bd.txt", 'a', encoding="utf-8") as arquivo:
        arquivo.writelines(f'{usuario}\n')
        arquivo.writelines(f'{senha}\n')


#Função logar conta 
def logar_conta():
    input_user_procurado = input("Insira seu usuario: ")
    input_senha_user_procurado = input("insira a sua senha: ")
    flag_user_encontrado = False
    flag_senha_encontrado = False
    with open("bd\\bd.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for i in range(0, len(linhas), 2):
            usuario_armazenado = linhas[i].strip()
            senha_armazenada = linhas[i+1].strip()
            if usuario_armazenado == input_user_procurado:
                flag_user_encontrado = True
                if senha_armazenada == input_senha_user_procurado: 
                    flag_senha_encontrado = True
                break
    
    if(flag_user_encontrado==True):                          
        time.sleep(1)
        print("Usuario encontrado")
        if(flag_senha_encontrado==True):
            time.sleep(1)
            print('...')
            time.sleep(1)                                           
            print('...')
            time.sleep(1)
            print('...')
            print("Login realizado com sucesso!")
        else:
            print("Senha não encontrada")
    else:
        print("Usuario não encontrado")                            

if resposta == '1':
    criar_conta()
    print('\nProntinho!')
    print('\nAgora vamos logar em sua conta\n')
    logar_conta()

elif resposta == '2':
    logar_conta()

    



