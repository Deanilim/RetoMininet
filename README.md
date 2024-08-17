                              PROYECTO DE REDES CON MININET Y COMO SE INTERACTÚA CON COMANDOS MEDIANTE LA TERMINAL DE UBUNTU

#PROCEDIMIENTOS
1.- Ejecutar un comando de prueba con Mininet:
    Este comando inicia una red virtual usando un switch de tipo Open vSwitch y prueba la conectividad entre     todos los nodos.
              sudo mn --switch ovsk --test pingall

2.- Iniciar la interfaz gráfica de Mininet (Miniedit):
    Este comando abre el editor gráfico Miniedit para diseñar y simular topologías de red.
              sudo python /usr/share/mininet/examples/miniedit.py

3.- Obtener ayuda sobre los comandos disponibles en Mininet:
    Muestra una lista de comandos y su descripción en Mininet.
              help

4.- Ver los nodos conectados en la red:
    Este comando lista todos los nodos activos en la red virtual.
              nodes

5.- Ver los puertos y enlaces de la red:
    Muestra la topología actual de la red, incluyendo los enlaces entre switches y hosts.
              net

6.- Obtener detalles de todos los nodos:
    Proporciona información detallada sobre cada nodo, como IP, MAC, interfaces, etc.
              dump

7.- Ver los procesos activos en un host específico:
    Muestra los procesos que están corriendo en un host determinado (ejemplo: h1).
            h1 ps -a

8.- Iniciar Mininet desde la terminal:
    Inicia una sesión de Mininet para crear y controlar una red virtual.
            sudo mn

9.- Hacer ping entre dos nodos específicos:
    Envía un ping desde un nodo a otro para verificar la conectividad (ejemplo: h1 a h2).
            h1 ping -c 1 h2

10.- Hacer ping a todos los nodos de la red:
      Prueba la conectividad entre todos los nodos en la red.
            pingall

11.- Habilitar un enlace de un switch:
      Activa un enlace específico de un switch (ejemplo: s1).
            link s1 up

12.- Deshabilitar un enlace de un switch:
      Desactiva un enlace específico de un switch (ejemplo: s1).
            link s1 down

13.- Medir el ancho de banda entre dos nodos con iperf:
      Inicia un servidor de iperf en un nodo y mide el ancho de banda desde otro nodo (ejemplo: h1 y h2).
            h1 iperf -s &
            h2 iperf -c h1

14.- Salir de Mininet:
      Finaliza la sesión de Mininet y limpia la red.
            exit













