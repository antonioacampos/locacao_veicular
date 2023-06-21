class Cliente:
    cpf = ''
    nome =  ''
    endereco = ''
    tel_fixo = -1
    tel_cel = -1
    nascimento = ''
    
def existe_arquivo(nome_arquivo):
    import os
    if os.path.exists(nome_arquivo):
       return True
    else:
       return False

def ler_arq_clientes(nome_arquivo):
    todos_clientes = []
    if existe_arquivo(nome_arquivo):
        ref_arq = open(nome_arquivo,'r')
        for linha in ref_arq: #itera sobre cada linha do arquivo
            info = linha.strip().split(';')
            if len(info) == 6: #Verifica se há informações suficientes para preencher todos os campos
                f = Cliente()
                f.cpf = info[0]
                f.nome = info[1]
                f.endereco = info[2]
                f.tel_fixo = int(info[3])
                f.tel_cel = int(info[4])
                f.nascimento = info[5]
                todos_clientes.append(f)
        ref_arq.close()
    return todos_clientes #retorna a lista com dados de todos os clientes
       

def procurar_cliente(lista_client, cpf):
        for i in range (len(lista_client)):
            if lista_client[i].cpf == cpf: #verifica se o cpf informado é igual ao cpf da posição i
                return i #se o cpf já existe, então retorna a sua posição na lista
        return -1 #retorna -1 para indicar que o cpf não está cadastrado na lista


def imprimir_todos_clientes(lista_client):
    if len(lista_client) == 0:
        print("Nenhum registro feito ainda!")
    else:
        for i in range(len(lista_client)):
            print()
            print(f"Cliente: {lista_client[i].nome} | CPF: {lista_client[i].cpf} | Telefone fixo: {lista_client[i].tel_fixo} | Celular: {lista_client[i].tel_cel} | Data de nascimento: {lista_client[i].nascimento}")
            print(f"Endereço do cliente: {lista_client[i].endereco}")

def imprimir_cliente(lista_client, cpf_cliente):
    i = 0
    achou = False
    while i < len(lista_client):
        if lista_client[i].cpf == cpf_cliente:
            achou = True
            print()
            print(f"{lista_client[i].nome} tem o endereço {lista_client[i].endereco} e telefones {lista_client[i].tel_fixo}(fixo) e {lista_client[i].tel_cel} (celular). Data de nascimento: {lista_client[i].nascimento}")
        i += 1
    if achou == False:
        print("CPF não encontrado!")


def registrar_cliente(lista_client):
    client = Cliente()
    client.cpf = input("Informe o CPF do cliente a ser cadastrado: ")
    existente = procurar_cliente(lista_client, client.cpf)
    if existente == -1:
        client.nome = input("Informe o nome do cliente a ser cadastrado: ")
        client.endereco = input("Informe o endereço do cliente: ")
        client.tel_fixo = int(input("Informe o telefone fixo (apenas números): "))
        client.tel_cel = int(input("Informe o telefone celular (apenas números): "))
        client.nascimento = input("Informe a data de nascimento do cliente: ")
        lista_client.append(client)
    else:
        print(f"O CPF indica que o cliente já foi cadastrado! (Registro número {existente})")

def gravar_dados_clientes(nome_arquivo,lista_client):
    ref_arq = open(nome_arquivo,'w')
    for i in range(len(lista_client)):
        f = lista_client[i]
        ref_arq.write(f.cpf + ';' + f.nome + ';' + f.endereco + ';' + str(f.tel_fixo) + ';' + str(f.tel_cel) + ';' + f.nascimento + '\n')
    ref_arq.close()
    
def alterar_cliente(lista_client, cpf):
    position = procurar_cliente(lista_client, cpf)
    if position == -1:
        print("Cliente não encontrado!")
    else:
        print("Escolha o dado a ser alterado")
        print("1. Nome")
        print("2. Endereço")
        print("3. Telefone fixo")
        print("4. Telefone celular")
        print("5. Data de nascimento")
        option_client = int(input("Digite uma opção (1-5): "))
        if option_client == 1:
            del lista_client[position].nome
            lista_client[position].nome = input("Digite o nome a ser armazenado: ")
        elif option_client == 2:
            del lista_client[position].endereco
            lista_client[position].endereco = input("Digite o novo endereço: ")
        elif option_client == 3:
            del lista_client[position].tel_fixo
            lista_client[position].tel_fixo = int(input("Digite o novo telefone fixo: "))
        elif option_client == 4:
            del lista_client[position].tel_cel
            lista_client[position].tel_cel = int(input("Digite o novo telefone celular: "))
        elif option_client == 5:
            del lista_client[position].nascimento
            lista_client[position].nascimento = input("Digite a nova data de nascimento: ")
        else:
            print("Opção inválida!")
        print("Deseja realizar mais alguma alteração?")
        print("1. Sim  | 2. Não")
        option1 = int(input("Selecione um (1-2): "))
        if option1 == 1:
            alterar_cliente(lista_client, cpf)
        elif option1 == 2:
            print("Voltando ao menu inicial...")
        else:
            print("Opção inválida! Voltando ao menu inicial...")
        main()
        
def excluir_cliente(lista_client, cpf):
    position = procurar_cliente(lista_client, cpf)
    if position == -1:
        print("Cliente não cadastrado! Impossível excluir")
    else:
        excluir = 0
        while excluir!= 1 and excluir!=2:
            print(f"Tem certeza de que quer excluir o cadastro do CPF {cpf}?")
            print("1. Não | 2. Sim")
            excluir = int(input("Informe a opção (1-2): "))
            if excluir == 1:
                print("Cancelando operação...")
            elif excluir == 2:
                del lista_client[position]
                print("Cliente excluído com sucesso!")
            else:
                print("Opção inválida!")

def menu_clientes(Clientes):
    arq_client = './arq_clientes.txt'    
    Clientes_Lista = ler_arq_clientes(arq_client)
    option_clientes = menu_opcoes_cliente()
    if option_clientes == 1:
        print("Imprimindo todos os clientes cadastrados...")
        imprimir_todos_clientes(Clientes_Lista)
    elif option_clientes == 2:
        if len(Clientes_Lista) < 1:
                print("Nenhum registro feito ainda!")
        else:
            cpf = input("Informe o CPF do cliente a ser consultado: ")
            imprimir_cliente(Clientes_Lista, cpf)
    elif option_clientes == 3:
        registrar_cliente(Clientes_Lista)
        gravar_dados_clientes(arq_client, Clientes_Lista)
    elif option_clientes == 4:
        if len(Clientes_Lista) < 1:
                print("Nenhum registro feito ainda!")
        else:
            cpf = input("Insira o CPF do cliente a ter seus dados alterados: ")
            alterar_cliente(Clientes_Lista, cpf)
            gravar_dados_clientes(arq_client, Clientes_Lista)
    elif option_clientes == 5:
        if len(Clientes_Lista) < 1:
                print("Nenhum registro feito ainda!")
        else:
            cpf = input("Insira o CPF do do cliente a ser excluído: ")
            excluir_cliente(Clientes_Lista, cpf)
            gravar_dados_clientes(arq_client, Clientes_Lista)
    elif option_clientes == 6:
        print("Voltando ao menu anterior...")
        print()
        main()
    else:
        print("Opção inválida!")
        menu_clientes()

def menu_opcoes_cliente():
    print("Escolha uma opção dentro da área de clientes:")
    print("1. Imprimir todos os clientes cadastrados")
    print("2. Imprimir um cliente")
    print("3. Cadastrar cliente")
    print("4. Alterar cadastro de cliente")
    print("5. Excluir cadastro de cliente")
    print("6. Voltar ao menu anterior")
    op_menu_opcoes_cliente = int(input("Selecione a opção (1-6): "))
    return op_menu_opcoes_cliente



####################################################################

class Veiculo:
    codigo = ''
    modelo = ''
    categoria = ''
    ano = -1
    capacidade = -1
    combustivel = ''
    descricao =  ''

def procurar_veiculo(lista, codigo):
    for i in range(len(lista)):
        if lista[i].codigo == codigo: #verifica se o código informado é igual ao código da posição i
            return i #se o código já existe, então retorna a sua posição na lista
    return -1 #retorna -1 para indicar que o código não está cadastrado na lista

def ler_arq_veiculos(nome_arquivo):
    todos_veiculos = []
    if existe_arquivo(nome_arquivo):
        ref_arq = open(nome_arquivo,'r')
        for linha in ref_arq: #itera sobre cada linha do arquivo
            info = linha.strip().split(';')
            if len(info) == 7: #Verifica se há informações suficientes para preencher todos os campos
                f = Veiculo()
                f.codigo = info[0]
                f.modelo = info[1]
                f.categoria = info[2]
                f.ano = int(info[3])
                f.capacidade = int(info[4])
                f.combustivel = info[5]
                f.descricao = info[6]
                todos_veiculos.append(f)
        ref_arq.close()
    return todos_veiculos #retorna a lista com dados de todos os veiculos
    
def gravar_dados_veiculos(nome_arquivo,lista_veic):
    ref_arq = open(nome_arquivo,'w')
    for i in range(len(lista_veic)):
        f = lista_veic[i]
        ref_arq.write(f.codigo + ';' + f.modelo + ';' + f.categoria + ';' + str(f.ano) + ';' + str(f.capacidade) + ';' + f.combustivel + ';' + f.descricao + '\n')
    ref_arq.close()    

def imprimir_todos_veiculos(lista):
    if len(lista) == 0:
        print("Nenhum registro feito ainda!")
    else:
        for i in range(len(lista)):
            print()
            print(f"Carro: {lista[i].modelo} | Combustível: {lista[i].combustivel} | Categoria: {lista[i].categoria} | Capacidade: {lista[i].capacidade} pessoas | Ano: {lista[i].ano} | Descrição: {lista[i].descricao}")

def imprimir_veiculo(lista, codigo_veic):
    i = 0
    achou = False
    while i < len(lista):
        if lista[i].codigo == codigo_veic:
            achou = True
            print()
            print(f"Carro: {lista[i].modelo} | Combustível: {lista[i].combustivel} | Categoria: {lista[i].categoria} | Capacidade: {lista[i].capacidade} pessoas | Ano: {lista[i].ano} | Descrição: {lista[i].descricao}")
        i += 1
    if achou == False:
        print("Veículo não encontrado!")


def registrar_veiculo(lista):
    veic = Veiculo()
    veic.codigo = input("Informe o código do veículo a ser cadastrado: ")
    existente = procurar_veiculo(lista, veic.codigo)
    if existente == -1:
        veic.modelo = input("Informe o modelo do veículo a ser cadastrado: ")
        veic.descricao = input("Informe a descrição do veículo: ")
        veic.categoria = input("Informe a categoria do veículo: ")
        veic.ano = int(input("Informe o ano do veículo: "))
        veic.capacidade = int(input("Informe a capacidade do veículo: "))
        veic.combustivel = input("Informe o combustível utilizado pelo veículo: ")
        lista.append(veic)
    else:
        print(f"O código do veículo indica que ele já foi cadastrado! (Registro número {existente})")

def alterar_veiculo(lista, codigo):
    position = procurar_veiculo(lista, codigo)
    if position == -1:
        print("Veículo não encontrado!")
    else:
        print("Escolha o dado a ser alterado")
        print("1. Modelo")
        print("2. Categoria")
        print("3. Ano")
        print("4. Capacidade")
        print("5. Combustível")
        print("6. Descrição")
        option = int(input("Digite uma opção (1-6): "))
        if option == 1:
            del lista[position].modelo
            lista[position].modelo = input("Digite o modelo a ser armazenado: ")
        elif option == 2:
            del lista[position].categoria
            lista[position].categoria = input("Digite a nova categoria: ")
        elif option == 3:
            del lista[position].ano
            lista[position].ano = int(input("Digite o novo ano: "))
        elif option == 4:
            del lista[position].capacidade
            lista[position].capacidade = int(input("Digite a nova capacidade: "))
        elif option == 5:
            del lista[position].combustivel
            lista[position].combustivel = input("Digite o novo combustível utilizado: ")
        elif option == 6:
            del lista[position].descricao
            lista[position].descricao = input("Digite a nova descrição do veículo: ")
        else:
            print("Opção inválida!")
        print("Deseja realizar mais alguma alteração?")
        print("1. Sim  | 2. Não")
        option1 = int(input("Selecione um (1-2): "))
        if option1 == 1:
            alterar_veiculo(lista, codigo)
        elif option1 == 2:
            print("Voltando ao menu inicial...")
        else:
            print("Opção inválida! Voltando ao menu inicial...")
        main()
        
def excluir_veiculo(lista, codigo):
    position = procurar_veiculo(lista, codigo)
    if position == -1:
        print("Veículo não cadastrado! Impossível excluir")
    else:
        excluir = 0
        while excluir!= 1 and excluir!=2:
            print(f"Tem certeza de que quer excluir o cadastro do veículo {codigo}?")
            print("1. Não | 2. Sim")
            excluir = int(input("Informe a opção (1-2): "))
            if excluir == 1:
                print("Cancelando operação...")
            elif excluir == 2:
                del lista[position]
                print("Veículo excluído com sucesso!")
            else:
                print("Opção inválida!")

def menu_veiculos(lista):
    arq_veic = './arq_veiculos.txt'    
    Veiculos_Lista = ler_arq_veiculos(arq_veic)
    option_veiculo = menu_opcoes_veiculo()
    if option_veiculo == 1:
        print("Imprimindo todos os veículos cadastrados...")
        imprimir_todos_veiculos(Veiculos_Lista)
    elif option_veiculo == 2:
        if len(Veiculos_Lista) < 1:
                print("Nenhum registro feito ainda!")
        else:
            codigo = input("Informe o código do veículo a ser consultado: ")
            imprimir_veiculo(Veiculos_Lista, codigo)
    elif option_veiculo == 3:
        registrar_veiculo(Veiculos_Lista)
        gravar_dados_veiculos(arq_veic, Veiculos_Lista)
    elif option_veiculo == 4:
        if len(Veiculos_Lista) < 1:
                print("Nenhum registro feito ainda!")
        else:
            codigo = input("Insira o código do veículo a ter seus dados alterados: ")
            alterar_veiculo(Veiculos_Lista, codigo)
            gravar_dados_veiculos(arq_veic, Veiculos_Lista)
    elif option_veiculo == 5:
        if len(Veiculos_Lista) < 1:
                print("Nenhum registro feito ainda!")
        else:
            codigo = input("Insira o código do veículo a ser excluído: ")
            excluir_veiculo(Veiculos_Lista, codigo)
            gravar_dados_veiculos(arq_veic, Veiculos_Lista)
    elif option_veiculo == 6:
        print("Voltando ao menu anterior...")
        print()
        main()
    else:
        print("Opção inválida!")
        menu_veiculos()

def menu_opcoes_veiculo():
    print("Escolha uma opção dentro da área de veículos:")
    print("1. Imprimir todos os veículos cadastrados")
    print("2. Imprimir um veículo específico")
    print("3. Cadastrar veículo")
    print("4. Alterar cadastro de veículo")
    print("5. Excluir cadastro de veículo")
    print("6. Voltar ao menu anterior")
    op_menu_opcoes_veiculo = int(input("Selecione a opção (1-6): "))
    return op_menu_opcoes_veiculo

#############################################################################

class Aluguel:
    cpf_locador = ''
    codigo_veic = ''
    data_entrada = ''
    data_saida = ''
    

def verificar_aluguel(lista_aluguel, cpf_loc, codigo_veic, entrada, saida):
    exist = -1
    for i in range(len(lista_aluguel)):
        if lista_aluguel[i].cpf_locador == cpf_loc:
            exist = i
            break
        elif lista_aluguel[i].codigo_veic == codigo_veic: #verifica se o código informado é igual ao código da posição i
            exist = i #se o código já existe, então retorna a sua posição na lista
            break
        elif lista_aluguel[i].data_entrada == entrada:
            exist = i
            break
        elif lista_aluguel[i].data_saida == saida:
            exist = i
    return exist #retorna -1 para indicar que o código não está cadastrado na lista

def ler_arq_alugueis(nome_arquivo):
    todos_alugueis = []
    if existe_arquivo(nome_arquivo):
        ref_arq = open(nome_arquivo,'r')
        for linha in ref_arq: #itera sobre cada linha do arquivo
            info = linha.strip().split(';')
            if len(info) == 4: #Verifica se há informações suficientes para preencher todos os campos
                f = Aluguel()
                f.cpf_locador = info[0]
                f.codigo_veic = info[1]
                f.data_entrada = info[2]
                f.data_saida = info[3]
                todos_alugueis.append(f)
        ref_arq.close()
    print(todos_alugueis)
    return todos_alugueis #retorna a lista com dados de todos os alugueis

def gravar_dados_alugueis(nome_arquivo,lista_alug):
    ref_arq = open(nome_arquivo,'w')
    for i in range(len(lista_alug)):
        f = lista_alug[i]
        ref_arq.write(f.cpf_locador + ';' + f.codigo_veic + ';' + f.data_entrada + ';' + f.data_saida + '\n')
    ref_arq.close()

def imprimir_alugueis(lista_alugel):
    if len(lista_alugel) == 0:
        print("Nenhum registro feito ainda!")
    else:
        for i in range(len(lista_alugel)):
            print()
            print(f"CPF do locador: {lista_alugel[i].cpf_locador} | Código do veículo: {lista_alugel[i].codigo_veic} | Data de entrada: {lista_alugel[i].data_entrada} | Data de saída: {lista_alugel[i].data_saida}")

def imprimir_aluguel_especifico(lista_aluguel):
    print("Selecione o dado para buscar aluguel")
    print("1. CPF do locador")
    print("2. Código do veículo")
    print("3. Data de entrada")
    print("4. Data de saída")
    opt_print = int(input("Escolha um dado para informar (1-4): "))
    alugueis_encontrados_cpf = []
    alugueis_encontrados_codigo = []
    alugueis_encontrados_entrada = []
    alugueis_encontrados_saida = []
    exist = -1
    if opt_print == 1:
        cpf_loc_search = input("Informe o CPF: ")
        for k in range(len(lista_aluguel)):
            if lista_aluguel[k].cpf_locador == cpf_loc_search:
                alugueis_encontrados_cpf.append(k)
        if len(alugueis_encontrados_cpf) > 1:
            print(f"Foram encontrados {len(alugueis_encontrados_cpf)} aluguéis vinculados a este CPF")
            print("Por favor, informe o código do veículo vinculado ao aluguel que procura")
            codigo_veic_search = input("Informe o código: ")
            for j in range(len(alugueis_encontrados_cpf)):
                l = alugueis_encontrados_cpf[j]
                if lista_aluguel[l].codigo_veic == codigo_veic_search:
                    alugueis_encontrados_codigo.append(l)
                    i = l
            if len(alugueis_encontrados_codigo) > 1:
                print(f"Foram encontrados {len(alugueis_encontrados_codigo)} aluguéis vinculados a este CPF e código")
                print("Por favor, informe a data de entrada do aluguel que procura")
                data_entrada_search = input("Informe a data de entrada: ")  
                for a in range(len(alugueis_encontrados_codigo)):
                    i1 = alugueis_encontrados_codigo[a]
                    if lista_aluguel[i1].data_entrada == data_entrada_search:
                        i = i1
                        exist = i
                alugueis_encontrados_codigo = []
                alugueis_encontrados_cpf = []
                        
            else:
                exist = i
                alugueis_encontrados_codigo = []
                alugueis_encontrados_cpf = []
        else:
            exist = alugueis_encontrados_cpf[0]
            alugueis_encontrados_cpf = []

    elif opt_print == 2:
        codigo_veic_search = input("Informe o código: ")
        for k in range(len(lista_aluguel)):
            if lista_aluguel[k].codigo_veic == codigo_veic_search:
                alugueis_encontrados_codigo.append(k)
        if len(alugueis_encontrados_codigo) > 1:
            print(f"Foram encontrados {len(alugueis_encontrados_codigo)} aluguéis vinculados a este código")
            print("Por favor, informe o CPF do locador vinculado ao aluguel que procura")
            cpf_loc_search = input("Informe o CPF: ")
            for j in range(len(alugueis_encontrados_codigo)):
                l = alugueis_encontrados_codigo[j]
                if lista_aluguel[l].cpf_locador == cpf_loc_search:
                    alugueis_encontrados_cpf.append(l)
                    i = l
            if len(alugueis_encontrados_cpf) > 1:
                print(f"Foram encontrados {len(alugueis_encontrados_cpf)} aluguéis vinculados a este CPF e código")
                print("Por favor, informe a data de entrada do aluguel que procura")
                data_entrada_search = input("Informe a data de entrada: ")  
                for a in range(len(alugueis_encontrados_cpf)):
                    i1 = alugueis_encontrados_cpf[a]
                    if lista_aluguel[i1].data_entrada == data_entrada_search:
                        i = i1
                        exist = i
                alugueis_encontrados_codigo = []
                alugueis_encontrados_cpf = []
                        
            else:
                exist = i
                alugueis_encontrados_codigo = []
                alugueis_encontrados_cpf = []
        else:
            exist = alugueis_encontrados_codigo[0]
            alugueis_encontrados_codigo = []
    elif opt_print == 3:
        entrada_search = input("Informe a data de entrada: ")
        for k in range(len(lista_aluguel)):
            if lista_aluguel[k].data_entrada == entrada_search:
                alugueis_encontrados_entrada.append(k)
        if len(alugueis_encontrados_entrada) > 1:
            print(f"Foram encontrados {len(alugueis_encontrados_entrada)} aluguéis vinculados a esta entrada")
            print("Por favor, informe o CPF do locador vinculado ao aluguel que procura")
            cpf_loc_search = input("Informe o CPF: ")
            for j in range(len(alugueis_encontrados_entrada)):
                l = alugueis_encontrados_entrada[j]
                if lista_aluguel[l].cpf_locador == cpf_loc_search:
                    alugueis_encontrados_cpf.append(l)
                    i = l
            if len(alugueis_encontrados_cpf) > 1:
                print(f"Foram encontrados {len(alugueis_encontrados_cpf)} aluguéis vinculados a este CPF e entrada")
                print("Por favor, informe o código vinculado o aluguel que procura")
                codigo_veic_search = input("Informe o código: ")  
                for a in range(len(alugueis_encontrados_cpf)):
                    i1 = alugueis_encontrados_cpf[a]
                    if lista_aluguel[i1].codigo_veic == codigo_veic_search:
                        i = i1
                        exist = i
                alugueis_encontrados_codigo = []
                alugueis_encontrados_cpf = []
                alugueis_encontrados_entrada = []
                
                        
            else:
                exist = i
                alugueis_encontrados_cpf = []
                alugueis_encontrados_entrada = []
        else:
            exist = alugueis_encontrados_entrada[0]
            alugueis_encontrados_entrada = []

    elif opt_print == 4:
        saida_search = input("Informe a data de saída: ")
        for k in range(len(lista_aluguel)):
            if lista_aluguel[k].data_saida == saida_search:
                alugueis_encontrados_saida.append(k)
        if len(alugueis_encontrados_saida) > 1:
            print(f"Foram encontrados {len(alugueis_encontrados_saida)} aluguéis vinculados a esta saída")
            print("Por favor, informe o CPF do locador vinculado ao aluguel que procura")
            cpf_loc_search = input("Informe o CPF: ")
            for j in range(len(alugueis_encontrados_saida)):
                l = alugueis_encontrados_entrada[j]
                if lista_aluguel[l].cpf_locador == cpf_loc_search:
                    alugueis_encontrados_cpf.append(l)
                    i = l
            if len(alugueis_encontrados_cpf) > 1:
                print(f"Foram encontrados {len(alugueis_encontrados_cpf)} aluguéis vinculados a este CPF e saida")
                print("Por favor, informe o código vinculado o aluguel que procura")
                codigo_veic_search = input("Informe o código: ")  
                for a in range(len(alugueis_encontrados_cpf)):
                    i1 = alugueis_encontrados_cpf[a]
                    if lista_aluguel[i1].codigo_veic == codigo_veic_search:
                        i = i1
                        exist = i
                alugueis_encontrados_codigo = []
                alugueis_encontrados_cpf = []
                alugueis_encontrados_saida = []
                
                        
            else:
                exist = i
                alugueis_encontrados_cpf = []
                alugueis_encontrados_saida = []
        else:
            exist = alugueis_encontrados_saida[0]
            alugueis_encontrados_saida = []
    if exist == -1:
        print("Aluguel não encontrado")
    else:
        print(f"CPF do locador: {lista_aluguel[exist].cpf_locador} | Código do veículo: {lista_aluguel[exist].codigo_veic} | Data de entrada: {lista_aluguel[exist].data_entrada} | Data de saída: {lista_aluguel[exist].data_saida}")



def registrar_aluguel(lista_aluguel, cpf_locador, codigo_veic, data_entrada, data_saida):
    alug = Aluguel()
    alug.cpf_locador, alug.codigo_veic, alug.data_entrada, alug.data_saida = cpf_locador, codigo_veic, data_entrada, data_saida
    lista_aluguel.append(alug)
    

def alterar_aluguel(lista_aluguel, cpf_locador, codigo_veic, data_entrada, data_saida, Clientes, Veiculos):
    position = verificar_aluguel(lista_aluguel, cpf_locador, codigo_veic, data_entrada, data_saida)
    if position == -1:
        print("Registro não encontrado!")
    else:
        print("Escolha o dado a ser alterado")
        print("1. CPF do locador")
        print("2. Código do veículo")
        print("3. Data de entrada")
        print("4. Data de saída")
        option = int(input("Digite uma opção (1-5): "))
        if option == 1:
            del lista_aluguel[position].cpf_locador
            cpf_locador = input("Digite o CPF novo: ")
            for i in range(len(Clientes)):
                if Clientes[i].cpf == cpf_locador:
                    lista_aluguel[position].cpf_locador
                    break 
                else:
                    print("CPF inválido!")
                    print()
                    main()
        elif option == 2:
            del lista_aluguel[position].codigo_veic
            codigo_veic = input("Digite o código novo: ")
            for i in range(len(Veiculos)):
                if Veiculos[i].codigo == codigo_veic:
                    lista_aluguel[position].codigo_veic
                    break 
                else:
                    print("Código inválido!")
                    print()
                    main()
        elif option == 3:
            del lista_aluguel[position].data_entrada
            lista_aluguel[position-1].data_entrada = input("Digite a nova data de entrada: ")
        elif option == 4:
            del lista_aluguel[position-1].data_saida
            lista_aluguel[position].data_saida = input("Digite a nova data de saída: ")
        else:
            print("Opção inválida!")
        print("Deseja realizar mais alguma alteração?")
        print("1. Sim  | 2. Não")
        option1 = int(input("Selecione um (1-2): "))
        if option1 == 1:
            alterar_aluguel(lista_aluguel, cpf_locador, codigo_veic, data_entrada, data_saida)
        elif option1 == 2:
            print("Voltando ao menu inicial...")
        else:
            print("Opção inválida! Voltando ao menu inicial...")
        main()
        
def excluir_aluguel(lista_aluguel, cpf_locador, codigo_veic, data_entrada, data_saida):
    position = verificar_aluguel(lista_aluguel, cpf_locador, codigo_veic, data_entrada, data_saida)
    if position == -1:
        print("Aluguel não registrado! Impossível excluir")
    else:
        excluir = 0
        while excluir!= 1 and excluir!=2:
            print(f"Tem certeza de que quer excluir este aluguel?")
            print("1. Não | 2. Sim")
            excluir = int(input("Informe a opção (1-2): "))
            if excluir == 1:
                print("Cancelando operação...")
            elif excluir == 2:
                del lista_aluguel[position]
                print("Registro excluído com sucesso!")
            else:
                print("Opção inválida!")

def menu_alugueis(lista_alug):
    arq_alug = './arq_alugueis.txt'    
    Aluguel_Lista = ler_arq_alugueis(arq_alug)
    option_alug = menu_opcoes_aluguel()
    if option_alug == 1:
        if len(Aluguel_Lista) < 1:
                print("Nenhum registro feito ainda!")
        else:
            print("Imprimindo todos os aluguéis registrados...")
            imprimir_alugueis(Aluguel_Lista)
    elif option_alug == 2:
        if len(Aluguel_Lista) < 1:
                print("Nenhum registro feito ainda!")
        else:
            imprimir_aluguel_especifico(Aluguel_Lista)
    elif option_alug == 3 or option_alug == 4 or option_alug == 5:
        cpf_loc = input("Informe o CPF do locador: ")
        achou_cpf = 0
        i = 0
        arq_client2 = './arq_clientes.txt'    
        Clientes_Lista2 = ler_arq_clientes(arq_client2)
        while i < len(Clientes_Lista2):
            if cpf_loc != Clientes_Lista2[i].cpf :
                    achou_cpf += 1
            i += 1
        if achou_cpf != (len(Clientes_Lista2)-1) :
            print("CPF inválido!")
            print()
            main()
            
        codigo_veic = input("Informe o código do veículo locado: ")
        achou_code = 0
        i = 0
        arq_veic2 = './arq_veiculos.txt'    
        Veiculos_Lista2 = ler_arq_veiculos(arq_veic2)
        while i < len(Veiculos_Lista2):
            if codigo_veic != Veiculos_Lista2[i].codigo :
                    achou_code += 1
            i += 1
        if achou_code != (len(Veiculos_Lista2)-1) :
            print("Código inválido!")
            print()
            main()
        data_entrada = input("Informe a data de entrada: ")
        data_saida = input("Informe a data de saída: ")
        if option_alug == 3:
            registrar_aluguel(Aluguel_Lista, cpf_loc, codigo_veic, data_entrada, data_saida)
            gravar_dados_alugueis(arq_alug, Aluguel_Lista)
        elif option_alug == 4:
            if len(Aluguel_Lista) < 1:
                print("Nenhum registro feito ainda!")
            else:
                alterar_aluguel(Aluguel_Lista, cpf_loc, codigo_veic, data_entrada, data_saida, Clientes_Lista2, Veiculos_Lista2)
                gravar_dados_alugueis(arq_alug, Aluguel_Lista)
        elif option_alug == 5:
            if len(Aluguel_Lista) < 1:
                print("Nenhum registro feito ainda!")
            else:
                excluir_aluguel(Aluguel_Lista, cpf_loc, codigo_veic, data_entrada, data_saida)
                gravar_dados_alugueis(arq_alug, Aluguel_Lista)
    elif option_alug == 6:
        print("Voltando ao menu anterior...")
        print()
        main()
    else:
        print("Opção inválida!")
        menu_alugueis()

def menu_opcoes_aluguel():
    print("Escolha uma opção dentro da área de veículos:")
    print("1. Imprimir todos os alugueis registrados")
    print("2. Imprimir um aluguel específico")
    print("3. Registrar aluguel")
    print("4. Alterar registro de aluguel")
    print("5. Excluir registro de aluguel")
    print("6. Voltar ao menu anterior")
    op_menu_opcoes_aluguel = int(input("Selecione a opção (1-6): "))
    return op_menu_opcoes_aluguel

###############################################################################
def menu_opcoes_relatorios():
    print("Escolha uma opção dentro da área de veículos:")
    print("1. Imprimir todas as reservas de um cliente ")
    print("2. Imprimir todas as reservas de um veículo")
    print("3. Imprimir dados de reservas entre determinadas datas")
    print("4. Voltar ao menu anterior")
    op_menu_opcoes_relatorio = int(input("Selecione a opção (1-3): "))
    return op_menu_opcoes_relatorio
    menu_relatorios()
    
    
def relatorio_reservas_cliente(cpf):
    contador = 0
    with open('./arq_alugueis.txt', 'r') as arquivo2:
        alugueis = arquivo2.readlines()
        for aluguel in alugueis:
            dados = aluguel.strip().split(';')
            if dados[0] == cpf:
                contador += 1 
                print(f"CPF do Locador: {dados[0]} / Código do Veículo: {dados[1]} / Data de Entrada: {dados[2]} / Data de saída: {dados[3]}")
                print()
        if contador == 0:     
            print("Nenhum aluguel registrado neste CPF")
            
def relatorio_reservas_veiculo(codigo):
    contador = 0
    with open('./arq_alugueis.txt', 'r') as arquivo2:
        alugueis = arquivo2.readlines()
        for aluguel in alugueis:
            dados = aluguel.strip().split(';')
            if dados[1] == codigo:
                contador += 1
                print(f"Código do Veículo: {dados[1]} / CPF do Locador: {dados[0]} / Data de Entrada: {dados[2]} / Data de saída: {dados[3]}")
                print()
        if contador == 0:     
            print("Nenhum aluguel registrado neste Código")
        
        
def menu_relatorios():
    option_relat = menu_opcoes_relatorios()
    if option_relat == 1:
        cpf_loc_relat = input("Digite o CPF do cliente que deseja consultar as reservas: ")
        print()
        print("Imprimindo todas as reservas registradas...")
        relatorio_reservas_cliente(cpf_loc_relat)
    elif option_relat == 2:
        codigo_loc_relat = input("Digite o Código do cliente que deseja consultar as reservas: ")
        print()
        print("Imprimindo todas as reservas registradas...")
        relatorio_reservas_veiculo(codigo_loc_relat)
    elif option_relat == 3:
        data_entrada_relat = input("Digite a Data de Entrada para consultar as reservas: ")
        data_saida_relat = input("Digite a Data de Saída para consultar as reservas: ")
        print()
        relatorio_reservas_periodo(data_entrada_relat, data_saida_relat)
    elif option_relat == 4:
        print("Voltando ao menu anterior...")
        print()
        main()
    else:
        print("Opção inválida!")
        menu_relatorios()    

def relatorio_reservas_periodo(data_inicio, data_fim):
    with open('./arq_alugueis.txt', 'r') as arquivo_alugueis:
        alugueis = arquivo_alugueis.readlines()
    with open('./arq_clientes.txt', 'r') as arquivo_clientes:
        clientes = arquivo_clientes.readlines()

    for aluguel in alugueis:
        dados_aluguel = aluguel.strip().split(';')
        cpf_cliente = dados_aluguel[0]

        for cliente in clientes:
            dados_cliente = cliente.strip().split(';')
            if dados_cliente[0] == cpf_cliente:
                nome_cliente = dados_cliente[1]
                break

        data_entrada = dados_aluguel[2]
        data_saida = dados_aluguel[3]
        if data_inicio <= data_entrada <= data_fim and data_inicio <= data_saida <= data_fim:
            print(f"Nome do Cliente: {dados_cliente[1]} / Data de Entrada: {dados_aluguel[2]} / Data de saída: {dados_aluguel[3]} / CPF do Locador: {dados_aluguel[0]} / Código do Veículo: {dados_aluguel[1]}")
            print()

###############################################################################
def menu_opcoes():
    print("Escolha qual área acessar:")
    print("1. Submenu de clientes")
    print("2. Submenu de veículos")
    print("3. Submenu de aluguéis")
    print("4. Submenu de relatórios")
    print("5. Sair")
    opcao = int(input("Selecionar (1-5): "))
    return opcao

def main():
    op = menu_opcoes()
    if op == 1 :
            print()
            menu_clientes(Cliente)
            print()
            main()
    elif op == 2:
            print()
            menu_veiculos(Veiculo)
            print()
            main()
    elif op == 3:
            print()
            menu_alugueis(Aluguel)
            print()
            main()
    elif op == 4:
            print()
            menu_relatorios()
            print()
            main()        
    elif op == 5:
        print()
        print("Saindo...")
        exit
    else:
        print("Opção inválida")
        print()
        main()
main()
