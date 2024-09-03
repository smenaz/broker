# tests/test_broker.py

import unittest
from rq import Queue
import redis

class TestBroker(unittest.TestCase):

    def setUp(self):
        # Cliente de redis
        # En este caso es un broker de mensajes
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
    
    @unittest.skip("Omit response queue test_message_handling")
    def test_message_handling(self):
        print("Entrando a test_message_handling")
        # Enviar un mensaje ala cola de mensajes
        mensaje_prueba = 'test_control_message'
        self.redis_client.lpush('control', mensaje_prueba)
        # Obtener el mensaje de la cola 'control'
        mensaje = self.redis_client.brpop('control', timeout=5)  # Espera hasta 5 segundos para obtener un mensaje
        if mensaje:
            # `message` es una tupla (nombre_de_la_cola, contenido_del_mensaje)
            mensaje_decodificado = mensaje[1].decode('utf-8')  # Imprime solo el contenido del mensaje
            print("mensaje::::",mensaje_decodificado)  
            self.assertEqual(mensaje_prueba, mensaje_decodificado)
        else:
            print("No mensaje")
   
    def test_enqueue_and_process_response(self):
        print("Entrando a test_enqueue_and_process_response")
        # Enviar un mensaje ala cola de mensajes
        mensaje_prueba = 'test_control_response_message'
        self.redis_client.lpush('control_respuesta', mensaje_prueba)
        # Obtener el mensaje de la cola 'control'
        mensaje = self.redis_client.brpop('control_respuesta', timeout=5)  # Espera hasta 5 segundos para obtener un mensaje
        if mensaje:
            # `message` es una tupla (nombre_de_la_cola, contenido_del_mensaje)
            mensaje_decodificado = mensaje[1].decode('utf-8')
            print("mensaje::::",mensaje_decodificado)  
            self.assertEqual(mensaje_prueba, mensaje_decodificado)
        else:
            print("No mensaje")

if __name__ == '__main__':
    unittest.main()
