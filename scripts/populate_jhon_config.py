# scripts/populate_jhon_config.py
# Script para insertar el perfil master de Jhon en la base de datos

import sys
import os
from datetime import datetime

# Agregar el directorio raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.database import get_db
from utils.jhon_models import JhonProfileMaster
from config.jhon_master_config import JHON_PROFILE_MASTER

def insertar_perfil_jhon():
    """
    Inserta el perfil único de Jhon en la base de datos
    """
    print("🚀 Insertando perfil master de Jhon...")
    
    try:
        with get_db() as session:
            # Verificar si ya existe un perfil
            perfil_existente = session.query(JhonProfileMaster).first()
            
            if perfil_existente:
                print("⚠️ Ya existe un perfil en la base de datos:")
                print(f"   Matrícula: {perfil_existente.matricula}")
                print(f"   Promedio actual: {perfil_existente.promedio_actual}")
                print(f"   Peso inicial: {perfil_existente.peso_inicial}kg")
                
                respuesta = input("\n¿Deseas actualizarlo? (s/n): ").lower().strip()
                if respuesta == 's':
                    actualizar_perfil_existente(session, perfil_existente)
                else:
                    print("❌ Operación cancelada")
                return
            
            # Extraer datos de la configuración (ESTRUCTURA CORREGIDA)
            personal = JHON_PROFILE_MASTER["personal"]
            academico = JHON_PROFILE_MASTER["academico"] 
            finanzas = JHON_PROFILE_MASTER["finanzas"]
            
            # Crear nuevo perfil con estructura correcta
            nuevo_perfil = JhonProfileMaster(
                # Datos académicos - CORREGIDO
                matricula=personal["matricula"],  # ← Está en personal, no académico
                universidad=academico["universidad"],
                carrera=academico["carrera"],
                facultad=academico["facultad"],
                ciclo_actual=academico["ciclo_actual"],
                creditos_acumulados=academico["creditos_acumulados"],
                promedio_actual=academico["promedio_actual"],
                meta_promedio_final=academico["meta_promedio_final"],
                meta_ciclo_2025_2=academico["meta_ciclo_2025_2"],
                ranking_facultad=academico["ranking_facultad"],
                ranking_carrera=academico["ranking_carrera"],
                
                # Datos físicos
                peso_inicial=personal["peso_inicial"],
                peso_meta=personal["peso_meta_final"],
                altura=personal["altura"],
                imc_inicial=personal["peso_inicial"] / (personal["altura"] ** 2),
                imc_meta=personal["peso_meta_final"] / (personal["altura"] ** 2),
                
                # Datos financieros
                ingreso_mensual_base=finanzas["ingresos"]["total_base_garantizado"],
                gastos_fijos_agosto_octubre=414.0,
                gastos_fijos_noviembre_adelante=424.0,
                presupuesto_variable_agosto_octubre=536.0,
                presupuesto_variable_noviembre_adelante=526.0,
                
                # Dispositivos
                dispositivo_principal=personal["telefono_principal"],
                sistema_operativo=personal["sistema_operativo"],
                plan_datos="Ilimitado",
                
                # Timestamps
                fecha_inicio_sistema=datetime.utcnow(),
                ciclo_academico_actual="2025-II"
            )
            
            # Insertar en la base de datos
            session.add(nuevo_perfil)
            session.commit()
            
            print("✅ Perfil de Jhon insertado exitosamente!")
            print("\n📊 Datos insertados:")
            print(f"   👤 Matrícula: {nuevo_perfil.matricula}")
            print(f"   🎯 Meta académica: {nuevo_perfil.meta_ciclo_2025_2}")
            print(f"   📚 Créditos acumulados: {nuevo_perfil.creditos_acumulados}")
            print(f"   📈 Promedio actual: {nuevo_perfil.promedio_actual}")
            print(f"   💪 Peso inicial: {nuevo_perfil.peso_inicial}kg → {nuevo_perfil.peso_meta}kg")
            print(f"   💰 Ingreso base: S/{nuevo_perfil.ingreso_mensual_base}")
            print(f"   📱 Dispositivo: {nuevo_perfil.dispositivo_principal}")
            
    except Exception as e:
        print(f"❌ Error insertando perfil: {e}")
        import traceback
        traceback.print_exc()

def actualizar_perfil_existente(session, perfil_existente):
    """Actualiza el perfil existente"""
    print("🔄 Actualizando perfil existente...")
    
    academico = JHON_PROFILE_MASTER["academico"]
    personal = JHON_PROFILE_MASTER["personal"]
    
    perfil_existente.creditos_acumulados = academico["creditos_acumulados"]
    perfil_existente.promedio_actual = academico["promedio_actual"]
    perfil_existente.meta_ciclo_2025_2 = academico["meta_ciclo_2025_2"]
    perfil_existente.peso_inicial = personal["peso_inicial"]
    perfil_existente.peso_meta = personal["peso_meta_final"]
    perfil_existente.ultima_actualizacion = datetime.utcnow()
    
    session.commit()
    print("✅ Perfil actualizado correctamente!")

def verificar_perfil():
    """Verifica que el perfil esté correctamente insertado"""
    print("\n🔍 Verificando perfil en base de datos...")
    
    try:
        with get_db() as session:
            perfil = session.query(JhonProfileMaster).first()
            
            if perfil:
                print("✅ Perfil encontrado:")
                print(f"   ID: {perfil.id}")
                print(f"   Matrícula: {perfil.matricula}")
                print(f"   Meta 15.82: {perfil.meta_ciclo_2025_2}")
                print(f"   Créditos: {perfil.creditos_acumulados}")
                print(f"   Peso inicial: {perfil.peso_inicial}kg")
                return True
            else:
                print("❌ No se encontró perfil en la base de datos")
                return False
                
    except Exception as e:
        print(f"❌ Error verificando perfil: {e}")
        return False

def main():
    """Función principal del script"""
    print("=" * 60)
    print("🏗️  PROMETEO-JHON: Configuración Inicial del Perfil")
    print("=" * 60)
    
    # Insertar perfil
    insertar_perfil_jhon()
    
    # Verificar que se insertó correctamente
    if verificar_perfil():
        print("\n🎉 Configuración inicial completada!")
        print("📋 Próximos pasos:")
        print("   1. Completar formularios de registro")
        print("   2. Implementar función calcular_progreso_meta_1582()")
        print("   3. Crear dashboard principal")
    else:
        print("\n⚠️ Hubo problemas con la configuración")

if __name__ == "__main__":
    main()