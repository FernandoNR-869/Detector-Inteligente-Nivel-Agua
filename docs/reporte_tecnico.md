# Diseño y Simulación de un Detector Inteligente de Nivel de Agua

**Fernando Navarro Rodríguez** | **Andrea Romero Pilar**
*Ingeniería en Software y Sistemas Computacionales*

## Resumen
Este documento detalla el diseño, cálculo y simulación de un detector de nivel de agua basado en electrónica analógica. El sistema indica visualmente tres niveles de un depósito y activa una alarma sonora al alcanzar su capacidad máxima.

## I. Introducción
La medición del nivel del agua es un proceso crítico, tanto en ambientes domésticos, como industriales y de construcción. La falta de un control adecuado genera pérdidas importantes de agua, daños mecánicos por funcionamiento en seco de las bombas e incluso riesgos de infraestructura por desbordamientos. Ante la necesidad de una empresa de automatización por un sistema económico y confiable, este proyecto documenta el desarrollo de un detector de nivel de agua basado en electrónica analógica pura. El sistema propuesto, empleando sensores de conductividad, comparadores de voltaje y transistores en estado de conmutación, monitorea continuamente el tanque actualizando de forma automática los indicadores visuales (Bajo, Medio, Alto) y activando una alerta sonora al llegar a niveles críticos.

## II. Diseño del Sistema
### A. Diagrama de Bloques
(Espacio para insertar la imagen del diagrama).

### B. Lista de Materiales (BOM)
| Cantidad | Componente | Descripción / Modelo Sugerido | Función en el Sistema |
| :---: | :--- | :--- | :--- |
| 1 | Amplificador Operacional | LM324 (Cuádruple) | Comparadores de voltaje para los 3 niveles. |
| 1 | Sensor de Nivel | Arreglo de electrodos / Switch | Detectar la presencia de agua (conductividad). |
| 3 | Diodo LED | 5mm (Rojo, Amarillo, Verde) | Indicadores visuales de nivel (Bajo, Medio, Alto). |
| 1 | Zumbador (Buzzer) | Buzzer Activo 5V/9V | Alarma sonora para el nivel crítico (Alto). |
| 1 | Transistor BJT | 2N2222A (NPN) | Interruptor para activar el buzzer. |
| 2 | Diodo Rectificador/Señal | 1N4148 o 1N4007 | Diodo flyback para el buzzer y protección. |
| Var. | Resistencias | 330Ω, 2.2kΩ, 10kΩ | Divisores de voltaje, limitadores de LED y base BJT. |
| 1 | Fuente de Alimentación | Batería o Fuente DC de 9V | Suministro de energía general del circuito. |

## III. Memoria de Cálculos
(Sección para la fuente de alimentación, divisores de voltaje, polarización de transistores, corriente de LEDs y potencia).

## IV. Simulación y Resultados
(Espacio para capturas del circuito operando en Proteus y la tabla comparativa de estados).

## V. Conclusión
(Análisis final y validación técnica del proyecto).
