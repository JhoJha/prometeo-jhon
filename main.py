import sys
from config.database import DatabaseManager  # Importa la clase de gestión de base de datos

def main():
    db = DatabaseManager()  # Crea la instancia de DatabaseManager
    print("Probando conexión a la base de datos...")

    if db.initialize_connection():
        print("✅ Conexión inicializada correctamente!")
        try:
            test_result = db.test_connection()
            print("Resultado del test de conexión:")
            for key, value in test_result.items():
                print(f" - {key}: {value}")
        except Exception as e:
            print(f"❌ Error durante el test: {e}")
    else:
        print("❌ Error inicializando la conexión a la base de datos.")
        sys.exit(1)

if __name__ == "__main__":
    main()