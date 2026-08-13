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
## III. Memoria de Cálculos

Para el diseño del circuito, se establece una fuente de alimentación de 9V (DC) estándar, adecuada para la operación del LM324 y la activación del buzzer.

### A. Divisores de Voltaje (Umbrales de Activación)
Se requiere establecer tres voltajes de referencia para los comparadores (Nivel Bajo, Medio y Alto). Se implementa un divisor de tensión múltiple con cuatro resistencias en serie ($R_1$, $R_2$, $R_3$, $R_4$) de 10 k$\Omega$ cada una. Los umbrales se calculan con la siguiente relación:

$$V_{ref\_alto} = 9\text{ V} \cdot \frac{R_2 + R_3 + R_4}{R_1 + R_2 + R_3 + R_4} = 6.75\text{ V}$$

$$V_{ref\_medio} = 9\text{ V} \cdot \frac{R_3 + R_4}{R_1 + R_2 + R_3 + R_4} = 4.5\text{ V}$$

$$V_{ref\_bajo} = 9\text{ V} \cdot \frac{R_4}{R_1 + R_2 + R_3 + R_4} = 2.25\text{ V}$$

### B. Corriente de los LEDs
Asumiendo una caída de tensión típica de 2V para los LEDs y una corriente de operación óptima de 20 mA ($0.02\text{ A}$), se calcula la resistencia limitadora:

$$R_{LED} = \frac{V_{CC} - V_{LED}}{I_{LED}} = \frac{9 - 2}{0.02} = 350 \, \Omega$$

Se seleccionará el valor comercial más cercano de 330 $\Omega$ para asegurar el brillo adecuado.

### C. Polarización del Transistor y Corriente del Buzzer
El buzzer activo requiere un consumo aproximado de 30 mA. Para activarlo, se utiliza un transistor BJT 2N2222 en estado de corte/saturación. Asumiendo una ganancia mínima ($\beta$) de 100, la corriente de base necesaria es:

$$I_B \geq \frac{I_C}{\beta} = \frac{30\text{ mA}}{100} = 0.3\text{ mA}$$

Para garantizar una saturación profunda, se aplica un factor de sobremarcha de 10, fijando $I_B = 3\text{ mA}$. El voltaje de salida del LM324 en estado alto es de aproximadamente 7.5V. El cálculo de la resistencia de base ($R_B$) es:

$$R_B = \frac{V_{out} - V_{BE}}{I_B} = \frac{7.5 - 0.7}{0.003} = 2266 \, \Omega$$

Se utilizará una resistencia estándar de 2.2 k$\Omega$.

### D. Potencia Disipada
Para validar la seguridad térmica del transistor 2N2222 (que soporta hasta 625 mW), se calcula su disipación en estado de saturación (asumiendo $V_{CE(sat)} \approx 0.2\text{ V}$):

$$P_Q = V_{CE(sat)} \cdot I_C = 0.2 \cdot 0.03 = 0.006\text{ W} = 6\text{ mW}$$

El transistor operará completamente dentro de su margen de seguridad térmica.

## IV. Simulación y Resultados
(Espacio para capturas del circuito operando en Proteus y la tabla comparativa de estados).

## V. Conclusión
(Análisis final y validación técnica del proyecto).
