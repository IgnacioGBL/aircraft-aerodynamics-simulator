def descomponer_naca(codigo):
    curv_max = int(codigo[0])
    pos_curv_max = int(codigo[1])
    esp_max = int(codigo[2:4])
    return curv_max, pos_curv_max, esp_max