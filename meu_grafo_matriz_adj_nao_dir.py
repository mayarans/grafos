from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def __vertices_incidentes_sem_laco(self, V):
        '''
        Função auxiliar que retorna uma lista com os vertices que incidem sobre
        um determinado vértice V passado como parâmetro
        '''
        arestas_incidentes = self.arestas_sobre_vertice(V)
        lista_vertices_incidentes = list()

        for aresta in arestas_incidentes:
            aresta = self.get_aresta(aresta)
            if aresta.v1.rotulo != V:
                lista_vertices_incidentes.append(aresta.v1.rotulo)
            elif aresta.v2.rotulo != V:
                lista_vertices_incidentes.append(aresta.v2.rotulo)

        return lista_vertices_incidentes

    def __vertices_incidentes_com_laco(self, V):
        '''
        Função auxiliar que retorna uma lista com os vertices que incidem sobre
        um determinado vértice V passado como parâmetro
        '''
        arestas_incidentes = self.arestas_sobre_vertice(V)
        lista_vertices_incidentes = list()

        for aresta in arestas_incidentes:
            aresta = self.get_aresta(aresta)
            if aresta.v1.rotulo != V:
                lista_vertices_incidentes.append(aresta.v1.rotulo)
            else:
                lista_vertices_incidentes.append(aresta.v2.rotulo)

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
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
        '''
        lista_vertices = self.__rotulos_vertices()

        conjunto = []
        for vertice in self.vertices:
            for i in range(len(lista_vertices)):
                lista_vertices_incidentes = self.__vertices_incidentes_sem_laco(vertice.rotulo)
                if lista_vertices[i] not in lista_vertices_incidentes and lista_vertices[
                    i] != vertice.rotulo and f'{vertice.rotulo}-{lista_vertices[i]}'[::-1] not in conjunto:
                    conjunto.append(f'{vertice.rotulo}-{lista_vertices[i]}')

        return set(conjunto)

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.vertices)):
            if self.arestas[i][i]:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_vertice(self.get_vertice(V)):
            raise VerticeInvalidoError('O vértice não existe no grafo')

        arestas_incidentes = self.arestas_sobre_vertice(V)
        grau = 0

        for aresta in arestas_incidentes:
            aresta = self.get_aresta(aresta)
            if aresta.v1.rotulo == V and aresta.v2.rotulo == V:
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
            vertices_incidentes = self.__vertices_incidentes_com_laco(vertice.rotulo)
            for vertice_oposto in vertices_incidentes:
                if vertices_incidentes.count(vertice_oposto) > 1:
                    return True

        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
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
        vertices = self.__rotulos_vertices()

        for vertice in vertices:
            vertices_incidentes = self.__vertices_incidentes_com_laco(vertice)
            if len(vertices_incidentes) < len(vertices) - 1:
                return False
            for vertice_oposto in vertices_incidentes:
                if vertice_oposto == vertice or vertices_incidentes.count(vertice_oposto) > 2:
                    return False

        return True
