# 🤖 ATIN AI (by xDino99)

¡Hola! Soy **xDino99** y este es **ATIN AI**, un asistente personal de terminal escrito en Python que no solo responde preguntas, sino que **aprende de ti** en tiempo real. 

A diferencia de otros bots con respuestas predefinidas, ATIN nace con el "cerebro" vacío. Tú eres quien le enseña qué responder, cómo pensar y cómo interactuar, guardando todo ese conocimiento en una base de datos local.

---

## 🚀 ¿Cómo funciona el "cerebro"?

ATIN utiliza una lógica de **Fuzzy Matching** (coincidencia difusa). Esto significa que no necesitas escribir la pregunta exactamente igual a como se la enseñaste; gracias a la librería `difflib`, el bot entiende variaciones en tu escritura y busca la respuesta más parecida en su memoria.



Toda su "inteligencia" se almacena en un archivo llamado `memory.dat` en formato JSON. Si el bot no sabe algo, entrará en modo aprendizaje y te pedirá que le digas qué debería responder la próxima vez.

---

## ✨ Características principales

* **🧠 Aprendizaje Dinámico:** Si no conoce una respuesta, te pide que lo instruyas.
* **💾 Memoria Persistente:** Todo lo aprendido se guarda en un archivo local, sin necesidad de servidores externos.
* **🎮 Módulos de Entretenimiento:** * `game1`: Un juego de adivinanza de números.
    * `game2`: Un juego de **Snake (la serpiente)** clásico directamente en la terminal.
* **📊 System Fetch:** Un comando especial para ver estadísticas técnicas como uso de memoria, versión de Python y complejidad de las respuestas.
* **🎨 Interfaz Colorida:** Uso de códigos ANSI para una experiencia visual más cómoda en la consola.

---

## 🛠️ Instalación y Uso

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/xDino99/ATIN-AI.git
   ```

2. **Ejecuta el bot:** (Requiere Python 3)
  ```bash
  python atin_ai.py
  ```
El juego Snake (game2) utiliza la librería msvcrt, por lo que está diseñado principalmente para Windows.

### ⌨️ Comandos del Sistema

Usa estos comandos dentro de la terminal de ATIN AI para gestionar su funcionamiento:

| Comando | Descripción |
| :--- | :--- |
| `help` | Muestra la lista completa de comandos disponibles. |
| `info` | Explica brevemente cómo funciona el aprendizaje de la IA. |
| `games` | Lista los mini-juegos disponibles (`game1` y `game2`). |
| `refresh` | Recarga la memoria desde el archivo `memory.dat` (útil si editaste el archivo a mano). |
| `fetch` | Muestra información técnica: PID, versión de Python, tamaño de memoria y estadísticas. |
| `clear` | Limpia todo el texto de la pantalla de la terminal. |
| `reset` | Borra todo el conocimiento aprendido y restaura la base de datos. |
| `delete_memory` | Elimina físicamente el archivo `memory.dat` del disco. |
| `cancel` | Cancela el proceso de aprendizaje cuando la IA te pregunta una respuesta. |
| `exit` | Apaga ATIN AI y cierra la aplicación. |

## 🛠️ Tecnologías

* **Python 3**

* **JSON:** (Almacenamiento)

* **Difflib:** (Lógica de coincidencia)

*  **Visual Studio Code**

## 👤 Autor

### Desarrollado por xDino99

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Esto significa que puedes usar, copiar, modificar y distribuir el código libremente, siempre que mantengas el aviso de autoría. 

Consulta el archivo [LICENSE](LICENSE) para más detalles.
