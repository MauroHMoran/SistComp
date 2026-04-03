# Facultad de Ciencias Exactas Físicas y Naturales - UNC
# Sistemas de Computación

## TP1: Rendimiento

|Alumnos|
| :--- |
|Mora Ivan|
|Moran Mauro|

----
# Consigna

El objetivo de esta tarea es poner en práctica los conocimientos sobre performance y rendimiento de los computadores. 
El trabajo consta de dos partes: la primera es utilizar benchmarks de terceros para tomar decisiones de hardware y la segunda consiste en utilizar herramientas para medir la performance de nuestro código.

1.  Realizar una tabla de dos entradas con las tareas que realiza cada alumno y que benchmark la representa mejor. Correr uno y comparar los resultados. 

2. Rendimiento de los siguientes procesadores para compilar el kernel de linux: 
- Intel Core i5-13600K
- AMD Ryzen 9 5900X 12-Core

¿Cual es la aceleración cuando usamos un AMD Ryzen 9 7950X 16-Core? ¿Cual de ellos hace un uso más eficiente de la cantidad de núcleos que tiene? ¿Cuál es más eficiente en términos de costo?

3. Conseguir un procesador al que se le pueda cambiar la frecuencia y ejecutar un código que demore alrededor de 10 segundos. 
¿Qué sucede con el tiempo del programa al duplicar (variar) la frecuencia?

4. Realice el tutorial descripto en time profiling. Adjunte conclusiones sobre el uso del tiempo de las funciones. ¿Como podría disminuir el tiempo de ejecución de ese código? 
---

# Desarrollo
## 1. Benchmarks
Un benchmark es un programa o script que ejecuta una tarea predefinida y exigente para medir cuánto tiempo tarda o cuántas operaciones hace por segundo. 
### Tabla de Benchmarks por Integrante
#### Ivan Mora
| Tareas realizadas a diario | Benchmark representativo | Descripción |
| :--- | :--- | :--- |
| Simulación de circuitos en LTSpice | `ngspice` | Motor principal de los simuladores tipo SPICE. |
| Redacción de informes (LaTeX/PDF) | `selenium` | Mide tiempo de respuesta del DOM y renderizado de PDF en el navegador. |

#### Mauro Moran
| Tareas realizadas a diario | Benchmark representativo | Descripción |
| :--- | :--- | :--- |
| Simulación de circuitos en LTSpice | `ngspice` | Mide la capacidad de cálculo matemático puro por núcleo. |
| Analisis de señales en Matlab | `scimark2` | Mide qué tan rápida es una computadora resolviendo cálculos científicos. |

### Comparacion de benchmark

Se elige correr el benchamrk SciMark 2.0 .
Se enfoca exclusivamente en la Unidad de Punto Flotante (FPU) del procesador y en qué tan rápido se comunica con la memoria caché. 
El resultado lo da en Mflops (Millones de operaciones de punto flotante por segundo).

Los analisis realizados fueron:

* Composite
* Monte Carlo
* Fast Fourier Transform
* Sparse Matrix Multiply
* Dense LU Matrix Factorization
* Jacobi Successive Over-Relaxation 

Los resultados obtenidos fueron los siguientes:

| Analisis | Ivan Mora - Intel Core i3-10110U | Mauro Moran - AMD Ryzen 3 3200U|
| :--- | :--- | :--- |
|Composite|$303,5$|$414,16$|
|Monte Carlo|$67,31$|$122,28$|
|Fast Fourier Transform | $113,85 $| $135,47$|
|Spars Matrix Multiply|$340,68$|$528,63$|
|Dense LU MAtrix Factorization|$426,74$|$367,27$|
|Jacobi Successive Over-Relaxation|$568,92$|$920,52$|

En el unico analisis donde existe una distinción importante respecto a la cantidad de Mflops es en el de 'Jacobi Successive Over-Relaxation'. 
Se ve claramente que el procesador AMD Ryzen 3 es superior.

## 2. Rendimiento en Compilación del Kernel de Linux
Se analiza el desempeño de tres microprocesadores distintos utilizando datos de OpenBenchmarking.org. El rendimiento ($\eta$) se define como la inversa del tiempo de ejecución ($1/T$).

### Tabla de Rendimiento Base
| Procesador | Tiempo (promedio) | Núcleos | Rendimiento $(\eta=1/T)$ |
| :--- | :--- | :--- | :--- |
| **Intel Core i5-13600K** | $72\pm5$ s | $14$ | $0,013889$ |
| **AMD Ryzen 9 5900X** | $76\pm8$ s | $12$ | $0,013158$ |
| **AMD Ryzen 9 7950X** | $50\pm6$ s | $16$ | $0,02$ |

### Aceleración y Eficiencia
Para calcular la aceleración obtenida al utilizar el procesador AMD Ryzen 9 7950X de 16 núcleos frente a los otros modelos se comparan sus desempeños.
* Speedup (vs i5-13600K): $72/50=1,44$
* Speedup (vs Ryzen 9 5900X): $76/50=1,52$

Tomando como pivote el rendimiento del AMD Ryzen 9 5900X, calculamos la eficiencia por núcleo:

|Procesador|Speedup |Cores |Eficiencia (Speedup / Cores)|
| :--- | :--- | :--- | :--- |
|AMD Ryzen 9 5900X |$1$|$12$|1/12=0,0833$|
|Intel Core i5-13600K| $1,0555$ | $14$|$1,0555/14=0,0754$|
|AMD Ryzen 9 7950X| $1,52$ |$16$| $1,52/16=0,095$|

El AMD Ryzen 9 7950X hace el uso más eficiente de sus núcleos. 
No solo posee una mayor cantidad de hilos, sino que su capacidad de procesamiento paralelo le permite ser un 52% más rápido que el Ryzen 9 5900X y un 44% más rápido que el Intel i5-13600K en esta tarea específica.

### Eficiencia en términos de Costo y Energía
Se evalúa la relación entre el rendimiento, el costo de adquisición (USD) y el consumo de potencia (Watts).
|Procesador| Precio aprox. (u$s)| Consumo (watts)|Efic. / Precio (×10−3)|Efic. / Consumo (×10−3)|
| :--- | :--- | :--- | :--- |:--- |
|AMD Ryzen 9 5900X |$270$|$105$|$0.3085$|$0.7933$|
|Intel Core i5-13600K|$275$|$125$|$0,2741$|$0,6032$|
|AMD Ryzen 9 7950X|480|$170$|$0,1979$|$0,5588$|

A pesar de que el Ryzen 9 7950X es el más potente, el AMD Ryzen 9 5900X resulta ser el más eficiente en términos de costo-beneficio. 
Presenta la mejor relación entre rendimiento por dólar invertido y rendimiento por watt consumido. 
El Ryzen 9 7950X maximiza el rendimiento paralelo, pero ese incremento de potencia conlleva un costo económico y energético significativamente mayor.

---

## 3. Pruebas en ESP32 (Frecuencia Variable)
Utilizando un Simulador Wokwi se ejecutó un código en un ESP32 variando su frecuencia de reloj para observar el impacto en el tiempo de ejecución.

<img width="904" height="882" alt="imagen" src="https://github.com/user-attachments/assets/f5761dac-d9fa-46bf-967f-33a7248770bb" />

Las frecuencias de trabjo elegidas y los tiempos de ejecución se muestran a continuacion:

| Configuración | Tiempo (entero) | Tiempo (float) |
| :--- | :--- | :--- |
| **Frecuencia 4 MHz** | 78 ms | 6238 ms |
| **Frecuencia 8 MHz** | 82 ms | 4984 ms |

### Relación Frecuencia vs. Tiempo
El tiempo de ejecución es inversamente proporcional a la frecuencia ($T \propto 1/f$). Al duplicar la frecuencia de **4 MHz** a **8 MHz**, se observó una reducción significativa en el tiempo de los cálculos `float` (de 6238 ms a 4984 ms). 

La reducción no fue exactamente del 50% debido al *overhead* de las funciones de impresión por consola (`Serial.print`) y a las limitaciones de precisión del simulador.

### Aceleración por Hardware (FPU)
El ESP32 cuenta con una Unidad de Punto Flotante (FPU). Sin embargo, la diferencia abismal entre los tiempos de enteros (~80 ms) y floats (>4000 ms) demuestra la complejidad intrínseca de las operaciones decimales.
* Las operaciones con **enteros** son órdenes de magnitud más rápidas ya que requieren menos ciclos de reloj por instrucción.
* Para los **doubles** (que no poseen aceleración por hardware en este chip), se esperaría un tiempo aún mayor que el de los floats.

### Conclusión 
Se confirma que el aumento de la frecuencia de trabajo disminuye el tiempo de ejecución de tareas intensivas. Para aplicaciones de ingeniería que requieran procesamiento de señales en tiempo real (como el análisis de armónicos o control de motores), es crítico operar a frecuencias más altas (ej. 160 MHz o 240 MHz) para garantizar que los tiempos de respuesta sean mínimos[cite: 32, 325, 328].


---

## 4. Time Profiling 

### Tutorial

1. Creamos la carpeta donde se van a guardar los archivos con:

```
$ mkdir nombreCarpeta 
```

2. Entramos a la carpeta

```
$ cd nombreCarpeta
```

3. Creamos los archivos .c

```
$ nano nombreArchivo.c
```

![alt text](<Consigna 4/Imagenes/image.png>)

4. Copiamos el codigo y luego guardar y salir

![alt text](<Consigna 4/Imagenes/image-1.png>)


1. Repetimos con el segundo codigo

2. Corremos el programa con:

```
$ cgc -pg nombreArchivo1.c nombreArchivo2.c -o mi_programa

$ ./mi_prorgama
```

7. Esperamos que se ejecute y creamos el reporte con

```
$ gprof mi_programa gmon.out > reporte.txt
```

![alt text](<Consigna 4/Imagenes/image-2.png>)

El profiling  permite identificar qué funciones consumen más recursos del procesador.

### Conclusiones del Flat Profile
* **func1 (55.61% - 11.69s)**: Función más pesada debido al bucle `0xffffffff`.
* **func2 (37.39% - 7.86s)**: Segunda en consumo con un bucle de `0xafffffff`.
* **new_func1 y main (~3.5%)**: Impacto mínimo en el tiempo total.

### Propuestas de Mejora
1. **Flags del Compilador**: Usar `gcc -O3` para eliminar bucles vacíos.
2. **Delays Eficientes**: Reemplazar bucles por `usleep()` o `nanosleep()` para liberar la CPU.
3. **Refactorización**:Usar tipos de datos acordes al procesador o `register int`

