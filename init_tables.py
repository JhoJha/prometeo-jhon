# init_tables.py - Script para inicializar las tablas en la base de datos

from config.database import init_database

def main():
    print("Inicializando tablas en la base de datos...")
    if init_database():
        print("✅ Tablas creadas/verificadas exitosamente.")
    else:
        print("❌ Hubo un error al inicializar las tablas.")

if __name__ == "__main__":
    main()
