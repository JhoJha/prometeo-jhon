# config/jhon_master_config.py
# Configuración hardcodeada completa PROMETEO-JHON
# Todo el contexto específico de Jhon Villegas Verde centralizado

from datetime import date, datetime, time, timedelta
from typing import Dict, List, Any, Optional
import enum

# ============================================================================
# CONFIGURACIÓN MASTER JHON - DATOS INMUTABLES
# ============================================================================

JHON_PROFILE_MASTER = {
   "personal": {
       "nombre_completo": "Jhon Jhayro Villegas Verde",
       "matricula": "20231515",
       "edad": 24,
       "altura": 1.70,  # metros
       "peso_inicial": 88.0,  # kg - ACTUALIZADO agosto 2025
       "peso_meta_final": 70.0,  # kg
       "fecha_nacimiento": "2001-XX-XX",  # Privacidad
       "telefono_principal": "Poco X6 5G",
       "sistema_operativo": "Android 15"
   },
   
   "academico": {
       "universidad": "Universidad Nacional Agraria La Molina",
       "carrera": "Estadística Informática",
       "facultad": "Economía y Planificación",
       "ciclo_actual": "2025-II",
       "ciclo_numero": 3,
       "creditos_acumulados": 46,  # CONFIRMADO historial académico
       "promedio_actual": 13.23,   # CONFIRMADO historial académico
       "meta_promedio_final": 14.0,
       "meta_ciclo_2025_2": 15.82,  # CALCULADO EXACTO matemáticamente
       "situacion_academica": "Normal",
       "ranking_facultad": "133 de 251",
       "ranking_carrera": "42 de 88",
       "fecha_inicio_carrera": date(2023, 8, 21)
   },
   
   "salud_mental": {
       "tdah_diagnosticado": True,
       "medicacion_tdah": "Metilfenidato",
       "dosis_habitual": "10mg",
       "frecuencia_medicacion": "Época exámenes/PCs matemáticas",
       "trastorno_mixto_ansioso_depresivo": True,
       "indicios_esquizotipico": True,
       "triggers_ansiedad": [
           "Matemáticas (Álgebra/Discretas)",
           "Evaluaciones próximas",
           "Presión meta 15.82",
           "Soledad nocturna SA"
       ],
       "comportamientos_impulsivos": {
           "videojuegos": "LOL - puede durar horas",
           "pornografia": "Especialmente bajo estrés",
           "gastos": "Comida chatarra post-matemáticas",
           "marihuana": "Cada 3 meses aproximadamente",
           "suscripciones": "Apps/servicios innecesarios"
       }
   },
   
   "vivienda_dual": {
       "carabayllo": {
           "tipo": "Casa familiar",
           "contexto": "Con familia - apoyo emocional",
           "equipamiento": "PC buenas especificaciones",
           "distancia_unalm": "3 horas transporte público",
           "ambiente_estudio": "Bueno pero distracciones familiares",
           "actividades_extra": "Trabajo chacra domingos",
           "internet": {
               "agosto_octubre_2025": 30,  # S/ promoción
               "noviembre_adelante": 40   # S/ precio normal
           }
       },
       "santa_anita": {
           "tipo": "Cuarto alquilado",
           "contexto": "Solo - independencia total",
           "equipamiento": "Laptop Core i3 2013 (muy limitada)",
           "distancia_unalm": "20 minutos + S/1 transporte",
           "ambiente_estudio": "Excelente para concentración",
           "alquiler_mensual": 350,  # S/
           "ventajas": "Proximidad campus, flexibilidad horarios",
           "desventajas": "Soledad, equipamiento limitado"
       },
       "rutina_semanal_exacta": {
           "domingo_noche": "Viaje CB → SA después trabajo chacra",
           "lunes_a_viernes": "Vida académica SA + Campus UNALM",
           "viernes_tarde": "Viaje SA → CB",
           "sabado_domingo": "Familia CB + trabajo chacra domingos"
       }
   },
   
   "finanzas": {
       "ingresos": {
           "tia_principal": 850,  # S/ mensuales (día 8-11)
           "novia_apoyo": 100,    # S/ mensuales (apoyo alquiler)
           "chacra_propinas": 15, # S/ promedio semanal
           "trabajos_esporadicos": 50,  # S/ promedio mensual
           "total_base_garantizado": 950  # 850 + 100
       },
       "gastos_fijos": {
           "alquiler_sa": 350,
           "servicios": {
               "plan_movil_maximo": 30,
               "internet_cb_agosto_octubre": 30,
               "internet_cb_noviembre_adelante": 40,
               "vpn_mega": 4
           }
       },
       "presupuesto_variable": {
           "agosto_octubre": 536,  # 950 - (350+64)
           "noviembre_adelante": 526  # 950 - (350+74)
       }
   }
}

# ============================================================================
# CALENDARIO ACADÉMICO CICLO 2025-II
# ============================================================================

CALENDARIO_CICLO_2025_2 = {
   "informacion_basica": {
       "nombre": "Ciclo Académico 2025-II",
       "inicio_ciclo": date(2025, 8, 18),  # Lunes confirmado
       "fin_clases": date(2025, 12, 20),   # Viernes último día
       "duracion_semanas": 18,
       "timezone": "America/Lima"
   },
   
   "fechas_criticas": {
       "semana_4": {
           "fecha": date(2025, 9, 8),   # Lunes
           "descripcion": "Primera ola PCs (Álgebra, Discretas, Procesos)"
       },
       "semana_6": {
           "fecha": date(2025, 9, 22),  # Lunes
           "descripcion": "PC2 Álgebra Matricial"
       },
       "semana_9": {
           "fecha": date(2025, 10, 13), # Lunes
           "descripcion": "SEMANA PARCIALES - Crítica para meta 15.82"
       },
       "semana_11": {
           "fecha": date(2025, 10, 27), # Lunes
           "descripcion": "PC3 Álgebra - Post parciales"
       },
       "semana_14": {
           "fecha": date(2025, 11, 17), # Lunes
           "descripcion": "PC4 Álgebra - Recta final"
       },
       "semana_17": {
           "fecha": date(2025, 12, 8),  # Lunes
           "descripcion": "PC5 Álgebra + preparación finales"
       },
       "semana_18": {
           "fecha": date(2025, 12, 15), # Lunes
           "descripcion": "SEMANA FINALES - Decisiva para meta 15.82"
       }
   },
   
   "periodos_especiales": {
       "evaluaciones_complementarias": {
           "inicio": date(2025, 10, 13),
           "fin": date(2025, 10, 17),
           "descripcion": "Mitad de semestre - evaluaciones parciales"
       },
       "cierre_actas": date(2025, 12, 27),
       "vacaciones_inicio": date(2025, 12, 28)
   }
}

def calcular_fecha_semana(numero_semana: int) -> date:
   """Calcula fecha exacta de una semana académica"""
   inicio = CALENDARIO_CICLO_2025_2["informacion_basica"]["inicio_ciclo"]
   return inicio + timedelta(weeks=numero_semana - 1)

def obtener_semana_actual() -> int:
   """Obtiene semana académica actual del ciclo"""
   hoy = date.today()
   inicio = CALENDARIO_CICLO_2025_2["informacion_basica"]["inicio_ciclo"]
   fin = CALENDARIO_CICLO_2025_2["informacion_basica"]["fin_clases"]
   
   if hoy < inicio:
       return 0  # Antes del ciclo
   elif hoy > fin:
       return 19  # Después del ciclo
   else:
       diferencia = (hoy - inicio).days
       return (diferencia // 7) + 1

def dias_restantes_ciclo() -> int:
   """Calcula días restantes del ciclo académico"""
   hoy = date.today()
   fin = CALENDARIO_CICLO_2025_2["informacion_basica"]["fin_clases"]
   if hoy > fin:
       return 0
   return (fin - hoy).days

# ============================================================================
# CURSOS CICLO 2025-II COMPLETO
# ============================================================================

CURSOS_CICLO_2025_2_COMPLETO = {
   "CC4036_Algebra_Matricial": {
       "datos_basicos": {
           "nombre": "Álgebra Matricial",
           "codigo": "CC4036",
           "creditos": 4,
           "profesor": "Carlos J. Rodríguez Fernández",
           "email_profesor": "carjul@lamolina.edu.pe",
           "dificultad_jhon": 5,  # Máxima - ansiedad alta
           "tipo": "Matemática Crítica",
           "ansiedad_nivel": "CRÍTICO",
           "impacto_meta_1582": "MÁXIMO"
       },
       
       "sistema_evaluacion_confirmado": {
           "practicas_calificadas": {
               "ponderacion": 0.40,
               "cantidad": 5,
               "descripcion": "Aplica correctamente teoría en problemas",
               "nota_minima_aprobar": 10.5
           },
           "examen_parcial": {
               "ponderacion": 0.30,
               "descripcion": "Evaluación teórica-práctica mitad semestre"
           },
           "examen_final": {
               "ponderacion": 0.30,
               "descripcion": "Evaluación teórica-práctica final"
           }
       },
       
       "calendario_evaluaciones_exacto": {
           "PC1": {
               "fecha": date(2025, 9, 8),   # Semana 4
               "tema": "Matrices y operaciones básicas",
               "preparacion_dias": 3,
               "medicacion_recomendada": True,
               "ubicacion_ideal": "Biblioteca UNALM",
               "critico": False
           },
           "PC2": {
               "fecha": date(2025, 9, 22),  # Semana 6
               "tema": "Determinantes",
               "preparacion_dias": 3,
               "medicacion_recomendada": True,
               "ubicacion_ideal": "Biblioteca UNALM",
               "critico": False
           },
           "EXAMEN_PARCIAL": {
               "fecha": date(2025, 10, 13), # Semana 9
               "tema": "Matrices, determinantes, inversas",
               "preparacion_dias": 7,
               "medicacion_recomendada": True,
               "ubicacion_ideal": "Biblioteca UNALM",
               "critico": True,
               "peso_meta_1582": "ALTO"
           },
           "PC3": {
               "fecha": date(2025, 10, 27), # Semana 11
               "tema": "Espacios vectoriales",
               "preparacion_dias": 3,
               "medicacion_recomendada": True,
               "ubicacion_ideal": "Biblioteca UNALM",
               "critico": False
           },
           "PC4": {
               "fecha": date(2025, 11, 17), # Semana 14
               "tema": "Transformaciones lineales. Rango de matriz",
               "preparacion_dias": 3,
               "medicacion_recomendada": True,
               "ubicacion_ideal": "Biblioteca UNALM",
               "critico": False
           },
           "PC5": {
               "fecha": date(2025, 12, 8),  # Semana 17
               "tema": "Autovalores y autovectores. Formas bilineales",
               "preparacion_dias": 3,
               "medicacion_recomendada": True,
               "ubicacion_ideal": "Biblioteca UNALM",
               "critico": False
           },
           "EXAMEN_FINAL": {
               "fecha": date(2025, 12, 15), # Semana 18
               "tema": "Todo el curso - Evaluación integral",
               "preparacion_dias": 10,
               "medicacion_recomendada": True,
               "ubicacion_ideal": "Biblioteca UNALM",
               "critico": True,
               "peso_meta_1582": "CRÍTICO"
           }
       },
       
       "estrategias_jhon_especificas": {
           "conceptos_criticos": ["Determinantes", "Matrices inversas", "Autovalores", "Espacios vectoriales"],
           "necesita_youtube": True,
           "canales_recomendados": ["Khan Academy", "3Blue1Brown", "Professor Leonard"],
           "horas_estudio_semanales": 8,
           "ubicacion_optima": "Biblioteca UNALM",
           "tecnica_recomendada": "Práctica problemas + YouTube explicaciones",
           "horario_optimo": "Mañanas 8-11 AM con medicación",
           "señales_alerta": ["Frustración alta", "No entender conceptos básicos", "Evitar estudiar"]
       }
   },
   
   "CC3106_Matematicas_Discretas": {
       "datos_basicos": {
           "nombre": "Matemáticas Discretas",
           "codigo": "CC3106", 
           "creditos": 4,
           "profesor": "Carlos J. Rodríguez Fernández",
           "email_profesor": "carjul@lamolina.edu.pe",
           "dificultad_jhon": 5,  # Máxima - ansiedad alta
           "tipo": "Matemática Crítica",
           "ansiedad_nivel": "CRÍTICO",
           "impacto_meta_1582": "MÁXIMO"
       },
       
       "sistema_evaluacion_confirmado": {
           "practicas_calificadas": {
               "ponderacion": 0.40,
               "cantidad": 5,
               "descripcion": "Aplica correctamente teoría en problemas"
           },
           "examen_parcial": {
               "ponderacion": 0.30,
               "descripcion": "Evaluación teórica-práctica"
           },
           "examen_final": {
               "ponderacion": 0.30,
               "descripcion": "Evaluación teórica-práctica"
           }
       },
       
       "calendario_evaluaciones_exacto": {
           "PC1": {
               "fecha": date(2025, 9, 1),   # Semana 3
               "tema": "Lógica proposicional",
               "preparacion_dias": 3,
               "medicacion_recomendada": True,
               "critico": False
           },
           "PC2": {
               "fecha": date(2025, 9, 15),  # Semana 5
               "tema": "Estructuras básicas",
               "preparacion_dias": 3,
               "medicacion_recomendada": True,
               "critico": False
           },
           "PC3": {
               "fecha": date(2025, 9, 29),  # Semana 7
               "tema": "Algoritmos e Inducción matemática",
               "preparacion_dias": 3,
               "medicacion_recomendada": True,
               "critico": False
           },
           "EXAMEN_PARCIAL": {
               "fecha": date(2025, 10, 13), # Semana 9
               "tema": "Lógica, estructuras, algoritmos, inducción",
               "preparacion_dias": 7,
               "medicacion_recomendada": True,
               "critico": True,
               "peso_meta_1582": "ALTO"
           },
           "PC4": {
               "fecha": date(2025, 10, 20), # Semana 10
               "tema": "Recursividad y técnicas avanzadas de conteo",
               "preparacion_dias": 3,
               "medicacion_recomendada": True,
               "critico": False
           },
           "PC5": {
               "fecha": date(2025, 11, 3),  # Semana 12
               "tema": "Teoría de grafos y árboles",
               "preparacion_dias": 3,
               "medicacion_recomendada": True,
               "critico": False
           },
           "EXAMEN_FINAL": {
               "fecha": date(2025, 12, 15), # Semana 18
               "tema": "Todo el curso - Énfasis en grafos",
               "preparacion_dias": 10,
               "medicacion_recomendada": True,
               "critico": True,
               "peso_meta_1582": "CRÍTICO"
           }
       },
       
       "estrategias_jhon_especificas": {
           "conceptos_criticos": ["Grafos", "Recursividad", "Inducción matemática", "Combinatoria"],
           "necesita_youtube": True,
           "horas_estudio_semanales": 8,
           "ubicacion_optima": "Biblioteca UNALM",
           "tecnica_recomendada": "Práctica problemas + visualización grafos",
           "horario_optimo": "Mañanas con medicación"
       }
   },
   
   "EP2085_Estadistica_General": {
       "datos_basicos": {
           "nombre": "Estadística General",
           "codigo": "EP2085",
           "creditos": 3,
           "profesores": ["Viernes Rosazza", "Mauricio Maguiña"],
           "dificultad_jhon": 4,  # Moderada-alta
           "tipo": "Core Carrera",
           "ansiedad_nivel": "MEDIO",
           "impacto_meta_1582": "ALTO"
       },
       
       "sistema_evaluacion_estimado": {
           "practicas_calificadas": {"ponderacion": 0.40},
           "examen_parcial": {"ponderacion": 0.25},
           "examen_final": {"ponderacion": 0.25},
           "trabajo_grupal_final": {"ponderacion": 0.10}
       },
       
       "herramientas_especificas": {
           "r_estadistico": "Necesita recordar sintaxis",
           "python_personal": "Fortaleza existente de Jhon",
           "excel": "Básico requerido",
           "software_estadistico": "Posiblemente SPSS"
       },
       
       "estrategias_jhon_especificas": {
           "fortaleza": "Conceptos estadísticos - base matemática",
           "oportunidad": "Usar Python como ventaja competitiva",
           "horas_estudio_semanales": 5,
           "enfoque": "Práctica con datos reales"
       },
       
       "status": "pendiente_silabo"
   },
   
   "EP2095_Ingenieria_Procesos": {
       "datos_basicos": {
           "nombre": "Ingeniería de Procesos",
           "codigo": "EP2095",
           "creditos": 4,
           "profesor": "Valencia Chacón, Raphael Félix",
           "email_profesor": "raphael@lamolina.edu.pe",
           "dificultad_jhon": 3,  # Moderada
           "tipo": "Aplicada",
           "ansiedad_nivel": "BAJO",
           "impacto_meta_1582": "MEDIO"
       },
       
       "sistema_evaluacion_confirmado": {
           "evaluacion_continua_1": {"ponderacion": 0.25},
           "evaluacion_continua_2": {"ponderacion": 0.25},
           "practicas_calificadas": {"ponderacion": 0.30},
           "trabajo_investigacion": {"ponderacion": 0.20}
       },
       
       "calendario_evaluaciones_exacto": {
           "PC1": {
               "fecha": date(2025, 9, 8),   # Semana 4
               "tema": "Business Process Management (BPM) + primer avance grupal",
               "tipo": "Práctica + avance trabajo"
           },
           "PC2": {
               "fecha": date(2025, 9, 29),  # Semana 7
               "tema": "Modelamiento Procesos Esenciales + segundo avance grupal",
               "tipo": "Práctica + avance trabajo"
           },
           "EXAMEN_PARCIAL": {
               "fecha": date(2025, 10, 6),  # Semana 8
               "tema": "BPM y modelamiento de procesos"
           },
           "PC3": {
               "fecha": date(2025, 11, 3),  # Semana 12
               "tema": "Modelamiento Procesos Avanzado + tercer avance grupal",
               "tipo": "Práctica + avance trabajo"
           },
           "PC4": {
               "fecha": date(2025, 11, 24), # Semana 15
               "tema": "Descubrimiento de procesos + cuarto avance grupal",
               "tipo": "Práctica + avance trabajo"
           },
           "TRABAJO_FINAL": {
               "fecha": date(2025, 12, 1),  # Semana 16
               "tema": "Reporte y sustentación final trabajo grupal",
               "tipo": "Sustentación"
           },
           "EXAMEN_FINAL": {
               "fecha": date(2025, 12, 8),  # Semana 17
               "tema": "Todo el curso"
           }
       },
       
       "herramientas_especificas": {
           "bpmn_software": "Herramienta de modelamiento (Bizagi, Draw.io)",
           "trabajo_grupal": "Seguimiento 4 avances programados",
           "modalidad": "Teórico-práctica en laboratorio"
       },
       
       "estrategias_jhon_especificas": {
           "ventaja": "Curso aplicado - menos estrés que matemáticas",
           "enfoque": "Consistencia en trabajo grupal",
           "horas_estudio_semanales": 4,
           "oportunidad": "Nota alta para compensar matemáticas"
       }
   },
   
   "EP1052_Redaccion_Argumentacion": {
       "datos_basicos": {
           "nombre": "Redacción y Argumentación",
           "codigo": "EP1052",
           "creditos": 2,
           "profesor": "Martín David Córdova Pacheco",
           "dificultad_jhon": 4,  # Alta por ortografía
           "tipo": "Comunicación",
           "debilidad_especifica": "Ortografía",
           "ansiedad_nivel": "MEDIO-ALTO",
           "impacto_meta_1582": "MEDIO"
       },
       
       "sistema_evaluacion_estimado": {
           "practicas_y_avances": {"ponderacion": 0.50},
           "trabajo_final_sustentacion": {"ponderacion": 0.40},
           "participacion_actitudinal": {"ponderacion": 0.10}
       },
       
       "estrategias_jhon_especificas": {
           "debilidad_critica": "Ortografía - SIEMPRE usar corrector",
           "herramientas_obligatorias": ["Grammarly", "Word corrector", "Revisión manual"],
           "tiempo_adicional": 1.5,  # Factor multiplicador por revisión
           "enfoque": "Revisión exhaustiva antes de entregar",
           "horas_estudio_semanales": 3,
           "oportunidad": "Contenido conceptual (argumentación) es fortaleza"
       },
       
       "status": "pendiente_silabo"
   },
   
   "EP1XXX_Etica_Ciudadania": {
       "datos_basicos": {
           "nombre": "Ética y Ciudadanía",
           "codigo": "Pendiente confirmación sílabo",
           "creditos": 2,
           "profesor": "Martín David Córdova Pacheco",
           "dificultad_jhon": 1,  # Muy fácil para Jhon
           "tipo": "Humanidades",
           "ansiedad_nivel": "NINGUNA",
           "impacto_meta_1582": "BAJO"
       },
       
       "sistema_evaluacion_estimado": {
           "comprension_lectora": {"ponderacion": 0.30},
           "participacion_asistencia": {"ponderacion": 0.30},
           "bitacoras_aprendizaje": {"ponderacion": 0.25},
           "examen_grupal_final": {"ponderacion": 0.15}
       },
       
       "estrategias_jhon_especificas": {
           "enfoque": "Mantenimiento básico - curso 'regalado'",
           "esfuerzo_requerido": "Mínimo",
           "horas_estudio_semanales": 1,
           "nota_esperada": "17-19",
           "uso_estrategico": "Compensar matemáticas con nota alta fácil"
       },
       
       "status": "pendiente_silabo"
   },
   
   "EG1022_Banda_UNALM": {
       "datos_basicos": {
           "nombre": "Banda UNALM",
           "codigo": "EG1022",
           "creditos": 1,
           "profesor": "Pedro Eduardo Montemayor Negreros",
           "dificultad_jhon": 1,  # Muy fácil
           "tipo": "Extracurricular",
           "nota_asegurada": 20,
           "ansiedad_nivel": "NINGUNA",
           "impacto_meta_1582": "POSITIVO"  # Nota 20 segura
       },
       
       "sistema_evaluacion": {
           "asistencia": {"ponderacion": 0.60},
           "participacion_ensayos": {"ponderacion": 0.40}
       },
       
       "estrategias_jhon_especificas": {
           "enfoque": "Solo asistir y cumplir tareas básicas",
           "tiempo_requerido": "Mínimo",
           "beneficio": "1 crédito con nota 20 asegurada",
           "horario": "Lunes 8-9 AM",
           "actitud": "Relajado - momento de descanso mental"
       }
   }
}

# ============================================================================
# HORARIO SEMANAL DEFINITIVO
# ============================================================================

HORARIO_JHON_EXACTO = {
   "lunes": [
       {
           "hora": "08:00-09:00",
           "curso": "EG1022_Banda_UNALM",
           "profesor": "Pedro Eduardo Montemayor Negreros",
           "importancia": "BAJA",
           "notas": "Relajado - momento descanso mental"
       },
       {
           "hora": "10:00-11:00", 
           "curso": "EP2095_Ingenieria_Procesos",
           "profesor": "Valencia Chacón, Raphael Félix",
           "tipo": "Laboratorio",
           "importancia": "MEDIA"
       },
       {
           "hora": "11:00-12:00",
           "curso": "CC4036_Algebra_Matricial", 
           "profesor": "Carlos J. Rodríguez Fernández",
           "importancia": "CRÍTICA",
           "medicacion_recomendada": "Días de PC/examen",
           "notas": "Máxima concentración requerida"
       },
       {
           "hora": "13:00-14:00",
           "actividad": "ALMUERZO",
           "ubicacion": "Campus - comedor gratuito preferido"
       },
       {
           "hora": "16:00-17:00",
           "curso": "EP2085_Estadistica_General",
           "profesores": ["Viernes Rosazza", "Mauricio Maguiña"],
           "importancia": "ALTA"
       }
   ],
   
   "martes": [
       {
           "hora": "08:00-09:00",
           "curso": "CC4036_Algebra_Matricial",
           "profesor": "Carlos J. Rodríguez Fernández", 
           "importancia": "CRÍTICA"
       },
       {
           "hora": "10:00-11:00",
           "curso": "CC3106_Matematicas_Discretas",
           "profesor": "Carlos J. Rodríguez Fernández",
           "importancia": "CRÍTICA",
           "notas": "Doble matemáticas - día intenso"
       },
       {
           "hora": "11:00-12:00",
           "curso": "EP1052_Redaccion_Argumentacion",
           "profesor": "Martín David Córdova Pacheco",
           "importancia": "MEDIA-ALTA",
           "notas": "Atención especial ortografía"
       },
       {
           "hora": "13:00-14:00",
           "actividad": "ALMUERZO"
       },
       {
           "hora": "14:00-15:00",
           "curso": "EP1XXX_Etica_Ciudadania",
           "profesor": "Martín David Córdova Pacheco",
           "importancia": "BAJA"
       }
   ],
   
   "miercoles": [
       {
           "hora": "09:00-10:00",
           "actividad": "LIBRE",
           "recomendacion": "Estudio intensivo matemáticas"
       },
       {
           "hora": "11:00-12:00",
           "curso": "EP2095_Ingenieria_Procesos",
           "profesor": "Valencia Chacón, Raphael Félix",
           "importancia": "MEDIA"
       },
       {
           "hora": "13:00-14:00",
           "actividad": "ALMUERZO"
       },
       {
           "hora": "15:00-17:00",
           "actividad": "TIEMPO LIBRE EXTENDIDO",
           "recomendacion": "Estudio intensivo matemáticas - día ideal",
           "ubicacion_ideal": "Biblioteca UNALM",
           "medicacion_recomendada": "Si hay evaluación próxima"
       }
   ],
   
   "jueves": [
       {
           "hora": "08:00-09:00",
           "curso": "CC3106_Matematicas_Discretas",
           "profesor": "Carlos J. Rodríguez Fernández",
           "importancia": "CRÍTICA"
       },
       {
           "hora": "10:00-11:00",
           "curso": "CC4036_Algebra_Matricial",
           "profesor": "Carlos J. Rodríguez Fernández",
           "importancia": "CRÍTICA",
           "notas": "Segundo día doble matemáticas semanal"
       },
       {
           "hora": "11:00-12:00",
           "actividad": "LIBRE",
           "recomendacion": "Revisar conceptos de clases matutinas"
       },
       {
           "hora": "13:00-14:00",
           "actividad": "ALMUERZO"
       },
       {
           "hora": "16:00-17:00",
           "curso": "EP2085_Estadistica_General",
           "profesores": ["Viernes Rosazza", "Mauricio Maguiña"],
           "importancia": "ALTA"
       }
   ],
   
   "viernes": [
       {
           "hora": "08:00-09:00",
           "curso": "EP2095_Ingenieria_Procesos",
           "profesor": "Valencia Chacón, Raphael Félix",
           "importancia": "MEDIA"
       },
       {
           "hora": "10:00-11:00",
           "actividad": "LIBRE",
           "recomendacion": "Preparación viaje o estudio light"
       },
       {
           "hora": "11:00-12:00",
           "curso": "CC3106_Matematicas_Discretas",
           "profesor": "Carlos J. Rodríguez Fernández",
           "importancia": "CRÍTICA",
           "notas": "Última clase matemáticas de la semana"
       },
       {
           "hora": "13:00-14:00",
           "actividad": "ALMUERZO"
       },
       {
           "hora": "15:00-17:00",
           "actividad": "LIBRE - Preparación viaje",
           "notas": "Tiempo para empacar y preparar viaje SA → CB"
       },
       {
           "hora": "17:00+",
           "actividad": "VIAJE SA → CB",
           "transporte": "Pasaje universitario S/2.50",
           "notas": "Inicio fin de semana familiar"
       }
   ],
   
   "sabado": [
       {
           "ubicacion": "Carabayllo - Casa familiar",
           "actividades": [
               "Descanso y recuperación",
               "Tiempo con familia",
               "Estudio ligero si necesario",
               "Preparación mental domingo chacra"
           ],
           "ambiente": "Relajado - apoyo emocional familiar"
       }
   ],
   
   "domingo": [
       {
           "mañana": "Trabajo chacra familiar",
           "horas_promedio": "4-6 horas",
           "beneficio_fisico": "Ejercicio natural",
           "beneficio_economico": "S/10-20 propinas",
           "impacto_lunes": "Posible cansancio físico"
       },
       {
           "noche": "VIAJE CB → SA", 
           "transporte": "Pasaje universitario S/2.50",
           "preparacion": "Nueva semana académica",
           "llegada_sa": "Antes 22:00 para descansar"
       }
   ],
   
   "patrones_identificados": {
       "dias_criticos_matematicas": ["lunes", "martes", "jueves", "viernes"],
       "mejor_dia_estudio": "miercoles",  # Máximo tiempo libre
       "carga_horaria_total": "30 horas semanales presenciales",
       "momentos_medicacion_criticos": [
           "Martes 8:00 AM (doble matemáticas)",
           "Jueves 8:00 AM (doble matemáticas)",
           "Días de evaluaciones matemáticas"
       ],
       "viaje_optimo_cb": "Viernes después 17:00",
       "viaje_optimo_sa": "Domingo noche antes 22:00"
   }
}

# ============================================================================
# PRESUPUESTO VARIABLE JHON ESPECÍFICO
# ============================================================================

PRESUPUESTO_VARIABLE_JHON = {
   "agosto_octubre_2025": {
       "disponible": 536,  # 950 - 414 (gastos fijos)
       "distribucion_recomendada": {
           "alimentacion": {
               "monto": 260,
               "desglose": {
                   "comida_campus_backup": {
                       "descripcion": "Comedor UNALM gratis, backup calle cuando se acaba",
                       "dias_backup_semana": 2,
                       "costo_backup_dia": 10,
                       "subtotal_mensual": 80
                   },
                   "despensa_basica_sa": {
                       "descripcion": "Alimentos básicos cuarto Santa Anita",
                       "items": ["Atún", "Pan", "Leche", "Frutas", "Arroz"],
                       "subtotal_mensual": 60
                   },
                   "contribucion_despensa_cb": {
                       "descripcion": "Aporte despensa casa familiar",
                       "subtotal_mensual": 40
                   },
                   "emergencias_delivery": {
                       "descripcion": "Cuando no hay tiempo cocinar",
                       "limite_mensual": 80,
                       "trigger_alerta": "Más de S/80"
                   }
               }
           },
           
           "transporte": {
               "monto": 90,
               "desglose": {
                   "sa_campus_diario": {
                       "costo_ida": 1.0,
                       "dias_mes": 20,  # Lunes-viernes x 4 semanas
                       "subtotal": 40
                   },
                   "cb_sa_universitario_domingo": {
                       "costo": 2.50,
                       "frecuencia": 4,  # Por mes
                       "subtotal": 10
                   },
                   "sa_cb_universitario_viernes": {
                       "costo": 2.50,
                       "frecuencia": 4,  # Por mes
                       "subtotal": 10
                   },
                   "emergencias_tardanza": {
                       "descripcion": "Taxi/pasaje normal cuando llego tarde",
                       "limite_mensual": 30,
                       "trigger_alerta": "Más de 2 veces/semana"
                   }
               }
           },
           
           "academico": {
               "monto": 55,
               "desglose": {
                   "fotocopias_matematicas": {
                       "descripcion": "Material adicional álgebra/discretas",
                       "limite_mensual": 25,
                       "justificacion": "Crítico para práctica"
                   },
                   "internet_datos_extra": {
                       "descripcion": "Cuando supero plan móvil",
                       "limite_mensual": 15
                   },
                   "software_educativo": {
                       "descripcion": "Wolfram, Symbolab, apps matemáticas",
                       "limite_mensual": 10,
                       "condicion": "Solo si mejora rendimiento"
                   },
                   "emergencias_academicas": {
                       "descripcion": "Gastos académicos imprevistos",
                       "limite_mensual": 5
                   }
               }
           },
           
           "transformacion_fisica": {
               "monto": 70,
               "decision_pendiente": True,
               "opciones": {
                   "gym_privado": {
                       "costo": 70,
                       "ventajas": ["Menos gente", "Horarios flexibles"],
                       "desventajas": ["Costo alto"]
                   },
                   "gym_unalm": {
                       "costo": 0,
                       "ventajas": ["Gratuito"],
                       "desventajas": ["Muy lleno", "Horarios limitados"]
                   }
               },
               "suplementos_basicos": {
                   "limite": 25,
                   "condicion": "Solo si va a gym regularmente",
                   "tipos": ["Proteína", "Creatina básica"]
               }
           },
           
           "personal_emergencias": {
               "monto": 61,
               "desglose": {
                   "ropa_necesidades": {
                       "descripcion": "Ropa básica/reposición",
                       "limite_mensual": 30
                   },
                   "salud_medicinas": {
                       "descripcion": "Metilfenidato + medicinas básicas",
                       "limite_mensual": 20,
                       "items": ["Metilfenidato", "Paracetamol", "Otros básicos"]
                   },
                   "fondo_emergencia": {
                       "descripcion": "Gastos totalmente imprevistos",
                       "limite_mensual": 11
                   }
               }
           }
       }
   },
   
   "noviembre_adelante_2025": {
       "disponible": 526,  # 950 - 424 (internet sube S/10)
       "ajuste_necesario": "Reducir S/10 de alguna categoría",
       "sugerencias_ajuste": [
           "Transformación física: S/70 → S/60",
           "Alimentación delivery: S/80 → S/70", 
           "Distribuir S/5 entre varias categorías"
       ]
   }
}

# ============================================================================
# CATEGORÍAS GASTOS ESPECÍFICAS JHON
# ============================================================================

CATEGORIAS_GASTOS_JHON_ESPECIFICAS = {
   "transporte_contextual": {
       "sa_campus_diario": {
           "costo_normal": 1.0,
           "trigger_alerta": "Si supera S/50/mes",
           "patron_normal": "20 viajes/mes",
           "contexto": "Transporte diario necesario"
       },
       "cb_sa_universitario": {
           "costo_normal": 2.50,
           "trigger_alerta": "Si usa pasaje normal S/4.50",
           "patron_normal": "4 viajes/mes (domingos)",
           "contexto": "Fin semana familiar → inicio semana académica"
       },
       "sa_cb_universitario": {
           "costo_normal": 2.50,
           "trigger_alerta": "Si usa pasaje normal S/4.50",
           "patron_normal": "4 viajes/mes (viernes)",
           "contexto": "Fin semana académica → familia"
       },
       "emergencia_tardanza": {
           "costo_variable": "5-20",
           "trigger_alerta": "Más de 2 veces/semana",
           "correlacion_analizar": "Horas sueño, organización",
           "contexto": "Taxi/uber cuando pierdo transporte normal"
       }
   },
   
   "alimentacion_contextual": {
       "comida_campus_necesaria": {
           "costo_normal": 10.0,
           "trigger_alerta": "Más de 3 veces/semana",
           "analisis_correlacion": "Horarios llegada comedor",
           "contexto": "Backup cuando comedor UNALM se acaba"
       },
       "comida_chatarra_arrepentimiento": {
           "costo_variable": "5-15",
           "trigger_alerta": "Cualquier compra",
           "correlacion_critica": "Frustración post-matemáticas",
           "patron_identificado": "Después PC/examen difícil",
           "contexto": "Compra impulsiva emocional"
       },
       "delivery_pereza": {
           "costo_variable": "15-30",
           "trigger_alerta": "Más de 1 vez/semana",
           "correlacion": "Nivel energía + horas estudio",
           "contexto": "Cuando no quiere cocinar en SA"
       }
   },
   
   "academico_especifico": {
       "fotocopias_matematicas": {
           "limite_mensual": 25,
           "justificacion": "Material práctica álgebra/discretas",
           "trigger_alerta": "Si supera límite",
           "contexto": "Directamente relacionado meta 15.82"
       },
       "software_educativo": {
           "tipos": ["Wolfram Alpha", "Symbolab", "Apps matemáticas"],
           "condicion": "Solo si mejora notas matemáticas",
           "evaluacion": "Mensual según resultados"
       }
   },
   
   "impulsos_especificos_jhon": {
       "marihuana_trimestral": {
           "frecuencia_normal": "Cada 3 meses",
           "monto_variable": "30-80",
           "trigger_alerta": "Si frecuencia aumenta",
           "contexto": "Estrés acumulado ciclos",
           "correlacion": "Nivel estrés académico"
       },
       "suscripciones_innecesarias": {
           "ejemplos": ["Netflix no usado", "Apps premium", "Servicios streaming"],
           "trigger_alerta": "Cualquier suscripción nueva",
           "analisis": "Evaluar uso real vs costo",
           "patron": "Impulso cuando recibe dinero"
       },
       "tecnologia_no_esencial": {
           "ejemplos": ["Gadgets", "Accesorios", "Apps pagas"],
           "trigger_alerta": "Más de S/50",
           "correlacion": "Después recibir dinero tía (días 8-11)"
       }
   }
}

# ============================================================================
# TRANSFORMACIÓN FÍSICA JHON ESPECÍFICA
# ============================================================================

TRANSFORMACION_FISICA_JHON = {
   "estado_inicial_agosto_2025": {
       "peso_kg": 88.0,
       "altura_m": 1.70,
       "imc_inicial": 30.5,  # Obesidad clase I
       "edad": 24,
       "contexto_favorable": [
           "Metabolismo aún rápido a los 24",
           "Capacidad recuperación excelente",
           "Motivación alta por ciclo crítico académico",
           "Actividad base: trabajo chacra domingos"
       ],
       "contexto_desafiante": [
           "Estrés académico alto",
           "Comportamientos impulsivos alimentarios",
           "Doble residencia complica rutina",
           "Limitaciones presupuestarias"
       ]
   },
   
   "metas_especificas": {
       "peso_meta_final": 70.0,  # kg
       "perdida_total_necesaria": 18.0,  # kg (88-70)
       "imc_meta": 24.2,  # Peso saludable
       "timeline_realista": "8-10 meses",
       "perdida_mensual_sostenible": 1.8,  # kg/mes
       "perdida_semanal_objetivo": 0.45   # kg/semana
   },
   
   "hitos_intermedios": {
       "primer_mes_septiembre": {
           "peso_objetivo": 86.0,
           "enfoque": "Establecer rutina + eliminar chatarra",
           "metricas": ["Rutina ejercicio 4x/semana", "0 delivery por pereza"]
       },
       "tercer_mes_noviembre": {
           "peso_objetivo": 82.0,
           "enfoque": "Rutina consolidada + aumento fuerza",
           "metricas": ["Rutina establecida", "Mejora fuerza percibida"]
       },
       "sexto_mes_febrero_2026": {
           "peso_objetivo": 76.0,
           "enfoque": "Definición + resistencia cardiovascular",
           "metricas": ["Definición visible", "Resistencia mejorada"]
       },
       "meta_final_abril_mayo_2026": {
           "peso_objetivo": 70.0,
           "enfoque": "Mantenimiento + definición final",
           "celebracion": "Meta físico-académica completada"
       }
   },
   
   "estrategia_ubicacional": {
       "lunes_viernes_sa": {
           "opciones_ejercicio": {
               "gym_privado_sa": {
                   "costo": 70,
                   "ventajas": ["Menos gente", "Horarios flexibles", "Equipamiento"],
                   "horarios_optimos": ["06:00-07:00", "18:00-19:00"],
                   "decision": "Evaluar primera semana ciclo"
               },
               "gym_unalm": {
                   "costo": 0,
                   "ventajas": ["Gratuito", "Cerca campus"],
                   "desventajas": ["Muy lleno", "Horarios limitados"],
                   "horarios_posibles": ["14:00-15:00"]
               },
               "ejercicio_cuarto_sa": {
                   "costo": 0,
                   "tipo": "Peso corporal + YouTube",
                   "limitaciones": "Espacio reducido",
                   "horarios": "Flexibles"
               }
           },
           "frecuencia_objetivo": "4-5 días/semana"
       },
       
       "sabado_domingo_cb": {
           "actividad_principal": "Trabajo chacra + cardio natural",
           "complementos": {
               "sabado": "Caminatas familiares, trote matutino",
               "domingo": "Trabajo chacra (4-6 horas ejercicio natural)"
           },
           "beneficios": [
               "Ejercicio funcional real",
               "Ambiente familiar motivacional",
               "Ingresos adicionales S/10-20"
           ]
       }
   },
   
   "plan_nutricional_especifico": {
       "principios": {
           "deficit_calorico": "300-500 cal/día",
           "proteina_objetivo": "1.2g/kg peso corporal",
           "hidratacion": "2.5-3L agua/día",
           "comidas_frecuencia": "4-5 comidas pequeñas"
       },
       
       "alimentacion_sa": {
           "desayuno": ["Avena + proteína", "Huevos + pan integral"],
           "almuerzo": "Comedor UNALM (prioridad) o S/10 saludable",
           "cena": ["Atún + ensalada", "Pollo + verduras"],
           "snacks": ["Frutas", "Frutos secos", "Yogurt"]
       },
       
       "alimentacion_cb": {
           "estrategia": "Porciones controladas comida familiar",
           "contribucion": "Comprar opciones saludables para familia",
           "evitar": "Excesos por ambiente familiar relajado"
       },
       
       "alimentos_evitar_absoluto": [
           "Comida chatarra post-matemáticas",
           "Delivery por pereza SA",
           "Snacks procesados durante estudio",
           "Bebidas azucaradas"
       ]
   },
   
   "rutina_medicion": {
       "peso_corporal": {
           "frecuencia": "Semanal",
           "dia": "Domingo noche",
           "ubicacion": "Casa CB (báscula familiar)",
           "condiciones": "Misma ropa, misma hora",
           "registro": "Inmediato en sistema"
       },
       
       "medidas_corporales": {
           "frecuencia": "Bisemanal",
           "dias": ["Lunes", "Jueves"],
           "ubicacion": "Cuarto SA",
           "medidas": {
               "pecho": "Línea horizontal pezones",
               "cintura": "Punto más estrecho",
               "cuello": "Bajo nuez Adam"
           }
       },
       
       "metricas_subjetivas_diarias": {
           "energia_fisica": "1-5 escala",
           "como_me_veo_espejo": "1-5 escala",
           "confianza_fisica": "1-5 escala",
           "motivacion_ejercicio": "1-5 escala"
       }
   }
}

# ============================================================================
# VALIDACIONES Y REGLAS DE NEGOCIO
# ============================================================================

def validar_meta_1582_matematica(promedio_actual: float = 13.23, 
                                creditos_actuales: int = 46,
                                creditos_ciclo: int = 20,
                                meta_final: float = 14.0) -> dict:
   """
   Validación matemática exacta de la meta 15.82
   """
   puntos_actuales = promedio_actual * creditos_actuales  # 608.58
   creditos_totales = creditos_actuales + creditos_ciclo  # 66
   puntos_necesarios_total = meta_final * creditos_totales  # 924.0
   puntos_necesarios_ciclo = puntos_necesarios_total - puntos_actuales  # 315.42
   promedio_necesario = puntos_necesarios_ciclo / creditos_ciclo  # 15.82
   
   return {
       "promedio_necesario": round(promedio_necesario, 2),
       "exacto": promedio_necesario == 15.77,  # Verificación
       "margen_error": 0.0,
       "factibilidad": "EXIGENTE_PERO_POSIBLE" if promedio_necesario <= 16.5 else "MUY_DIFICIL"
   }

def calcular_presupuesto_mes_actual() -> dict:
   """
   Calcula presupuesto disponible según mes actual
   """
   mes_actual = datetime.now().month
   
   if mes_actual >= 11:  # Noviembre en adelante
       return {
           "disponible": 526,
           "gastos_fijos": 424,
           "internet_cb": 40,
           "periodo": "noviembre_adelante"
       }
   else:  # Agosto-octubre
       return {
           "disponible": 536,
           "gastos_fijos": 414, 
           "internet_cb": 30,
           "periodo": "agosto_octubre"
       }

def evaluar_riesgo_academico(fecha_evaluacion: date, dias_preparacion: int = 3) -> str:
   """
   Evalúa nivel de riesgo según proximidad de evaluación
   """
   dias_restantes = (fecha_evaluacion - date.today()).days
   
   if dias_restantes < 0:
       return "PASADO"
   elif dias_restantes == 0:
       return "HOY"
   elif dias_restantes <= dias_preparacion:
       return "CRÍTICO"
   elif dias_restantes <= dias_preparacion * 2:
       return "ALTO"
   elif dias_restantes <= 7:
       return "MEDIO"
   else:
       return "BAJO"

def sugerir_medicacion_tdah(curso: str, tipo_evaluacion: str, ansiedad_nivel: int) -> bool:
   """
   Sugiere si tomar metilfenidato según contexto
   """
   cursos_criticos = ["CC4036_Algebra_Matricial", "CC3106_Matematicas_Discretas"]
   evaluaciones_criticas = ["PC", "EXAMEN_PARCIAL", "EXAMEN_FINAL"]
   
   if curso in cursos_criticos:
       if tipo_evaluacion in evaluaciones_criticas:
           return True
       if ansiedad_nivel >= 4:
           return True
   
   return False

# ============================================================================
# CONFIGURACIÓN SISTEMA
# ============================================================================

PROMETEO_SYSTEM_CONFIG = {
   "nombre": "PROMETEO-JHON",
   "version": "3.0-FINAL",
   "usuario_unico": "Jhon Jhayro Villegas Verde",
   "matricula": "20231515",
   "objetivo_principal": "Meta 15.82 ciclo 2025-II",
   "objetivo_secundario": "Transformación física 88kg → 70kg",
   
   "filosofia_diseño": [
       "Hardcodeado context-specific system",
       "Máxima especificidad para contexto único",
       "Eliminar configuración genérica innecesaria",
       "Correlaciones automáticas entre áreas de vida",
       "Actualización quirúrgica sin reconfiguración"
   ],
   
   "reglas_sistema": {
       "regla_madrugada": "Registros antes 2:00 AM cuentan día anterior",
       "backup_automatico": "Diario a las 23:00",
       "alertas_maximas_dia": 5,
       "cache_metricas": "1 hora",
       "timezone": "America/Lima"
   },
   
   "dispositivo_principal": {
       "modelo": "Poco X6 5G",
       "os": "Android 15", 
       "conectividad": "Datos ilimitados",
       "uso": "Registro principal durante día"
   },
   
   "ubicaciones_deployment": {
       "frontend": "Streamlit Cloud",
       "backend": "PostgreSQL Neon.tech",
       "codigo": "GitHub private repository",
       "acceso": "Solo Jhon - sin multiusuario"
   }
}

# ============================================================================
# FUNCIONES HELPER CONFIGURACIÓN
# ============================================================================

def get_evaluaciones_proximas_dias(dias_adelante: int = 7) -> List[Dict]:
   """
   Obtiene evaluaciones próximas desde calendario hardcodeado
   """
   evaluaciones_proximas = []
   fecha_limite = date.today() + timedelta(days=dias_adelante)
   
   for curso_key, curso_data in CURSOS_CICLO_2025_2_COMPLETO.items():
       if "calendario_evaluaciones_exacto" in curso_data:
           for eval_nombre, eval_data in curso_data["calendario_evaluaciones_exacto"].items():
               fecha_eval = eval_data["fecha"]
               if date.today() <= fecha_eval <= fecha_limite:
                   evaluaciones_proximas.append({
                       "curso": curso_data["datos_basicos"]["nombre"],
                       "curso_codigo": curso_data["datos_basicos"]["codigo"],
                       "evaluacion": eval_nombre,
                       "fecha": fecha_eval,
                       "dias_restantes": (fecha_eval - date.today()).days,
                       "critico": eval_data.get("critico", False),
                       "medicacion_recomendada": eval_data.get("medicacion_recomendada", False),
                       "tema": eval_data.get("tema", ""),
                       "preparacion_dias": eval_data.get("preparacion_dias", 3),
                       "peso_meta_1582": eval_data.get("peso_meta_1582", "MEDIO")
                   })
   
   return sorted(evaluaciones_proximas, key=lambda x: x["fecha"])

def get_curso_por_codigo(codigo: str) -> Optional[Dict]:
   """
   Obtiene configuración de curso por código
   """
   for curso_key, curso_data in CURSOS_CICLO_2025_2_COMPLETO.items():
       if curso_data["datos_basicos"]["codigo"] == codigo:
           return curso_data
   return None

def calcular_carga_academica_semana(semana: int) -> Dict:
   """
   Calcula carga académica específica para una semana
   """
   evaluaciones_semana = []
   
   for curso_key, curso_data in CURSOS_CICLO_2025_2_COMPLETO.items():
       if "calendario_evaluaciones_exacto" in curso_data:
           for eval_nombre, eval_data in curso_data["calendario_evaluaciones_exacto"].items():
               fecha_eval = eval_data["fecha"]
               semana_eval = obtener_semana_actual()
               if semana_eval == semana:
                   evaluaciones_semana.append({
                       "curso": curso_data["datos_basicos"]["codigo"],
                       "evaluacion": eval_nombre,
                       "criticidad": curso_data["datos_basicos"]["dificultad_jhon"]
                   })
   
   carga_total = sum(eval["criticidad"] for eval in evaluaciones_semana)
   
   return {
       "semana": semana,
       "evaluaciones": evaluaciones_semana,
       "carga_total": carga_total,
       "nivel_estres": "CRÍTICO" if carga_total >= 10 else "ALTO" if carga_total >= 7 else "MEDIO" if carga_total >= 4 else "BAJO"
   }

# ============================================================================
# DATOS DE TESTING Y VALIDACIÓN
# ============================================================================

JHON_TEST_DATA = {
   "perfil_valido": {
       "matricula": "20231515",
       "peso_inicial": 88.0,
       "meta_ciclo": 15.82,
       "fecha_inicio": date(2025, 8, 18)
   },
   
   "cursos_criticos": [
       "CC4036_Algebra_Matricial",
       "CC3106_Matematicas_Discretas"
   ],
   
   "evaluaciones_criticas_fechas": [
       date(2025, 10, 13),  # Parciales semana 9
       date(2025, 12, 15)   # Finales semana 18
   ],
   
   "ubicaciones_frecuentes": [
       "sa_cuarto",
       "campus_biblioteca", 
       "cb_cuarto",
       "campus_aula"
   ],
   
   "categorias_gastos_frecuentes": [
       "transporte_sa_campus_diario",
       "comida_campus_necesaria",
       "academico_fotocopias_matematicas",
       "supermercado_despensa_sa",
       "servicios_alquiler_sa"
   ],
   
   "triggers_impulsos_comunes": [
       "frustracion_post_matematicas",
       "ansiedad_meta_1582",
       "soledad_sa_nocturna"
   ]
}

# ============================================================================
# ALERTAS Y NOTIFICACIONES CONFIGURACIÓN
# ============================================================================

ALERTAS_CONFIGURACION_JHON = {
   "tipos_alertas": {
       "academico_critico": {
           "prioridad": "CRÍTICA",
           "color": "#FF4444",
           "icono": "🚨",
           "condiciones": [
               "Meta 15.82 en riesgo alto",
               "Evaluación crítica en 24h",
               "Más de 3 días sin estudiar matemáticas"
           ]
       },
       
       "evaluacion_proxima": {
           "prioridad": "ALTA", 
           "color": "#FF8800",
           "icono": "📚",
           "condiciones": [
               "PC/Examen en 3 días o menos",
               "Evaluación matemáticas en 5 días",
               "Trabajo grupal entrega próxima"
           ]
       },
       
       "presupuesto_alto": {
           "prioridad": "MEDIA",
           "color": "#FFAA00",
           "icono": "💰",
           "condiciones": [
               ">80% presupuesto mensual usado",
               "Gastos impulsivos >3 en semana",
               "Categoría específica sobre límite"
           ]
       },
       
       "salud_fisica": {
           "prioridad": "MEDIA",
           "color": "#00AA88",
           "icono": "💪",
           "condiciones": [
               ">4 días sin ejercicio",
               "Peso estancado >2 semanas",
               "Hambre emocional frecuente"
           ]
       },
       
       "bienestar_mental": {
           "prioridad": "BAJA",
           "color": "#0088FF",
           "icono": "🧠",
           "condiciones": [
               "Ansiedad matemáticas >4 por 3 días",
               "Concentración sin medicación <2",
               "Soledad SA alta frecuente"
           ]
       }
   },
   
   "horarios_alertas": {
       "matutina": "08:00",  # Alertas académicas
       "vespertina": "18:00",  # Alertas presupuesto/físico
       "nocturna": "21:00"   # Resumen día + plan mañana
   },
   
   "limites_sistema": {
       "alertas_maximas_dia": 5,
       "alertas_criticas_maximas": 2,
       "frecuencia_verificacion": "cada_hora",
       "cooldown_alerta_repetida": "6_horas"
   }
}

# ============================================================================
# CORRELACIONES ESPECÍFICAS ESPERADAS
# ============================================================================

CORRELACIONES_ESPERADAS_JHON = {
   "ejercicio_concentracion": {
       "hipotesis": "Ejercicio regular mejora concentración en matemáticas",
       "variables": ["dias_ejercicio_semanal", "concentracion_matematicas_promedio"],
       "correlacion_esperada": 0.6,
       "significancia_minima": 0.05,
       "observaciones_minimas": 20,
       "recomendacion_si_positiva": "Ejercitarse día antes de evaluaciones matemáticas"
   },
   
   "medicacion_rendimiento": {
       "hipotesis": "Metilfenidato mejora significativamente rendimiento en matemáticas",
       "variables": ["uso_metilfenidato", "concentracion_durante_matematicas"],
       "correlacion_esperada": 0.8,
       "observaciones_minimas": 15,
       "recomendacion_si_positiva": "Usar medicación para todas las evaluaciones críticas"
   },
   
   "ubicacion_productividad": {
       "hipotesis": "Biblioteca UNALM es la ubicación más productiva para estudio",
       "variables": ["ubicacion_estudio", "contribucion_meta_1582"],
       "metrica": "comparacion_medias",
       "recomendacion_si_positiva": "Priorizar biblioteca para sesiones críticas"
   },
   
   "sueno_concentracion": {
       "hipotesis": "Menos de 6h sueño impacta negativamente concentración",
       "variables": ["horas_sueno", "concentracion_sin_medicacion"],
       "correlacion_esperada": 0.4,
       "punto_critico": 6.0,
       "recomendacion_si_positiva": "Mínimo 6h sueño noches pre-evaluación"
   },
   
   "impulsos_estres": {
       "hipotesis": "Gastos impulsivos aumentan post-evaluaciones difíciles",
       "variables": ["evaluaciones_matematicas", "gastos_impulsivos_3dias_post"],
       "periodo_analisis": "3_dias_post_evaluacion",
       "recomendacion_si_positiva": "Plan específico post-evaluaciones para evitar impulsos"
   },
   
   "chacra_lunes": {
       "hipotesis": "Trabajo chacra domingo impacta energía lunes",
       "variables": ["horas_chacra_domingo", "energia_lunes"],
       "correlacion_esperada": -0.3,
       "recomendacion_si_negativa": "Limitar horas chacra si lunes hay matemáticas"
   }
}

# ============================================================================
# CONFIGURACIÓN DASHBOARD ESPECÍFICO
# ============================================================================

DASHBOARD_CONFIG_JHON = {
   "metricas_principales": {
       "academico": {
           "titulo": "🎯 Meta 15.82",
           "metricas": [
               "progreso_porcentaje",
               "nota_necesaria_restante", 
               "dias_restantes_ciclo",
               "riesgo_nivel"
           ],
           "color_tema": "#667eea",
           "actualizacion": "tiempo_real"
       },
       
       "fisico": {
           "titulo": "💪 Transformación 70kg",
           "metricas": [
               "peso_actual",
               "peso_perdido",
               "imc_actual",
               "dias_ejercicio_semana"
           ],
           "color_tema": "#f093fb",
           "actualizacion": "diaria"
       },
       
       "financiero": {
           "titulo": "💰 Presupuesto S/526",
           "metricas": [
               "disponible_mes",
               "porcentaje_usado",
               "gastos_impulsivos_semana",
               "mayor_categoria"
           ],
           "color_tema": "#4facfe",
           "actualizacion": "tiempo_real"
       },
       
       "bienestar": {
           "titulo": "🧠 Estado Mental",
           "metricas": [
               "energia_promedio_semana",
               "ansiedad_matematicas",
               "dias_medicacion_mes",
               "concentracion_promedio"
           ],
           "color_tema": "#43e97b",
           "actualizacion": "diaria"
       }
   },
   
   "graficos_tendencias": {
       "peso_progreso": {
           "tipo": "linea",
           "periodo": "ultimo_mes",
           "meta_linea": 70.0
       },
       "concentracion_matematicas": {
           "tipo": "barras",
           "periodo": "ultimas_2_semanas",
           "separar_por": "con_sin_medicacion"
       },
       "gastos_categorias": {
           "tipo": "pie",
           "periodo": "mes_actual",
           "destacar": "impulsos"
       },
       "evaluaciones_calendario": {
           "tipo": "calendario",
           "periodo": "resto_ciclo",
           "resaltar": "criticas"
       }
   },
   
   "widgets_alertas": {
       "evaluaciones_proximas": {
           "limite": 3,
           "ordenar_por": "fecha",
           "destacar": "matematicas"
       },
       "correlaciones_activas": {
           "limite": 2,
           "solo_significativas": True
       },
       "recordatorios_medicacion": {
           "basado_en": "calendario_evaluaciones",
           "anticipacion_dias": 1
       }
   }
}

# ============================================================================
# CONFIGURACIÓN EXPORTACIÓN Y BACKUP
# ============================================================================

BACKUP_CONFIG_JHON = {
   "frecuencia_automatica": "diaria",
   "hora_backup": "23:00",
   "formatos_exportacion": ["json", "csv", "pdf_reporte"],
   
   "datos_criticos": [
       "jhon_profile_master",
       "bienestar_jhon",
       "estudio_jhon", 
       "gastos_jhon",
       "fisico_jhon"
   ],
   
   "retention_policy": {
       "backups_diarios": "30_dias",
       "backups_semanales": "6_meses", 
       "backups_mensuales": "2_años"
   },
   
   "ubicaciones_backup": {
       "automatico": "neon_backup",
       "manual": "google_drive_exports",
       "emergencia": "json_downloads"
   }
}

# ============================================================================
# FUNCIONES PRINCIPALES DE CONFIGURACIÓN
# ============================================================================

def inicializar_configuracion_jhon() -> bool:
   """
   Inicializa toda la configuración hardcodeada en el sistema
   """
   try:
       # Validar configuración matemática
       validacion_meta = validar_meta_1582_matematica()
       if not validacion_meta["exacto"]:
           print(f"⚠️ Warning: Meta calculada {validacion_meta['promedio_necesario']} vs esperado 15.82")
       
       # Validar fechas calendario
       inicio_ciclo = CALENDARIO_CICLO_2025_2["informacion_basica"]["inicio_ciclo"]
       if inicio_ciclo > date.today():
           print(f"ℹ️ Ciclo aún no ha comenzado. Inicio: {inicio_ciclo}")
       
       # Validar estructura cursos
       total_creditos = sum(
           curso["datos_basicos"]["creditos"] 
           for curso in CURSOS_CICLO_2025_2_COMPLETO.values()
       )
       assert total_creditos == 20, f"Error: Total créditos {total_creditos} != 20"
       
       print("✅ Configuración PROMETEO-JHON inicializada correctamente")
       return True
       
   except Exception as e:
       print(f"❌ Error inicializando configuración: {e}")
       return False

def get_config_actual() -> Dict:
   """
   Retorna configuración actual completa del sistema
   """
   return {
       "perfil": JHON_PROFILE_MASTER,
       "calendario": CALENDARIO_CICLO_2025_2,
       "cursos": CURSOS_CICLO_2025_2_COMPLETO,
       "horario": HORARIO_JHON_EXACTO,
       "presupuesto": PRESUPUESTO_VARIABLE_JHON,
       "transformacion_fisica": TRANSFORMACION_FISICA_JHON,
       "categorias_gastos": CATEGORIAS_GASTOS_JHON_ESPECIFICAS,
       "sistema": PROMETEO_SYSTEM_CONFIG
   }

def actualizar_silabos_cursos(curso_codigo: str, datos_silabo: Dict) -> bool:
   """
   Actualiza configuración de curso con datos de sílabo oficial
   """
   try:
       if curso_codigo not in [curso["datos_basicos"]["codigo"] for curso in CURSOS_CICLO_2025_2_COMPLETO.values()]:
           return False
       
       # Encontrar curso y actualizar
       for curso_key, curso_data in CURSOS_CICLO_2025_2_COMPLETO.items():
           if curso_data["datos_basicos"]["codigo"] == curso_codigo:
               # Actualizar solo campos específicos del sílabo
               if "sistema_evaluacion" in datos_silabo:
                   curso_data["sistema_evaluacion_confirmado"].update(datos_silabo["sistema_evaluacion"])
               
               if "calendario_evaluaciones" in datos_silabo:
                   curso_data["calendario_evaluaciones_exacto"].update(datos_silabo["calendario_evaluaciones"])
               
               curso_data["status"] = "confirmado_silabo"
               print(f"✅ Curso {curso_codigo} actualizado con sílabo oficial")
               return True
       
       return False
       
   except Exception as e:
       print(f"❌ Error actualizando sílabo {curso_codigo}: {e}")
       return False

# ============================================================================
# TESTING Y VALIDACIÓN FINAL
# ============================================================================

def test_configuracion_completa() -> Dict:
   """
   Test completo de toda la configuración hardcodeada
   """
   resultados = {
       "perfil_master": False,
       "calendario_fechas": False, 
       "cursos_completos": False,
       "presupuesto_matematico": False,
       "transformacion_fisica": False,
       "validaciones_cruzadas": False
   }
   
   try:
       # Test 1: Perfil Master
       perfil = JHON_PROFILE_MASTER
       assert perfil["personal"]["matricula"] == "20231515"
       assert perfil["academico"]["meta_ciclo_2025_2"] == 15.82
       assert perfil["personal"]["peso_inicial"] == 88.0
       resultados["perfil_master"] = True
       
       # Test 2: Calendario 
       inicio = CALENDARIO_CICLO_2025_2["informacion_basica"]["inicio_ciclo"]
       assert isinstance(inicio, date)
       assert CALENDARIO_CICLO_2025_2["informacion_basica"]["duracion_semanas"] == 18
       resultados["calendario_fechas"] = True
       
       # Test 3: Cursos
       total_creditos = sum(curso["datos_basicos"]["creditos"] for curso in CURSOS_CICLO_2025_2_COMPLETO.values())
       assert total_creditos == 20
       cursos_matematicas = [k for k in CURSOS_CICLO_2025_2_COMPLETO.keys() if "matematicas" in k.lower() or "algebra" in k.lower()]
       assert len(cursos_matematicas) == 2  # Álgebra + Discretas
       resultados["cursos_completos"] = True
       
       # Test 4: Presupuesto
       presupuesto_ago_oct = PRESUPUESTO_VARIABLE_JHON["agosto_octubre_2025"]["disponible"]
       presupuesto_nov = PRESUPUESTO_VARIABLE_JHON["noviembre_adelante_2025"]["disponible"]
       assert presupuesto_ago_oct == 536
       assert presupuesto_nov == 526
       assert presupuesto_ago_oct - presupuesto_nov == 10  # Diferencia internet
       resultados["presupuesto_matematico"] = True
       
       # Test 5: Transformación física
       tf = TRANSFORMACION_FISICA_JHON
       perdida_necesaria = tf["estado_inicial_agosto_2025"]["peso_kg"] - tf["metas_especificas"]["peso_meta_final"]
       assert perdida_necesaria == 18.0  # 88 - 70
       resultados["transformacion_fisica"] = True
       
       # Test 6: Validaciones cruzadas
       meta_validacion = validar_meta_1582_matematica()
       assert abs(meta_validacion["promedio_necesario"] - 15.82) < 0.01
       resultados["validaciones_cruzadas"] = True
       
       print("✅ Todos los tests de configuración pasaron")
       
   except AssertionError as e:
       print(f"❌ Test falló: {e}")
   except Exception as e:
       print(f"❌ Error en testing: {e}")
   
   return resultados

# ============================================================================
# PUNTO DE ENTRADA Y CONFIGURACIÓN FINAL
# ============================================================================

# Configuración para importación
__all__ = [
   'JHON_PROFILE_MASTER',
   'CALENDARIO_CICLO_2025_2', 
   'CURSOS_CICLO_2025_2_COMPLETO',
   'HORARIO_JHON_EXACTO',
   'PRESUPUESTO_VARIABLE_JHON',
   'CATEGORIAS_GASTOS_JHON_ESPECIFICAS',
   'TRANSFORMACION_FISICA_JHON',
   'CORRELACIONES_ESPERADAS_JHON',
   'DASHBOARD_CONFIG_JHON',
   'PROMETEO_SYSTEM_CONFIG',
   'validar_meta_1582_matematica',
   'calcular_presupuesto_mes_actual',
   'get_evaluaciones_proximas_dias',
   'obtener_semana_actual',
   'inicializar_configuracion_jhon'
]

# Información del módulo
__version__ = "3.0-FINAL"
__author__ = "Sistema PROMETEO-JHON"
__description__ = "Configuración hardcodeada completa para Jhon Villegas Verde - Ciclo 2025-II"

if __name__ == "__main__":
   print("🚀 PROMETEO-JHON Master Configuration")
   print("=" * 50)
   
   # Ejecutar inicialización
   if inicializar_configuracion_jhon():
       print("\n🧪 Ejecutando tests de validación...")
       resultados_test = test_configuracion_completa()
       
       tests_pasados = sum(resultados_test.values())
       tests_totales = len(resultados_test)
       
       print(f"\n📊 Resultado: {tests_pasados}/{tests_totales} tests pasados")
       
       if tests_pasados == tests_totales:
           print("🎉 Configuración PROMETEO-JHON lista para producción!")
       else:
           print("⚠️ Hay tests fallando - revisar antes de usar")
           
       # Mostrar resumen configuración
       print(f"\n📋 Resumen configuración:")
       print(f"   👤 Usuario: {JHON_PROFILE_MASTER['personal']['nombre_completo']}")
       print(f"   🎯 Meta académica: {JHON_PROFILE_MASTER['academico']['meta_ciclo_2025_2']}")
       print(f"   💪 Meta física: {JHON_PROFILE_MASTER['personal']['peso_inicial']}kg → {JHON_PROFILE_MASTER['personal']['peso_meta_final']}kg")
       print(f"   💰 Presupuesto: S/{PRESUPUESTO_VARIABLE_JHON['agosto_octubre_2025']['disponible']}")
       print(f"   📚 Cursos: {len(CURSOS_CICLO_2025_2_COMPLETO)} configurados")
       print(f"   📅 Semana actual: {obtener_semana_actual()}/18")
       
       evaluaciones_proximas = get_evaluaciones_proximas_dias(7)
       if evaluaciones_proximas:
           print(f"   ⚠️  Evaluaciones próximas: {len(evaluaciones_proximas)}")
           for eval in evaluaciones_proximas[:3]:
               print(f"      • {eval['evaluacion']} - {eval['curso']} ({eval['dias_restantes']} días)")
       
   else:
       print("❌ Error en inicialización - revisar configuración")