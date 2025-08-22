# migrate_jhon_data.py - MigraciÃ³n datos
# scripts/test_connection.py
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_secrets():
    """Test simple de lectura de secrets"""
    print("🔍 Probando lectura de secrets...")
    
    try:
        import streamlit as st
        
        # Intentar leer secrets
        if hasattr(st, 'secrets'):
            print("✅ st.secrets disponible")
            
            if 'database' in st.secrets:
                print("✅ Sección [database] encontrada")
                
                if 'DATABASE_URL' in st.secrets['database']:
                    url = st.secrets['database']['DATABASE_URL']
                    print(f"✅ DATABASE_URL encontrada: {url[:30]}...")
                else:
                    print("❌ DATABASE_URL no encontrada")
            else:
                print("❌ Sección [database] no encontrada")
        else:
            print("❌ st.secrets no disponible")
            
    except Exception as e:
        print(f"❌ Error leyendo secrets: {e}")

def test_direct_connection():
    """Test directo con la URL"""
    print("\n🔗 Probando conexión directa...")
    
    try:
        from sqlalchemy import create_engine, text
        
        # URL directa (reemplaza con la tuya)
        url = "postgresql://neondb_owner:npg_xjW3q1AeEZNM@ep-dawn-hall-acnwccbe-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"
        
        engine = create_engine(url)
        
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1 as test"))
            test_value = result.scalar()
            
            if test_value == 1:
                print("✅ Conexión directa exitosa!")
                return True
            else:
                print("❌ Conexión falló")
                return False
                
    except Exception as e:
        print(f"❌ Error conexión directa: {e}")
        return False

if __name__ == "__main__":
    test_secrets()
    test_direct_connection()