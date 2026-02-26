import cv2
#from cvzone.HandTrackingModule import HandDetector

#webcam = cv2.VideoCapture(1)


webcam = cv2.VideoCapture(0)
if not webcam.isOpened():
    print("Error: Could not open webcam")
    exit()

#rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while True:

    exito, imagen = webcam.read()
    #imagen = cv2.resize(imagen, (1280, 720))

   # coordenadas, imagen_manos = rastreador.findHands(imagen)

   # print(coordenadas)

    cv2.imshow("Proyecto 04 - IA", imagen)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()


