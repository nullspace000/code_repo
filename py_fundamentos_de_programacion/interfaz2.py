import customtkinter as ctk

# Configurar el aspecto visual de la aplicacion
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class Interfaz(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("mi interfaz")
        self.geometry("400x300")
        self.resizable(True, True)

        self.crear_elementos()

    def crear_elementos(self):
        # Crear un contenedor
        contenedor_principal = ctk.CTkFrame(self)
        contenedor_principal.pack(pady=20, padx=0, fill="both", expand=True)

        # Crear una etiqueta
        etiqueta = ctk.CTkLabel(
            contenedor_principal,
            text="primera etiqueta"
        )
        etiqueta.pack(pady=10)

        # Crear un input (guardar como atributo de la clase)
        self.campo_entrada = ctk.CTkEntry(
            contenedor_principal,
            placeholder_text="Escribe tu nombre",
            width=250
        )
        self.campo_entrada.pack(pady=10)

        # Crear un botón (usar referencia al método, no ejecutarlo)
        boton = ctk.CTkButton(
            contenedor_principal,
            text="Click",
            fg_color="#035E7B",
            hover_color="#C70039",
            command=self.saludar
        )
        boton.pack(pady=10)

        # Crear un área de resultados (guardar como atributo de la clase)
        self.area_resultado = ctk.CTkTextbox(
            contenedor_principal,
            height=80,
            width=300
        )
        self.area_resultado.pack(pady=10)

    def saludar(self):
        nombre = self.campo_entrada.get()
        mensaje = f"Hola {nombre}!\n"
        self.area_resultado.insert("end", mensaje)
        self.area_resultado.configure(text_color="red")

if __name__ == "__main__":
    app = Interfaz()
