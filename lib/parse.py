from argparse import ArgumentParser # Manejo de argumentos

def parse():
    # Definimos los argumentos de linea de comando que aceptamos
    parser = ArgumentParser()

    # Verbosidad, opcional, False por defecto
    parser.add_argument('-v', '--verbose', action = 'store_true',
                        help = 'Muestra mas informacion')

    # Cantidad de iteraciones, opcional, 1500 por defecto
    parser.add_argument('-i', '--iters', type = int, default = 1500,
                        help = 'Cantidad de iteraciones a efectuar')

    # Ancho del dibujo, opcional, 1024 por defecto
    parser.add_argument('-w', '--width', type = int, default = 1024,
                        help = 'Ancho del dibujo')

    # Diametro de los nodos, opcional, 5 por defecto
    parser.add_argument('-d', '--diameter', type = int, default = 5,
                        help = 'Diametro de los nodos')

    # Margen, opcional, 15 por defecto
    parser.add_argument('-m', '--margin', type = int, default = 15,
                        help = 'Margen de la ventana')

    # Alto del dibujo, opcional, 768 por defecto
    parser.add_argument('-l', '--height', type = int, default = 768,
                        help = 'Alto del dibujo')

    # Escala del dibujo, opcional, 1 por defecto
    parser.add_argument('-r', '--ratio', type = float, default = 0.7,
                        help = 'Escala del dibujo')

    # Pausa entre iteraciones, opcional, 0.1 por defecto
    parser.add_argument('-p', '--pause', type = float, default = 0.05,
                        help = 'Pausa entre iteraciones')

    # Pausa final, opcional, 1.5 por defecto
    parser.add_argument('-n', '--end', type = float, default = 1.5,
                        help = 'Pausa final')

    # Fuerza minima, opcional, 6 por defecto
    parser.add_argument('-t', '--stop', type = int, default = 6,
                        help = 'Fuerza minima')

    # Salteo de frames por iteracion, opcional, 50 por defecto
    parser.add_argument('-f', '--frame_skip', type = int, default = 50,
                        help = 'Salteo de frames por iteracion')

    # Fuerza de gravedad
    parser.add_argument('-g', '--gravity', type = int, default = 2,
                        help = 'Fuerza de gravedad')

    # Archivo del cual leer el grafo
    parser.add_argument('file_name',
                        help = 'Archivo del cual leer el grafo a dibujar')

    return parser.parse_args()
