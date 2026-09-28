from perfiles import descomponer_naca

perfiles_guardados = {}

seguir = True

while seguir:
    codigo = input("Introduce el código NACA: ")

    if codigo == "salir":
        seguir = False

    elif len(codigo) == 4 and codigo.isdigit():

        if codigo in perfiles_guardados:
            print("Curvatura:", perfiles_guardados[codigo]["curvatura"])
            print("Posición:", perfiles_guardados[codigo]["posicion"])
            print("Espesor:", perfiles_guardados[codigo]["espesor"])

        else:
            curv_max, pos_curv_max, esp_max = descomponer_naca(codigo)
            print("Curvatura:", curv_max)
            print("Posición:", pos_curv_max)
            print("Espesor:", esp_max)
            perfiles_guardados[codigo] = {"curvatura": curv_max, "posicion": pos_curv_max, "espesor": esp_max}

        if perfiles_guardados[codigo]["curvatura"] == 0:
            print("El perfil es simétrico.")

    else:
        print("Eso no es un código NACA válido ni 'salir'. Inténtalo de nuevo.")