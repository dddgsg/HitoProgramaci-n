import pprint



tiendaRopa={'camiseta':25,'pantalon':20,'abrigo':50,'sudadera':30, 'pantalon_corto':10,'calcetines':5 }

class Bienvenidos:
    def __init__(self,nombre,apellidos,edad,tlf,correo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.tlf = tlf
        self.correo = correo
    print('Bienvenido a nuestra página de ropa')
    def registro(self):
        print('')
        print('Usted ha sido registrado como...')

        print(f'nombre: {self.nombre}\napellidos: {self.apellidos}\nedad: {self.edad}\ntlf: {self.tlf}\ncorreo {self.correo}')

        validar = input('Valide si sus datos son correctos')
        while validar.lower()!='si':
            print()
            print('Vuelva a introducir sus datos')
            cliente1=Bienvenidos(input('Nombre:'),input('apellidos:'),input('edad:'),int(input('tlf:')),input('correo:'))
            print()
            print('Registro:')
            print(f'nombre: {self.nombre}\napellidos: {self.apellidos}\nedad: {self.edad}\ntlf: {self.tlf}\ncorreo {self.correo}')
            validar = input('Confirme si sus datos son correctos')
            print(f'Quiere empezar con la compra? {self.nombre}')
            print()
            print('Estos son nuestros productos disponibles')

cliente1 = Bienvenidos(input('Nombre:'), input('apellidos:'), input('edad:'), int(input('tlf:')), input('correo:'))
cliente1.registro()


pprint.pprint(tiendaRopa)

carrito={}
lista_reyes={}


def productos():
    nomp=input('Escoge la prenda que mas te guste:')
    agrega = float(input(f'quieres meter {nomp} a la cesta (1) o para regalo (2) '))

    if agrega == 1:
        carrito[nomp] = tiendaRopa[nomp]
        print(f'Cesta: {carrito}')
        print(f'Total: {sum(carrito.values())}')

    elif agrega == 2:

        lista_reyes[nomp] = tiendaRopa[nomp]

        print(f'lista reyes magos: {lista_reyes}')

        print(f'Total: {sum(lista_reyes.values())}')

    elif agrega >= 3:
        print('Introduce la opcion valida')

productos()


def segcompra():
    print()
    seguir_comprando=input('¿Quieres seguir comprando?\n')

    if seguir_comprando.lower() == 'si':

        pprint.pprint(tiendaRopa)

        productos()
        scompra()

    elif seguir_comprando.lower() == 'no':
        print('Recuerda mover los productos de la lista de regalos a la cesta')
        mreyes=float(input('¿Quieres añadir los productos para regalo a la cesta? SI (1) NO (2)\n'))

        match mreyes:
            case 1:
                pprint.pprint(lista_reyes)
                cambio=input('Agregar productos a la cesta:\n')
                carrito[cambio] =tiendaRopa[cambio]
                print(f'cesta: {carrito}')
                print(f'Total: {sum(carrito.values())}')
            case 2:
                print('Te toca pagar')
    else:
        print('Tienes que escribir si o no')
        scompra()

segcompra()


def pagar():

    pais=input('Dinos de que pais eres\n')

    if pais.lower() == 'españa':
        print('El IVA de España es del 21%')
        print(f'El total con IVA incluido es el total de {sum(carrito.values())*1.21}€')



    else:
        print('Al ser un pais internacional el IVA que se sumara es del 10%')
        print(f'El total con iva incluido es de {sum(carrito.values())*1.10}€')

    print()
    print('Para terminar con la compra debe de elegir el formato de pago')
    fpago=int(input('1| pago con tarjeta\n2| Paypal\n(Formato numero): '))
    match fpago:
        case 1:
            print('Ha decidido pagar con tarjeta')
            numtarjeta=input('Numero de tarjeta: ')
            fechacaduca=input('Fecha de caducidad(mm/yy): ')
            cvv=input('CVV: ')
            print(f'Numero de tarjeta: {numtarjeta}\nFecha de caducidad: {fechacaduca}\nCVV: {cvv}')
            confirmadat1=input('¿Sus datos estan correctos?')
            while confirmadat1.lower() != 'si':
                numtarjeta = input('Numero de tarjeta: ')
                fechacaduca = input('Fecha de caducidad(mm/yy): ')
                cvv = input('CVV: ')
                print(f'Numero de tarjeta: {numtarjeta}\nFecha de caducidad: {fechacaduca}\nCVV: {cvv}')
                confirmadat1 = input('Sus datos estan correctos?\n')
                fact=input('¿Desea que le llegue la factura al gmail o por sms?\n')
                while fact.lower() != 'email' or fact.lower() != 'sms':
                    print('Ha elegido una opción incorrecta')
                if fact.lower() == 'email':
                    print('La factura ha sido enviado a su gmail')
                    if fact.lower() == 'sms':
                        print('La factura ha sido enviada a por sms')

                else:
                    print('Esta opcion no es la correcta reinicie la pagina')

        case 2:
            print('Usted ha decidido pagar por Paypal rellene los correspondientes datos')
            correo=input('Correo: ')
            contraseña=input('Contraseña: ')
            print(f'correo: {correo}\ncontraseña: {contraseña}')
            confirmadat2 = input('¿Sus datos son correctos?\n')
            while confirmadat2.lower() != 'si':
                print()
                print('Rellene nuevamente sus datos')
                correo = input('Correo electrónico: ')
                contraseña = input('Contraseña: ')
                print(f'correo: {correo}\ncontraseña: {contraseña}')
                confirmadat2 = input('¿Sus datos son correctos?')
            fact1 = input('¿Desea que le llegue la factura al gmail o por sms?\n')
            while fact1.lower() != 'email' or fact1.lower() != 'sms':
                print('Ha elegido una opcion incorrecta')
            if fact1.lower() == 'email':
                print('La factura ha sido enviado a su gmail')
                if fact1.lower() == 'sms':
                    print('La factura ha sido enviada a por sms')
            else:
                print('Esta opcion no es la correcta reinicie la pagina')

pagar()
