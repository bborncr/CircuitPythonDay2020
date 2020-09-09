# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
import uos, machine
import network
from umqtt.robust import MQTTClient
import time
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()