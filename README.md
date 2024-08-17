       
<p align="center">
  <strong>PROYECTO DE REDES CON MININET Y CÓMO SE INTERACTÚA CON COMANDOS MEDIANTE LA TERMINAL DE UBUNTU</strong>
</p>

## PROCEDIMIENTOS

1. **Ejecutar un comando de prueba con Mininet:**
   - ```bash
     sudo mn --switch ovsk --test pingall
     ```

2. **Iniciar la interfaz gráfica de Mininet (Miniedit):**
   - ```bash
     sudo python /usr/share/mininet/examples/miniedit.py
     ```

3. **Obtener ayuda sobre los comandos disponibles en Mininet:**
   - ```bash
     help
     ```

4. **Ver los nodos conectados en la red:**
   - ```bash
     nodes
     ```

5. **Ver los puertos y enlaces de la red:**
   - ```bash
     net
     ```

6. **Obtener detalles de todos los nodos:**
   - ```bash
     dump
     ```

7. **Ver los procesos activos en un host específico (ejemplo: h1):**
   - ```bash
     h1 ps -a
     ```

8. **Iniciar Mininet desde la terminal:**
   - ```bash
     sudo mn
     ```

9. **Hacer ping entre dos nodos específicos (ejemplo: h1 a h2):**
   - ```bash
     h1 ping -c 1 h2
     ```

10. **Hacer ping a todos los nodos de la red:**
    - ```bash
      pingall
      ```

11. **Habilitar un enlace de un switch (ejemplo: s1):**
    - ```bash
      link s1 up
      ```

12. **Deshabilitar un enlace de un switch (ejemplo: s1):**
    - ```bash
      link s1 down
      ```

13. **Medir el ancho de banda entre dos nodos con iperf (ejemplo: h1 y h2):**
    - ```bash
      h1 iperf -s &
      ```
    - ```bash
      h2 iperf -c h1
      ```

14. **Salir de Mininet:**
    - ```bash
      exit
      ```
