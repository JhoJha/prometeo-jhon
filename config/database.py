# database.py - ConexiÃ³n PostgreSQL/Neon
# config/database.py
# Conexión PostgreSQL/Neon específica PROMETEO-JHON

import os
import streamlit as st
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool
from contextlib import contextmanager
import logging
from typing import Generator

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Base para todos los modelos
Base = declarative_base()

class DatabaseManager:
    """
    Gestor de base de datos específico para PROMETEO-JHON
    Optimizado para PostgreSQL en Neon.tech
    """
    
    def __init__(self):
        self.engine = None
        self.SessionLocal = None
        self._connection_verified = False
    
    def get_database_url(self) -> str:
        """
        Obtiene la URL de conexión desde variables de entorno o secrets de Streamlit
        """
        try:
            # Intentar desde variables de entorno primero
            database_url = os.getenv("DATABASE_URL")
            if database_url:
                logger.info("🔍 Obteniendo URL desde variable de entorno")
                return database_url
        
         # URL directa mientras arreglamos secrets
            logger.info("🔍 Usando URL directa hardcodeada")
            return "postgresql://neondb_owner:npg_xjW3q1AeEZNM@ep-dawn-hall-acnwccbe-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"
            
        except Exception as e:
            logger.error(f"❌ Error obteniendo URL de base de datos: {e}")
            raise
    
    def initialize_connection(self) -> bool:
        """
        Inicializa la conexión a la base de datos
        """
        try:
            database_url = self.get_database_url()
            
            # Configurar engine específico para Neon
            self.engine = create_engine(
                database_url,
                # Configuración optimizada para Neon.tech
                poolclass=NullPool,  # Sin pool para Neon serverless
                pool_pre_ping=True,  # Verificar conexión antes de usar
                pool_recycle=300,    # Reciclar conexiones cada 5 min
                echo=False,          # Sin logging SQL (cambiar a True para debug)
                connect_args={
                    "sslmode": "require",  # SSL requerido para Neon
                    "application_name": "prometeo_jhon_streamlit",
                    "connect_timeout": 10
                }
            )
            
            # Crear sessionmaker
            self.SessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine
            )
            
            # Verificar conexión
            self._verify_connection()
            
            logger.info("✅ Conexión a base de datos inicializada correctamente")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error inicializando conexión: {e}")
            return False
    
    def _verify_connection(self) -> bool:
        """
        Verifica que la conexión funcione correctamente
        """
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text("SELECT 1 as test"))
                test_value = result.scalar()
                
                if test_value == 1:
                    self._connection_verified = True
                    logger.info("✅ Conexión verificada exitosamente")
                    return True
                else:
                    raise Exception("Query de prueba no retornó valor esperado")
                    
        except Exception as e:
            logger.error(f"❌ Error verificando conexión: {e}")
            self._connection_verified = False
            return False
    
    def get_session(self) -> Session:
        """
        Crea una nueva sesión de base de datos
        """
        if not self.SessionLocal:
            if not self.initialize_connection():
                raise Exception("No se pudo inicializar la conexión a la base de datos")
        
        return self.SessionLocal()
    
    def test_connection(self) -> dict:
        """
        Prueba la conexión y retorna información detallada
        """
        try:
            with self.get_session() as session:
                # Test básico
                result = session.execute(text("SELECT version() as version"))
                version = result.scalar()
                
                # Test específico tablas Jhon (si existen)
                tables_check = {}
                tabla_tests = [
                    "jhon_profile_master",
                    "bienestar_jhon", 
                    "estudio_jhon",
                    "gastos_jhon",
                    "fisico_jhon"
                ]
                
                for tabla in tabla_tests:
                    try:
                        session.execute(text(f"SELECT 1 FROM {tabla} LIMIT 1"))
                        tables_check[tabla] = "✅ Existe"
                    except:
                        tables_check[tabla] = "❌ No existe"
                
                return {
                    "status": "success",
                    "message": "Conexión exitosa",
                    "postgresql_version": version,
                    "connection_verified": self._connection_verified,
                    "tables_status": tables_check
                }
                
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error de conexión: {str(e)}",
                "postgresql_version": None,
                "connection_verified": False,
                "tables_status": {}
            }
    
    def close_connections(self):
        """
        Cierra todas las conexiones
        """
        if self.engine:
            self.engine.dispose()
            logger.info("🔐 Conexiones cerradas")

# Instancia global del gestor de base de datos
db_manager = DatabaseManager()

@contextmanager
def get_db() -> Generator[Session, None, None]:
    """
    Context manager para obtener sesión de base de datos
    Uso: 
        with get_db() as session:
            # usar session aquí
    """
    session = db_manager.get_session()
    try:
        yield session
    except Exception as e:
        session.rollback()
        logger.error(f"❌ Error en sesión de BD: {e}")
        raise
    finally:
        session.close()

def init_database() -> bool:
    """
    Inicializa la base de datos y crea las tablas
    """
    try:
        logger.info("🚀 Inicializando base de datos...")
        
        # Inicializar conexión
        if not db_manager.initialize_connection():
            return False
        
        # Importar todos los modelos para crear las tablas
        try:
            from utils.jhon_models import (
                JhonProfileMaster, BienestarJhon, EstudioJhon, 
                GastosJhon, FisicoJhon, ConfiguracionCursoJhon
            )
            logger.info("✅ Modelos importados correctamente")
        except ImportError as e:
            logger.warning(f"⚠️ Algunos modelos no disponibles aún: {e}")
        
        # Crear todas las tablas
        Base.metadata.create_all(bind=db_manager.engine)
        logger.info("✅ Tablas creadas/verificadas exitosamente")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Error inicializando base de datos: {e}")
        return False

def get_connection_status() -> dict:
    """
    Función helper para obtener estado de conexión (para UI)
    """
    return db_manager.test_connection()

# Función helper para Streamlit
@st.cache_resource
def get_cached_db_manager():
    """
    Retorna el gestor de BD cacheado para Streamlit
    """
    if not db_manager._connection_verified:
        db_manager.initialize_connection()
    return db_manager

# Configuración específica para PROMETEO-JHON
PROMETEO_DB_CONFIG = {
    "name": "PROMETEO-JHON Database",
    "target_user": "Jhon Villegas Verde",
    "purpose": "Life logging específico ciclo 2025-II",
    "tables_expected": [
        "jhon_profile_master",      # Configuración única Jhon
        "bienestar_jhon",           # Bienestar diario específico
        "estudio_jhon",             # Estudio meta 15.82
        "gastos_jhon",              # Gastos categorizados específicos
        "fisico_jhon",              # Transformación 88kg→70kg
        "configuracion_curso_jhon", # Cursos hardcodeados
        "correlaciones_jhon",       # Correlaciones automáticas
        "alertas_jhon"              # Sistema alertas específico
    ],
    "backup_frequency": "daily",
    "timezone": "America/Lima"
}

if __name__ == "__main__":
    # Test de conexión standalone
    print("🧪 Probando conexión a base de datos...")
    
    status = get_connection_status()
    print(f"Estado: {status['status']}")
    print(f"Mensaje: {status['message']}")
    
    if status['status'] == 'success':
        print(f"PostgreSQL: {status['postgresql_version']}")
        print("\nEstado de tablas:")
        for tabla, estado in status['tables_status'].items():
            print(f"  {tabla}: {estado}")
    
    print("\n✅ Test completado")