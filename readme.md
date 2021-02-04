# Dependencias

```bash
sudo apt install gnuplot python3
pip install numpy py-gnuplot
```

# Formato de grafos

El formato de archivo para almacenar un grafo consta de una primera linea 
indicando el numero total de vertices, luego una linea por cada vertice 
y finalmente una linea por cada arista, donde una arista son dos vertices 
separados por un espacio.

El siguiente ejemplo muestra como puede almacenarse en un archivo el grafo 
completo K6:

```
6
a
b
c
d
e
f
a b
a c
a d
a e
a f
b c
b d
b e
b f
c d
c e
c f
d e
d f
e f
```

# Uso

Para ver intrucciones de uso puede escribir el comando:

```bash
./gg -h
```
