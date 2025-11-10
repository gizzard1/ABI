import base64
from openai import OpenAI

client = OpenAI(
  api_key="sk-..."  # Reemplaza con tu clave de API de OpenAI
)

# Define el prompt para la edición de la imagen
prompt = """
{
  # key: contexto para definir el rol del asesor virtual

  "contexto": "Eres un asesor virtual experto en cortes y estilos de salón.",

  #key: cliente obtenido del formulario diseñado para recopilar información relevante sobre el cliente

  "cliente": {
    "genero": "",
    "edad": ,
    "ocupacion": "",
    "preferencias": "",
    "mantenimiento": "",
    "objetivo": ""
    "intensidad": ""
  },
  "imagen": "foto del cliente adjunta",

  # key: catalogo_salon editable según la disponibilidad de los servicios en el salón

  "catalogo_salon": ["corte en capas", "bro flow", "tinte discreto", "tratamiento hidratante", "corte degradado", "peinado con textura", "corte clásico", "corte undercut", "corte pompadour", "corte buzz cut",  "corte fade", "corte crew cut", "corte quiff", "corte side part", "corte taper", "corte comb over", "corte messy", "corte spiky"],

  # key: comentarios_adicionales para cualquier detalle extra que el cliente quiera agregar

  "comentarios_adicionales": "Edita la imagen adjunta para mostrar un corte de cabello moderno y profesional que se adapte a las preferencias y objetivos del cliente. Asegúrate de que el estilo sea fácil de mantener y adecuado para alguien que usa casco de moto con frecuencia. Además trata de manetener la apariencia realista y natural.",
}
"""

# Realiza la solicitud para editar la imagen con el prompt proporcionado
result = client.images.edit(
    model="gpt-image-1",
    image=open("ruta_de_la_imagen_id", "rb"),
    prompt=prompt,
)

# Decodifica la imagen base64 y guárdala en un archivo
image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Guarda la imagen editada en un archivo para su posterior visualización
with open("imagen_id.png", "wb") as f:
    f.write(image_bytes)

    