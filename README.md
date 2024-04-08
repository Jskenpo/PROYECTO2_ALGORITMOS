# Longest Non-Prefix Set Algorithms (PROYECTO 2)

Este programa implementa tres algoritmos para encontrar el conjunto más largo de cadenas que no son prefijos de otras cadenas en el conjunto dado.

## Algoritmos Implementados

1. **Divide and Conquer**: Divide recursivamente el conjunto en dos mitades, resuelve el problema para cada mitad y luego fusiona las soluciones.
2. **Dynamic Programming**: Utiliza programación dinámica para encontrar la longitud máxima de subsecuencia para cada cadena.
3. **Greedy**: Ordena las cadenas por longitud y selecciona iterativamente aquellas que no son prefijos de las ya seleccionadas.

## Uso

Para ejecutar el programa y probar los algoritmos con diferentes tamaños de entrada, puedes modificar el rango `n_range`, la longitud mínima `min_length` y la longitud máxima `max_length` en el código y luego ejecutarlo:

```python
n_range = [10, 50, 100, 200, 500, 1000]
min_length = 3
max_length = 10
test_and_plot(n_range, min_length, max_length)
```

Esto generará casos de prueba aleatorios con las longitudes especificadas, ejecutará los algoritmos en esos casos de prueba y mostrará un gráfico comparativo de los tiempos de ejecución.

## Requerimientos 

1. Python 3.x
2. matplotlib



