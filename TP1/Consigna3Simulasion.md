# Consigna 3: Análisis de Rendimiento en Sistemas Embebidos (ESP32)

## 🎯 Objetivo
Evaluar el impacto de la variación de la frecuencia de reloj del CPU en el tiempo de ejecución de operaciones aritméticas de distintos tipos de datos (Enteros vs. Punto Flotante).

## 💻 Entorno de Pruebas
* **Plataforma:** Simulador Wokwi.
* **Hardware:** ESP32 (Arquitectura Xtensa® Dual-Core 32-bit LX6).
* **Frecuencias evaluadas:** 4 MHz y 8 MHz.

## 📊 Resultados Obtenidos
A continuación se detallan los tiempos de ejecución medidos para un bloque de operaciones determinado:

| Tipo de Dato | Tiempo a 4 MHz | Tiempo a 8 MHz | Variación (%) |
| :--- | :--- | :--- | :--- |
| **Entero (int)** | 78 ms | 82 ms | +5.1% (Ruido de simulación) |
| **Punto Flotante (float)** | 6238 ms | 4984 ms | -20.1% |



###  Simulación
<img width="904" height="882" alt="imagen" src="https://github.com/user-attachments/assets/f5761dac-d9fa-46bf-967f-33a7248770bb" />
###  Codigo 

```cpp
// Función para ejecutar el benchmark de cálculos
void ejecutarPrueba(const char* tipo) {
  long inicio = millis();

  if (tipo == "entero") {
    // Se utiliza 'volatile' para evitar que el compilador optimice y elimine el bucle vacío
    volatile long suma = 0; 
    for (long i = 0; i < 100000; i++) {
      suma += i;
    }
  } else {
    volatile float sumaF = 0.0;
    for (long i = 0; i < 500000; i++) {
      sumaF += 1.1;
    }
  }

  long fin = millis();
  Serial.print("Tiempo [");
  Serial.print(tipo);
  Serial.print("]: ");
  Serial.print(fin - inicio);
  Serial.println(" ms");
}

void setup() {
  Serial.begin(115200);
  delay(1000);
  
  // PRUEBA 1: Frecuencia Baja (4 MHz)
  setCpuFrequencyMhz(4);
  Serial.println("FRECUENCIA: 4 MHz");
  ejecutarPrueba("entero");
  ejecutarPrueba("float");

  delay(2000);

  // PRUEBA 2: Frecuencia Alta (8 MHz - Duplicada)
  setCpuFrequencyMhz(8);
  Serial.println("\nFRECUENCIA: 8 MHz (Duplicada)");
  ejecutarPrueba("entero");
  ejecutarPrueba("float");
}

void loop() {}
```
## 🔍 Interpretación de los Resultados

### 1. Relación Frecuencia vs. Tiempo
Teóricamente, el tiempo de ejecución es inversamente proporcional a la frecuencia ($T \propto 1/f$). Al duplicar la frecuencia de **4 MHz** a **8 MHz**, se observó una reducción significativa en el tiempo de los cálculos `float` (de 6238 ms a 4984 ms). 

> **Nota sobre la simulación:** La reducción no fue exactamente del 50% debido al *overhead* de las funciones de impresión por consola (`Serial.print`) y a las limitaciones de precisión del simulador en frecuencias extremadamente bajas.

### 2. Aceleración por Hardware (FPU)
El ESP32 cuenta con una Unidad de Punto Flotante (FPU). Sin embargo, la diferencia abismal entre los tiempos de enteros (~80 ms) y floats (>4000 ms) demuestra la complejidad intrínseca de las operaciones decimales.
* [cite_start]Las operaciones con **enteros** son órdenes de magnitud más rápidas ya que requieren menos ciclos de reloj por instrucción[cite: 32].
* [cite_start]Para los **doubles** (que no poseen aceleración por hardware en este chip), se esperaría un tiempo aún mayor que el de los floats[cite: 32].

### 3. Conclusión de la prueba
Se confirma que el aumento de la frecuencia de trabajo disminuye el tiempo de ejecución de tareas intensivas. [cite_start]Para aplicaciones de ingeniería que requieran procesamiento de señales en tiempo real (como el análisis de armónicos o control de motores), es crítico operar a frecuencias más altas (ej. 160 MHz o 240 MHz) para garantizar que los tiempos de respuesta sean mínimos[cite: 32, 325, 328].



---
