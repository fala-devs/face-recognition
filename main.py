import face_recognition as fr
import cv2

image_path = "foto.jpg"

image = fr.load_image_file(image_path)
faces = fr.face_locations(image)

if len(faces) == 0:
    print("Não há faces")
else:
    img = cv2.imread(image_path)
    for (y1, x2, y2, x1) in faces:
        cv2.rectangle(img, (x1, y1) , (x2, y2), (255, 0, 0), 2)
    cv2.imwrite('r_' + image_path, img)
    print("Imagem gerada!")