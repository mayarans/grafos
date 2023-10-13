from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def __vertices_incidentes(self, V):
        '''
        Função auxiliar que retorna uma lista com os vertices que incidem sobre
        um determinado vértice V passado como parâmetro
        '''
        arestas_incidentes = self.arestas_sobre_vertice(V)
        lista_vertices_incidentes = list()
        for aresta in arestas_incidentes:
            if self.arestas[aresta].v1.rotulo != V:
                lista_vertices_incidentes.append(self.arestas[aresta].v1.rotulo)
            elif self.arestas[aresta].v2.rotulo != V:
                lista_vertices_incidentes.append(self.arestas[aresta].v2.rotulo)

        return lista_vertices_incidentes


    def __rotulos_vertices(self):
        '''
        Função auxiliar que retorna uma lista com os rótulos
        dos vértices do grafo
        '''
        lista_vertices = []
        for vertice in self.vertices:
            lista_vertices.append(vertice.rotulo)

        return lista_vertices


    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        lista_vertices = self.__rotulos_vertices()

        conjunto = []
        for vertice in self.vertices:
            for i in range(len(lista_vertices)):
                lista_vertices_incidentes = self.__vertices_incidentes(vertice.rotulo)
                if lista_vertices[i] not in lista_vertices_incidentes and lista_vertices[i] != vertice.rotulo and f'{vertice.rotulo}-{lista_vertices[i]}'[::-1] not in conjunto:
                    conjunto.append(f'{vertice.rotulo}-{lista_vertices[i]}')

        return set(conjunto)


    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for aresta in self.arestas:
            if self.arestas[aresta].v1 == self.arestas[aresta].v2:
                return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        arestas_incidentes = self.arestas_sobre_vertice(V)
        grau = 0
        if type(arestas_incidentes) is not set:
            return grau

        for aresta in arestas_incidentes:
            if self.arestas[aresta].v1 == self.arestas[aresta].v2:
                grau += 2
            else:
                grau += 1

        return grau


    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for vertice in self.vertices:
            arestas_incidentes = list(self.arestas_sobre_vertice(vertice.rotulo))
            if (len(arestas_incidentes) < 2):
                continue
            else:
                listaVerticesIncidentes = []
                verticeIncidente = ""
                for aresta in arestas_incidentes:
                    if self.arestas[aresta].v1.rotulo != vertice.rotulo:
                        verticeIncidente = self.arestas[aresta].v1.rotulo
                    elif self.arestas[aresta].v2.rotulo != vertice.rotulo:
                        verticeIncidente = self.arestas[aresta].v2.rotulo

                    if verticeIncidente in listaVerticesIncidentes:
                        return True
                    else:
                        listaVerticesIncidentes.append(verticeIncidente)
        return False


    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        vertice = self.get_vertice(V)
        if self.existe_vertice(vertice):
            arestas_incidentes = list()
            for aresta in self.arestas.values():
                if aresta.v1.rotulo == V or aresta.v2.rotulo == V:
                    arestas_incidentes.append(aresta.rotulo)

            return set(arestas_incidentes)
        else:
            raise VerticeInvalidoError("O vértice não existe no grafo")


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if len(self.vertices_nao_adjacentes()) > 0 or self.ha_laco() or self.ha_paralelas():
            return False
        return True


    def __destinos_de_um_vertice(self, V):
        '''
        Função auxiliar que retorna um dicionário com os destinos de um vértice
        passado como parâmetro
        '''
        destinos = dict()
        arestas_incidentes = sorted(self.arestas_sobre_vertice(V))
        for a in arestas_incidentes:
            if self.arestas[a].v1.rotulo != V:
                destinos[a] = self.arestas[a].v1.rotulo
            elif self.arestas[a].v2.rotulo != V:
                destinos[a] = self.arestas[a].v2.rotulo

        return destinos

    def dfs(self, V):
        '''
        Executa a busca em profundidade (DFS) a partir do vértice V.
        :param V: O rótulo do vértice a ser iniciada a busca.
        :return: Uma árvore DFS com os seguintes itens
            - todos os vértices do grafo original
            - arestas que fazem parte da árvore DFS
            A chave é o vértice de origem e o valor é o vértice de destino.
        '''
        arvore_dfs = MeuGrafo()
        arvore_dfs.adiciona_vertice(V)

        def dfs_auxiliar(V, arvore_dfs):
            destinos_ordenados = self.__destinos_de_um_vertice(V)
            for aresta, vertice_oposto in destinos_ordenados.items():
                if not arvore_dfs.existe_rotulo_vertice(vertice_oposto):
                    arvore_dfs.adiciona_vertice(vertice_oposto)
                    arvore_dfs.adiciona_aresta(aresta, V, vertice_oposto)
                    dfs_auxiliar(vertice_oposto, arvore_dfs)
            return arvore_dfs

        return dfs_auxiliar(V, arvore_dfs)

    def bfs(self, V):
        '''
        Executa a busca em largura (BFS) a partir do vértice V.
        :param V: O rótulo do vértice a ser iniciada a busca.
        :return: Um dicionário com os seguintes itens:
            - todos os vértices do grafo original
            - arestas que fazem parte da árvore BFS
        '''

        arvore_bfs = MeuGrafo()
        arvore_bfs.adiciona_vertice(V)

        def bfs_auxiliar(V, arvore_bfs):
            destinos_ordenados = self.__destinos_de_um_vertice(V)
            vertices_em_camada = []
            for aresta, vertice_oposto in destinos_ordenados.items():
                if not arvore_bfs.existe_rotulo_vertice(vertice_oposto):
                    vertices_em_camada.append(vertice_oposto)
                    arvore_bfs.adiciona_vertice(vertice_oposto)
                    arvore_bfs.adiciona_aresta(aresta, V, vertice_oposto)
            for vertice_oposto in vertices_em_camada:
                bfs_auxiliar(vertice_oposto, arvore_bfs)
            return arvore_bfs

        return bfs_auxiliar(V, arvore_bfs)

    def conexo(self):
        vertices_do_grafo = self.__rotulos_vertices()
        arvore_dfs = self.dfs(vertices_do_grafo[0])

        vertices_da_arvore = arvore_dfs.__rotulos_vertices()

        for vertice in vertices_do_grafo:
            if vertice not in vertices_da_arvore:
                return False

        return True

    def ha_ciclo(self):
        vertices_do_grafo = self.__rotulos_vertices()

        def ciclo_auxiliar(V, lista_ciclo):
            destinos = dict()
            arestas_incidentes = sorted(self.arestas_sobre_vertice(V))

            if V not in vertices_visitados:
                vertices_visitados[V] = list()

            for a in arestas_incidentes:
                if self.arestas[a].v1.rotulo == V and self.arestas[a].v2.rotulo == V:
                    destinos[a] = self.arestas[a].v1.rotulo
                elif self.arestas[a].v1.rotulo != V:
                    destinos[a] = self.arestas[a].v1.rotulo
                elif self.arestas[a].v2.rotulo != V:
                    destinos[a] = self.arestas[a].v2.rotulo

            for aresta, vertice_oposto in destinos.items():
                if aresta not in lista_ciclo and vertice_oposto == vertice_pai:
                    lista_ciclo.append(aresta)
                    lista_ciclo.append(vertice_oposto)
                    return lista_ciclo
                elif aresta not in lista_ciclo and vertice_oposto not in lista_ciclo and vertice_oposto not in vertices_visitados[V]:
                    vertices_visitados[V].append(vertice_oposto)
                    lista_ciclo.append(aresta)
                    lista_ciclo.append(vertice_oposto)
                    return ciclo_auxiliar(vertice_oposto, lista_ciclo)
                elif aresta == list(destinos.keys())[-1]:
                    vertices_visitados[V] = list()
                    lista_ciclo.pop()
                    if not lista_ciclo:
                        return False
                    lista_ciclo.pop()
                    return ciclo_auxiliar(lista_ciclo[-1], lista_ciclo)
            return False

        for v in vertices_do_grafo:
            vertice_pai = v
            vertices_visitados = dict()

            lista_ciclo = list()
            lista_ciclo.append(vertice_pai)

            resultado = ciclo_auxiliar(vertice_pai, lista_ciclo)

            if resultado:
                return resultado

        return False

    def caminho(self, n):
        vertices_do_grafo = self.__rotulos_vertices()
        if n == 0:
            return False
        def caminho_auxiliar(V, lista_caminho, tamanho_atual):
            if tamanho_atual == n:
                return lista_caminho

            destinos_ordenados = self.__destinos_de_um_vertice(V)

            if V not in vertices_visitados:
                vertices_visitados[V] = list()


            for aresta, vertice_oposto in destinos_ordenados.items():
                if aresta not in lista_caminho and vertice_oposto not in lista_caminho and vertice_oposto not in vertices_visitados[V]:
                    vertices_visitados[V].append(vertice_oposto)
                    lista_caminho.append(aresta)
                    lista_caminho.append(vertice_oposto)
                    tamanho_atual += 1
                    return caminho_auxiliar(vertice_oposto, lista_caminho, tamanho_atual)
                elif (aresta not in lista_caminho) and (vertice_pai == vertice_oposto) and (tamanho_atual + 1 == n):
                    lista_caminho.append(aresta)
                    lista_caminho.append(vertice_oposto)
                    tamanho_atual += 1
                    return lista_caminho
                elif aresta == list(destinos_ordenados.keys())[-1]:
                    vertices_visitados[V] = list()
                    lista_caminho.pop()
                    if not lista_caminho:

                        return False
                    lista_caminho.pop()
                    tamanho_atual -= 1
                    return caminho_auxiliar(lista_caminho[-1], lista_caminho, tamanho_atual)

        for v in vertices_do_grafo:
            tamanho_atual = 0
            vertice_pai = v
            vertices_visitados = dict()

            lista_caminho = list()
            lista_caminho.append(vertice_pai)
            resultado = caminho_auxiliar(v, lista_caminho, tamanho_atual)

            if resultado:
                return resultado

        return False
