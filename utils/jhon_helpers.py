# utils/jhon_helpers.py
# PROMETEO-JHON: Funciones Helper Completas - VERSIÓN CORREGIDA
# Todas las funciones necesarias para que el sistema funcione al 100%

import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta, time
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, func, desc, text
from typing import Dict, List, Tuple, Optional, Any, Union
import json
import streamlit as st

# Imports de modelos y configuración
from config.database import get_db
from utils.jhon_models import (
    JhonProfileMaster, BienestarJhon, EstudioJhon, GastosJhon, FisicoJhon,
    ConfiguracionCursoJhon, CorrelacionJhon, AlertaJhon,
    UbicacionJhonEnum, CursoJhonEnum, CategoriaGastoJhonEnum, TriggerImpulsivoJhonEnum
)

# ============================================================================
# FUNCIONES CORE CRÍTICAS - META 15.82
# ============================================================================

def calcular_progreso_meta_1582() -> Dict[str, Any]:
    """
    FUNCIÓN CRÍTICA: Calcula progreso exacto hacia meta 15.82
    
    Returns:
        Dict con progreso, riesgo, y métricas detalladas
    """
    try:
        with get_db() as session:
            # Obtener perfil único de Jhon
            perfil = session.query(JhonProfileMaster).first()
            if not perfil:
                return {
                    "error": "Perfil de Jhon no encontrado en BD",
                    "status": "error"
                }
            
            # Datos base confirmados del perfil
            creditos_acumulados = perfil.creditos_acumulados  # 46
            promedio_actual = perfil.promedio_actual  # 13.23
            creditos_ciclo_2025_2 = 20  # 7 cursos hardcodeados
            meta_promedio_final = perfil.meta_promedio_final  # 14.0
            meta_ciclo = perfil.meta_ciclo_2025_2  # 15.82
            
            # Obtener notas actuales del ciclo (si las hay)
            notas_ciclo = obtener_notas_ciclo_actual(session)
            
            # Si no hay notas aún, usar datos base
            if not notas_ciclo:
                creditos_con_nota = 0
                promedio_ciclo_actual = 0.0
                creditos_pendientes = creditos_ciclo_2025_2
                nota_necesaria_restante = meta_ciclo
            else:
                # Calcular con notas existentes
                creditos_con_nota = sum(nota["creditos"] for nota in notas_ciclo)
                puntos_obtenidos = sum(nota["nota"] * nota["creditos"] for nota in notas_ciclo)
                promedio_ciclo_actual = puntos_obtenidos / creditos_con_nota if creditos_con_nota > 0 else 0
                
                creditos_pendientes = creditos_ciclo_2025_2 - creditos_con_nota
                if creditos_pendientes > 0:
                    puntos_necesarios_totales = meta_ciclo * creditos_ciclo_2025_2
                    puntos_necesarios_restantes = puntos_necesarios_totales - puntos_obtenidos
                    nota_necesaria_restante = puntos_necesarios_restantes / creditos_pendientes
                else:
                    nota_necesaria_restante = 0
            
            # Calcular nivel de riesgo específico
            if nota_necesaria_restante > 18.0:
                riesgo = "CRÍTICO"
                mensaje_riesgo = "Necesitas notas casi perfectas (>18)"
                color_riesgo = "🔴"
            elif nota_necesaria_restante > 16.5:
                riesgo = "ALTO"
                mensaje_riesgo = "Margen de error muy pequeño"
                color_riesgo = "🟠"
            elif nota_necesaria_restante > 15.0:
                riesgo = "MEDIO"
                mensaje_riesgo = "Factible con esfuerzo sostenido"
                color_riesgo = "🟡"
            elif nota_necesaria_restante > 13.0:
                riesgo = "BAJO"
                mensaje_riesgo = "Meta alcanzable con trabajo normal"
                color_riesgo = "🟢"
            else:
                riesgo = "SEGURO"
                mensaje_riesgo = "Meta prácticamente asegurada"
                color_riesgo = "✅"
            
            # Calcular días restantes del ciclo
            dias_restantes = calcular_dias_restantes_ciclo()
            
            # Calcular impacto en promedio general
            if promedio_ciclo_actual > 0:
                puntos_totales_futuros = (creditos_acumulados * promedio_actual) + (creditos_ciclo_2025_2 * promedio_ciclo_actual)
                promedio_general_proyectado = puntos_totales_futuros / (creditos_acumulados + creditos_ciclo_2025_2)
            else:
                # Proyección con meta 15.82
                puntos_totales_futuros = (creditos_acumulados * promedio_actual) + (creditos_ciclo_2025_2 * meta_ciclo)
                promedio_general_proyectado = puntos_totales_futuros / (creditos_acumulados + creditos_ciclo_2025_2)
            
            # Obtener evaluaciones próximas críticas
            evaluaciones_proximas = obtener_evaluaciones_proximas(session, dias_adelante=14)
            
            return {
                "status": "success",
                
                # Progreso principal
                "progreso_porcentaje": round((creditos_con_nota / creditos_ciclo_2025_2) * 100, 1),
                "creditos_evaluados": creditos_con_nota,
                "creditos_pendientes": creditos_pendientes,
                "creditos_totales_ciclo": creditos_ciclo_2025_2,
                
                # Promedios y metas
                "promedio_ciclo_actual": round(promedio_ciclo_actual, 2),
                "promedio_necesario_final": meta_ciclo,
                "nota_necesaria_restante": round(nota_necesaria_restante, 2),
                "promedio_general_actual": promedio_actual,
                "promedio_general_proyectado": round(promedio_general_proyectado, 2),
                "meta_promedio_final": meta_promedio_final,
                
                # Análisis de riesgo
                "riesgo_nivel": riesgo,
                "mensaje_riesgo": mensaje_riesgo,
                "color_riesgo": color_riesgo,
                "factible": nota_necesaria_restante <= 20.0,
                
                # Contexto temporal
                "dias_restantes_ciclo": dias_restantes,
                "semanas_restantes": round(dias_restantes / 7, 1),
                "fecha_fin_ciclo": date(2025, 12, 20).isoformat(),
                
                # Evaluaciones críticas
                "evaluaciones_proximas": evaluaciones_proximas[:3],  # Máximo 3
                "evaluaciones_criticas_pendientes": len([e for e in evaluaciones_proximas if e.get("critico", False)]),
                
                # Métricas adicionales
                "notas_actuales_ciclo": notas_ciclo,
                "cursos_con_nota": len(notas_ciclo) if notas_ciclo else 0,
                "cursos_sin_nota": 7 - (len(notas_ciclo) if notas_ciclo else 0),
                
                # Timestamps
                "fecha_calculo": datetime.now().isoformat(),
                "ultima_actualizacion": perfil.ultima_actualizacion.isoformat() if perfil.ultima_actualizacion else None
            }
            
    except Exception as e:
        return {
            "error": f"Error calculando progreso meta 15.82: {str(e)}",
            "status": "error"
        }

def obtener_notas_ciclo_actual(session: Session) -> List[Dict]:
    """
    Obtiene notas actuales del ciclo 2025-2 desde registros de estudio
    (Por ahora mockup, se actualizará cuando haya notas reales)
    """
    try:
        # TODO: Implementar cuando tengamos tabla de notas
        # Por ahora retorna lista vacía
        return []
        
    except Exception as e:
        print(f"Error obteniendo notas: {e}")
        return []

def calcular_dias_restantes_ciclo() -> int:
    """
    Calcula días restantes hasta fin del ciclo académico
    """
    try:
        fecha_fin_ciclo = date(2025, 12, 20)  # Hardcodeado del calendario
        hoy = date.today()
        dias_restantes = (fecha_fin_ciclo - hoy).days
        return max(0, dias_restantes)  # No puede ser negativo
        
    except Exception as e:
        print(f"Error calculando días restantes: {e}")
        return 0

def obtener_evaluaciones_proximas(session: Session, dias_adelante: int = 14) -> List[Dict]:
    """
    Obtiene evaluaciones próximas desde configuración hardcodeada
    """
    try:
        from config.jhon_master_config import CURSOS_CICLO_2025_2_COMPLETO
        
        evaluaciones_proximas = []
        fecha_limite = date.today() + timedelta(days=dias_adelante)
        hoy = date.today()
        
        for curso_codigo, curso_data in CURSOS_CICLO_2025_2_COMPLETO.items():
            if "calendario_evaluaciones_exacto" in curso_data:
                for eval_nombre, eval_data in curso_data["calendario_evaluaciones_exacto"].items():
                    fecha_eval = eval_data.get("fecha")
                    if fecha_eval and hoy <= fecha_eval <= fecha_limite:
                        evaluaciones_proximas.append({
                            "curso_codigo": curso_codigo,
                            "curso_nombre": curso_data["datos_basicos"]["nombre"],
                            "evaluacion": eval_nombre,
                            "fecha": fecha_eval.isoformat(),
                            "dias_restantes": (fecha_eval - hoy).days,
                            "critico": eval_data.get("critico", False),
                            "medicacion_recomendada": eval_data.get("medicacion_recomendada", False),
                            "tema": eval_data.get("tema", ""),
                            "preparacion_dias": eval_data.get("preparacion_dias", 3),
                            "dificultad": curso_data["datos_basicos"].get("dificultad_jhon", 3)
                        })
        
        # Ordenar por fecha
        evaluaciones_proximas.sort(key=lambda x: x["fecha"])
        
        return evaluaciones_proximas
        
    except Exception as e:
        print(f"Error obteniendo evaluaciones próximas: {e}")
        return []

# ============================================================================
# FUNCIONES BIENESTAR ESPECÍFICAS
# ============================================================================

def obtener_bienestar_hoy_jhon(session: Session) -> Optional[BienestarJhon]:
    """
    Obtiene registro de bienestar de hoy (si existe)
    """
    try:
        hoy = date.today()
        return session.query(BienestarJhon).filter(
            BienestarJhon.fecha == hoy
        ).first()
        
    except Exception as e:
        print(f"Error obteniendo bienestar hoy: {e}")
        return None

def extraer_defaults_bienestar_jhon(registro: Optional[BienestarJhon]) -> Dict:
    """
    Extrae valores por defecto del último registro de bienestar
    """
    if not registro:
        return {
            "energia_nivel": 3,
            "animo_nivel": 3,
            "sueno_horas": 7.0,
            "ubicacion_principal_dia": UbicacionJhonEnum.SA_CUARTO.value,
            "ubicacion_registro": UbicacionJhonEnum.SA_CUARTO.value,
            "concentracion_sin_medicacion": 3,
            "tomo_metilfenidato": False,
            "presion_matematicas_hoy": 3,
            "presion_redaccion_ortografia": 3,
            "presion_tiempo_ciclo": 3,
            "confianza_meta_15_82_hoy": 3,
            "ansiedad_evaluaciones_proximas": 3,
            "tiempo_lol_minutos": 0,
            "tiempo_pornografia_minutos": 0,
            "tiempo_estudio_productivo_total": 0,
            "tiempo_youtube_educativo": 0,
            "tiempo_redes_sociales": 0
        }
    
    return {
        "energia_nivel": registro.energia_nivel,
        "animo_nivel": registro.animo_nivel,
        "sueno_horas": registro.sueno_horas,
        "ubicacion_principal_dia": registro.ubicacion_principal_dia,
        "ubicacion_registro": registro.ubicacion_registro,
        "concentracion_sin_medicacion": registro.concentracion_sin_medicacion,
        "tomo_metilfenidato": registro.tomo_metilfenidato,
        "if_medicacion_hora": registro.if_medicacion_hora,
        "if_medicacion_motivo": registro.if_medicacion_motivo,
        "if_medicacion_efecto_percibido": registro.if_medicacion_efecto_percibido,
        "concentracion_con_medicacion": registro.concentracion_con_medicacion,
        "presion_matematicas_hoy": registro.presion_matematicas_hoy,
        "presion_redaccion_ortografia": registro.presion_redaccion_ortografia,
        "presion_tiempo_ciclo": registro.presion_tiempo_ciclo,
        "confianza_meta_15_82_hoy": registro.confianza_meta_15_82_hoy,
        "ansiedad_evaluaciones_proximas": registro.ansiedad_evaluaciones_proximas,
        "tiempo_lol_minutos": registro.tiempo_lol_minutos,
        "tiempo_pornografia_minutos": registro.tiempo_pornografia_minutos,
        "tiempo_estudio_productivo_total": registro.tiempo_estudio_productivo_total,
        "tiempo_youtube_educativo": registro.tiempo_youtube_educativo,
        "tiempo_redes_sociales": registro.tiempo_redes_sociales,
        "principal_logro_hoy": registro.principal_logro_hoy,
        "principal_frustracion_hoy": registro.principal_frustracion_hoy,
        "nivel_satisfaccion_dia": registro.nivel_satisfaccion_dia,
        "plan_manana": registro.plan_manana,
        # Campos condicionales por ubicación
        "if_sa_soledad_nivel": registro.if_sa_soledad_nivel,
        "if_sa_extrano_familia": registro.if_sa_extrano_familia,
        "if_sa_productividad_cuarto": registro.if_sa_productividad_cuarto,
        "if_cb_apoyo_familia_hoy": registro.if_cb_apoyo_familia_hoy,
        "if_cb_distraccion_familia": registro.if_cb_distraccion_familia,
        "if_cb_ambiente_estudio": registro.if_cb_ambiente_estudio,
        "if_campus_productividad": registro.if_campus_productividad,
        "if_campus_concentracion_aulas": registro.if_campus_concentracion_aulas,
        "if_trabajo_chacra_hoy": registro.if_trabajo_chacra_hoy,
        "if_chacra_horas_trabajadas": registro.if_chacra_horas_trabajadas,
        "if_chacra_cansancio_fisico": registro.if_chacra_cansancio_fisico,
        "if_chacra_impacto_lunes_predicho": registro.if_chacra_impacto_lunes_predicho,
        "if_chacra_satisfaccion": registro.if_chacra_satisfaccion,
        "if_viaje_cb_sa_hoy": registro.if_viaje_cb_sa_hoy,
        "if_viaje_sa_cb_hoy": registro.if_viaje_sa_cb_hoy,
        "if_viaje_cansancio": registro.if_viaje_cansancio,
        "if_viaje_productivo_transporte": registro.if_viaje_productivo_transporte
    }

def guardar_o_actualizar_bienestar_jhon(datos: Dict) -> bool:
    """
    Guarda o actualiza registro de bienestar de Jhon
    """
    try:
        with get_db() as session:
            hoy = date.today()
            
            # Buscar registro existente
            registro_existente = session.query(BienestarJhon).filter(
                BienestarJhon.fecha == hoy
            ).first()
            
            if registro_existente:
                # Actualizar registro existente
                for campo, valor in datos.items():
                    if hasattr(registro_existente, campo):
                        setattr(registro_existente, campo, valor)
            else:
                # Crear nuevo registro
                datos["fecha"] = hoy
                nuevo_registro = BienestarJhon(**datos)
                session.add(nuevo_registro)
            
            session.commit()
            return True
            
    except Exception as e:
        print(f"Error guardando bienestar: {e}")
        return False

# ============================================================================
# FUNCIONES ESTUDIO ESPECÍFICAS
# ============================================================================

def sugerir_curso_por_horario() -> Optional[str]:
    """
    Sugiere curso a estudiar según horario actual y configuración
    """
    try:
        from config.jhon_master_config import HORARIO_JHON_EXACTO
        
        now = datetime.now()
        dia_semana = now.strftime("%A").lower()
        hora_actual = now.time()
        
        # Traducir días al español
        dias_map = {
            "monday": "lunes",
            "tuesday": "martes", 
            "wednesday": "miercoles",
            "thursday": "jueves",
            "friday": "viernes",
            "saturday": "sabado",
            "sunday": "domingo"
        }
        
        dia_es = dias_map.get(dia_semana, dia_semana)
        
        if dia_es in HORARIO_JHON_EXACTO:
            horario_dia = HORARIO_JHON_EXACTO[dia_es]
            
            # Buscar curso en horario actual (±1 hora)
            if isinstance(horario_dia, list):
                for bloque in horario_dia:
                    if isinstance(bloque, dict) and "curso" in bloque:
                        # Extraer hora inicio del bloque
                        hora_inicio = bloque.get("hora", "").split("-")[0]
                        try:
                            hora_bloque = datetime.strptime(hora_inicio, "%H:%M").time()
                            # Si estamos cerca del horario del curso
                            if abs((datetime.combine(date.today(), hora_actual) - 
                                   datetime.combine(date.today(), hora_bloque)).seconds) < 3600:
                                return bloque["curso"]
                        except:
                            continue
        
        # Sugerencias por día si no hay horario específico
        sugerencias_dia = {
            "lunes": "Álgebra Matricial",
            "martes": "Matemáticas Discretas", 
            "miercoles": "Matemáticas (día libre - aprovecha)",
            "jueves": "Álgebra Matricial",
            "viernes": "Repaso general",
            "sabado": "Proyectos grupales",
            "domingo": "Planificación semanal"
        }
        
        return sugerencias_dia.get(dia_es)
        
    except Exception as e:
        print(f"Error sugiriendo curso: {e}")
        return None

def guardar_sesion_estudio_jhon(datos: Dict) -> bool:
    """
    Guarda sesión de estudio específica de Jhon
    """
    try:
        with get_db() as session:
            # Crear nuevo registro de estudio
            nuevo_estudio = EstudioJhon(**datos)
            session.add(nuevo_estudio)
            session.commit()
            return True
            
    except Exception as e:
        print(f"Error guardando sesión estudio: {e}")
        return False

def obtener_sesiones_estudio_recientes(session: Session, dias: int = 7) -> List[EstudioJhon]:
    """
    Obtiene sesiones de estudio recientes
    """
    try:
        fecha_inicio = date.today() - timedelta(days=dias)
        return session.query(EstudioJhon).filter(
            EstudioJhon.fecha >= fecha_inicio
        ).order_by(EstudioJhon.fecha.desc()).all()
        
    except Exception as e:
        print(f"Error obteniendo sesiones recientes: {e}")
        return []

def calcular_horas_estudio_semana(session: Session) -> Dict[str, Any]:
    """
    Calcula horas de estudio de la semana actual
    """
    try:
        # Calcular inicio de semana (lunes)
        hoy = date.today()
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        
        sesiones_semana = session.query(EstudioJhon).filter(
            EstudioJhon.fecha >= inicio_semana
        ).all()
        
        if not sesiones_semana:
            return {
                "total_minutos": 0,
                "total_horas": 0.0,
                "sesiones": 0,
                "promedio_concentracion": 0.0,
                "contribucion_meta_promedio": 0.0,
                "sesiones_matematicas": 0
            }
        
        total_minutos = sum(s.duracion_minutos for s in sesiones_semana)
        concentracion_promedio = np.mean([s.concentracion_durante for s in sesiones_semana])
        contribucion_promedio = np.mean([s.contribucion_meta_1582 for s in sesiones_semana])
        
        return {
            "total_minutos": total_minutos,
            "total_horas": round(total_minutos / 60, 1),
            "sesiones": len(sesiones_semana),
            "promedio_concentracion": round(concentracion_promedio, 2),
            "contribucion_meta_promedio": round(contribucion_promedio, 2),
            "sesiones_matematicas": len([s for s in sesiones_semana 
                                       if 'algebra' in s.curso or 'matematicas' in s.curso])
        }
        
    except Exception as e:
        print(f"Error calculando horas estudio semana: {e}")
        return {
            "total_minutos": 0,
            "total_horas": 0.0,
            "sesiones": 0,
            "promedio_concentracion": 0.0,
            "contribucion_meta_promedio": 0.0,
            "sesiones_matematicas": 0
        }

# ============================================================================
# FUNCIONES GASTOS ESPECÍFICAS
# ============================================================================

def calcular_presupuesto_restante_mes() -> Dict[str, Any]:
    """
    Calcula presupuesto restante del mes actual
    """
    try:
        with get_db() as session:
            hoy = date.today()
            inicio_mes = hoy.replace(day=1)
            
            # Presupuesto según mes (hardcodeado de configuración)
            presupuesto_total = 526 if hoy.month >= 11 else 536
            
            # Obtener gastos del mes que afectan presupuesto variable
            gastos_mes = session.query(func.sum(GastosJhon.monto)).filter(
                GastosJhon.fecha >= inicio_mes,
                GastosJhon.fecha <= hoy,
                GastosJhon.afecta_presupuesto_variable == True
            ).scalar() or 0.0
            
            # Calcular métricas
            restante = presupuesto_total - gastos_mes
            porcentaje_gastado = (gastos_mes / presupuesto_total) * 100
            dias_transcurridos = (hoy - inicio_mes).days + 1
            
            # Proyección fin de mes
            if hoy.month == 12:
                ultimo_dia_mes = date(hoy.year, 12, 31)
            else:
                ultimo_dia_mes = date(hoy.year, hoy.month + 1, 1) - timedelta(days=1)
            
            dias_totales_mes = (ultimo_dia_mes - inicio_mes).days + 1
            gasto_diario_promedio = gastos_mes / dias_transcurridos if dias_transcurridos > 0 else 0
            proyeccion_fin_mes = gasto_diario_promedio * dias_totales_mes
            
            # Evaluar estado
            if porcentaje_gastado >= 90:
                estado = "CRÍTICO"
                color = "🔴"
            elif porcentaje_gastado >= 75:
                estado = "ALTO"
                color = "🟠"
            elif porcentaje_gastado >= 50:
                estado = "MEDIO"
                color = "🟡"
            else:
                estado = "BUENO"
                color = "🟢"
            
            return {
                "presupuesto_total": presupuesto_total,
                "gastado": round(gastos_mes, 2),
                "restante": round(restante, 2),
                "porcentaje_usado": round(porcentaje_gastado, 1),
                "porcentaje_restante": round(100 - porcentaje_gastado, 1),
                "estado": estado,
                "color": color,
                "dias_transcurridos": dias_transcurridos,
                "dias_restantes_mes": dias_totales_mes - dias_transcurridos,
                "gasto_diario_promedio": round(gasto_diario_promedio, 2),
                "proyeccion_fin_mes": round(proyeccion_fin_mes, 2),
                "riesgo_exceso": proyeccion_fin_mes > presupuesto_total
            }
            
    except Exception as e:
        print(f"Error calculando presupuesto: {e}")
        return {
            "presupuesto_total": 526,
            "gastado": 0.0,
            "restante": 526.0,
            "porcentaje_usado": 0.0,
            "estado": "BUENO",
            "color": "🟢",
            "error": str(e)
        }

def detectar_duplicados_gastos_jhon(session: Session, monto: float, 
                                   categoria: str, 
                                   fecha: date, tolerancia_horas: int = 2) -> List[GastosJhon]:
    """
    Detecta posibles gastos duplicados
    """
    try:
        fecha_inicio = datetime.combine(fecha, time.min) - timedelta(hours=tolerancia_horas)
        fecha_fin = datetime.combine(fecha, time.min) + timedelta(hours=tolerancia_horas)
        
        duplicados = session.query(GastosJhon).filter(
            GastosJhon.fecha >= fecha_inicio.date(),
            GastosJhon.fecha <= fecha_fin.date(),
            GastosJhon.categoria == categoria,
            func.abs(GastosJhon.monto - monto) < 0.5  # Tolerancia S/0.50
        ).all()
        
        return duplicados
        
    except Exception as e:
        print(f"Error detectando duplicados: {e}")
        return []

def analizar_gastos_impulsivos_semana(session: Session) -> Dict[str, Any]:
    """
    Analiza gastos impulsivos de la semana actual
    """
    try:
        hoy = date.today()
        inicio_semana = hoy - timedelta(days=hoy.weekday())
        
        gastos_impulsivos = session.query(GastosJhon).filter(
            GastosJhon.fecha >= inicio_semana,
            GastosJhon.es_gasto_impulsivo == True
        ).all()
        
        if not gastos_impulsivos:
            return {
                "total_gastos_impulsivos": 0.0,
                "cantidad": 0,
                "triggers_principales": [],
                "promedio_arrepentimiento": 0.0,
                "nivel_control": "BUENO"
            }
        
        total_monto = sum(g.monto for g in gastos_impulsivos)
        
        # Analizar triggers
        triggers = {}
        arrepentimientos = []
        
        for gasto in gastos_impulsivos:
            if gasto.if_impulsivo_trigger:
                trigger = gasto.if_impulsivo_trigger
                triggers[trigger] = triggers.get(trigger, 0) + 1
            
            if gasto.if_impulsivo_arrepentimiento_nivel:
                arrepentimientos.append(gasto.if_impulsivo_arrepentimiento_nivel)
        
        triggers_ordenados = sorted(triggers.items(), key=lambda x: x[1], reverse=True)
        promedio_arrepentimiento = np.mean(arrepentimientos) if arrepentimientos else 0
        
        # Continuación desde analizar_gastos_impulsivos_semana
        return {
            "total_gastos_impulsivos": round(total_monto, 2),
            "cantidad": len(gastos_impulsivos),
            "triggers_principales": triggers_ordenados[:3],
            "promedio_arrepentimiento": round(promedio_arrepentimiento, 2),
            "nivel_control": "BUENO" if promedio_arrepentimiento < 3 else "REGULAR" if promedio_arrepentimiento < 4 else "MALO"
        }
        
    except Exception as e:
        print(f"Error analizando gastos impulsivos: {e}")
        return {
            "total_gastos_impulsivos": 0.0,
            "cantidad": 0,
            "triggers_principales": [],
            "promedio_arrepentimiento": 0.0,
            "nivel_control": "BUENO"
        }

def guardar_gasto_jhon(datos: Dict) -> bool:
    """
    Guarda nuevo gasto específico de Jhon
    """
    try:
        with get_db() as session:
            nuevo_gasto = GastosJhon(**datos)
            session.add(nuevo_gasto)
            session.commit()
            return True
            
    except Exception as e:
        print(f"Error guardando gasto: {e}")
        return False

# ============================================================================
# FUNCIONES FÍSICO ESPECÍFICAS
# ============================================================================

def calcular_progreso_fisico_jhon() -> Dict[str, Any]:
    """
    Calcula progreso detallado transformación física 88kg → 70kg
    """
    try:
        with get_db() as session:
            # Obtener perfil para metas
            perfil = session.query(JhonProfileMaster).first()
            if not perfil:
                return {"error": "Perfil no encontrado"}
            
            peso_inicial = perfil.peso_inicial  # 88.0
            peso_meta = perfil.peso_meta  # 70.0
            perdida_objetivo_total = peso_inicial - peso_meta  # 18.0 kg
            
            # Último peso registrado
            ultimo_registro = session.query(FisicoJhon).filter(
                FisicoJhon.peso_kg.isnot(None)
            ).order_by(FisicoJhon.fecha.desc()).first()
            
            if not ultimo_registro:
                return {
                    "peso_actual": peso_inicial,
                    "peso_inicial": peso_inicial,
                    "peso_meta": peso_meta,
                    "peso_perdido": 0.0,
                    "peso_restante": perdida_objetivo_total,
                    "progreso_porcentaje": 0.0,
                    "imc_actual": round(peso_inicial / (1.70 ** 2), 1),
                    "imc_meta": round(peso_meta / (1.70 ** 2), 1),
                    "tendencia": "SIN_DATOS",
                    "mensaje": "Aún no hay registros de peso",
                    "velocidad_perdida_semanal": 0.0
                }
            
            peso_actual = ultimo_registro.peso_kg
            peso_perdido = peso_inicial - peso_actual
            progreso_porcentaje = (peso_perdido / perdida_objetivo_total) * 100
            peso_restante = peso_actual - peso_meta
            imc_actual = peso_actual / (1.70 ** 2)
            imc_meta = peso_meta / (1.70 ** 2)
            
            # Analizar tendencia últimas 4 semanas
            fecha_4_semanas = date.today() - timedelta(weeks=4)
            registros_recientes = session.query(FisicoJhon).filter(
                FisicoJhon.fecha >= fecha_4_semanas,
                FisicoJhon.peso_kg.isnot(None)
            ).order_by(FisicoJhon.fecha).all()
            
            tendencia = "ESTABLE"
            velocidad_perdida = 0.0
            cambio_4_semanas = 0.0
            
            if len(registros_recientes) >= 2:
                peso_hace_4_semanas = registros_recientes[0].peso_kg
                cambio_4_semanas = peso_actual - peso_hace_4_semanas
                semanas_transcurridas = len(registros_recientes)
                velocidad_perdida = abs(cambio_4_semanas) / semanas_transcurridas
                
                if cambio_4_semanas <= -2.0:
                    tendencia = "EXCELENTE"
                elif cambio_4_semanas <= -1.0:
                    tendencia = "BUENA"
                elif cambio_4_semanas <= -0.5:
                    tendencia = "LENTA"
                elif cambio_4_semanas <= 0.5:
                    tendencia = "ESTABLE"
                else:
                    tendencia = "PREOCUPANTE"
            
            # Proyección fecha meta
            fecha_meta_estimada = None
            semanas_estimadas = None
            
            if velocidad_perdida > 0:
                semanas_estimadas = peso_restante / velocidad_perdida
                fecha_meta_estimada = date.today() + timedelta(weeks=int(semanas_estimadas))
            
            # Días sin ejercicio
            ultimo_ejercicio = session.query(FisicoJhon).filter(
                FisicoJhon.hizo_ejercicio_hoy == True
            ).order_by(FisicoJhon.fecha.desc()).first()
            
            dias_sin_ejercicio = 0
            if ultimo_ejercicio:
                dias_sin_ejercicio = (date.today() - ultimo_ejercicio.fecha).days
            
            return {
                "peso_actual": peso_actual,
                "peso_inicial": peso_inicial,
                "peso_meta": peso_meta,
                "peso_perdido": round(peso_perdido, 1),
                "peso_restante": round(peso_restante, 1),
                "progreso_porcentaje": round(max(0, progreso_porcentaje), 1),
                "imc_actual": round(imc_actual, 1),
                "imc_meta": round(imc_meta, 1),
                "tendencia_4_semanas": tendencia,
                "cambio_4_semanas": round(cambio_4_semanas, 1),
                "velocidad_perdida_semanal": round(velocidad_perdida, 2),
                "semanas_estimadas_meta": int(semanas_estimadas) if semanas_estimadas else None,
                "fecha_meta_estimada": fecha_meta_estimada.isoformat() if fecha_meta_estimada else None,
                "dias_sin_ejercicio": dias_sin_ejercicio,
                "ultimo_registro": ultimo_registro.fecha.isoformat(),
                "meta_alcanzada": peso_actual <= peso_meta
            }
            
    except Exception as e:
        print(f"Error calculando progreso físico: {e}")
        return {"error": f"Error: {str(e)}"}

def obtener_fisico_hoy_jhon(session: Session) -> Optional[FisicoJhon]:
    """
    Obtiene registro físico de hoy (si existe)
    """
    try:
        hoy = date.today()
        return session.query(FisicoJhon).filter(
            FisicoJhon.fecha == hoy
        ).first()
        
    except Exception as e:
        print(f"Error obteniendo físico hoy: {e}")
        return None

def guardar_o_actualizar_fisico_jhon(datos: Dict) -> bool:
    """
    Guarda o actualiza registro físico de Jhon
    """
    try:
        with get_db() as session:
            hoy = date.today()
            
            # Buscar registro existente
            registro_existente = session.query(FisicoJhon).filter(
                FisicoJhon.fecha == hoy
            ).first()
            
            if registro_existente:
                # Actualizar registro existente
                for campo, valor in datos.items():
                    if hasattr(registro_existente, campo):
                        setattr(registro_existente, campo, valor)
            else:
                # Crear nuevo registro
                datos["fecha"] = hoy
                nuevo_registro = FisicoJhon(**datos)
                session.add(nuevo_registro)
            
            session.commit()
            return True
            
    except Exception as e:
        print(f"Error guardando físico: {e}")
        return False

# ============================================================================
# FUNCIONES DASHBOARD Y MÉTRICAS
# ============================================================================

def obtener_metricas_dashboard_jhon() -> Dict[str, Any]:
    """
    Obtiene todas las métricas principales para el dashboard
    """
    try:
        with get_db() as session:
            # Métricas principales
            progreso_meta = calcular_progreso_meta_1582()
            progreso_fisico = calcular_progreso_fisico_jhon()
            presupuesto = calcular_presupuesto_restante_mes()
            
            # Métricas de estudio
            horas_estudio = calcular_horas_estudio_semana(session)
            
            # Métricas de bienestar
            bienestar_hoy = obtener_bienestar_hoy_jhon(session)
            
            # Gastos impulsivos
            gastos_impulsivos = analizar_gastos_impulsivos_semana(session)
            
            # Días sin actividades clave
            ultimo_estudio_matematicas = session.query(EstudioJhon).filter(
                or_(
                    EstudioJhon.curso == CursoJhonEnum.CC4036_ALGEBRA_MATRICIAL.value,
                    EstudioJhon.curso == CursoJhonEnum.CC3106_MATEMATICAS_DISCRETAS.value
                )
            ).order_by(EstudioJhon.fecha.desc()).first()
            
            dias_sin_matematicas = 0
            if ultimo_estudio_matematicas:
                dias_sin_matematicas = (date.today() - ultimo_estudio_matematicas.fecha).days
            
            # Evaluaciones próximas críticas
            evaluaciones_criticas = [e for e in progreso_meta.get("evaluaciones_proximas", []) 
                                   if e.get("critico", False) and e.get("dias_restantes", 999) <= 7]
            
            return {
                "status": "success",
                "timestamp": datetime.now().isoformat(),
                
                # Progreso académico
                "academico": {
                    "progreso_meta_1582": progreso_meta.get("progreso_porcentaje", 0),
                    "nota_necesaria_restante": progreso_meta.get("nota_necesaria_restante", 15.82),
                    "riesgo_nivel": progreso_meta.get("riesgo_nivel", "MEDIO"),
                    "color_riesgo": progreso_meta.get("color_riesgo", "🟡"),
                    "dias_restantes_ciclo": progreso_meta.get("dias_restantes_ciclo", 0),
                    "evaluaciones_criticas_proximas": len(evaluaciones_criticas),
                    "dias_sin_matematicas": dias_sin_matematicas
                },
                
                # Progreso físico
                "fisico": {
                    "progreso_peso": progreso_fisico.get("progreso_porcentaje", 0),
                    "peso_actual": progreso_fisico.get("peso_actual", 88.0),
                    "peso_perdido": progreso_fisico.get("peso_perdido", 0.0),
                    "tendencia": progreso_fisico.get("tendencia_4_semanas", "SIN_DATOS"),
                    "dias_sin_ejercicio": progreso_fisico.get("dias_sin_ejercicio", 0)
                },
                
                # Finanzas
                "financiero": {
                    "presupuesto_restante": presupuesto.get("restante", 526),
                    "porcentaje_usado": presupuesto.get("porcentaje_usado", 0),
                    "estado_presupuesto": presupuesto.get("estado", "BUENO"),
                    "color_presupuesto": presupuesto.get("color", "🟢"),
                    "gastos_impulsivos_semana": gastos_impulsivos.get("total_gastos_impulsivos", 0),
                    "riesgo_exceso": presupuesto.get("riesgo_exceso", False)
                },
                
                # Estudio y productividad
                "productividad": {
                    "horas_estudio_semana": horas_estudio.get("total_horas", 0),
                    "sesiones_semana": horas_estudio.get("sesiones", 0),
                    "concentracion_promedio": horas_estudio.get("promedio_concentracion", 0),
                    "contribucion_meta_promedio": horas_estudio.get("contribucion_meta_promedio", 0),
                    "sesiones_matematicas": horas_estudio.get("sesiones_matematicas", 0)
                },
                
                # Bienestar
                "bienestar": {
                    "registrado_hoy": bienestar_hoy is not None,
                    "energia_hoy": bienestar_hoy.energia_nivel if bienestar_hoy else None,
                    "animo_hoy": bienestar_hoy.animo_nivel if bienestar_hoy else None,
                    "concentracion_hoy": bienestar_hoy.concentracion_sin_medicacion if bienestar_hoy else None,
                    "tomo_medicacion_hoy": bienestar_hoy.tomo_metilfenidato if bienestar_hoy else False
                },
                
                # Alertas y recordatorios
                "alertas": {
                    "evaluaciones_criticas": evaluaciones_criticas,
                    "presupuesto_alto": presupuesto.get("porcentaje_usado", 0) > 80,
                    "dias_sin_matematicas_alto": dias_sin_matematicas > 3,
                    "dias_sin_ejercicio_alto": progreso_fisico.get("dias_sin_ejercicio", 0) > 4,
                    "control_impulsos_malo": gastos_impulsivos.get("nivel_control") == "MALO"
                }
            }
            
    except Exception as e:
        print(f"Error obteniendo métricas dashboard: {e}")
        return {
            "status": "error",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

def obtener_resumen_semanal_jhon() -> Dict[str, Any]:
    """
    Obtiene resumen completo de la semana actual
    """
    try:
        with get_db() as session:
            # Calcular inicio de semana (lunes)
            hoy = date.today()
            inicio_semana = hoy - timedelta(days=hoy.weekday())
            
            # Registros de la semana
            bienestar_semana = session.query(BienestarJhon).filter(
                BienestarJhon.fecha >= inicio_semana
            ).all()
            
            estudio_semana = session.query(EstudioJhon).filter(
                EstudioJhon.fecha >= inicio_semana
            ).all()
            
            gastos_semana = session.query(GastosJhon).filter(
                GastosJhon.fecha >= inicio_semana
            ).all()
            
            fisico_semana = session.query(FisicoJhon).filter(
                FisicoJhon.fecha >= inicio_semana
            ).all()
            
            # Análisis bienestar
            if bienestar_semana:
                energia_promedio = np.mean([b.energia_nivel for b in bienestar_semana])
                animo_promedio = np.mean([b.animo_nivel for b in bienestar_semana])
                concentracion_promedio = np.mean([b.concentracion_sin_medicacion for b in bienestar_semana])
                dias_medicacion = sum(1 for b in bienestar_semana if b.tomo_metilfenidato)
                horas_sueno_promedio = np.mean([b.sueno_horas for b in bienestar_semana])
            else:
                energia_promedio = animo_promedio = concentracion_promedio = 0
                dias_medicacion = 0
                horas_sueno_promedio = 0
            
            # Análisis estudio
            if estudio_semana:
                total_minutos_estudio = sum(e.duracion_minutos for e in estudio_semana)
                concentracion_estudio_promedio = np.mean([e.concentracion_durante for e in estudio_semana])
                contribucion_meta_promedio = np.mean([e.contribucion_meta_1582 for e in estudio_semana])
                sesiones_matematicas = len([e for e in estudio_semana if 'algebra' in e.curso or 'matematicas' in e.curso])
            else:
                total_minutos_estudio = 0
                concentracion_estudio_promedio = contribucion_meta_promedio = 0
                sesiones_matematicas = 0
            
            # Análisis gastos
            total_gastos = sum(g.monto for g in gastos_semana)
            gastos_impulsivos_total = sum(g.monto for g in gastos_semana if g.es_gasto_impulsivo)
            gastos_impulsivos_cantidad = len([g for g in gastos_semana if g.es_gasto_impulsivo])
            
            # Análisis físico
            dias_ejercicio = len([f for f in fisico_semana if f.hizo_ejercicio_hoy])
            
            return {
                "periodo": f"Semana del {inicio_semana.strftime('%d/%m')} al {hoy.strftime('%d/%m')}",
                "dias_registrados": {
                    "bienestar": len(bienestar_semana),
                    "estudio": len(set(e.fecha for e in estudio_semana)),
                    "gastos": len(set(g.fecha for g in gastos_semana)),
                    "fisico": len(fisico_semana)
                },
                
                "bienestar": {
                    "energia_promedio": round(energia_promedio, 1),
                    "animo_promedio": round(animo_promedio, 1),
                    "concentracion_promedio": round(concentracion_promedio, 1),
                    "dias_medicacion": dias_medicacion,
                    "horas_sueno_promedio": round(horas_sueno_promedio, 1)
                },
                
                "estudio": {
                    "total_horas": round(total_minutos_estudio / 60, 1),
                    "total_sesiones": len(estudio_semana),
                    "concentracion_promedio": round(concentracion_estudio_promedio, 1),
                    "contribucion_meta_promedio": round(contribucion_meta_promedio, 1),
                    "sesiones_matematicas": sesiones_matematicas,
                    "porcentaje_matematicas": round((sesiones_matematicas / max(len(estudio_semana), 1)) * 100, 1)
                },
                
                "gastos": {
                    "total_gastado": round(total_gastos, 2),
                    "gastos_impulsivos": round(gastos_impulsivos_total, 2),
                    "cantidad_impulsos": gastos_impulsivos_cantidad,
                    "porcentaje_impulsos": round((gastos_impulsivos_total / max(total_gastos, 1)) * 100, 1)
                },
                
                "fisico": {
                    "dias_ejercicio": dias_ejercicio,
                    "porcentaje_ejercicio": round((dias_ejercicio / 7) * 100, 1)
                }
            }
            
    except Exception as e:
        print(f"Error obteniendo resumen semanal: {e}")
        return {"error": str(e)}

# ============================================================================
# FUNCIONES DE CORRELACIONES AUTOMÁTICAS
# ============================================================================

def calcular_correlacion_ejercicio_concentracion(dias_analisis: int = 30) -> Dict[str, Any]:
    """
    Calcula correlación entre ejercicio y concentración en estudios
    """
    try:
        with get_db() as session:
            fecha_inicio = date.today() - timedelta(days=dias_analisis)
            
            # Obtener días con y sin ejercicio
            registros_fisico = session.query(FisicoJhon).filter(
                FisicoJhon.fecha >= fecha_inicio
            ).all()
            
            registros_estudio = session.query(EstudioJhon).filter(
                EstudioJhon.fecha >= fecha_inicio
            ).all()
            
            if len(registros_fisico) < 10 or len(registros_estudio) < 10:
                return {
                    "error": "Datos insuficientes para correlación",
                    "registros_fisico": len(registros_fisico),
                    "registros_estudio": len(registros_estudio)
                }
            
            # Crear diccionarios por fecha
            ejercicio_por_fecha = {r.fecha: r.hizo_ejercicio_hoy for r in registros_fisico}
            
            # Agrupar concentración por fecha
            concentracion_por_fecha = {}
            for estudio in registros_estudio:
                if estudio.fecha not in concentracion_por_fecha:
                    concentracion_por_fecha[estudio.fecha] = []
                concentracion_por_fecha[estudio.fecha].append(estudio.concentracion_durante)
            
            # Promediar concentración por día
            concentracion_promedio_fecha = {
                fecha: np.mean(concentraciones) 
                for fecha, concentraciones in concentracion_por_fecha.items()
            }
            
            # Encontrar fechas comunes
            fechas_comunes = set(ejercicio_por_fecha.keys()) & set(concentracion_promedio_fecha.keys())
            
            if len(fechas_comunes) < 7:
                return {
                    "error": "Fechas comunes insuficientes",
                    "fechas_comunes": len(fechas_comunes)
                }
            
            # Preparar datos para correlación
            ejercicio_valores = [1 if ejercicio_por_fecha[fecha] else 0 for fecha in fechas_comunes]
            concentracion_valores = [concentracion_promedio_fecha[fecha] for fecha in fechas_comunes]
            
            # Calcular correlación
            correlacion = np.corrcoef(ejercicio_valores, concentracion_valores)[0, 1]
            
            # Análisis por grupos
            concentracion_con_ejercicio = [concentracion_promedio_fecha[fecha] 
                                         for fecha in fechas_comunes 
                                         if ejercicio_por_fecha[fecha]]
            concentracion_sin_ejercicio = [concentracion_promedio_fecha[fecha] 
                                         for fecha in fechas_comunes 
                                         if not ejercicio_por_fecha[fecha]]
            
            promedio_con_ejercicio = np.mean(concentracion_con_ejercicio) if concentracion_con_ejercicio else 0
            promedio_sin_ejercicio = np.mean(concentracion_sin_ejercicio) if concentracion_sin_ejercicio else 0
            diferencia = promedio_con_ejercicio - promedio_sin_ejercicio
            
            # Interpretación
            if correlacion > 0.3:
                interpretacion = "Correlación positiva moderada"
                recomendacion = "El ejercicio mejora tu concentración - manténlo"
            elif correlacion > 0.1:
                interpretacion = "Correlación positiva leve"
                recomendacion = "El ejercicio puede ayudar tu concentración"
            elif correlacion < -0.1:
                interpretacion = "Correlación negativa"
                recomendacion = "Revisa si el ejercicio te está agotando"
            else:
                interpretacion = "Sin correlación clara"
                recomendacion = "No hay patrón claro entre ejercicio y concentración"
            
            return {
                "correlacion": round(correlacion, 3),
                "promedio_concentracion_con_ejercicio": round(promedio_con_ejercicio, 2),
                "promedio_concentracion_sin_ejercicio": round(promedio_sin_ejercicio, 2),
                "diferencia": round(diferencia, 2),
                "interpretacion": interpretacion,
                "recomendacion": recomendacion,
                "dias_con_ejercicio": len(concentracion_con_ejercicio),
                "dias_sin_ejercicio": len(concentracion_sin_ejercicio),
                "fechas_analizadas": len(fechas_comunes),
                "significativo": abs(correlacion) > 0.2 and len(fechas_comunes) >= 14
            }
            
    except Exception as e:
        print(f"Error calculando correlación ejercicio-concentración: {e}")
        return {"error": str(e)}

def calcular_correlacion_sueno_energia(dias_analisis: int = 30) -> Dict[str, Any]:
    """
    Calcula correlación entre horas de sueño y nivel de energía
    """
    try:
        with get_db() as session:
            fecha_inicio = date.today() - timedelta(days=dias_analisis)
            
            registros = session.query(BienestarJhon).filter(
                BienestarJhon.fecha >= fecha_inicio
            ).all()
            
            if len(registros) < 7:
                return {"error": "Datos insuficientes para correlación"}
            
            horas_sueno = [r.sueno_horas for r in registros]
            niveles_energia = [r.energia_nivel for r in registros]
            
            correlacion = np.corrcoef(horas_sueno, niveles_energia)[0, 1]
            
            # Análisis por rangos de sueño
            registros_poco_sueno = [r for r in registros if r.sueno_horas < 6.5]
            registros_sueno_normal = [r for r in registros if 6.5 <= r.sueno_horas <= 8.5]
            registros_mucho_sueno = [r for r in registros if r.sueno_horas > 8.5]
            
            energia_poco_sueno = np.mean([r.energia_nivel for r in registros_poco_sueno]) if registros_poco_sueno else 0
            energia_sueno_normal = np.mean([r.energia_nivel for r in registros_sueno_normal]) if registros_sueno_normal else 0
            energia_mucho_sueno = np.mean([r.energia_nivel for r in registros_mucho_sueno]) if registros_mucho_sueno else 0
            
            # Encontrar rango óptimo
            rangos_energia = [
                ("Poco sueño (<6.5h)", energia_poco_sueno, len(registros_poco_sueno)),
                ("Sueño normal (6.5-8.5h)", energia_sueno_normal, len(registros_sueno_normal)),
                ("Mucho sueño (>8.5h)", energia_mucho_sueno, len(registros_mucho_sueno))
            ]
            
            mejor_rango = max(rangos_energia, key=lambda x: x[1] if x[2] > 0 else 0)
            
            return {
                "correlacion": round(correlacion, 3),
                "promedio_horas_sueno": round(np.mean(horas_sueno), 1),
                "promedio_energia": round(np.mean(niveles_energia), 1),
                "energia_por_rango": {
                    "poco_sueno": round(energia_poco_sueno, 1),
                    "sueno_normal": round(energia_sueno_normal, 1),
                    "mucho_sueno": round(energia_mucho_sueno, 1)
                },
                "mejor_rango_sueno": mejor_rango[0],
                "registros_analizados": len(registros),
                "recomendacion": f"Tu mejor energía es con {mejor_rango[0].lower()}"
            }
            
    except Exception as e:
        print(f"Error calculando correlación sueño-energía: {e}")
        return {"error": str(e)}

# ============================================================================
# FUNCIONES DE ALERTAS Y NOTIFICACIONES
# ============================================================================

def generar_alertas_automaticas() -> List[Dict[str, Any]]:
    """
    Genera alertas automáticas basadas en el estado actual
    """
    alertas = []
    
    try:
        # Alerta 1: Progreso meta 15.82
        progreso_meta = calcular_progreso_meta_1582()
        if progreso_meta.get("status") == "success":
            riesgo = progreso_meta.get("riesgo_nivel")
            if riesgo in ["CRÍTICO", "ALTO"]:
                alertas.append({
                    "tipo": "academico",
                    "prioridad": "CRÍTICA" if riesgo == "CRÍTICO" else "ALTA",
                    "titulo": f"🚨 Meta 15.82 en Riesgo {riesgo}",
                    "mensaje": f"Necesitas {progreso_meta.get('nota_necesaria_restante')} en créditos restantes",
                    "accion": "Revisar estrategia de estudio en matemáticas",
                    "datos": progreso_meta
                })
        
        # Alerta 2: Evaluaciones próximas
        evaluaciones = progreso_meta.get("evaluaciones_proximas", [])
        for evaluacion in evaluaciones:
            if evaluacion.get("dias_restantes", 999) <= 3:
                alertas.append({
                    "tipo": "evaluacion",
                    "prioridad": "ALTA",
                    "titulo": f"📚 {evaluacion['evaluacion']} en {evaluacion['dias_restantes']} días",
                    "mensaje": f"{evaluacion['curso_nombre']} - {evaluacion['tema']}",
                    "accion": "Preparación intensiva" + (" + medicación" if evaluacion.get("medicacion_recomendada") else ""),
                    "datos": evaluacion
                })
        
        # Alerta 3: Presupuesto alto
        presupuesto = calcular_presupuesto_restante_mes()
        if presupuesto.get("porcentaje_usado", 0) > 80:
            alertas.append({
                "tipo": "financiero",
                "prioridad": "MEDIA",
                "titulo": f"💰 Presupuesto al {presupuesto['porcentaje_usado']:.0f}%",
                "mensaje": f"S/{presupuesto['restante']:.0f} restantes de S/{presupuesto['presupuesto_total']}",
                "accion": "Controlar gastos impulsivos",
                "datos": presupuesto
            })
        
        # Alerta 4: Días sin matemáticas
        with get_db() as session:
            ultimo_matematicas = session.query(EstudioJhon).filter(
                or_(
                    EstudioJhon.curso == CursoJhonEnum.CC4036_ALGEBRA_MATRICIAL.value,
                    EstudioJhon.curso == CursoJhonEnum.CC3106_MATEMATICAS_DISCRETAS.value
                )
            ).order_by(EstudioJhon.fecha.desc()).first()
            
            dias_sin_matematicas = 999
            if ultimo_matematicas:
                dias_sin_matematicas = (date.today() - ultimo_matematicas.fecha).days
            
            if dias_sin_matematicas > 3:
                alertas.append({
                    "tipo": "estudio",
                    "prioridad": "MEDIA",
                    "titulo": f"📐 {dias_sin_matematicas} días sin matemáticas",
                    "mensaje": "Álgebra y Discretas requieren práctica constante",
                    "accion": "Sesión de repaso urgente",
                    "datos": {"dias_sin_matematicas": dias_sin_matematicas}
                })
        
        # Alerta 5: Días sin ejercicio
        progreso_fisico = calcular_progreso_fisico_jhon()
        dias_sin_ejercicio = progreso_fisico.get("dias_sin_ejercicio", 0)
        if dias_sin_ejercicio > 4:
            alertas.append({
                "tipo": "fisico",
                "prioridad": "BAJA",
                "titulo": f"🏃 {dias_sin_ejercicio} días sin ejercicio",
                "mensaje": "Meta 70kg requiere actividad física regular",
                "accion": "Sesión corta de ejercicio hoy",
                "datos": {"dias_sin_ejercicio": dias_sin_ejercicio}
            })
        
        # Ordenar por prioridad
        orden_prioridad = {"CRÍTICA": 4, "ALTA": 3, "MEDIA": 2, "BAJA": 1}
        alertas.sort(key=lambda x: orden_prioridad.get(x["prioridad"], 0), reverse=True)
        
        # Limitar a máximo 5 alertas
        return alertas[:5]
        
    except Exception as e:
        print(f"Error generando alertas: {e}")
        return []

def obtener_alertas_hoy() -> List[Dict[str, Any]]:
    """
    Obtiene alertas específicas para hoy
    """
    try:
        alertas_automaticas = generar_alertas_automaticas()
        
        # Agregar alertas específicas del día
        alertas_hoy = []
        
        # Verificar si es día de evaluación
        progreso = calcular_progreso_meta_1582()
        evaluaciones_hoy = [e for e in progreso.get("evaluaciones_proximas", []) 
                           if e.get("dias_restantes") == 0]
        
        for evaluacion in evaluaciones_hoy:
            alertas_hoy.append({
                "tipo": "evaluacion_hoy",
                "prioridad": "CRÍTICA",
                "titulo": f"🎯 HOY: {evaluacion['evaluacion']}",
                "mensaje": f"{evaluacion['curso_nombre']} - {evaluacion['tema']}",
                "accion": "¡Es hoy! " + ("Tomar medicación" if evaluacion.get("medicacion_recomendada") else "¡Éxito!"),
                "datos": evaluacion
            })
        
        # Verificar si no ha registrado bienestar hoy
        with get_db() as session:
            bienestar_hoy = obtener_bienestar_hoy_jhon(session)
            if not bienestar_hoy and datetime.now().hour >= 10:
                alertas_hoy.append({
                    "tipo": "registro_faltante",
                    "prioridad": "BAJA",
                    "titulo": "📝 Falta registro bienestar",
                    "mensaje": "No has registrado tu bienestar hoy",
                    "accion": "Completar registro rápido",
                    "datos": {}
                })
        
        # Combinar alertas automáticas con alertas del día
        todas_alertas = alertas_hoy + alertas_automaticas
        
        # Ordenar y limitar
        orden_prioridad = {"CRÍTICA": 4, "ALTA": 3, "MEDIA": 2, "BAJA": 1}
        todas_alertas.sort(key=lambda x: orden_prioridad.get(x["prioridad"], 0), reverse=True)
        
        return todas_alertas[:5]
        
    except Exception as e:
        print(f"Error obteniendo alertas hoy: {e}")
        return []

# ============================================================================
# FUNCIONES DE ANÁLISIS Y REPORTES
# ============================================================================

def generar_reporte_semanal_completo() -> Dict[str, Any]:
    """
    Genera reporte completo de la semana para análisis
    """
    try:
        resumen_semanal = obtener_resumen_semanal_jhon()
        metricas_dashboard = obtener_metricas_dashboard_jhon()
        
        # Análisis de tendencias
        with get_db() as session:
            # Tendencia estudio matemáticas
            fecha_inicio = date.today() - timedelta(days=7)
            sesiones_matematicas = session.query(EstudioJhon).filter(
                EstudioJhon.fecha >= fecha_inicio,
                or_(
                    EstudioJhon.curso == CursoJhonEnum.CC4036_ALGEBRA_MATRICIAL.value,
                    EstudioJhon.curso == CursoJhonEnum.CC3106_MATEMATICAS_DISCRETAS.value
                )
            ).all()
            
            # Tendencia gastos impulsivos
            gastos_impulsivos = session.query(GastosJhon).filter(
                GastosJhon.fecha >= fecha_inicio,
                GastosJhon.es_gasto_impulsivo == True
            ).all()
            
            # Tendencia ejercicio
            dias_ejercicio = session.query(FisicoJhon).filter(
                FisicoJhon.fecha >= fecha_inicio,
                FisicoJhon.hizo_ejercicio_hoy == True
            ).count()
        
        # Calcular scores de rendimiento
        score_academico = calcular_score_academico_semanal(resumen_semanal.get("estudio", {}))
        score_fisico = calcular_score_fisico_semanal(resumen_semanal.get("fisico", {}), dias_ejercicio)
        score_financiero = calcular_score_financiero_semanal(resumen_semanal.get("gastos", {}))
        score_bienestar = calcular_score_bienestar_semanal(resumen_semanal.get("bienestar", {}))
        
        score_general = (score_academico + score_fisico + score_financiero + score_bienestar) / 4
        
        # Recomendaciones específicas
        recomendaciones = generar_recomendaciones_semanales(
            resumen_semanal, score_academico, score_fisico, score_financiero, score_bienestar
        )
        
        return {
            "periodo": resumen_semanal.get("periodo", "Semana actual"),
            "resumen_general": resumen_semanal,
            "metricas_principales": metricas_dashboard,
            "scores": {
                "academico": score_academico,
                "fisico": score_fisico,
                "financiero": score_financiero,
                "bienestar": score_bienestar,
                "general": round(score_general, 1)
            },
            "tendencias": {
                "sesiones_matematicas_semana": len(sesiones_matematicas),
                "gastos_impulsivos_frecuencia": len(gastos_impulsivos),
                "dias_ejercicio_semana": dias_ejercicio
            },
            "recomendaciones": recomendaciones,
            "fecha_generacion": datetime.now().isoformat()
        }
        
    except Exception as e:
        print(f"Error generando reporte semanal: {e}")
        return {"error": str(e)}

def calcular_score_academico_semanal(datos_estudio: Dict) -> float:
    """
    Calcula score académico semanal (0-10)
    """
    try:
        horas = datos_estudio.get("total_horas", 0)
        concentracion = datos_estudio.get("concentracion_promedio", 0)
        contribucion_meta = datos_estudio.get("contribucion_meta_promedio", 0)
        porcentaje_matematicas = datos_estudio.get("porcentaje_matematicas", 0)
        
        # Pesos específicos para meta 15.82
        score = (
            min(horas / 20, 1) * 3 +  # Máximo 20h/semana = 3 puntos
            (concentracion / 5) * 2 +  # Concentración máxima = 2 puntos
            (contribucion_meta / 5) * 3 +  # Contribución meta = 3 puntos
            (porcentaje_matematicas / 100) * 2  # % matemáticas = 2 puntos
        ) * 10
        
        return round(min(score, 10), 1)
        
    except Exception as e:
        print(f"Error calculando score académico: {e}")
        return 0.0

def calcular_score_fisico_semanal(datos_fisico: Dict, dias_ejercicio: int) -> float:
    """
    Calcula score físico semanal (0-10)
    """
    try:
        # Score basado en días de ejercicio objetivo (4-5 días/semana)
        if dias_ejercicio >= 5:
            score = 10
        elif dias_ejercicio >= 4:
            score = 8
        elif dias_ejercicio >= 3:
            score = 6
        elif dias_ejercicio >= 2:
            score = 4
        elif dias_ejercicio >= 1:
            score = 2
        else:
            score = 0
        
        return float(score)
        
    except Exception as e:
        print(f"Error calculando score físico: {e}")
        return 0.0

def calcular_score_financiero_semanal(datos_gastos: Dict) -> float:
    """
    Calcula score financiero semanal (0-10)
    """
    try:
        porcentaje_impulsos = datos_gastos.get("porcentaje_impulsos", 0)
        total_gastado = datos_gastos.get("total_gastado", 0)
        
        # Score basado en control de impulsos y gasto semanal
        score_impulsos = max(0, 10 - (porcentaje_impulsos / 10))  # -1 punto por cada 10% impulsos
        score_cantidad = 10 if total_gastado <= 100 else max(0, 10 - ((total_gastado - 100) / 20))
        
        score = (score_impulsos + score_cantidad) / 2
        return round(score, 1)
        
    except Exception as e:
        print(f"Error calculando score financiero: {e}")
        return 0.0

def calcular_score_bienestar_semanal(datos_bienestar: Dict) -> float:
    """
    Calcula score bienestar semanal (0-10)
    """
    try:
        energia = datos_bienestar.get("energia_promedio", 0)
        animo = datos_bienestar.get("animo_promedio", 0)
        concentracion = datos_bienestar.get("concentracion_promedio", 0)
        sueno = datos_bienestar.get("horas_sueno_promedio", 0)
        
        # Score basado en niveles promedio
        score_energia = (energia / 5) * 2.5
        score_animo = (animo / 5) * 2.5
        score_concentracion = (concentracion / 5) * 2.5
        
        # Score sueño (óptimo 7-8 horas)
        if 7 <= sueno <= 8:
            score_sueno = 2.5
        elif 6.5 <= sueno <= 8.5:
            score_sueno = 2
        elif 6 <= sueno <= 9:
            score_sueno = 1.5
        else:
            score_sueno = 1
        
        score = score_energia + score_animo + score_concentracion + score_sueno
        return round(min(score, 10), 1)
        
    except Exception as e:
        print(f"Error calculando score bienestar: {e}")
        return 0.0

def generar_recomendaciones_semanales(resumen: Dict, score_acad: float, 
                                     score_fis: float, score_fin: float, score_bien: float) -> List[str]:
    """
    Genera recomendaciones específicas basadas en scores semanales
    """
    recomendaciones = []
    
    try:
        # Recomendaciones académicas
        if score_acad < 6:
            recomendaciones.append("📚 URGENTE: Aumentar horas de estudio, especialmente matemáticas")
        elif score_acad < 8:
            recomendaciones.append("📖 Mejorar concentración en sesiones de estudio")
        else:
            recomendaciones.append("✅ Excelente rendimiento académico - mantener el ritmo")
        
        # Recomendaciones físicas
        if score_fis < 6:
            recomendaciones.append("💪 Incrementar actividad física - mínimo 3 días/semana")
        elif score_fis < 8:
            recomendaciones.append("🏃 Ser más consistente con ejercicio diario")
        else:
            recomendaciones.append("🎯 Rutina física excelente - enfocarse en progresión")
        
        # Recomendaciones financieras
        if score_fin < 6:
            recomendaciones.append("💰 ALERTA: Controlar gastos impulsivos urgentemente")
        elif score_fin < 8:
            recomendaciones.append("🛒 Revisar patrones de gasto y planificar mejor")
        else:
            recomendaciones.append("💳 Control financiero excelente")
        
        # Recomendaciones bienestar
        if score_bien < 6:
            recomendaciones.append("🧠 Priorizar descanso y manejo del estrés")
        elif score_bien < 8:
            recomendaciones.append("😊 Optimizar rutina de sueño y técnicas de concentración")
        else:
            recomendaciones.append("🌟 Excelente equilibrio mental y emocional")
        
        # Recomendación general basada en área más débil
        scores = [
            ("académico", score_acad),
            ("físico", score_fis), 
            ("financiero", score_fin),
            ("bienestar", score_bien)
        ]
        area_debil = min(scores, key=lambda x: x[1])
        
        if area_debil[1] < 5:
            recomendaciones.insert(0, f"🔥 PRIORIDAD: Enfoque crítico en área {area_debil[0]}")
        
        return recomendaciones
        
    except Exception as e:
        print(f"Error generando recomendaciones: {e}")
        return ["Error generando recomendaciones personalizadas"]

# ============================================================================
# FUNCIONES DE VALIDACIÓN Y HELPERS
# ============================================================================

def validar_datos_entrada(datos: Dict, tipo_registro: str) -> Tuple[bool, List[str]]:
    """
    Valida datos de entrada según el tipo de registro
    """
    errores = []
    
    try:
        if tipo_registro == "bienestar":
            # Validaciones específicas bienestar
            if datos.get("energia_nivel", 0) not in range(1, 6):
                errores.append("Nivel de energía debe estar entre 1 y 5")
            
            if datos.get("animo_nivel", 0) not in range(1, 6):
                errores.append("Nivel de ánimo debe estar entre 1 y 5")
            
            if not (0 <= datos.get("sueno_horas", 0) <= 12):
                errores.append("Horas de sueño deben estar entre 0 y 12")
        
        elif tipo_registro == "estudio":
            # Validaciones específicas estudio
            if datos.get("duracion_minutos", 0) < 5:
                errores.append("Duración mínima de estudio: 5 minutos")
            
            if datos.get("duracion_minutos", 0) > 480:
                errores.append("Duración máxima de estudio: 8 horas")
            
            for campo in ["concentracion_inicio", "concentracion_durante", "concentracion_final"]:
                if datos.get(campo, 0) not in range(1, 6):
                    errores.append(f"{campo} debe estar entre 1 y 5")
        
        elif tipo_registro == "gastos":
            # Validaciones específicas gastos
            if datos.get("monto", 0) <= 0:
                errores.append("Monto debe ser mayor a 0")
            
            if datos.get("monto", 0) > 2000:
                errores.append("Monto parece excesivo - verificar")
        
        elif tipo_registro == "fisico":
            # Validaciones específicas físico
            if datos.get("peso_kg") and not (40 <= datos.get("peso_kg") <= 150):
                errores.append("Peso debe estar entre 40 y 150 kg")
            
            for campo in ["energia_fisica", "fuerza_percibida", "resistencia_percibida"]:
                if datos.get(campo, 0) not in range(1, 6):
                    errores.append(f"{campo} debe estar entre 1 y 5")
        
        return len(errores) == 0, errores
        
    except Exception as e:
        return False, [f"Error validando datos: {str(e)}"]

def formatear_fecha_legible(fecha: Union[date, str]) -> str:
    """
    Formatea fecha en formato legible español
    """
    try:
        if isinstance(fecha, str):
            fecha = datetime.fromisoformat(fecha).date()
        
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        
        dia_semana = dias_semana[fecha.weekday()]
        mes = meses[fecha.month - 1]
        
        return f"{dia_semana} {fecha.day} de {mes}"
        
    except Exception as e:
        print(f"Error formateando fecha: {e}")
        return str(fecha)

def calcular_semana_academica(fecha: date = None) -> int:
    """
    Calcula la semana académica actual del ciclo 2025-II
    """
    try:
        if fecha is None:
            fecha = date.today()
        
        inicio_ciclo = date(2025, 8, 18)  # Lunes semana 1
        diferencia = (fecha - inicio_ciclo).days
        semana = (diferencia // 7) + 1
        
        return max(1, min(semana, 18))  # Entre semana 1 y 18
        
    except Exception as e:
        print(f"Error calculando semana académica: {e}")
        return 1

def obtener_configuracion_curso(codigo_curso: str) -> Dict[str, Any]:
    """
    Obtiene configuración específica de un curso
    """
    try:
        from config.jhon_master_config import CURSOS_CICLO_2025_2_COMPLETO
        
        for curso_key, curso_data in CURSOS_CICLO_2025_2_COMPLETO.items():
            if curso_key.startswith(codigo_curso) or codigo_curso in curso_key:
                return curso_data
        
        return {}
        
    except Exception as e:
        print(f"Error obteniendo configuración curso: {e}")
        return {}

def limpiar_cache_streamlit():
    """
    Limpia cache de Streamlit para forzar actualización de datos
    """
    try:
        if hasattr(st, 'cache_data'):
            st.cache_data.clear()
        if hasattr(st, 'cache_resource'):
            st.cache_resource.clear()
        print("✅ Cache de Streamlit limpiado")
        
    except Exception as e:
        print(f"Error limpiando cache: {e}")

# ============================================================================
# FUNCIONES DE CACHE ESPECÍFICAS
# ============================================================================

def get_datos_formularios_jhon() -> Dict[str, Any]:
    """
    Obtiene datos para formularios con defaults inteligentes
    """
    try:
        with get_db() as session:
            # Último registro de cada tipo
            ultimo_bienestar = session.query(BienestarJhon).order_by(
                BienestarJhon.fecha.desc()
            ).first()
            
            ultimo_fisico = session.query(FisicoJhon).order_by(
                FisicoJhon.fecha.desc()
            ).first()
            
            ultimo_estudio = session.query(EstudioJhon).order_by(
                EstudioJhon.timestamp_fin.desc()
            ).first()
            
            return {
                "defaults_bienestar": extraer_defaults_bienestar_jhon(ultimo_bienestar),
                "defaults_fisico": extraer_defaults_fisico_jhon(ultimo_fisico),
                "defaults_estudio": extraer_defaults_estudio_jhon(ultimo_estudio),
                "evaluaciones_proximas": obtener_evaluaciones_proximas(session),
                "ubicaciones_frecuentes": obtener_ubicaciones_frecuentes_jhon(session)
            }
            
    except Exception as e:
        print(f"Error obteniendo datos formularios: {e}")
        return {
            "defaults_bienestar": {},
            "defaults_fisico": {},
            "defaults_estudio": {},
            "evaluaciones_proximas": [],
            "ubicaciones_frecuentes": []
        }

def extraer_defaults_fisico_jhon(registro: Optional[FisicoJhon]) -> Dict:
    """
    Extrae defaults del último registro físico
    """
    if not registro:
        return {
            "energia_fisica": 3,
            "fuerza_percibida": 3,
            "resistencia_percibida": 3,
            "como_me_veo_espejo": 3,
            "confianza_fisica": 3,
            "nivel_motivacion": 3,
            "hizo_ejercicio_hoy": False
        }
    
    return {
        "energia_fisica": registro.energia_fisica,
        "fuerza_percibida": registro.fuerza_percibida,
        "resistencia_percibida": registro.resistencia_percibida,
        "como_me_veo_espejo": registro.como_me_veo_espejo,
        "confianza_fisica": registro.confianza_fisica,
        "nivel_motivacion": registro.nivel_motivacion,
        "hizo_ejercicio_hoy": False  # Siempre falso por defecto para nuevo día
    }

def extraer_defaults_estudio_jhon(registro: Optional[EstudioJhon]) -> Dict:
    """
    Extrae defaults del último registro de estudio
    """
    if not registro:
        return {
            "curso": CursoJhonEnum.CC4036_ALGEBRA_MATRICIAL.value,
            "ubicacion_estudio": UbicacionJhonEnum.CAMPUS_BIBLIOTECA.value,
            "concentracion_inicio": 3,
            "concentracion_durante": 3,
            "concentracion_final": 3,
            "con_medicacion_metilfenidato": False
        }
    
    return {
        "curso": registro.curso,
        "ubicacion_estudio": registro.ubicacion_estudio,
        "concentracion_inicio": 3,  # Siempre resetear para nueva sesión
        "concentracion_durante": 3,
        "concentracion_final": 3,
        "con_medicacion_metilfenidato": False
    }

def obtener_ubicaciones_frecuentes_jhon(session: Session) -> List[str]:
    """
    Obtiene ubicaciones más frecuentes de Jhon
    """
    try:
        # Ubicaciones más frecuentes últimos 30 días
        fecha_inicio = date.today() - timedelta(days=30)
        
        ubicaciones_bienestar = session.query(
            BienestarJhon.ubicacion_principal_dia,
            func.count(BienestarJhon.ubicacion_principal_dia).label('frecuencia')
        ).filter(
            BienestarJhon.fecha >= fecha_inicio
        ).group_by(BienestarJhon.ubicacion_principal_dia).order_by(
            func.count(BienestarJhon.ubicacion_principal_dia).desc()
        ).limit(5).all()
        
        return [ub.ubicacion_principal_dia for ub in ubicaciones_bienestar]
        
    except Exception as e:
        print(f"Error obteniendo ubicaciones frecuentes: {e}")
        return [UbicacionJhonEnum.SA_CUARTO.value, UbicacionJhonEnum.CAMPUS_BIBLIOTECA.value]

def invalidar_cache_relacionado(tipo_dato: str):
    """
    Invalida caches relacionados cuando se insertan nuevos datos
    """
    try:
        # Limpiar cache específico según tipo
        if hasattr(st, 'cache_data'):
            st.cache_data.clear()
        
        print(f"✅ Cache invalidado para tipo: {tipo_dato}")
        
    except Exception as e:
        print(f"Error invalidando cache: {e}")

# ============================================================================
# FUNCIONES DE INICIALIZACIÓN Y SETUP
# ============================================================================

# ============================================================================
# CONTINUACIÓN DEL ARCHIVO jhon_helpers.py
# Desde la función verificar_sistema_jhon()
# ============================================================================

def verificar_sistema_jhon() -> Dict[str, Any]:
    """
    Verifica que todo el sistema esté funcionando correctamente
    """
    try:
        resultados = {
            "database": False,
            "perfil_jhon": False,
            "funciones_core": False,
            "configuracion": False,
            "errores": []
        }
        
        # Test 1: Conexión a base de datos
        try:
            with get_db() as session:
                session.execute(text("SELECT 1")).scalar()
                resultados["database"] = True
        except Exception as e:
            resultados["errores"].append(f"Error BD: {str(e)}")
        
        # Test 2: Perfil de Jhon
        try:
            with get_db() as session:
                perfil = session.query(JhonProfileMaster).first()
                if perfil and perfil.matricula == "20231515":
                    resultados["perfil_jhon"] = True
                else:
                    resultados["errores"].append("Perfil de Jhon no encontrado")
        except Exception as e:
            resultados["errores"].append(f"Error perfil: {str(e)}")
        
        # Test 3: Funciones core
        try:
            progreso = calcular_progreso_meta_1582()
            if progreso.get("status") == "success":
                resultados["funciones_core"] = True
            else:
                resultados["errores"].append(f"Error funciones core: {progreso.get('error', 'Unknown')}")
        except Exception as e:
            resultados["errores"].append(f"Error funciones: {str(e)}")
        
        # Test 4: Configuración hardcodeada
        try:
            from config.jhon_master_config import CURSOS_CICLO_2025_2_COMPLETO
            if len(CURSOS_CICLO_2025_2_COMPLETO) == 7:  # 7 cursos exactos
                resultados["configuracion"] = True
            else:
                resultados["errores"].append("Configuración incompleta")
        except Exception as e:
            resultados["errores"].append(f"Error configuración: {str(e)}")
        
        # Test 5: Validación meta 15.82
        try:
            from utils.jhon_models import validar_promedio_meta_1582
            validacion = validar_promedio_meta_1582(13.23, 46, 20, 14.0)
            if abs(validacion["promedio_necesario"] - 15.82) < 0.1:
                resultados["meta_1582_correcta"] = True
            else:
                resultados["errores"].append(f"Meta 15.82 incorrecta: {validacion['promedio_necesario']}")
        except Exception as e:
            resultados["errores"].append(f"Error validación meta: {str(e)}")
        
        # Resultado general
        resultados["sistema_ok"] = all([
            resultados["database"],
            resultados["perfil_jhon"],
            resultados["funciones_core"],
            resultados["configuracion"]
        ])
        
        return resultados
        
    except Exception as e:
        return {
            "sistema_ok": False,
            "error_general": str(e),
            "errores": [f"Error crítico del sistema: {str(e)}"]
        }

def inicializar_sistema_jhon() -> bool:
    """
    Inicializa el sistema PROMETEO-JHON con datos base
    """
    try:
        print("🚀 Inicializando Sistema PROMETEO-JHON...")
        
        with get_db() as session:
            # 1. Crear perfil master de Jhon si no existe
            perfil_existente = session.query(JhonProfileMaster).first()
            if not perfil_existente:
                print("📋 Creando perfil master de Jhon...")
                nuevo_perfil = JhonProfileMaster()
                session.add(nuevo_perfil)
                session.commit()
                print("✅ Perfil master creado")
            else:
                print("✅ Perfil master ya existe")
            
            # 2. Verificar configuración de cursos
            cursos_existentes = session.query(ConfiguracionCursoJhon).count()
            if cursos_existentes == 0:
                print("📚 Creando configuración de cursos...")
                crear_configuracion_cursos_base(session)
                session.commit()
                print("✅ Configuración de cursos creada")
            else:
                print(f"✅ Configuración de cursos existe ({cursos_existentes} cursos)")
            
            # 3. Crear evaluaciones calendarizadas si no existen
            evaluaciones_existentes = session.query(EvaluacionCalendarizada).count()
            if evaluaciones_existentes == 0:
                print("📅 Creando calendario de evaluaciones...")
                crear_evaluaciones_calendarizadas(session)
                session.commit()
                print("✅ Calendario de evaluaciones creado")
            else:
                print(f"✅ Calendario de evaluaciones existe ({evaluaciones_existentes} evaluaciones)")
        
        print("🎯 Sistema PROMETEO-JHON inicializado correctamente")
        return True
        
    except Exception as e:
        print(f"❌ Error inicializando sistema: {e}")
        return False

def crear_configuracion_cursos_base(session: Session):
    """
    Crea configuración base de cursos del ciclo 2025-II
    """
    try:
        from config.jhon_master_config import CURSOS_CICLO_2025_2_COMPLETO
        
        for curso_codigo, curso_data in CURSOS_CICLO_2025_2_COMPLETO.items():
            datos_basicos = curso_data.get("datos_basicos", {})
            
            config_curso = ConfiguracionCursoJhon(
                curso_codigo=curso_codigo,
                curso_nombre=datos_basicos.get("nombre", "Curso sin nombre"),
                creditos=datos_basicos.get("creditos", 3),
                profesor_principal=datos_basicos.get("profesor", "Por confirmar"),
                email_profesor=datos_basicos.get("email_profesor"),
                dificultad_jhon=datos_basicos.get("dificultad_jhon", 3),
                ansiedad_nivel_jhon=datos_basicos.get("ansiedad_nivel", "MEDIO"),
                tipo_curso=datos_basicos.get("tipo", "General"),
                sistema_evaluacion=curso_data.get("sistema_evaluacion_confirmado", {}),
                calendario_evaluaciones=curso_data.get("calendario_evaluaciones_exacto", {}),
                estrategias_jhon=curso_data.get("estrategias_jhon_especificas", {}),
                status_configuracion="confirmado" if "confirmado" in curso_codigo else "estimado",
                fuente_datos="config_hardcodeada",
                recordatorios_medicacion=datos_basicos.get("tipo") == "Matemática Crítica",
                criticidad_meta="CRÍTICA" if datos_basicos.get("dificultad_jhon", 0) >= 5 else "MEDIA"
            )
            
            session.add(config_curso)
        
        print(f"✅ Configuración creada para {len(CURSOS_CICLO_2025_2_COMPLETO)} cursos")
        
    except Exception as e:
        print(f"Error creando configuración cursos: {e}")
        raise

def crear_evaluaciones_calendarizadas(session: Session):
    """
    Crea evaluaciones calendarizadas desde configuración hardcodeada
    """
    try:
        from config.jhon_master_config import CURSOS_CICLO_2025_2_COMPLETO
        
        evaluaciones_creadas = 0
        
        for curso_codigo, curso_data in CURSOS_CICLO_2025_2_COMPLETO.items():
            calendario = curso_data.get("calendario_evaluaciones_exacto", {})
            
            for eval_nombre, eval_data in calendario.items():
                evaluacion = EvaluacionCalendarizada(
                    curso_codigo=curso_codigo,
                    evaluacion_nombre=eval_nombre,
                    evaluacion_tipo="EXAMEN" if "EXAMEN" in eval_nombre else "PC",
                    fecha_evaluacion=eval_data.get("fecha"),
                    semana_academica=eval_data.get("semana", 1),
                    dias_preparacion_recomendados=eval_data.get("preparacion_dias", 3),
                    tema_principal=eval_data.get("tema", ""),
                    dificultad_esperada=curso_data["datos_basicos"].get("dificultad_jhon", 3),
                    criticidad_meta_1582="CRÍTICA" if eval_data.get("critico", False) else "MEDIA",
                    medicacion_recomendada=eval_data.get("medicacion_recomendada", False),
                    ubicacion_estudio_recomendada="Biblioteca UNALM",
                    horas_estudio_sugeridas=eval_data.get("preparacion_dias", 3) * 2
                )
                
                session.add(evaluacion)
                evaluaciones_creadas += 1
        
        print(f"✅ {evaluaciones_creadas} evaluaciones calendarizadas creadas")
        
    except Exception as e:
        print(f"Error creando evaluaciones: {e}")
        raise

# ============================================================================
# FUNCIONES DE ANÁLISIS AVANZADO
# ============================================================================

def analizar_patron_concentracion_ubicacion(dias_analisis: int = 30) -> Dict[str, Any]:
    """
    Analiza dónde Jhon se concentra mejor según ubicación y contexto
    """
    try:
        with get_db() as session:
            fecha_inicio = date.today() - timedelta(days=dias_analisis)
            
            # Obtener registros de estudio
            registros_estudio = session.query(EstudioJhon).filter(
                EstudioJhon.fecha >= fecha_inicio
            ).all()
            
            if not registros_estudio:
                return {"error": "Sin datos suficientes de estudio"}
            
            # Agrupar por ubicación
            patron_ubicacion = {}
            for registro in registros_estudio:
                ubicacion = registro.ubicacion_estudio
                curso = registro.curso
                
                if ubicacion not in patron_ubicacion:
                    patron_ubicacion[ubicacion] = {
                        "sesiones_totales": 0,
                        "minutos_totales": 0,
                        "concentracion_promedio": 0,
                        "contribucion_meta_promedio": 0,
                        "cursos_estudiados": set(),
                        "con_medicacion": 0,
                        "hiperfoco_logrado": 0,
                        "satisfaccion_promedio": 0
                    }
                
                datos = patron_ubicacion[ubicacion]
                datos["sesiones_totales"] += 1
                datos["minutos_totales"] += registro.duracion_minutos
                datos["concentracion_promedio"] += registro.concentracion_durante
                datos["contribucion_meta_promedio"] += registro.contribucion_meta_1582
                datos["cursos_estudiados"].add(curso)
                datos["satisfaccion_promedio"] += registro.satisfaccion_sesion
                
                if registro.con_medicacion_metilfenidato:
                    datos["con_medicacion"] += 1
                if registro.logre_hiperfoco:
                    datos["hiperfoco_logrado"] += 1
            
            # Calcular promedios y métricas
            for ubicacion, datos in patron_ubicacion.items():
                sesiones = datos["sesiones_totales"]
                datos["concentracion_promedio"] = round(datos["concentracion_promedio"] / sesiones, 2)
                datos["contribucion_meta_promedio"] = round(datos["contribucion_meta_promedio"] / sesiones, 2)
                datos["satisfaccion_promedio"] = round(datos["satisfaccion_promedio"] / sesiones, 2)
                datos["minutos_promedio_sesion"] = round(datos["minutos_totales"] / sesiones, 0)
                datos["porcentaje_con_medicacion"] = round((datos["con_medicacion"] / sesiones) * 100, 1)
                datos["porcentaje_hiperfoco"] = round((datos["hiperfoco_logrado"] / sesiones) * 100, 1)
                datos["cursos_estudiados"] = list(datos["cursos_estudiados"])
                
                # Calcular score de productividad
                datos["score_productividad"] = round(
                    (datos["concentracion_promedio"] * 0.3 +
                     datos["contribucion_meta_promedio"] * 0.4 +
                     datos["satisfaccion_promedio"] * 0.2 +
                     (datos["porcentaje_hiperfoco"] / 20) * 0.1), 2
                )
            
            # Encontrar mejor ubicación
            mejor_ubicacion = max(patron_ubicacion.items(), 
                                 key=lambda x: x[1]["score_productividad"])
            
            # Análisis específico matemáticas
            matematicas_ubicacion = analizar_matematicas_por_ubicacion(session, fecha_inicio)
            
            # Recomendaciones específicas
            recomendaciones = generar_recomendaciones_ubicacion(
                mejor_ubicacion, patron_ubicacion, matematicas_ubicacion
            )
            
            return {
                "patron_completo": patron_ubicacion,
                "mejor_ubicacion": mejor_ubicacion[0],
                "mejor_score": mejor_ubicacion[1]["score_productividad"],
                "matematicas_por_ubicacion": matematicas_ubicacion,
                "recomendaciones": recomendaciones,
                "periodo_analisis": f"{dias_analisis} días",
                "total_sesiones": len(registros_estudio),
                "total_horas": sum(r.duracion_minutos for r in registros_estudio) / 60
            }
            
    except Exception as e:
        print(f"Error analizando ubicaciones: {e}")
        return {"error": f"Error analizando ubicaciones: {str(e)}"}

def analizar_matematicas_por_ubicacion(session: Session, fecha_inicio: date) -> Dict[str, Any]:
    """
    Analiza rendimiento en matemáticas por ubicación específicamente
    """
    try:
        sesiones_matematicas = session.query(EstudioJhon).filter(
            EstudioJhon.fecha >= fecha_inicio,
            or_(
                EstudioJhon.curso == CursoJhonEnum.CC4036_ALGEBRA_MATRICIAL.value,
                EstudioJhon.curso == CursoJhonEnum.CC3106_MATEMATICAS_DISCRETAS.value
            )
        ).all()
        
        if not sesiones_matematicas:
            return {"mensaje": "Sin sesiones de matemáticas en el período"}
        
        analisis_por_ubicacion = {}
        
        for sesion in sesiones_matematicas:
            ubicacion = sesion.ubicacion_estudio
            
            if ubicacion not in analisis_por_ubicacion:
                analisis_por_ubicacion[ubicacion] = {
                    "sesiones": 0,
                    "concentracion_promedio": 0,
                    "frustracion_promedio": 0,
                    "avance_real_porcentaje": 0,
                    "youtube_necesario_porcentaje": 0,
                    "confianza_pc_promedio": 0
                }
            
            datos = analisis_por_ubicacion[ubicacion]
            datos["sesiones"] += 1
            datos["concentracion_promedio"] += sesion.concentracion_durante
            
            if sesion.if_matematicas_frustracion:
                datos["frustracion_promedio"] += sesion.if_matematicas_frustracion
            
            if sesion.if_matematicas_avance_real:
                datos["avance_real_porcentaje"] += 1
            
            if sesion.if_matematicas_youtube_ayuda:
                datos["youtube_necesario_porcentaje"] += 1
            
            if sesion.if_matematicas_confianza_pc:
                datos["confianza_pc_promedio"] += sesion.if_matematicas_confianza_pc
        
        # Calcular promedios
        for ubicacion, datos in analisis_por_ubicacion.items():
            sesiones = datos["sesiones"]
            datos["concentracion_promedio"] = round(datos["concentracion_promedio"] / sesiones, 2)
            datos["frustracion_promedio"] = round(datos["frustracion_promedio"] / sesiones, 2)
            datos["avance_real_porcentaje"] = round((datos["avance_real_porcentaje"] / sesiones) * 100, 1)
            datos["youtube_necesario_porcentaje"] = round((datos["youtube_necesario_porcentaje"] / sesiones) * 100, 1)
            datos["confianza_pc_promedio"] = round(datos["confianza_pc_promedio"] / sesiones, 2)
            
            # Score específico para matemáticas
            datos["score_matematicas"] = round(
                (datos["concentracion_promedio"] * 0.3 +
                 (5 - datos["frustracion_promedio"]) * 0.2 +  # Menos frustración = mejor
                 (datos["avance_real_porcentaje"] / 100) * 0.3 +
                 datos["confianza_pc_promedio"] * 0.2), 2
            )
        
        return analisis_por_ubicacion
        
    except Exception as e:
        print(f"Error analizando matemáticas por ubicación: {e}")
        return {"error": str(e)}

def generar_recomendaciones_ubicacion(mejor_ubicacion: Tuple, patron_completo: Dict, 
                                     matematicas_analisis: Dict) -> List[str]:
    """
    Genera recomendaciones específicas sobre dónde estudiar
    """
    recomendaciones = []
    
    try:
        ubicacion_nombre = mejor_ubicacion[0]
        datos = mejor_ubicacion[1]
        
        recomendaciones.append(f"🎯 Tu mejor ubicación es {ubicacion_nombre.replace('_', ' ').title()}")
        recomendaciones.append(f"📊 Score de productividad: {datos['score_productividad']}/5.0")
        
        if datos["porcentaje_hiperfoco"] > 20:
            recomendaciones.append(f"⚡ Logras hiperfoco {datos['porcentaje_hiperfoco']}% del tiempo aquí")
        
        if datos["porcentaje_con_medicacion"] > 50:
            recomendaciones.append("💊 Considera tomar metilfenidato cuando estudies aquí")
        
        # Recomendaciones específicas matemáticas
        if matematicas_analisis and ubicacion_nombre in matematicas_analisis:
            math_data = matematicas_analisis[ubicacion_nombre]
            if math_data["concentracion_promedio"] >= 4:
                recomendaciones.append("🔢 Excelente para matemáticas - úsalo para Álgebra y Discretas")
            elif math_data["frustracion_promedio"] >= 4:
                recomendaciones.append("😤 Evita esta ubicación para matemáticas - alta frustración")
        
        # Recomendaciones por horario
        if "campus" in ubicacion_nombre.lower():
            recomendaciones.append("⏰ Mejor en horarios de campus (8:00-17:00)")
        elif "sa_cuarto" in ubicacion_nombre.lower():
            recomendaciones.append("🌙 Ideal para estudio nocturno y fines de semana")
        elif "cb_cuarto" in ubicacion_nombre.lower():
            recomendaciones.append("🏠 Perfecto para sesiones largas con apoyo familiar")
        
        return recomendaciones
        
    except Exception as e:
        print(f"Error generando recomendaciones ubicación: {e}")
        return ["Error generando recomendaciones"]

def analizar_efecto_medicacion_tdah(dias_analisis: int = 45) -> Dict[str, Any]:
    """
    Analiza impacto específico del metilfenidato en concentración y rendimiento
    """
    try:
        with get_db() as session:
            fecha_inicio = date.today() - timedelta(days=dias_analisis)
            
            # Datos de bienestar con y sin medicación
            registros_con_medicacion = session.query(BienestarJhon).filter(
                BienestarJhon.fecha >= fecha_inicio,
                BienestarJhon.tomo_metilfenidato == True
            ).all()
            
            registros_sin_medicacion = session.query(BienestarJhon).filter(
                BienestarJhon.fecha >= fecha_inicio,
                BienestarJhon.tomo_metilfenidato == False
            ).all()
            
            if not registros_con_medicacion or not registros_sin_medicacion:
                return {"error": "Datos insuficientes para comparar medicación"}
            
            # Análisis concentración
            concentracion_con_med = []
            concentracion_sin_med = []
            
            for registro in registros_con_medicacion:
                if registro.concentracion_con_medicacion:
                    concentracion_con_med.append(registro.concentracion_con_medicacion)
            
            for registro in registros_sin_medicacion:
                concentracion_sin_med.append(registro.concentracion_sin_medicacion)
            
            if not concentracion_con_med or not concentracion_sin_med:
                return {"error": "Datos de concentración insuficientes"}
            
            # Estadísticas básicas
            promedio_con_med = np.mean(concentracion_con_med)
            promedio_sin_med = np.mean(concentracion_sin_med)
            diferencia = promedio_con_med - promedio_sin_med
            mejora_porcentual = (diferencia / promedio_sin_med) * 100
            
            # Análisis por motivo de uso
            motivos_medicacion = {}
            for registro in registros_con_medicacion:
                if registro.if_medicacion_motivo:
                    motivo = registro.if_medicacion_motivo
                    if motivo not in motivos_medicacion:
                        motivos_medicacion[motivo] = {
                            "frecuencia": 0,
                            "efectividad_promedio": 0,
                            "concentracion_lograda": []
                        }
                    motivos_medicacion[motivo]["frecuencia"] += 1
                    if registro.if_medicacion_efecto_percibido:
                        motivos_medicacion[motivo]["efectividad_promedio"] += registro.if_medicacion_efecto_percibido
                    if registro.concentracion_con_medicacion:
                        motivos_medicacion[motivo]["concentracion_lograda"].append(registro.concentracion_con_medicacion)
            
            # Calcular promedios de motivos
            for motivo, datos in motivos_medicacion.items():
                if datos["frecuencia"] > 0:
                    datos["efectividad_promedio"] = round(datos["efectividad_promedio"] / datos["frecuencia"], 2)
                    if datos["concentracion_lograda"]:
                        datos["concentracion_promedio"] = round(np.mean(datos["concentracion_lograda"]), 2)
            
            # Análisis correlación con evaluaciones
            correlacion_evaluaciones = analizar_medicacion_evaluaciones(session, registros_con_medicacion)
            
            # Recomendaciones específicas
            recomendaciones = generar_recomendaciones_medicacion(
                diferencia, mejora_porcentual, motivos_medicacion
            )
            
            return {
                "concentracion_con_medicacion": round(promedio_con_med, 2),
                "concentracion_sin_medicacion": round(promedio_sin_med, 2),
                "diferencia_absoluta": round(diferencia, 2),
                "mejora_porcentual": round(mejora_porcentual, 1),
                "motivos_uso": motivos_medicacion,
                "correlacion_evaluaciones": correlacion_evaluaciones,
                "recomendaciones": recomendaciones,
                "dias_con_medicacion": len(registros_con_medicacion),
                "dias_sin_medicacion": len(registros_sin_medicacion),
                "periodo_analisis": f"{dias_analisis} días"
            }
            
    except Exception as e:
        print(f"Error analizando medicación: {e}")
        return {"error": f"Error analizando medicación: {str(e)}"}

def analizar_medicacion_evaluaciones(session: Session, registros_medicacion: List[BienestarJhon]) -> Dict[str, Any]:
    """
    Analiza correlación entre uso de medicación y evaluaciones próximas
    """
    try:
        correlaciones = {
            "dias_antes_evaluacion": [],
            "tipos_evaluacion": {},
            "efectividad_por_proximidad": {}
        }
        
        for registro in registros_medicacion:
            # Buscar evaluaciones cercanas a la fecha del registro
            evaluaciones_proximas = obtener_evaluaciones_proximas(session, dias_adelante=7)
            
            for evaluacion in evaluaciones_proximas:
                fecha_eval = datetime.fromisoformat(evaluacion["fecha"]).date()
                dias_diferencia = (fecha_eval - registro.fecha).days
                
                if 0 <= dias_diferencia <= 7:  # Medicación tomada hasta 7 días antes
                    correlaciones["dias_antes_evaluacion"].append(dias_diferencia)
                    
                    tipo_eval = evaluacion["evaluacion"]
                    if tipo_eval not in correlaciones["tipos_evaluacion"]:
                        correlaciones["tipos_evaluacion"][tipo_eval] = 0
                    correlaciones["tipos_evaluacion"][tipo_eval] += 1
                    
                    # Efectividad por proximidad
                    rango_dias = f"{dias_diferencia}-{min(dias_diferencia + 1, 7)} días antes"
                    if rango_dias not in correlaciones["efectividad_por_proximidad"]:
                        correlaciones["efectividad_por_proximidad"][rango_dias] = []
                    
                    if registro.if_medicacion_efecto_percibido:
                        correlaciones["efectividad_por_proximidad"][rango_dias].append(
                            registro.if_medicacion_efecto_percibido
                        )
        
        # Calcular promedios de efectividad
        for rango, efectividades in correlaciones["efectividad_por_proximidad"].items():
            if efectividades:
                correlaciones["efectividad_por_proximidad"][rango] = {
                    "promedio": round(np.mean(efectividades), 2),
                    "registros": len(efectividades)
                }
        
        return correlaciones
        
    except Exception as e:
        print(f"Error analizando medicación-evaluaciones: {e}")
        return {}

def generar_recomendaciones_medicacion(diferencia: float, mejora_porcentual: float, 
                                      motivos: Dict) -> List[str]:
    """
    Genera recomendaciones específicas sobre uso de metilfenidato
    """
    recomendaciones = []
    
    try:
        if mejora_porcentual > 15:
            recomendaciones.append("💊 El metilfenidato muestra beneficio significativo")
            recomendaciones.append("📅 Considera usarlo para todas las evaluaciones de matemáticas")
        elif mejora_porcentual > 5:
            recomendaciones.append("💊 Beneficio moderado del metilfenidato")
            recomendaciones.append("🎯 Úsalo selectivamente para evaluaciones críticas")
        else:
            recomendaciones.append("💊 Beneficio limitado detectado")
            recomendaciones.append("🔍 Evalúa si la dosis o timing son adecuados")
        
        # Análisis por motivo más efectivo
        if motivos:
            mejor_motivo = max(motivos.items(), key=lambda x: x[1].get("efectividad_promedio", 0))
            recomendaciones.append(f"🎯 Más efectivo para: {mejor_motivo[0]}")
        
        # Recomendaciones de timing
        if diferencia > 1.0:
            recomendaciones.append("⏰ Tomar 1-2 horas antes de sesiones críticas de estudio")
        
        return recomendaciones
        
    except Exception as e:
        print(f"Error generando recomendaciones medicación: {e}")
        return ["Error generando recomendaciones de medicación"]

def detectar_patrones_gastos_impulsivos(dias_analisis: int = 60) -> Dict[str, Any]:
    """
    Detecta patrones específicos en gastos impulsivos de Jhon
    """
    try:
        with get_db() as session:
            fecha_inicio = date.today() - timedelta(days=dias_analisis)
            
            gastos_impulsivos = session.query(GastosJhon).filter(
                GastosJhon.fecha >= fecha_inicio,
                GastosJhon.es_gasto_impulsivo == True
            ).all()
            
            if not gastos_impulsivos:
                return {"mensaje": "Sin gastos impulsivos registrados en el período"}
            
            # Análisis por trigger específico
            triggers_analisis = {}
            for gasto in gastos_impulsivos:
                trigger = gasto.if_impulsivo_trigger if gasto.if_impulsivo_trigger else "no_identificado"
                
                if trigger not in triggers_analisis:
                    triggers_analisis[trigger] = {
                        "frecuencia": 0,
                        "monto_total": 0,
                        "monto_promedio": 0,
                        "arrepentimiento_niveles": [],
                        "ubicaciones":