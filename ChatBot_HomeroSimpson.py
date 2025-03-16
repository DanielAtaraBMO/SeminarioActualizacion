import random
import tkinter as tk

# Frases de Homero para respuestas divertidas
frases_homero = [
    "¡D'oh! No sé mucho de eso, pero puedo recomendarte donas...",
    "Mmm... ¡esa es una buena pregunta! Déjame pensar... No, mejor cómprate una cerveza.",
    "¿Eso se come? Si no, no me interesa... ¡Ja ja ja!",
    "Yo solo trabajo aquí porque Marge dice que debo hacerlo... ¿En qué te ayudo?"
]

# Respuestas del chatbot para consultas frecuentes
respuestas = {
    "precio": "¡Mmm... los precios están en la etiqueta! Pero si necesitas ayuda, pregúntale a un empleado.",
    "horario": "¡Estamos abiertos desde las 8 AM hasta las 10 PM, a menos que me quede dormido!",
    "oferta": "¡Hoy hay ofertas en donas y cerveza Duff! ¡Woohoo!",
    "ubicacion": "Estamos en la calle Springfield #742. ¡No olvides traer a toda la familia!"
}

# Función para procesar la entrada del usuario y responder sin NLP
def responder_usuario(texto):
    texto = texto.lower()
    for clave in respuestas:
        if clave in texto:
            return respuestas[clave]
    return random.choice(frases_homero)

# Crear interfaz gráfica con Tkinter
def enviar_mensaje():
    user_input = entrada_usuario.get()
    if user_input.strip():
        chat_text.insert(tk.END, f"Tú: {user_input}\n", "usuario")
        chat_text.yview(tk.END)  # Desplaza el chat hacia abajo
        root.update_idletasks()  # Actualiza la interfaz gráfica
        
        respuesta = responder_usuario(user_input)
        chat_text.insert(tk.END, f"Homero: {respuesta}\n", "homero")
        chat_text.yview(tk.END)
        
        entrada_usuario.delete(0, tk.END)

# Configuración de la ventana de chat
root = tk.Tk()
root.title("Chatbot Homero")
root.geometry("400x500")

# Área de chat
chat_text = tk.Text(root, wrap=tk.WORD, bg="white", font=("Arial", 12))
chat_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
chat_text.tag_config("usuario", foreground="blue")
chat_text.tag_config("homero", foreground="green")

# Cuadro de entrada y botón de enviar
frame = tk.Frame(root)
frame.pack(pady=10)
entrada_usuario = tk.Entry(frame, font=("Arial", 12), width=30)
entrada_usuario.pack(side=tk.LEFT, padx=10)
boton_enviar = tk.Button(frame, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(side=tk.RIGHT)

# Mensaje de bienvenida
def iniciar_conversacion():
    saludo = random.choice([
        "¡Bienvenido al supermercado! ¿Buscas donas?",
        "¡Hola, amigo! ¿En qué puedo ayudarte hoy?",
        "¡Woohoo! Otro cliente, otra oportunidad para venderte algo... ¡Digo, ayudarte!"
    ])
    chat_text.insert(tk.END, f"Homero: {saludo}\n", "homero")

iniciar_conversacion()

root.mainloop()
