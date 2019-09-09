import sys, Ice, cv2
import Demo

# importar modelo
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

class ContadorI(Demo.Contador):
    def contarCaras(self, array, current = None):
        print("Arreglo recibido: {} bytes".format(len(array)))
        
        # Array de bytes a .jpg
        with open("caras.jpg", "wb") as imagen:
            bytes_written = imagen.write(array)
            print("Imagen guardada, {} bytes".format(len(array)))

        # leer imagen
        img = cv2.imread('caras.jpg')

        # imagen a gris
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # detectar caras
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        return len(faces)

with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000")
    object = ContadorI()
    adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
    adapter.activate()
    communicator.waitForShutdown()
