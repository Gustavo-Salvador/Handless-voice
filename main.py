import os, subprocess, sys, time

if __name__ == "__main__":
    tentativas = 0
    while True:
        tentativas += 1
        if tentativas > 3:
            print("\033[91mErro:\033[0m Não foi possível instalar as bibliotecas necessárias após várias tentativas.")
            print('Favor reinstalar o programa no github ""') # TODO: adicionar link do github
            sys.exit(1)

        # Verifica se as bibliotecas necessárias estão instaladas
        try:
            from core import importacoes
            break

        except ImportError as e:
            # Informa o usuário sobre a falta de bibliotecas
            print("\033[91mErro:\033[0m Algumas bibliotecas não estão instaladas, tentando instalar.")
            
            # Tenta instalar as bibliotecas necessárias de requiriments.txt
            # Verifica se o arquivo de requisitos existe
            import os
            if not os.path.isfile("requiriments.txt"):
                # Erro: Printar em vermelho
                print("\033[91mArquivo 'requiriments.txt' não encontrado.\033[0m")
                print('Favor reinstalar o programa no github ""') # TODO: adicionar link do github
                sys.exit(1)

            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requiriments.txt"])
            print("Bibliotecas instaladas com sucesso.")

