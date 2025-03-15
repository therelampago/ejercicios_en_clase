# Definir el perfil del usuario
perfil = {
    "nombre": "Kaeel Martínez",
    "edad": 18,
    "ciudad": "Barranquilla",
    "amigos": [
        {"nombre": "Ana Gómez", "tiempo_amistad": "5 años"},
        {"nombre": "Luis Torres", "tiempo_amistad": "3 años"},
        {"nombre": "Marta López", "tiempo_amistad": "2 años"}
    ],
    "posts": [
        {"contenido": "¡Hoy es un gran día!", "likes": 15, "comentarios": ["¡Sí lo es!", "Disfrútalo"]},
        {"contenido": "Amo la programación.", "likes": 25, "comentarios": ["Yo también!", "Sigue así"]}
    ]
}

# Agregar un nuevo post
nuevo_post = {"contenido": "Explorando Madrid", "likes": 10, "comentarios": ["¡Qué envidia!", "Disfruta mucho"]}
perfil["posts"].append(nuevo_post)

# Modificar la ciudad del usuario a "Madrid"
perfil["ciudad"] = "Madrid"

# Eliminar el segundo amigo de la lista
perfil["amigos"].pop(1)

# Mostrar el perfil actualizado de manera ordenada
print("\nPerfil del Usuario")
print("=" * 30)
print(f"Nombre: {perfil['nombre']}")
print(f"Edad: {perfil['edad']}")
print(f"Ciudad: {perfil['ciudad']}")

print("\nAmigos:")
for amigo in perfil["amigos"]:
    print(f"- {amigo['nombre']} ({amigo['tiempo_amistad']})")

print("\nPublicaciones:")
for post in perfil["posts"]:
    print(f"\nContenido: {post['contenido']}")
    print(f"Likes: {post['likes']}")
    print("Comentarios:")
    for comentario in post["comentarios"]:
        print(f"  - {comentario}")

