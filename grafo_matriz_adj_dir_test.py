import unittest
from meu_grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo()
        self.g_p2.adiciona_vertice("J")
        self.g_p2.adiciona_vertice("C")
        self.g_p2.adiciona_vertice("E")
        self.g_p2.adiciona_vertice("P")
        self.g_p2.adiciona_vertice("M")
        self.g_p2.adiciona_vertice("T")
        self.g_p2.adiciona_vertice("Z")
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'C', 'E')
        self.g_p3.adiciona_aresta('a3', 'C', 'E')
        self.g_p3.adiciona_aresta('a4', 'P', 'C')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'J', 'C')
        self.g_p4.adiciona_aresta('a2', 'J', 'E')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'P', 'C')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        # Grafo com ciclos e laços
        self.g_e = MeuGrafo()
        self.g_e.adiciona_vertice("A")
        self.g_e.adiciona_vertice("B")
        self.g_e.adiciona_vertice("C")
        self.g_e.adiciona_vertice("D")
        self.g_e.adiciona_vertice("E")
        self.g_e.adiciona_aresta('1', 'A', 'B')
        self.g_e.adiciona_aresta('2', 'A', 'C')
        self.g_e.adiciona_aresta('3', 'C', 'A')
        self.g_e.adiciona_aresta('4', 'C', 'B')
        self.g_e.adiciona_aresta('10', 'C', 'B')
        self.g_e.adiciona_aresta('5', 'C', 'D')
        self.g_e.adiciona_aresta('6', 'D', 'D')
        self.g_e.adiciona_aresta('7', 'D', 'B')
        self.g_e.adiciona_aresta('8', 'D', 'E')
        self.g_e.adiciona_aresta('9', 'E', 'A')
        self.g_e.adiciona_aresta('11', 'E', 'B')

        # Matrizes para teste do algoritmo de Warshall

        self.g_p_m = self.constroi_matriz(self.g_p)
        self.g_p_m[0][1] = 1
        self.g_p_m[0][2] = 1
        self.g_p_m[1][2] = 1
        self.g_p_m[3][1] = 1
        self.g_p_m[3][2] = 1
        self.g_p_m[4][1] = 1
        self.g_p_m[4][2] = 1
        self.g_p_m[4][5] = 1
        self.g_p_m[4][6] = 1
        self.g_p_m[5][1] = 1
        self.g_p_m[5][2] = 1
        self.g_p_m[5][6] = 1

        self.g_e_m = self.constroi_matriz(self.g_e)
        for i in range(0, len(self.g_e_m)):
            self.g_e_m[0][i] = 1
            self.g_e_m[2][i] = 1
            self.g_e_m[3][i] = 1
            self.g_e_m[4][i] = 1

        self.g_c_m = self.constroi_matriz(self.g_c)
        self.g_c_m[0][1] = 1
        self.g_c_m[0][2] = 1
        self.g_c_m[0][3] = 1
        self.g_c_m[0][0] = 0
        self.g_c_m[1][0] = 0
        self.g_c_m[1][2] = 0
        self.g_c_m[1][3] = 0
        self.g_c_m[1][1] = 0
        self.g_c_m[2][0] = 0
        self.g_c_m[2][1] = 1
        self.g_c_m[2][3] = 0
        self.g_c_m[2][2] = 0
        self.g_c_m[3][0] = 0
        self.g_c_m[3][1] = 1
        self.g_c_m[3][2] = 1
        self.g_c_m[3][3] = 0

        self.g_l1_m = self.constroi_matriz(self.g_l1)
        self.g_l1_m[0][0] = 1
        self.g_l1_m[0][1] = 1
        self.g_l1_m[0][2] = 0
        self.g_l1_m[0][3] = 0
        self.g_l1_m[1][0] = 0
        self.g_l1_m[1][1] = 0
        self.g_l1_m[1][2] = 0
        self.g_l1_m[1][3] = 0
        self.g_l1_m[2][0] = 0
        self.g_l1_m[2][1] = 0
        self.g_l1_m[2][2] = 0
        self.g_l1_m[2][3] = 0
        self.g_l1_m[3][0] = 0
        self.g_l1_m[3][1] = 0
        self.g_l1_m[3][2] = 0
        self.g_l1_m[3][3] = 0

        self.g_l4_m = self.constroi_matriz(self.g_l4)
        self.g_l4_m[0][0] = 1

        self.g_d_m = self.constroi_matriz(self.g_d)
        self.g_d_m[0][0] = 0
        self.g_d_m[0][1] = 1
        self.g_d_m[0][2] = 0
        self.g_d_m[0][3] = 0
        self.g_d_m[1][0] = 0
        self.g_d_m[1][1] = 0
        self.g_d_m[1][2] = 0
        self.g_d_m[1][3] = 0
        self.g_d_m[2][0] = 0
        self.g_d_m[2][1] = 0
        self.g_d_m[2][2] = 0
        self.g_d_m[2][3] = 0
        self.g_d_m[3][0] = 0
        self.g_d_m[3][1] = 0
        self.g_d_m[3][2] = 0
        self.g_d_m[3][3] = 0

        self.g_c3_m = self.constroi_matriz(self.g_c3)

        # Grafos desconexos
        self.g_dijkstra = MeuGrafo()
        self.g_dijkstra.adiciona_vertice("A")
        self.g_dijkstra.adiciona_vertice("B")
        self.g_dijkstra.adiciona_vertice("C")
        self.g_dijkstra.adiciona_vertice("D")
        self.g_dijkstra.adiciona_aresta('1', 'A', 'B', 1)
        self.g_dijkstra.adiciona_aresta('2', 'A', 'C', 1)
        self.g_dijkstra.adiciona_aresta('3', 'B', 'D', 1)
        self.g_dijkstra.adiciona_aresta('2', 'C', 'D', 2)

        #Grafos para testar o algoritmo de Dijkstra
        self.g_dijkstra2 = MeuGrafo()
        self.g_dijkstra2.adiciona_vertice("J")
        self.g_dijkstra2.adiciona_vertice("C")
        self.g_dijkstra2.adiciona_vertice("E")
        self.g_dijkstra2.adiciona_vertice("P")
        self.g_dijkstra2.adiciona_vertice("M")
        self.g_dijkstra2.adiciona_vertice("T")
        self.g_dijkstra2.adiciona_vertice("Z")
        self.g_dijkstra2.adiciona_aresta('a1', 'J', 'C', 2)
        self.g_dijkstra2.adiciona_aresta('a2', 'C', 'E', 2)
        self.g_dijkstra2.adiciona_aresta('a3', 'C', 'E', 3)
        self.g_dijkstra2.adiciona_aresta('a4', 'C', 'P', 1)
        self.g_dijkstra2.adiciona_aresta('a5', 'P', 'C', 2)
        self.g_dijkstra2.adiciona_aresta('a6', 'C', 'T', 5)
        self.g_dijkstra2.adiciona_aresta('a7', 'C', 'M', 2)
        self.g_dijkstra2.adiciona_aresta('a8', 'M', 'T', 1)
        self.g_dijkstra2.adiciona_aresta('a9', 'T', 'Z', 1)

        self.g_dijkstra3 = MeuGrafo()
        self.g_dijkstra3.adiciona_vertice('A')
        self.g_dijkstra3.adiciona_vertice('B')
        self.g_dijkstra3.adiciona_vertice('C')
        self.g_dijkstra3.adiciona_vertice('D')
        self.g_dijkstra3.adiciona_aresta('A1', 'A', 'B', 3)
        self.g_dijkstra3.adiciona_aresta('A2', 'A', 'C', 5)
        self.g_dijkstra3.adiciona_aresta('A3', 'B', 'C', 1)
        self.g_dijkstra3.adiciona_aresta('A4', 'B', 'D', 7)
        self.g_dijkstra3.adiciona_aresta('A5', 'C', 'D', 1)

        self.g_dijkstra4 = MeuGrafo()
        self.g_dijkstra4.adiciona_vertice('A')
        self.g_dijkstra4.adiciona_vertice('B')
        self.g_dijkstra4.adiciona_vertice('C')
        self.g_dijkstra4.adiciona_vertice('D')
        self.g_dijkstra4.adiciona_aresta('A1', 'A', 'B', 3)
        self.g_dijkstra4.adiciona_aresta('A2', 'A', 'C', 5)
        self.g_dijkstra4.adiciona_aresta('A3', 'B', 'C', 1)
        self.g_dijkstra4.adiciona_aresta('A4', 'B', 'D', 7)
        self.g_dijkstra4.adiciona_aresta('A5', 'C', 'D', 1)

        self.g_dijkstra5 = MeuGrafo()
        self.g_dijkstra5.adiciona_vertice('A')
        self.g_dijkstra5.adiciona_vertice('B')
        self.g_dijkstra5.adiciona_vertice('C')
        self.g_dijkstra5.adiciona_vertice('D')
        self.g_dijkstra5.adiciona_vertice('E')
        self.g_dijkstra5.adiciona_vertice('F')
        self.g_dijkstra5.adiciona_vertice('G')
        self.g_dijkstra5.adiciona_vertice('H')
        self.g_dijkstra5.adiciona_aresta('A1', 'A', 'B', 4)
        self.g_dijkstra5.adiciona_aresta('A2', 'A', 'D', 1)
        self.g_dijkstra5.adiciona_aresta('A3', 'B', 'C', 5)
        self.g_dijkstra5.adiciona_aresta('A4', 'C', 'H', 6)
        self.g_dijkstra5.adiciona_aresta('A5', 'C', 'G', 1)
        self.g_dijkstra5.adiciona_aresta('A6', 'G', 'F', 1)
        self.g_dijkstra5.adiciona_aresta('A7', 'E', 'F', 3)
        self.g_dijkstra5.adiciona_aresta('A8', 'D', 'E', 2)
        self.g_dijkstra5.adiciona_aresta('A9', 'D', 'H', 7)
        self.g_dijkstra5.adiciona_aresta('A10', 'F', 'H', 1)

        self.g_dijkstra6 = MeuGrafo()
        self.g_dijkstra6.adiciona_vertice('A')
        self.g_dijkstra6.adiciona_vertice('B')
        self.g_dijkstra6.adiciona_vertice('C')
        self.g_dijkstra6.adiciona_vertice('D')
        self.g_dijkstra6.adiciona_vertice('E')
        self.g_dijkstra6.adiciona_vertice('F')
        self.g_dijkstra6.adiciona_vertice('G')
        self.g_dijkstra6.adiciona_aresta('A1', 'A', 'B', 2)
        self.g_dijkstra6.adiciona_aresta('A2', 'A', 'C', 6)
        self.g_dijkstra6.adiciona_aresta('A3', 'B', 'D', 5)
        self.g_dijkstra6.adiciona_aresta('A4', 'C', 'D', 8)
        self.g_dijkstra6.adiciona_aresta('A5', 'D', 'E', 15)
        self.g_dijkstra6.adiciona_aresta('A6', 'D', 'F', 10)
        self.g_dijkstra6.adiciona_aresta('A7', 'F', 'E', 6)
        self.g_dijkstra6.adiciona_aresta('A8', 'E', 'G', 6)
        self.g_dijkstra6.adiciona_aresta('A9', 'F', 'G', 2)

        self.g_dijkstra7 = MeuGrafo()
        self.g_dijkstra7.adiciona_vertice('A')
        self.g_dijkstra7.adiciona_vertice('B')
        self.g_dijkstra7.adiciona_vertice('C')
        self.g_dijkstra7.adiciona_vertice('D')
        self.g_dijkstra7.adiciona_vertice('E')
        self.g_dijkstra7.adiciona_aresta('A1', 'A', 'B', 2)
        self.g_dijkstra7.adiciona_aresta('A2', 'A', 'C', 4)
        self.g_dijkstra7.adiciona_aresta('A3', 'C', 'D', 1)
        self.g_dijkstra7.adiciona_aresta('A4', 'B', 'D', 5)
        self.g_dijkstra7.adiciona_aresta('A5', 'C', 'E', 5)
        self.g_dijkstra7.adiciona_aresta('A6', 'D', 'E', 2)

        self.g_dijkstra8 = MeuGrafo()
        self.g_dijkstra8.adiciona_vertice('A')
        self.g_dijkstra8.adiciona_vertice('B')
        self.g_dijkstra8.adiciona_vertice('C')
        self.g_dijkstra8.adiciona_vertice('D')
        self.g_dijkstra8.adiciona_vertice('E')
        self.g_dijkstra8.adiciona_vertice('F')
        self.g_dijkstra8.adiciona_vertice('G')
        self.g_dijkstra8.adiciona_aresta('A1', 'A', 'B', 2)
        self.g_dijkstra8.adiciona_aresta('A2', 'A', 'C', 6)
        self.g_dijkstra8.adiciona_aresta('A3', 'B', 'D', 5)
        self.g_dijkstra8.adiciona_aresta('A4', 'C', 'D', 8)
        self.g_dijkstra8.adiciona_aresta('A5', 'D', 'E', 15)
        self.g_dijkstra8.adiciona_aresta('A6', 'D', 'F', 10)
        self.g_dijkstra8.adiciona_aresta('A7', 'F', 'E', 6)
        self.g_dijkstra8.adiciona_aresta('A8', 'E', 'G', 6)
        self.g_dijkstra8.adiciona_aresta('A9', 'F', 'G', 2)

        # Grafos para testar algoritmo de Bellman-Ford
        self.bellman_ford1 = MeuGrafo()
        self.bellman_ford1.adiciona_vertice('A')
        self.bellman_ford1.adiciona_vertice('B')
        self.bellman_ford1.adiciona_vertice('C')
        self.bellman_ford1.adiciona_vertice('D')

        self.bellman_ford1.adiciona_aresta('A1', 'A', 'B', 5)
        self.bellman_ford1.adiciona_aresta('A2', 'B', 'D', -4)
        self.bellman_ford1.adiciona_aresta('A3', 'D', 'C', 2)
        self.bellman_ford1.adiciona_aresta('A4', 'C', 'B', 1)
        self.bellman_ford1.adiciona_aresta('A5', 'C', 'D', 3)

        self.bellman_ford2 = MeuGrafo()
        self.bellman_ford2.adiciona_vertice('A')
        self.bellman_ford2.adiciona_vertice('B')
        self.bellman_ford2.adiciona_vertice('C')
        self.bellman_ford2.adiciona_vertice('D')
        self.bellman_ford2.adiciona_vertice('E')

        self.bellman_ford2.adiciona_aresta('A1', 'A', 'B', 4)
        self.bellman_ford2.adiciona_aresta('A2', 'A', 'D', 2)
        self.bellman_ford2.adiciona_aresta('A3', 'B', 'D', 3)
        self.bellman_ford2.adiciona_aresta('A4', 'D', 'B', 1)
        self.bellman_ford2.adiciona_aresta('A5', 'B', 'C', 2)
        self.bellman_ford2.adiciona_aresta('A6', 'D', 'E', 5)
        self.bellman_ford2.adiciona_aresta('A7', 'E', 'C', -5)
        self.bellman_ford2.adiciona_aresta('A8', 'D', 'C', 4)
        self.bellman_ford2.adiciona_aresta('A9', 'B', 'E', 3)

        self.bellman_ford3 = MeuGrafo()
        self.bellman_ford3.adiciona_vertice('A')
        self.bellman_ford3.adiciona_vertice('B')
        self.bellman_ford3.adiciona_vertice('C')
        self.bellman_ford3.adiciona_vertice('D')
        self.bellman_ford3.adiciona_vertice('E')
        self.bellman_ford3.adiciona_vertice('F')

        self.bellman_ford3.adiciona_aresta('A1', 'A', 'B', 5)
        self.bellman_ford3.adiciona_aresta('A2', 'A', 'C', -2)
        self.bellman_ford3.adiciona_aresta('A3', 'B', 'D', 1)
        self.bellman_ford3.adiciona_aresta('A4', 'C', 'B', 2)
        self.bellman_ford3.adiciona_aresta('A5', 'D', 'C', 2)
        self.bellman_ford3.adiciona_aresta('A6', 'C', 'E', 3)
        self.bellman_ford3.adiciona_aresta('A7', 'D', 'E', 7)
        self.bellman_ford3.adiciona_aresta('A8', 'E', 'F', 10)
        self.bellman_ford3.adiciona_aresta('A9', 'D', 'F', 3)

        self.bellman_ford4 = MeuGrafo()
        self.bellman_ford4.adiciona_vertice('A')
        self.bellman_ford4.adiciona_vertice('B')
        self.bellman_ford4.adiciona_vertice('C')
        self.bellman_ford4.adiciona_vertice('D')
        self.bellman_ford4.adiciona_vertice('E')

        self.bellman_ford4.adiciona_aresta('A1', 'A', 'B', -1)
        self.bellman_ford4.adiciona_aresta('A2', 'A', 'C', 4)
        self.bellman_ford4.adiciona_aresta('A3', 'B', 'C', 3)
        self.bellman_ford4.adiciona_aresta('A4', 'B', 'D', 2)
        self.bellman_ford4.adiciona_aresta('A5', 'D', 'B', 1)
        self.bellman_ford4.adiciona_aresta('A6', 'D', 'C', 5)
        self.bellman_ford4.adiciona_aresta('A7', 'B', 'E', 2)
        self.bellman_ford4.adiciona_aresta('A8', 'E', 'D', -3)

        self.bellman_ford5 = MeuGrafo()
        self.bellman_ford5.adiciona_vertice('A')
        self.bellman_ford5.adiciona_vertice('B')
        self.bellman_ford5.adiciona_vertice('C')
        self.bellman_ford5.adiciona_vertice('D')
        self.bellman_ford5.adiciona_vertice('E')
        self.bellman_ford5.adiciona_vertice('F')

        self.bellman_ford5.adiciona_aresta('A1', 'A', 'B', -10)
        self.bellman_ford5.adiciona_aresta('A2', 'A', 'D', -5)
        self.bellman_ford5.adiciona_aresta('A3', 'B', 'D', -7)
        self.bellman_ford5.adiciona_aresta('A4', 'B', 'C', -1)
        self.bellman_ford5.adiciona_aresta('A5', 'D', 'E', -15)
        self.bellman_ford5.adiciona_aresta('A6', 'E', 'C', -4)
        self.bellman_ford5.adiciona_aresta('A7', 'C', 'F', -2)
        self.bellman_ford5.adiciona_aresta('A8', 'E', 'F', -3)

        self.bellman_ford6 = MeuGrafo()
        self.bellman_ford6.adiciona_vertice('A')
        self.bellman_ford6.adiciona_vertice('B')
        self.bellman_ford6.adiciona_vertice('C')
        self.bellman_ford6.adiciona_vertice('D')
        self.bellman_ford6.adiciona_vertice('E')

        self.bellman_ford6.adiciona_aresta('A1', 'A', 'B', 5)
        self.bellman_ford6.adiciona_aresta('A2', 'A', 'C', 4)
        self.bellman_ford6.adiciona_aresta('A3', 'B', 'C', -3)
        self.bellman_ford6.adiciona_aresta('A4', 'C', 'D', -1)
        self.bellman_ford6.adiciona_aresta('A5', 'D', 'B', 6)
        self.bellman_ford6.adiciona_aresta('A6', 'C', 'E', 1)
        self.bellman_ford6.adiciona_aresta('A7', 'D', 'E', -5)
        self.bellman_ford6.adiciona_aresta('A8', 'E', 'A', 2)

        self.bellman_ford7 = MeuGrafo()
        self.bellman_ford7.adiciona_vertice('A')
        self.bellman_ford7.adiciona_vertice('B')
        self.bellman_ford7.adiciona_vertice('C')
        self.bellman_ford7.adiciona_vertice('D')
        self.bellman_ford7.adiciona_vertice('E')
        self.bellman_ford7.adiciona_vertice('F')
        self.bellman_ford7.adiciona_vertice('G')
        self.bellman_ford7.adiciona_vertice('H')

        self.bellman_ford7.adiciona_aresta('A1', 'H', 'A', 3)
        self.bellman_ford7.adiciona_aresta('A2', 'A', 'B', -4)
        self.bellman_ford7.adiciona_aresta('A3', 'B', 'G', 4)
        self.bellman_ford7.adiciona_aresta('A4', 'H', 'C', 5)
        self.bellman_ford7.adiciona_aresta('A5', 'C', 'D', 6)
        self.bellman_ford7.adiciona_aresta('A6', 'D', 'C', -3)
        self.bellman_ford7.adiciona_aresta('A7', 'D', 'G', 8)
        self.bellman_ford7.adiciona_aresta('A8', 'H', 'E', 2)
        self.bellman_ford7.adiciona_aresta('A9', 'E', 'F', 3)
        self.bellman_ford7.adiciona_aresta('A10', 'F', 'E', -6)
        self.bellman_ford7.adiciona_aresta('A11', 'F', 'G', 7)

        self.bellman_ford8 = MeuGrafo()
        self.bellman_ford8.adiciona_vertice('A')
        self.bellman_ford8.adiciona_vertice('B')
        self.bellman_ford8.adiciona_vertice('C')
        self.bellman_ford8.adiciona_vertice('D')
        self.bellman_ford8.adiciona_vertice('E')

        self.bellman_ford8.adiciona_aresta('A1', 'A', 'B', 3)
        self.bellman_ford8.adiciona_aresta('A2', 'A', 'E', -4)
        self.bellman_ford8.adiciona_aresta('A3', 'A', 'C', 8)
        self.bellman_ford8.adiciona_aresta('A4', 'B', 'E', 7)
        self.bellman_ford8.adiciona_aresta('A5', 'B', 'D', 1)
        self.bellman_ford8.adiciona_aresta('A6', 'C', 'B', 4)
        self.bellman_ford8.adiciona_aresta('A7', 'D', 'C', -5)
        self.bellman_ford8.adiciona_aresta('A8', 'D', 'A', 2)
        self.bellman_ford8.adiciona_aresta('A9', 'E', 'D', 6)

        self.bellman_ford9 = MeuGrafo()
        self.bellman_ford9.adiciona_vertice('A')
        self.bellman_ford9.adiciona_vertice('B')
        self.bellman_ford9.adiciona_vertice('C')
        self.bellman_ford9.adiciona_vertice('D')
        self.bellman_ford9.adiciona_vertice('E')

        self.bellman_ford9.adiciona_aresta('A1', 'A', 'B', 6)
        self.bellman_ford9.adiciona_aresta('A2', 'A', 'C', 7)
        self.bellman_ford9.adiciona_aresta('A3', 'B', 'D', 5)
        self.bellman_ford9.adiciona_aresta('A4', 'D', 'B', -2)
        self.bellman_ford9.adiciona_aresta('A5', 'B', 'C', 8)
        self.bellman_ford9.adiciona_aresta('A6', 'C', 'D', -3)
        self.bellman_ford9.adiciona_aresta('A7', 'B', 'E', -4)
        self.bellman_ford9.adiciona_aresta('A8', 'C', 'E', 9)
        self.bellman_ford9.adiciona_aresta('A9', 'E', 'D', 7)
        self.bellman_ford9.adiciona_aresta('A10', 'E', 'A', 2)

    def constroi_matriz(self, g: MeuGrafo):
        ordem = len(g._vertices)
        m = list()
        for i in range(ordem):
            m.append(list())
            for j in range(ordem):
                m[i].append(0)
        return m

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = ArestaDirecionada("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_remove_vertice(self):
        self.assertTrue(self.g_p.remove_vertice("J"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_vertice("J")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_vertice("K")
        self.assertTrue(self.g_p.remove_vertice("C"))
        self.assertTrue(self.g_p.remove_vertice("Z"))

    def test_remove_aresta(self):
        self.assertTrue(self.g_p.remove_aresta("a1"))
        self.assertFalse(self.g_p.remove_aresta("a1"))
        self.assertTrue(self.g_p.remove_aresta("a7"))
        self.assertFalse(self.g_c.remove_aresta("a"))
        self.assertTrue(self.g_c.remove_aresta("a6"))
        self.assertTrue(self.g_c.remove_aresta("a1", "J"))
        self.assertTrue(self.g_c.remove_aresta("a5", "C"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a2", "X", "C")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a3", "X")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a3", v2="X")

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-J', 'C-T', 'C-Z', 'C-M', 'C-P', 'E-C', 'E-J', 'E-P',
                                                                   'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-Z', 'T-J',
                                                                   'T-M', 'T-E', 'T-P', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-T'})


        self.assertEqual(self.g_c.vertices_nao_adjacentes(), {'C-J', 'C-E', 'C-P', 'E-J', 'E-P', 'P-J'})
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_e.vertices_nao_adjacentes(), {'A-D', 'A-E', 'B-A', 'B-C', 'B-D', 'B-E', 'C-E', 'D-C', 'D-A', 'E-D', 'E-C'})

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())
        self.assertTrue(self.g_e.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_e.grau('C'), 5)
        self.assertEqual(self.g_e.grau('D'), 5)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())
        self.assertTrue(self.g_e.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a2', 'a3'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')
        self.assertEqual(self.g_e.arestas_sobre_vertice('D'), {'6', '7', '8'})

    def test_warshall(self):
        self.assertEqual(self.g_p.warshall(), self.g_p_m)
        self.assertEqual(self.g_e.warshall(), self.g_e_m)
        self.assertEqual(self.g_c.warshall(), self.g_c_m)
        self.assertEqual(self.g_l1.warshall(), self.g_l1_m)
        self.assertEqual(self.g_d.warshall(), self.g_d_m)
        self.assertEqual(self.g_l4.warshall(), self.g_l4_m)
        self.assertEqual(self.g_c3.warshall(), self.g_c3_m)

    def test_dijkstra(self):
        self.assertEqual(self.g_dijkstra2.dijkstra('J', 'Z'), (['J', 'a1', 'C', 'a7', 'M', 'a8', 'T', 'a9', 'Z'], 6))
        self.assertEqual(self.g_dijkstra3.dijkstra('A', 'D'), (['A', 'A1', 'B', 'A3', 'C', 'A5', 'D'], 5))
        self.assertEqual(self.g_dijkstra4.dijkstra('A', 'C'), (['A', 'A1', 'B', 'A3', 'C'], 4))
        self.assertRaises(VerticeInvalidoError, self.g_dijkstra3.dijkstra, 'A', 'E')
        self.assertEqual(self.g_dijkstra5.dijkstra('A', 'H'), (['A', 'A2', 'D', 'A8', 'E', 'A7', 'F', 'A10', 'H'], 7))
        self.assertEqual(self.g_dijkstra6.dijkstra('A', 'G'), (['A', 'A1', 'B', 'A3', 'D', 'A6', 'F', 'A9', 'G'], 19))
        self.assertEqual(self.g_dijkstra7.dijkstra('A', 'E'), (['A', 'A2', 'C', 'A3', 'D', 'A6', 'E'], 7))
        self.assertEqual(self.g_dijkstra8.dijkstra('A', 'G'), (['A', 'A1', 'B', 'A3', 'D', 'A6', 'F', 'A9', 'G'], 19))
        self.assertRaises(KeyError, self.g_dijkstra3.dijkstra, 'D', 'A')

    def test_bellman_ford(self):
        self.assertFalse(self.bellman_ford1.bellman_ford('A', 'D'))
        self.assertEqual(self.bellman_ford2.bellman_ford('A', 'E'), (['A', 'A2', 'D', 'A4', 'B', 'A9', 'E'], 6))
        self.assertEqual(self.bellman_ford3.bellman_ford('A', 'E'), (['A', 'A2', 'C', 'A6', 'E'], 1))
        self.assertEqual(self.bellman_ford4.bellman_ford('A', 'D'), (['A', 'A1', 'B', 'A7', 'E', 'A8', 'D'], -2))
        self.assertEqual(self.bellman_ford5.bellman_ford('A', 'F'), (['A', 'A1', 'B', 'A3', 'D', 'A5', 'E', 'A6', 'C', 'A7', 'F'], -38))
        self.assertFalse(self.bellman_ford6.bellman_ford('B', 'A'))
        self.assertFalse(self.bellman_ford7.bellman_ford('H', 'G'))
        self.assertEqual(self.bellman_ford8.bellman_ford('C', 'A'), (['C', 'A6', 'B', 'A5', 'D', 'A8', 'A'], 7))
        self.assertEqual(self.bellman_ford8.bellman_ford('D', 'E'), (['D', 'A8', 'A', 'A2', 'E'], -2))
        self.assertEqual(self.bellman_ford8.bellman_ford('E', 'B'), (['E', 'A9', 'D', 'A7', 'C', 'A6', 'B'], 5))
        self.assertEqual(self.bellman_ford9.bellman_ford('A', 'D'), (['A', 'A2', 'C', 'A6', 'D'], 4))
        self.assertEqual(self.bellman_ford9.bellman_ford('E', 'B'), (['E', 'A10', 'A', 'A2', 'C', 'A6', 'D', 'A4', 'B'], 4))
        self.assertEqual(self.bellman_ford9.bellman_ford('A', 'B'), (['A', 'A2', 'C', 'A6', 'D', 'A4', 'B'], 2))