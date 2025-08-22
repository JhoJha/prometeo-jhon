# scripts/debug_database.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.database import get_db
from sqlalchemy import text

def verificar_tablas():
    """Verifica qué tablas existen en la BD"""
    print("🔍 Verificando estructura de base de datos...")
    
    try:
        with get_db() as session:
            # Listar todas las tablas
            result = session.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """))
            
            tablas = [row[0] for row in result.fetchall()]
            print(f"📋 Tablas encontradas: {tablas}")
            
            # Verificar específicamente la tabla jhon_profile_master
            if 'jhon_profile_master' in tablas:
                print("\n✅ Tabla jhon_profile_master existe")
                
                # Obtener estructura de columnas
                result = session.execute(text("""
                    SELECT column_name, data_type, is_nullable 
                    FROM information_schema.columns 
                    WHERE table_name = 'jhon_profile_master'
                    ORDER BY ordinal_position
                """))
                
                print("📊 Columnas en jhon_profile_master:")
                for row in result.fetchall():
                    print(f"   {row[0]} ({row[1]}) - Nullable: {row[2]}")
                    
            else:
                print("❌ Tabla jhon_profile_master NO existe")
                print("💡 Necesitas ejecutar init_tables.py primero")
                
    except Exception as e:
        print(f"❌ Error verificando BD: {e}")

if __name__ == "__main__":
    verificar_tablas()