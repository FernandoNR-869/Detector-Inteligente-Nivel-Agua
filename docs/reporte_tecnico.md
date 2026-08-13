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

Para que nuestro circuito funcione correctamente, decidimos utilizar una fuente de alimentación de 9V (DC). Elegimos este valor porque es un voltaje muy común, fácil de simular y suficiente para alimentar tanto el amplificador operacional LM324 como el buzzer.

### A. Divisores de Voltaje y Umbrales de Activación
Para que el sistema sepa cuándo el agua llega a los diferentes niveles, necesitamos establecer tres voltajes de referencia que servirán como umbrales (Bajo, Medio y Alto)[cite: 1]. Para lograrlo, diseñamos un divisor de voltaje usando cuatro resistencias del mismo valor (10 k$\Omega$) conectadas en serie[cite: 1]. Los voltajes de activación se calcularon de la siguiente manera:

$$V_{ref\_alto} = 9\text{ V} \cdot \frac{R_2 + R_3 + R_4}{R_1 + R_2 + R_3 + R_4} = 6.75\text{ V}$$

$$V_{ref\_medio} = 9\text{ V} \cdot \frac{R_3 + R_4}{R_1 + R_2 + R_3 + R_4} = 4.5\text{ V}$$

$$V_{ref\_bajo} = 9\text{ V} \cdot \frac{R_4}{R_1 + R_2 + R_3 + R_4} = 2.25\text{ V}$$

### B. Corriente de los LEDs
Para proteger los LEDs indicadores y asegurar que tengan un buen nivel de brillo, tomamos en cuenta que consumen alrededor de 20 mA (0.02 A) y tienen una caída de voltaje de aproximadamente 2V[cite: 1]. Usando la ley de Ohm calculamos la resistencia necesaria:

$$R_{LED} = \frac{V_{CC} - V_{LED}}{I_{LED}} = \frac{9 - 2}{0.02} = 350 \, \Omega$$

El resultado exacto es 350 $\Omega$, pero para fines prácticos y para el listado de materiales, usaremos el valor comercial más cercano que es de 330 $\Omega$.

### C. Polarización del Transistor y Corriente del Buzzer
El buzzer que vamos a utilizar como alarma necesita una corriente de unos 30 mA para emitir sonido[cite: 1]. Como el LM324 no siempre puede entregar tanta corriente de forma segura, usamos un transistor BJT 2N2222 funcionando como un interruptor[cite: 1]. Sabiendo que la ganancia mínima ($\beta$) de este transistor es de 100, primero calculamos la corriente mínima que necesitamos en su base:

$$I_B \geq \frac{I_C}{\beta} = \frac{30\text{ mA}}{100} = 0.3\text{ mA}$$

Para estar completamente seguros de que el transistor se active bien (que entre en saturación)[cite: 1], multiplicamos esa corriente por un factor de seguridad de 10, lo que nos da 3 mA. Como sabemos que el LM324 entrega unos 7.5V cuando se activa el nivel alto, calculamos la resistencia para la base del transistor:

$$R_B = \frac{V_{out} - V_{BE}}{I_B} = \frac{7.5 - 0.7}{0.003} \approx 2266 \, \Omega$$

Seleccionamos una resistencia estándar de 2.2 k$\Omega$.

### D. Potencia Disipada
Finalmente, para comprobar la seguridad del circuito, calculamos cuánta potencia va a disipar el componente principal (el transistor) cuando esté encendido, para asegurarnos de que no se caliente demasiado[cite: 1]. Considerando un voltaje colector-emisor en saturación de 0.2V:

$$P_Q = V_{CE(sat)} \cdot I_C = 0.2 \cdot 0.03 = 0.006\text{ W} = 6\text{ mW}$$

Como la hoja de datos del 2N2222 indica que soporta hasta 625 mW, con estos 6 mW comprobamos teóricamente que el transistor trabajará de forma muy holgada y segura.

## IV. Simulación y Resultados
(Espacio para capturas del circuito operando en Proteus y la tabla comparativa de estados).

## V. Conclusión
(Análisis final y validación técnica del proyecto).
