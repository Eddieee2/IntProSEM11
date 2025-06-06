
import models.classes.py as c
import dao.functions as f

def menu():
    print("""
          1. Agregar
          2. Mostrar
          3. Actualizar
          4. Eliminar
            5. Buscar
          6. Salir
          Digite una opcion:
          """)
    
    def main():
        while(True):
            menu()
            option = input()
            if option == '1':
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                existencia = int(input("Existencia: "))
            elif option == '2':
                print("Productos")
            elif option == '6':
                print("Saliendo del programa...")
                break
            else: 
                print("Opcion no valida, intente de nuevo")