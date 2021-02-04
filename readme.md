# Dependencias

Para poder correr la aplicacion necesitara contar con los programas `gnuplot`, 
`python3` y las librerias `numpy` y `py-gnuplot`. Puede utilizar los 
siguientes comandos para instalarlos en Ubuntu:

```bash
sudo apt install gnuplot python3
pip install numpy py-gnuplot
```
# Uso

Para ver intrucciones de uso puede escribir el comando:

```bash
./gg.py -h
```

o puede probar directamente el programa con uno de los grafos de muestra 
de la carpeta `grafos`, por ejemplo:

```bash
./gg.py grafos/g1.gr
```

# Formato de grafos

El formato de archivo para almacenar un grafo consta de una primera linea 
indicando el numero total de vertices, luego una linea por cada vertice 
y finalmente una linea por cada arista seguida opcionalmente de una etiqueta, 
donde una arista son dos vertices separados por un espacio.

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
