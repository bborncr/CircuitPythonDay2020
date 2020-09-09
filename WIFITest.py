import network
import urequests
import ujson
import config

# API de prueba para conseguir datos en formato JSON
url = 'http://dummy.restapiexample.com/api/v1/employee/2'

# Configurar el WIFI como cliente y activar
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    print('\n\nConectando a la red...', end='')
    # Conectar al WIFI
    wlan.connect(config.ap_ssid, config.ap_pass)
    while not wlan.isconnected():
        pass
print('conectado')
print('Config de la red:', wlan.ifconfig())

if wlan.isconnected():
    # Conectar al API usando un HTTP GET
    respuesta = urequests.get(url)
    # Convertir la respuesta (texto) a un objeto JSON
    data = ujson.loads(respuesta.text)
    # Acceder los datos del objeto JSON
    nombre = data['data']['employee_name']
    edad = data['data']['employee_age']
    salario = data['data']['employee_salary']
    
    print('Nombre:', nombre)
    print('Edad:', edad)
    print('Salario:', salario)
    
print('Listo')