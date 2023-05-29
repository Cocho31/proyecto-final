import tkinter as tk
import time


class Robot:
    def __init__(self):
        self.current_state = "Idle"
        self.current_category = ""
        self.target_object = None

    def start(self):
        self.current_state = "Exploring"
        return "Robot comenzó a explorar"

    def stop(self):
        self.current_state = "Idle"
        return "Robot se detuvo"

    def release_object(self):
        return "Se soltó un objeto de la garra del robot"

    def object_movement(self):
        return "El objeto se movió o cambió de posición/orientación mientras se intentaba agarrar"

    def unable_to_reach_object(self):
        return "El robot no pudo llegar a la posición del objeto"

    def emergency_stop(self):
        return "Se oprimió el botón de parada de emergencia"

    def resume_operation(self):
        return "Se oprimió el botón de continuar"

    def arrive_at_target(self):
        return "El robot llegó a la posición del objeto"

    def change_category(self):
        self.current_category = "Nueva Categoría"
        return f"Se cambió la categoría de los objetos a: {self.current_category}"

    def claw_extended(self):
        return "La garra del robot llegó a su posición más extendida"

    def no_more_objects(self):
        return "Ya no hay más objetos reciclables para recoger"

    def camera_disconnected(self):
        return "La cámara se desconectó y no hay imágenes"

    def unable_to_grab_object(self):
        return "El robot no logró agarrar el objeto después de varios minutos"

    def category_change_during_approach(self):
        self.current_category = "Botella"
        return "Mientras la garra se acerca a un objeto de la categoría 'lata', la AI cambia la categoría a 'botella'"

    def deposit_object(self):
        if self.current_category != "":
            message = f"El robot depositó el objeto en la categoría: {self.current_category}"
            self.current_category = ""
        else:
            message = "No hay categoría seleccionada"
        return message


class RobotGUI:
    def __init__(self):
        self.robot = Robot()
        self.window = tk.Tk()
        self.window.title("Robot Control")

        # Estado actual del robot
        self.state_label = tk.Label(self.window, text="Estado: Idle")
        self.state_label.pack()

        # Caja de texto para mostrar eventos
        self.events_text = tk.Text(self.window, height=10, width=50)
        self.events_text.pack()

        # Botón de inicio
        self.start_button = tk.Button(
            self.window, text="Iniciar", command=self.start_robot)
        self.start_button.pack()

        # Botón de finalizar
        self.stop_button = tk.Button(
            self.window, text="Finalizar", command=self.stop_robot)
        self.stop_button.pack()

    def start_robot(self):
        self.log_event(self.robot.start())
        self.state_label.configure(text="Estado: Explorando")
        # Deshabilitar el botón de inicio
        self.start_button.configure(state=tk.DISABLED)
        self.execute_cycle()
        self.state_label.configure(text="Estado: Terminado")
        # Deshabilitar el botón de finalizar
        self.stop_button.configure(state=tk.DISABLED)

    def stop_robot(self):
        self.log_event(self.robot.stop())
        self.window.destroy()  # Cerrar la ventana y finalizar el programa

    def execute_cycle(self):
        events = [
            self.robot.release_object,
            self.robot.object_movement,
            self.robot.unable_to_reach_object,
            self.robot.emergency_stop,
            self.robot.resume_operation,
            self.robot.arrive_at_target,
            self.robot.change_category,
            self.robot.claw_extended,
            self.robot.no_more_objects,
            self.robot.camera_disconnected,
            self.robot.unable_to_grab_object,
            self.robot.category_change_during_approach,
            self.robot.deposit_object
        ]

        for event in events:
            self.log_event_with_loading_bar(event())

    def log_event(self, event):
        self.events_text.insert(tk.END, event + "\n")
        self.events_text.see(tk.END)

    def log_event_with_loading_bar(self, event):
        self.events_text.insert(tk.END, event + " [")
        self.events_text.see(tk.END)
        self.window.update()  # Actualizar la ventana para mostrar la barra de carga
        time.sleep(2)  # Pausa de 2 segundos
        self.events_text.insert(tk.END, "###] \n")
        self.events_text.see(tk.END)
        self.window.update()  # Actualizar la ventana para mostrar la barra de carga completa


if __name__ == "__main__":
    robot_gui = RobotGUI()
    robot_gui.window.mainloop()
