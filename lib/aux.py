from pygnuplot import gnuplot   # Libreria de ploteo
from numpy import linalg, array # Manejo de vectores

# Funciones auxiliares
def fa(x, k):
    return (x ** 2) / k
def fr(x, k):
    return (k ** 2) / x
def modulo(x):
    return linalg.norm(x)

# Lee un grafo de un archivo
def lee_grafo_archivo(file_path):
    vertices, aristas = [], []

    with open(file_path, 'r') as f:
        cantidad = int(f.readline())

        for _ in range(cantidad):
            vertices += f.readline().split()

        for line in f:
            aristas += [ tuple(line.split()) ]

    return (vertices, aristas)

# Calcula las fuerzas de repulsion
def calcular_repulsion(vertices, fuerzas, posiciones, k):
    for v in vertices:
        fuerzas[v] = array([0.0, 0.0])
        for u in vertices:
            if u != v:
                delta = posiciones[v] - posiciones[u]
                if modulo(delta):
                    fuerzas[v] += (delta / modulo(delta)) * fr(modulo(delta), k)

# Calcula las fuerzas de atraccion
def calcular_atraccion(aristas, fuerzas, posiciones, k):
    for arista in aristas:
        v, u = arista[0], arista[1]
        delta = posiciones[v] - posiciones[u]
        if modulo(delta):
            fuerzas[v] -= (delta / modulo(delta)) * fa(modulo(delta), k)
            fuerzas[u] += (delta / modulo(delta)) * fa(modulo(delta), k)

# Calcula la gravedad
def calcular_gravedad(fuerzas, vertices, posiciones, gravedad):
    for v in vertices:
        fuerzas[v] -= posiciones[v] * gravedad

# Calcula las posiciones
def calcular_posiciones(vertices, fuerzas, posiciones, ancho, alto):
    for v in vertices:
        if modulo(fuerzas[v]):
            posiciones[v] = posiciones[v] + fuerzas[v] / modulo(fuerzas[v])

        # Impide que los vertices se escapen de la pantalla
        posiciones[v][0] = min(ancho / 2, max(-ancho / 2, posiciones[v][0]))
        posiciones[v][1] = min(alto / 2, max(-alto / 2, posiciones[v][1]))

# Crea la ventana
def setwindow(ancho, alto, margen):
    g = gnuplot.Gnuplot()
    g.set(terminal = 'wxt size ' + str(ancho) + ', ' + str(alto))
    g.set(xrange = '[' + str((-ancho / 2) - margen) + ':' + str((ancho / 2) + margen) + ']')
    g.set(yrange = '[' + str((-alto / 2) - margen) + ':' + str((alto / 2) + margen) + ']')
    g.set(key = None, ytics = None, xtics = None, border = None)
    g.plot('NaN')
    return g

# Dibuja el grafo
def dibujar(vertices, posiciones, aristas, g, diametro, margen):
    # Dibuja los nodos
    for i, v in enumerate(posiciones.keys()):
        g.set(object = str(i + 1) + ' circle center ' \
                     + str(posiciones[v][0]) + ', '   \
                     + str(posiciones[v][1])          \
                     + ' size ' + str(diametro))

        g.set(label = str(i + 2) + '"' + v + '" at '        \
                    + str(posiciones[v][0] + margen) + ', ' \
                    + str(posiciones[v][1]))

    # Dibuja las aristas
    for i, a in enumerate(aristas):
        u, v = a[0], a[1]
        midpoint = (posiciones[u] + posiciones[v]) / 2

        g.set(arrow = str(i + len(vertices) * 2) + ' nohead from ' \
                    + str(posiciones[u][0]) + ', '                 \
                    + str(posiciones[u][1]) + ' to '               \
                    + str(posiciones[v][0]) + ', '                 \
                    + str(posiciones[v][1]))

        # Etiqueta los pesos
        if len(a) > 2:
            g.set(label = str(i + len(vertices) * 2 + 1) + '"' \
                        + str(a[2]) + '" at '                  \
                        + str(midpoint[0] + margen) + ', '     \
                        + str(midpoint[1]))

    g('replot')
