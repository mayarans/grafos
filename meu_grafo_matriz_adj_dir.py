from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        vertice = self.get_vertice(V)
        if self.existe_vertice(vertice):
            arestas_incidentes = list()

            for linha in self.arestas[self.indice_do_vertice(vertice)]:
                for aresta in linha:
                    arestas_incidentes.append(aresta)

            return set(arestas_incidentes)
        else:
            raise VerticeInvalidoError("O vértice não existe no grafo")

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        matriz_copia = deepcopy(self.arestas)

        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if matriz_copia[j][i]:
                    matriz_copia[j][i] = 1
                    for k in range(len(self.vertices)):
                        matriz_copia[j][k] = 1 if matriz_copia[j][k] or matriz_copia[i][k] else 0
                else:
                    matriz_copia[j][i] = 0

        return matriz_copia

    def dijkstra(self, A, B):
        '''
        Provê a distância entre os vértices A e B usando o algoritmo de Dijkstra
        :param A: O vértice de origem
        :param B: O vértice de destino
        :return: A distância entre os vértices A e B e o caminho entre eles
        '''
        if not self.existe_vertice(self.get_vertice(A)) or not self.existe_vertice(self.get_vertice(B)):
            raise VerticeInvalidoError('O vértice não existe no grafo')

        dict_custos = dict()
        dict_predecessor = dict()

        for vertice in self.vertices:
            dict_custos[vertice.rotulo] = float('inf')
            dict_predecessor[vertice.rotulo] = ['0', 0]

        def dijkstra_auxiliar(v_atual):
            if v_atual == B:
                return dijkstra_auxiliar(dict_predecessor[B][0])

            arestas_incidentes = sorted(self.arestas_sobre_vertice(v_atual), key=lambda x: self.get_aresta(x).peso)
            for aresta in arestas_incidentes:
                aresta = self.get_aresta(aresta)
                if aresta.v2.rotulo == v_atual:
                    continue
                if (aresta.peso + dict_custos[v_atual]) < dict_custos[aresta.v2.rotulo]:
                    dict_custos[aresta.v2.rotulo] = aresta.peso + dict_custos[v_atual]
                    dict_predecessor[aresta.v2.rotulo][0] = v_atual
                    dict_predecessor[aresta.v2.rotulo][1] = aresta.rotulo
                    return dijkstra_auxiliar(aresta.v2.rotulo)

            if v_atual != A:
                return dijkstra_auxiliar(dict_predecessor[v_atual][0])

            return dict_custos[B]

        dict_custos[A] = 0
        valor_menor_caminho = dijkstra_auxiliar(A)

        menor_caminho = list()
        menor_caminho.append(B)
        vertice = B
        while dict_predecessor[vertice][0] != '0':
            menor_caminho.append(dict_predecessor[vertice][1])
            menor_caminho.append(dict_predecessor[vertice][0])

            vertice = dict_predecessor[vertice][0]

        if dict_predecessor[B][0] == '0':
            raise KeyError('Não existe caminho entre os vértices')

        return menor_caminho[::-1], valor_menor_caminho

    def bellman_ford(self, A, B):
        '''
        Provê a distância entre os vértices A e B usando o algoritmo de Bellman-Ford
        :param A: O vértice de origem
        :param B: O vértice de destino
        :return: A distância entre os vértices A e B e o caminho entre eles
        '''

        dict_custos = dict()
        dict_predecessor = dict()
        arestas_visitadas = dict()

        for vertice in self.vertices:
            dict_custos[vertice.rotulo] = float('inf')
            dict_predecessor[vertice.rotulo] = ['', '']
            arestas_visitadas[vertice.rotulo] = 0
        dict_custos[A] = 0

        def bellman_ford_auxiliar(v_atual, houve_mudanca):
            arestas_incidentes = sorted(self.arestas_sobre_vertice(v_atual), key=lambda x: self.get_aresta(x).peso)

            if arestas_visitadas[v_atual] >= len(self.vertices):
                raise ValueError('Existe ciclo negativo no grafo')

            for aresta in arestas_incidentes:
                aresta = self.get_aresta(aresta)
                if aresta.v2.rotulo == v_atual:
                    continue
                if (aresta.peso + dict_custos[v_atual]) < dict_custos[aresta.v2.rotulo]:
                    arestas_visitadas[v_atual] += 1
                    dict_custos[aresta.v2.rotulo] = aresta.peso + dict_custos[v_atual]
                    dict_predecessor[aresta.v2.rotulo][0] = v_atual
                    dict_predecessor[aresta.v2.rotulo][1] = aresta.rotulo
                    houve_mudanca = True
                    return bellman_ford_auxiliar(aresta.v2.rotulo, houve_mudanca)

            if v_atual != A:
                return bellman_ford_auxiliar(dict_predecessor[v_atual][0], houve_mudanca)

            return dict_custos[B], houve_mudanca

        for n in range(len(self.vertices)):
            houve_mudanca = False
            try:
                valor_menor_caminho, houve_mudanca = bellman_ford_auxiliar(A, houve_mudanca)
            except ValueError:
                return False
            if not houve_mudanca:
                break

        menor_caminho = list()
        menor_caminho.append(B)
        vertice = B
        while dict_predecessor[vertice][0] != '':
            menor_caminho.append(dict_predecessor[vertice][1])
            menor_caminho.append(dict_predecessor[vertice][0])

            vertice = dict_predecessor[vertice][0]

        return menor_caminho[::-1], valor_menor_caminho

