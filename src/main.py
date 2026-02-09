import json
import difflib
import os
import sys
import platform
import time
import random
import msvcrt

os.system("title ATIN AI (by xDino99)")

class TerminalAI:
    def __init__(self):

        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        else:
            application_path = os.path.dirname(os.path.abspath(__file__))

        os.system("")
        self.memory_file = os.path.join(application_path, "memory.dat")
        self.brain = {}
        self.blue = "\033[94m"
        self.green = "\033[92m"
        self.yellow = "\033[93m"
        self.red = "\033[91m"
        self.white = "\033[97m"
        self.reset_color = "\033[0m"
        self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            print(f"Buscando en: {self.memory_file}")
            if os.path.getsize(self.memory_file) > 0:
                try:
                    with open(self.memory_file, 'r', encoding='utf-8') as f:
                        self.brain = json.load(f)
                        print(f"{self.green}ÉXITO: Cargadas {len(self.brain)} respuestas.{self.reset_color}")
                except Exception as e:
                    print(f"{self.red}ERROR DE JSON: {e}")
        else:
            print(f"{self.yellow}SISTEMA: El archivo .dat no existe en esa ruta.{self.reset_color}")

    def save_memory(self):
        try:
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.brain, f, indent=4, ensure_ascii=False)
        except IOError:
            print(f"{self.red}SYSTEM: Error al guardar en memoria.{self.reset_color}")

    def reset_memory(self):
        self.brain = {}
        self.save_memory()
        print(f"{self.green}SYSTEM: Memoria reseteada a valores de fábrica.{self.reset_color}")

    def delete_memory(self):
        try:
            if os.path.exists(self.memory_file):
                os.remove(self.memory_file)
                self.brain = {}
                print(f"{self.green}SYSTEM: Archivo .dat eliminado y memoria limpia.{self.reset_color}")
            else:
                print(f"{self.red}SYSTEM: El archivo no existe.{self.reset_color}")
        except Exception as e:
            print(f"{self.red}SYSTEM: Error al eliminar: {e}{self.reset_color}")

    def find_best_match(self, user_question):
        if not self.brain: return None
        matches = difflib.get_close_matches(user_question, self.brain.keys(), n=1, cutoff=0.6)
        return matches[0] if matches else None

    def learn_new_response(self, question):
        print(f"{self.green}IA: No sé la respuesta a eso. ¿Qué debería decir?{self.reset_color}")
        print(f"{self.yellow}(Escribe la respuesta o 'cancel' para omitir){self.reset_color}")
        
        try:
            new_response = input(f"{self.red}Enseñanza:{self.reset_color} ").strip()
            
            if new_response.lower() == "cancel":
                print(f"{self.yellow}SYSTEM: Operación cancelada.{self.reset_color}")
                return

            if new_response:
                self.brain[question] = new_response
                self.save_memory()
                print(f"{self.green}IA: ¡Gracias! He aprendido una nueva respuesta.{self.reset_color}")
        except KeyboardInterrupt:
            print(f"\n{self.yellow}SYSTEM: Operación cancelada.{self.reset_color}")

    def play_game1(self):
        secret_number = random.randint(1, 100)
        attempts = 0
        
        print(f"\n{self.yellow}[JUEGO: Adivina el número]{self.reset_color}")
        print(f"{self.green}IA: He pensado un número entre 1 y 100. ¡Intenta adivinarlo!{self.reset_color}")

        while True:
            try:
                user_input = input(f"{self.blue}Tu número (o 'exit'): {self.reset_color}").lower().strip()
                
                if user_input == 'exit': 
                    break
                
                guess = int(user_input)
                attempts += 1

                if guess < secret_number:
                    print(f"{self.yellow}IA: Más alto...{self.reset_color}")
                elif guess > secret_number:
                    print(f"{self.yellow}IA: Más bajo...{self.reset_color}")
                else:
                    print(f"{self.green}IA: ¡GANASTE! Lo lograste en {attempts} intentos.{self.reset_color}")
                    break
            except ValueError:
                print(f"{self.red}Por favor, ingresa un número válido.{self.reset_color}")

    def play_game2(self):
        width = 20
        height = 10
        snake_pos = [[5, 5], [5, 4], [5, 3]]
        food_pos = [random.randint(1, height-2), random.randint(1, width-2)]
        direction = 'RIGHT'
        score = 0
        game_over = False

        print(f"{self.green}INICIANDO SNAKE... Usa WASD para moverte.{self.reset_color}")
        time.sleep(1)

        while not game_over:
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'w' and direction != 'DOWN': direction = 'UP'
                elif key == 's' and direction != 'UP': direction = 'DOWN'
                elif key == 'a' and direction != 'RIGHT': direction = 'LEFT'
                elif key == 'd' and direction != 'LEFT': direction = 'RIGHT'
                elif key == 'q': break

            head = list(snake_pos[0])
            if direction == 'UP': head[0] -= 1
            elif direction == 'DOWN': head[0] += 1
            elif direction == 'LEFT': head[1] -= 1
            elif direction == 'RIGHT': head[1] += 1

            if (head[0] < 0 or head[0] >= height or 
                head[1] < 0 or head[1] >= width or 
                head in snake_pos):
                game_over = True
                break

            snake_pos.insert(0, head)

            if head == food_pos:
                score += 1
                food_pos = [random.randint(0, height-1), random.randint(0, width-1)]
            else:
                snake_pos.pop()

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{self.yellow}Puntos: {score} | Presiona 'q' para salir{self.reset_color}")
            
            for r in range(height):
                row_str = ""
                for c in range(width):
                    if [r, c] == snake_pos[0]: row_str += "O"
                    elif [r, c] in snake_pos: row_str += "o"
                    elif [r, c] == food_pos: row_str += "X"
                    else: row_str += "."
                print(row_str)
            
            time.sleep(0.15)

        print(f"\n{self.red}GAME OVER! Puntuación final: {score}{self.reset_color}")
        time.sleep(2)

    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=========================================")
        print(" Bienvenido a ATIN AI")
        print(" Escribe 'help' para ver comandos.")
        print("=========================================")

        while True:
            try:
                user_input = input(f"\n{self.blue}Tu:{self.reset_color} ").lower().strip()

                if not user_input:
                    continue

                if user_input == "exit":
                    print(f"\n{self.red}SISTEMA: Apagando ATIN AI... ¡Adiós!{self.reset_color}")
                    time.sleep(1)
                    sys.exit()
                
                elif user_input == "help":
                    print()
                    print(f"{self.white}[COMANDOS DEL SISTEMA]{self.reset_color}")
                    print("- exit: Cierra la aplicación.")
                    print("- info: Información sobre cómo funciono.")
                    print("- reset: Borra todo lo aprendido y restaura la base original.")
                    print("- games: Lista Juegos para jugar con la ATIN AI.")
                    print("- refresh: Recarga la memoria si editaste el archivo externamente.")
                    print("- delete_memory: Borra el archivo memory.dat de forma permanente.")
                    print("- fetch: Muestra informacion profunda sobre la aplicacion. (usar solo para debuggear)")
                    print("- clear: Limpia la pantalla de la terminal.")
                    print("- cancel: Cancela el proceso de aprendizaje (cuando se solicita).")
                    continue

                elif user_input == "games":
                    print()
                    print(f"\n{self.white}[JUEGOS DEL SISTEMA]{self.reset_color}")
                    print("- game1: Adivina el numero.")
                    print("- game2: Snake el juego de la serpiente.")
                    continue

                elif user_input == "info":
                    print()
                    print(f"{self.white}[INFO]{self.reset_color}")
                    print()
                    print(f"{self.green}IA: Aprendo automáticamente. Si no sé algo, pregúntame y te pediré la respuesta.{self.reset_color}")
                    print(f"{self.green}Todo se guarda en 'memory.dat'.{self.reset_color}")
                    continue

                elif user_input == "fetch":
                    try:
                        total_entries = len(self.brain)
                        memory_usage_bytes = sys.getsizeof(self.brain)
                        if total_entries > 0:
                            avg_len = sum(len(str(v)) for v in self.brain.values()) / total_entries
                        else:
                            avg_len = 0
                            
                        file_status = "DETECTADO" if os.path.exists(self.memory_file) else "NO ENCONTRADO"
                        file_size = os.path.getsize(self.memory_file) if os.path.exists(self.memory_file) else 0

                        print()
                        print(f"{self.white}[SYSTEM FETCH]{self.reset_color}")
                        print()
                        
                        print(f"{self.white}[ENTORNO DE EJECUCIÓN]{self.reset_color}")
                        print(f"- ID Proceso (PID): {os.getpid()}")
                        print(f"- Python Ver: {sys.version.split()[0]}")
                        print(f"- Plataforma: {platform.system()} {platform.release()}")
                        print(f"- Codificación: {sys.getdefaultencoding().upper()}")
                        print("- Compilacion: x64")
                        print("- File Type: Debug")
                        print("- Version: 1.0.0")
                        print("- AI Protocol: 1")
                        
                        print(f"\n{self.white}[ANÁLISIS DE MEMORIA .DAT]{self.reset_color}")
                        print(f"- Ruta: {self.memory_file}")
                        print(f"- Estado del archivo: {file_status}")
                        print(f"- Tamaño en disco: {file_size} bytes")
                        print(f"- Carga en RAM (Cerebro): {memory_usage_bytes} bytes")
                        
                        print(f"\n{self.white}[ESTADÍSTICAS DE APRENDIZAJE]{self.reset_color}")
                        print(f"- Total de conocimientos: {total_entries} unidades")
                        print(f"- Complejidad media: {avg_len:.2f} caracteres/rta")
                        print(f"- Última sincronización: {time.strftime('%H:%M:%S')}")

                        print(f"\n{self.white}[MÓDULOS DE ENTRETENIMIENTO]{self.reset_color}")
                        g1 = "- CARGADO" if hasattr(self, 'play_game1') else "OFFLINE"
                        g2 = "- CARGADO" if hasattr(self, 'play_game2') else "OFFLINE"
                        print(f"- Sub-proceso game1: {g1}")
                        print(f"- Sub-proceso game2: {g2}")
                        
                    except Exception as e:
                        print(f"{self.red}SYSTEM ERROR en Fetch: {e}{self.reset_color}")
                    continue

                elif user_input == "reset":
                    confirm = input(f"{self.yellow}SYSTEM: ¿Estás seguro? Esto borrará todo (s/n): {self.reset_color}").lower()
                    if confirm == "s":
                        self.reset_memory()
                    continue
                
                elif user_input == "delete_memory":
                    confirm = input(f"{self.yellow}¡ADVERTENCIA! Esto borrará el archivo .dat permanentemente. (s/n): {self.reset_color}").lower()
                    if confirm == "s":
                        self.delete_memory()
                    continue

                elif user_input == "refresh":
                    self.load_memory()
                    print(f"{self.green}SYSTEM: Memoria recargada desde 'memory.dat'.{self.reset_color}")
                    continue

                elif user_input == "clear":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"{self.green}SYSTEM: Limpieza exitosa.{self.reset_color}")
                    continue

                elif user_input == "game1":
                    self.play_game1()
                    continue

                elif user_input == "game2":
                    self.play_game2()
                    continue

                best_match = self.find_best_match(user_input)

                if best_match:
                    print(f"{self.green}IA: {self.brain[best_match]}{self.reset_color}")
                else:
                    self.learn_new_response(user_input)
            
            except KeyboardInterrupt:
                print(f"\n{self.green}IA: Apagado forzoso.{self.reset_color}")
                sys.exit()
            except Exception as e:
                print(f"{self.red}SYSTEM: Error crítico: {e}{self.reset_color}")

if __name__ == "__main__":
    bot = TerminalAI()
    bot.run()