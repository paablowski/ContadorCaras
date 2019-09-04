import sys, Ice
import Demo

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimplePrinter:default -p 10000")
    printer = Demo.ContadorPrx.checkedCast(base)
    if not printer:
        raise RuntimeError("Invalid proxy")

    # Convertir imagen a arreglo de bytes
    with open("faces.jpg", "rb") as image:
        # traer archivo
        f = image.read()
        # convierte a bytes
        b = bytearray(f)

    print("Caras encontradas: {}".format(printer.contarCaras(b)))