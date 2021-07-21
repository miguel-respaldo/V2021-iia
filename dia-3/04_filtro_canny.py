import cv2 as cv

camara = cv.VideoCapture(0)

# Si la camara NO esta abierta
if not camara.isOpened():
    print("No se puede abrir la camara")
    exit(1)

while True:
    # Leemos la imagen de la camara
    ret, imagen = camara.read()

    if not ret:
        print("No podemos capturar la imagen de la camara")
        break

    espejo = cv.flip(imagen,1)
    # 1  espejo
    # 0  de cabeza
    # -1 de cabeza espejo

    # Usamos el filtro de Canny
    canny = cv.Canny(espejo, 100, 200)

    cv.imshow("Camara", canny)

    # Si precionamos la tecla Escape
    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()
