grafo = {'AC':{'RO':59},
         'RO':{'MT':44,'AC':22},
         'MT':{'RO':104,'GO':90,'MS':53},
         'GO':{'MT':76,'TO':87,'DF':150},
         'MS':{'MT':106,'PR':44},
         'TO':{'GO':23,'PA':82},
         'DF':{'GO':305,'MG':106,'AM':309,'RJ':240},
         'PR':{'MS':122,'RS':84,'SP':130},
         'RS':{'PR':84,'SC':109},
         'SC':{'RS':154,'SP':63},
         'SP':{'SC':111,'PR':122,'RJ':241,'MG':71,'CE':258},
         'RJ':{'SP':191,'DF':86,'ES':60},
         'ES':{'RJ':30,'BA':73},
         'BA':{'ES':30,'SE':31},
         'SE':{'BA':10,'AL':8},
         'AL':{'SE':7,'PE':13},
         'AM':{'DF':80,'RR':126,'PA':225},
         'RR':{'AM':48},
         'MG':{'DF':58,'SP':25,'CE':35},
         'CE':{'MA':118,'SP':72,'RN':120,'PE':202},
         'PE':{'AL':32,'PI':141,'PB-CGE':54,'CE':111},
         'PA':{'MA':30,'AP':90,'AM':170,'TO':314,'PI':24},
         'MA':{'PA':69,'CE':46},
         'AP':{'PA':20},
         'PI':{'PA':14,'PE':34},
         'RN':{'CE':34,'PB_JPA':15},
         'PB_JPA':{'RN':27,'PB-CGE':8},
         'PB-CGE':{'PE':17,'PB_JPA':11}}

def dijkstra(grafo,inicio,fim):
    menor_caminho = {}
    antecessor = {}
    n_visitados = grafo
    infinito = 999999
    caminho = []
    for node in n_visitados:
        menor_caminho[node] = infinito
    menor_caminho[inicio]=0

    while n_visitados:
        minNode = None
        for no in n_visitados:
            if minNode is None:
                minNode = no
            elif menor_caminho[no] < menor_caminho[minNode]:
                minNode = no
        for childNode, weight in grafo[minNode].items():
            if weight + menor_caminho[minNode] < menor_caminho[childNode]:
                menor_caminho[childNode] = weight + menor_caminho[minNode]
                antecessor[childNode] = minNode
        n_visitados.pop(minNode)

    no_atual = fim
    while no_atual != inicio:
        try:
            caminho.insert(0,no_atual)
            no_atual = antecessor[no_atual]
        except KeyError:
            print('erro no caminho')
            break
    caminho.insert(0,inicio)
    if menor_caminho[fim] != infinito:
        print('distancia do menor caminho é '+str(menor_caminho[fim]))
        print('o caminho é '+ str(caminho))


dijkstra(grafo,'AC','PE')