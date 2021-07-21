import cv2 as cv

camara = cv.VideoCapture(2)

# Si la camara NO esta abierta
if not camara.isOpened():
    print("No se puede abrir la camara")
    exit(1)

# Cargando el archivo ya entranado de cascada
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

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

    # Convertimos a escala de grises
    gris = cv.cvtColor(espejo, cv.COLOR_BGR2GRAY)

    # Detectamos las caras
    caras = face_cascade.detectMultiScale(gris, 1.1, 4)

    # Dibujar un rectangulo en cada cara
    for (x, y, w, h) in caras:
        cv.rectangle(espejo, (x,y), (x+w,y+h), (255,0,0), 2)

    cv.imshow("Camara", espejo)

    # Si precionamos la tecla Escape
    if cv.waitKey(1) == 27:
        break

camara.release()
cv.destroyAllWindows()
