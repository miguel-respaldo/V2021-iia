import cv2 as cv

camara = cv.VideoCapture(0)

# Si la camara NO esta abierta
if not camara.isOpened():
    print("No se puede abrir la camara")
    exit(1)

# Leemos la imagen de la camara
ret, imagen = camara.read()

if not ret:
    print("No podemos capturar la imagen de la camara")
else:
    cv.imshow("Camara", imagen)

espera = input("Dar Enter")

camara.release()
cv.destroyAllWindows()
