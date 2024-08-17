       
# PROYECTO DE REDES CON MININET Y CÓMO SE INTERACTÚA CON COMANDOS MEDIANTE LA TERMINAL DE UBUNTU

## PROCEDIMIENTOS

# 1. Ejecutar un comando de prueba con Mininet:
sudo mn --switch ovsk --test pingall

# 2. Iniciar la interfaz gráfica de Mininet (Miniedit):
sudo python /usr/share/mininet/examples/miniedit.py

# 3. Obtener ayuda sobre los comandos disponibles en Mininet:
help

# 4. Ver los nodos conectados en la red:
nodes

# 5. Ver los puertos y enlaces de la red:
net

# 6. Obtener detalles de todos los nodos:
dump

# 7. Ver los procesos activos en un host específico (ejemplo: h1):
h1 ps -a

# 8. Iniciar Mininet desde la terminal:
sudo mn

# 9. Hacer ping entre dos nodos específicos (ejemplo: h1 a h2):
h1 ping -c 1 h2

# 10. Hacer ping a todos los nodos de la red:
pingall

# 11. Habilitar un enlace de un switch (ejemplo: s1):
link s1 up

# 12. Deshabilitar un enlace de un switch (ejemplo: s1):
link s1 down

# 13. Medir el ancho de banda entre dos nodos con iperf (ejemplo: h1 y h2):
h1 iperf -s &
h2 iperf -c h1

# 14. Salir de Mininet:
exit
