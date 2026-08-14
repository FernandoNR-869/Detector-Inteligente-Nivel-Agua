# Detector Inteligente de Nivel de Agua

Sistema automatizado de monitoreo y control de nivel de agua, diseñado bajo un enfoque teórico analógico y validado mediante una arquitectura de control digital en entorno virtual.

* **Evidencia en Video:** [Ver Demostración y Explicación del Proyecto](https://drive.google.com/file/d/1bOHy4-GMGvpOdRw2NqZLTbuPnlRriqPz/view?usp=sharing)

## Arquitectura y Tecnologías

* **Plataforma de Control:** Raspberry Pi Pico (RP2040).
* **Entorno de Programación:** MicroPython.
* **Entorno de Simulación:** Wokwi.
* **Sensor / Entrada:** Potenciómetro conectado al canal analógico ADC (GP26) para emular la variación de nivel.
* **Indicadores Visuales:** 3 LEDs (Verde: Nivel Bajo/Seguro, Amarillo: Nivel Medio, Rojo: Nivel Crítico).
* **Alarma Sonora:** Zumbador (Buzzer) activo controlado por el pin GP12.

## Estructura del Repositorio

* `/docs/reporte_tecnico.md` : Documento técnico formal, memoria de cálculos teóricos, BOM y justificación de la arquitectura.
* `/src/main.py` : Código fuente en MicroPython con la lógica de umbrales y control de actuadores.
* `/media/` : Evidencias visuales, capturas de pantalla de la simulación y enlace al video de funcionamiento.

## Autores

* **Fernando Navarro Rodríguez**
* **Andrea Romero Pilar**
* *Ingeniería en Software y Sistemas Computacionales*
