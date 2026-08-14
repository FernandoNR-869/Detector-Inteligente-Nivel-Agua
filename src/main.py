from machine import Pin, ADC
from time import sleep

# Configuramos el pin analógico para leer el potenciómetro
sensor_agua = ADC(26) 

# Configuramos los pines de salida para los LEDs y el zumbador
led_rojo = Pin(13, Pin.OUT)       # Alarma crítica
led_amarillo = Pin(14, Pin.OUT)   # Nivel medio
led_verde = Pin(15, Pin.OUT)      # Nivel bajo / seguro
buzzer = Pin(12, Pin.OUT)

while True:
    # Leemos el valor del potenciómetro (rango de 0 a 65535)
    nivel = sensor_agua.read_u16() 
    
    # Reiniciamos los estados en cada lectura
    led_rojo.value(0)
    led_amarillo.value(0)
    led_verde.value(0)
    buzzer.value(0)
    
    # Lógica de comparación (El rojo es el nivel crítico)
    if nivel < 21845:        # Nivel bajo (< 33%) -> LED Verde encendido
        led_verde.value(1)
    elif nivel < 43690:      # Nivel medio (33% - 66%) -> LED Amarillo encendido
        led_amarillo.value(1)
    else:                    # Nivel crítico (> 66%) -> LED Rojo + Alarma
        led_rojo.value(1)
        buzzer.value(1)      
        
    sleep(0.1)
