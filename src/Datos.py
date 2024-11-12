import csv
import matplotlib.pyplot as plt


class FileManager:
    def __init__(self):
        self.file_path = None

    def seleccionar_archivo(self):
        self.file_path = input("Ingrese la ruta completa del archivo .csv: ")
        try:
            with open(self.file_path, 'r') as file:
                pass
        except FileNotFoundError:
            print("Archivo no encontrado.")
            self.file_path = None


class CSVProcessor:

    def __init__(self):
        pass

    def mostrar_15_filas(self, file_path):
        print("\nMostrando las primeras 15 filas del archivo:")
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i < 15:
                    print(row)
                else:
                    break

    def calcular_estadisticas(self, file_path, columna):
        datos = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    datos.append(float(row[columna]))
                except ValueError:
                    continue

        if datos:
            print(f"\nEstadísticas de la columna '{columna}':")
            print(f"Número de datos: {len(datos)}")
            print(f"Promedio: {sum(datos) / len(datos)}")
            print(f"Máximo: {max(datos)}")
            print(f"Mínimo: {min(datos)}")
            datos.sort()
            mediana = datos[len(datos) // 2] if len(datos) % 2 != 0 else \
                (datos[len(datos) // 2 - 1] + datos[len(datos) // 2]) / 2
            print(f"Mediana: {mediana}")
        else:
            print("Columna no encontrada o sin datos numéricos.")

    def graficar_columna(self, file_path, columna):
        datos = []
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    datos.append(float(row[columna]))
                except ValueError:
                    continue

        if datos:
            plt.plot(datos, label=columna)
            plt.title(f"Gráfica de la columna '{columna}'")
            plt.xlabel("Índice")
            plt.ylabel(columna)
            plt.legend()
            plt.show()
        else:
            print("Columna no encontrada o sin datos numéricos.")
            

def menu_principal():
    manager = FileManager()
    processor = CSVProcessor()
    while True:
        print("\nMenú Principal:")
        print("1. Seleccionar archivo .csv")
        print("2. Mostrar las primeras 15 filas del archivo .csv")
        print("3. Calcular estadísticas de una columna en el archivo .csv")
        print("4. Graficar una columna en el archivo .csv")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            manager.seleccionar_archivo()
        elif opcion == '2':
            if manager.file_path:
                processor.mostrar_15_filas(manager.file_path)
            else:
                print("Primero seleccione un archivo.")
        elif opcion == '3':
            if manager.file_path:
                columna = input("Ingrese el nombre de la columna: ")
                processor.calcular_estadisticas(
                    manager.file_path, columna)
            else:
                print("Primero seleccione un archivo.")
        elif opcion == '4':
            if manager.file_path:
                columna = input("Ingrese el nombre de la columna: ")
                processor.graficar_columna(
                    manager.file_path, columna)
            else:
                print("Primero seleccione un archivo.")
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu_principal()
