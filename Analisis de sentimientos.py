import tkinter as tk
from textblob import TextBlob

def analizar_sentimiento(texto):
    texto = texto.strip()  # Limpia espacios innecesarios
    if not texto:
        return "⚠️ Ingresa un mensaje válido.", "normal"

    analisis = TextBlob(texto)
    sentimiento = analisis.sentiment.polarity
    subjetividad = analisis.sentiment.subjectivity

    if sentimiento >= 0.5:
        return "😁 Muy feliz y positivo.", "positivo"
    elif 0.1 <= sentimiento < 0.5:
        return "😊 Un poco feliz.", "positivo"
    elif -0.1 < sentimiento < 0.1:
        if subjetividad > 0.5:
            return "😐 Parece neutral, pero subjetivo.", "neutral"
        else:
            return "😶 Completamente neutral.", "neutral"
    elif -0.5 <= sentimiento < -0.1:
        return "☹️ Un poco triste.", "triste"
    else:
        return "😢 Muy triste o negativo.", "triste"

def enviar_mensaje(event=None):  # Permite usar Enter para enviar
    mensaje_usuario = entrada_texto.get().strip()
    if mensaje_usuario:
        respuesta, tipo = analizar_sentimiento(mensaje_usuario)
        
        historial_texto.config(state=tk.NORMAL)
        historial_texto.insert(tk.END, "Tú: " + mensaje_usuario + "\n", "usuario")
        historial_texto.insert(tk.END, "Bot: " + respuesta + "\n", tipo)  # Se asigna el color dinámico
        
        historial_texto.config(state=tk.DISABLED)
        entrada_texto.delete(0, tk.END)
        historial_texto.yview(tk.END)  # Auto-scroll

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Chatbot con Análisis de Sentimientos")

# Área de conversación con scroll
frame_historial = tk.Frame(ventana)
frame_historial.pack()

scrollbar = tk.Scrollbar(frame_historial)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

historial_texto = tk.Text(frame_historial, height=20, width=50, yscrollcommand=scrollbar.set, state=tk.DISABLED)
historial_texto.pack()

scrollbar.config(command=historial_texto.yview)

# Campo de entrada y botón
entrada_texto = tk.Entry(ventana, width=50)
entrada_texto.pack()
entrada_texto.bind("<Return>", enviar_mensaje)  # Permite Enter para enviar

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack()

# Estilo de texto con diferentes colores según la emoción detectada
historial_texto.tag_config("usuario", foreground="black")  # Usuario en negro
historial_texto.tag_config("positivo", foreground="dark orange")  # Respuesta positiva en verde
historial_texto.tag_config("neutral", foreground="gray")  # Neutral en gris
historial_texto.tag_config("triste", foreground="blue")  # Respuesta triste en azul

ventana.mainloop()