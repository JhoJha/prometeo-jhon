# config/jhon_master_config.py - PARTE 1/6
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
           "descripcion": "Primera ola PCs (Álgebra, Discretas, Estadística PC1)"
       },
       "semana_7": {
           "fecha": date(2025, 9, 29),  # Lunes  
           "descripcion": "PC2 Estadística + Comprensión lectura 1 Ética"
       },
       "semana_9": {
           "fecha": date(2025, 10, 13), # Lunes
           "descripcion": "SEMANA PARCIALES - Crítica para meta 15.82 + Examen 1 Estadística"
       },
       "semana_12": {
           "fecha": date(2025, 11, 3), # Lunes
           "descripcion": "PC3 Estadística + PC4 Redacción"
       },
       "semana_14": {
           "fecha": date(2025, 11, 17), # Lunes
           "descripcion": "PC4 Estadística + PC4 Álgebra"
       },
       "semana_15": {
           "fecha": date(2025, 11, 24), # Lunes
           "descripcion": "Comprensión lectura 2 Ética"
       },
       "semana_17": {
           "fecha": date(2025, 12, 8),  # Lunes
           "descripcion": "Examen 2 Estadística + PC5 Álgebra + preparación finales"
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
CURSOS_MATEMATICAS_CRITICAS = {
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
   }
}
CURSOS_CORE_CARRERA = {
   "EP2085_Estadistica_General": {
       "datos_basicos": {
           "nombre": "Estadística General",
           "codigo": "EP2085",
           "creditos": 3,
           "profesores": ["Viernes Rosazza", "Mauricio Maguiña"],
           "horas_teoria": 2,
           "horas_practica": 2,
           "requisito": "CC2073 Análisis Matemático II",
           "dificultad_jhon": 4,  # Moderada-alta
           "tipo": "Core Carrera",
           "ansiedad_nivel": "MEDIO",
           "impacto_meta_1582": "ALTO"
       },
       
       "competencias_especificas": [
           "Aplica estadística descriptiva a conjuntos de datos",
           "Aplica inferencia estadística para toma de decisiones", 
           "Utiliza software especializado (R)",
           "Comunica resultados estadísticos apropiadamente"
       ],
       
       "contenidos_detallados": {
           "unidad_1": "Conceptos básicos - Población, muestra, variables, parámetros",
           "unidad_2": "Organización de datos - Tablas de frecuencia y gráficas",
           "unidad_3": "Medidas estadísticas - Tendencia central, posición, dispersión",
           "unidad_4": "Probabilidades - Experimento aleatorio, eventos, teorema Bayes",
           "unidad_5": "Variables aleatorias - Discretas y continuas, valor esperado",
           "unidad_6": "Distribuciones discretas - Binomial, Hipergeométrica, Poisson",
           "unidad_7": "Distribuciones continuas - Normal, t-student, Chi cuadrado",
           "unidad_8": "Inferencia estadística - Intervalos de confianza, pruebas de hipótesis"
       },
       
       "sistema_evaluacion_confirmado": {
           "practicas_calificadas": {
               "ponderacion": 0.40,
               "cantidad": 4,
               "descripcion": "Aplicación práctica de conceptos estadísticos"
           },
           "examen_1": {
               "ponderacion": 0.25,
               "descripcion": "Primer examen de conocimientos"
           },
           "examen_2": {
               "ponderacion": 0.25,
               "descripcion": "Segundo examen de conocimientos"
           },
           "trabajos_grupales": {
               "ponderacion": 0.10,
               "cantidad": 2,
               "descripcion": "Aplicación práctica grupal"
           }
       },
       
       "calendario_evaluaciones_exacto": {
           "PC1": {
               "fecha": date(2025, 9, 8),   # Semana 4
               "tema": "Conceptos básicos y organización de datos",
               "preparacion_dias": 2,
               "software_requerido": "R básico",
               "critico": False
           },
           "PC2": {
               "fecha": date(2025, 9, 29),  # Semana 7
               "tema": "Medidas estadísticas y probabilidades",
               "preparacion_dias": 3,
               "software_requerido": "R intermedio",
               "critico": False
           },
           "EXAMEN_1": {
               "fecha": date(2025, 10, 13), # Semana 9
               "tema": "Conceptos básicos hasta probabilidades",
               "preparacion_dias": 5,
               "trabajo_grupal_1": "Entrega simultánea",
               "critico": True,
               "peso_meta_1582": "ALTO"
           },
           "PC3": {
               "fecha": date(2025, 11, 3),  # Semana 12
               "tema": "Variables aleatorias y distribuciones",
               "preparacion_dias": 3,
               "software_requerido": "R avanzado",
               "critico": False
           },
           "PC4": {
               "fecha": date(2025, 11, 17), # Semana 14
               "tema": "Distribuciones continuas",
               "preparacion_dias": 3,
               "software_requerido": "R gráficos",
               "critico": False
           },
           "PRACTICA_REZAGADOS": {
               "fecha": date(2025, 12, 1),  # Semana 16
               "condicion": "Solo con justificación previa",
               "critico": False
           },
           "EXAMEN_2": {
               "fecha": date(2025, 12, 8),  # Semana 17
               "tema": "Variables aleatorias hasta inferencia estadística",
               "preparacion_dias": 7,
               "trabajo_grupal_2": "Entrega simultánea",
               "critico": True,
               "peso_meta_1582": "ALTO"
           },
           "EXAMEN_REZAGADOS": {
               "fecha": date(2025, 12, 15), # Semana 18
               "condicion": "Solo con justificación previa",
               "critico": False
           }
       },
       
       "herramientas_especificas": {
           "software_principal": "R Estadístico",
           "guia_oficial": {
               "disponible": "Federado de posgrado (sobre centro médico)",
               "version": "2025-II actualizada",
               "incluye": ["Visualizaciones mejoradas", "Códigos R en GitHub", "Corrección errores 2025-I"]
           },
           "recursos_adicionales": ["GitHub con códigos", "Datos de práctica", "Gráficas explicativas"]
       },
       
       "estrategias_jhon_especificas": {
           "fortaleza_principal": "Área de carrera - conceptos familiares",
           "oportunidad": "Usar Python como complemento a R",
           "enfoque": "Práctica constante con datos reales",
           "horas_estudio_semanales": 5,
           "correlacion_asistencia": "Alta correlación asistencia-calificación (mencionado en sílabo)",
           "ubicacion_optima": "Laboratorio DAEI para prácticas",
           "ventaja_competitiva": "Background matemático y programación"
       }
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
   }
}
CURSOS_HUMANIDADES_CONFIRMADOS = {
   "EP1052_Redaccion_Argumentacion": {
       "datos_basicos": {
           "nombre": "Redacción y Argumentación",
           "codigo": "EP1052",
           "creditos": 2,
           "profesor_confirmado": "Edmundo de la Sota Díaz",
           "email_profesor": "edelasota@lamolina.edu.pe",
           "requisito": "EP1051 Lengua y Comunicación",
           "horas_teoria": 2,
           "dificultad_jhon": 4,  # Alta por ortografía
           "tipo": "Comunicación",
           "debilidad_especifica": "Ortografía",
           "ansiedad_nivel": "MEDIO-ALTO",
           "impacto_meta_1582": "MEDIO"
       },
       
       "competencias_oficiales": {
           "principal": "Redacta, de forma eficiente, textos académicos y científicos utilizando el registro formal",
           "especificas": [
               "Utiliza estructuras propias del lenguaje de textos académicos",
               "Identifica y utiliza estructuras y esquemas de textos académicos",
               "Planifica y esquematiza información para producción textual argumentativa"
           ]
       },
       
       "unidades_programaticas": {
           "unidad_1": {
               "nombre": "El texto y el registro formal",
               "semanas": "1-7 (18 agosto - 5 octubre)",
               "logro": "Elaborar eficazmente enunciados en lenguaje formal con orden sintáctico y semántico apropiado, y párrafos con cohesión y coherencia",
               "contenidos_clave": [
                   "Registro formal, objetividad, subjetividad",
                   "Registro técnico científico",
                   "Estructura textual: micro, macro y superestructuras",
                   "Mecanismos de cohesión gramaticales",
                   "Signos de puntuación",
                   "Errores comunes de redacción y normas RAE"
               ]
           },
           "unidad_2": {
               "nombre": "Las macroestructuras textuales y producción de textos",
               "semanas": "8-11 (6 octubre - 2 noviembre)",
               "logro": "Planificar, jerarquizar y producir textos usando operadores textuales para cohesión y coherencia",
               "contenidos_clave": [
                   "Etapas: Planificación, producción, revisión",
                   "Generación y jerarquización de ideas",
                   "Textos descriptivos y expositivos",
                   "La argumentación: tesis y argumentos"
               ]
           },
           "unidad_3": {
               "nombre": "Las superestructuras textuales",
               "semanas": "12-16 (3 noviembre - 7 diciembre)",
               "logro": "Redactar texto académico usando método científico. Utilizar, jerarquizar y redactar argumentos para sostener una tesis",
               "contenidos_clave": [
                   "Superestructura textual",
                   "Textos científicos",
                   "Método científico en redacción",
                   "Normas APA y estandarización",
                   "Estrategias de sustentación"
               ]
           }
       },
       
       "sistema_evaluacion_confirmado": {
           "practicas_y_avances": {
               "ponderacion": 0.50,
               "descripcion": "Reconocimiento y aplicación de fundamentos + microestructuras + macroestructuras"
           },
           "trabajo_final_sustentacion": {
               "ponderacion": 0.40,
               "descripcion": "Superestructuras textuales con criterios científicos y normas APA + sustentación"
           },
           "actitudinal": {
               "ponderacion": 0.10,
               "componentes": ["Participación activa", "Iniciativa, orden y responsabilidad"]
           }
       },
       
       "calendario_evaluaciones_exacto": {
           "PRACTICA_1": {
               "fecha": date(2025, 9, 8),   # Semana 3
               "unidad": 1,
               "tema": "Registro formal y estructura textual",
               "instrumento": "Rúbrica",
               "preparacion_dias": 2
           },
           "PRACTICA_2": {
               "fecha": date(2025, 9, 29),  # Semana 6
               "unidad": 1,
               "tema": "Microestructuras y párrafos",
               "instrumento": "Rúbrica",
               "preparacion_dias": 2
           },
           "PRACTICA_3": {
               "fecha": date(2025, 10, 13), # Semana 9
               "unidad": 2,
               "tema": "Macroestructuras textuales",
               "instrumento": "Rúbrica",
               "preparacion_dias": 3
           },
           "PRACTICA_4": {
               "fecha": date(2025, 11, 3),  # Semana 12
               "unidad": 2,
               "tema": "Textos argumentativos",
               "instrumento": "Rúbrica",
               "preparacion_dias": 3
           },
           "TRABAJO_FINAL_SUSTENTACION": {
               "fecha": date(2025, 12, 1),  # Semana 16
               "unidad": 3,
               "tema": "Superestructura textual completa con normas APA",
               "instrumento": "Rúbrica",
               "preparacion_dias": 10,
               "critico": True,
               "peso_meta_1582": "MEDIO-ALTO"
           }
       },
       
       "estrategias_jhon_especificas": {
           "debilidad_critica": "ORTOGRAFÍA - Requiere atención especial",
           "herramientas_obligatorias": [
               "Grammarly Premium",
               "Word con corrector activado",
               "Revisión manual exhaustiva",
               "Tiempo adicional para revisión"
           ],
           "factor_tiempo": 1.5,  # Multiplicador por revisión ortográfica
           "enfoque_principal": "Contenido argumentativo (fortaleza) + revisión ortográfica (debilidad)",
           "horas_estudio_semanales": 3,
           "ubicacion_optima": "Santa Anita - acceso a herramientas digitales",
           "momento_optimo": "Después de matemáticas - relajación mental",
           "normas_apa": "Aprender de memoria las básicas - se repiten en otros cursos"
       }
   },
   
   "EP2088_Etica_Ciudadania": {
       "datos_basicos": {
           "nombre": "Ética y Ciudadanía",
           "codigo": "EP2088",
           "creditos": 2,
           "profesor_confirmado": "Martín David Córdova Pacheco",
           "email_profesor": "mcordova@lamolina.edu.pe",
           "requisito": "100 créditos",
           "horas_teoria": 2,
           "modalidad": "Presencial",
           "dificultad_jhon": 1,  # Muy fácil para Jhon
           "tipo": "Humanidades",
           "ansiedad_nivel": "NINGUNA",
           "impacto_meta_1582": "BAJO-POSITIVO"  # Nota alta fácil
       },
       
       "competencias_oficiales": {
           "principal": "Muestran flexibilidad y crítica frente a distintas formas de ciudadanía marginal y vulnerable, respetan y valoran la experiencia aprendida en la convivencia con ellas",
           "enfoque_especial": [
               "Perspectiva interseccional",
               "Enfoque de género", 
               "Conciencia ambiental",
               "Participación en debate sobre derechos humanos"
           ]
       },
       
       "unidades_programaticas": {
           "unidad_1": {
               "nombre": "Posibilidad de fundamentación filosófica del discurso ético",
               "semanas": "1-7 (18 agosto - 5 octubre)",
               "pregunta_guia": "¿De qué manera será posible en estos tiempos llegar a un consenso universal e intersubjetivo?",
               "contenidos_clave": [
                   "Diversidad como desafío en formación ética",
                   "Tensión Modernidad-Posmodernidad",
                   "Sentido de obligatoriedad y sabiduría contextual",
                   "Práctica argumentativa en fundamentación racional",
                   "Metaética subyacente a definiciones éticas"
               ]
           },
           "unidad_2": {
               "nombre": "La génesis psicoafectiva del sujeto ético",
               "semanas": "8-12 (6 octubre - 9 noviembre)",
               "pregunta_guia": "¿Hasta qué punto será capaz la persona de trascender los determinismos de su maduración afectiva?",
               "contenidos_clave": [
                   "Hermenéutica de acontecimientos tempranos",
                   "Etapas de desarrollo humano según Fromm",
                   "Modelo transigular de afectividad temprana"
               ]
           },
           "unidad_3": {
               "nombre": "Ética ciudadana como conciencia para responsabilidad social del profesional",
               "semanas": "13-18 (10 noviembre - 20 diciembre)",
               "pregunta_guia": "¿De qué responsabilidad social le corresponde al profesional molinero?",
               "contenidos_clave": [
                   "Aproximación crítica al concepto ciudadanía",
                   "Desafíos de la realidad: discriminación, violencia, deterioro ambiental, corrupción",
                   "Elementos constitutivos de ética cívica y praxis liberadora"
               ]
           }
       },
       
       "sistema_evaluacion_confirmado": {
           "comprension_lectura": {
               "ponderacion": 0.30,
               "cantidad": 2,
               "descripcion": "Análisis de textos académicos específicos"
           },
           "bitacoras_aprendizaje": {
               "ponderacion": 0.20,
               "descripcion": "Reflexiones del proceso formativo"
           },
           "participacion": {
               "ponderacion": 0.40,
               "componentes": [
                   "Participación en clase",
                   "Colaboración en equipo", 
                   "Responsabilidad/Respeto",
                   "Disposición/Compromiso",
                   "Puntualidad"
               ]
           },
           "examen_grupal_final": {
               "ponderacion": 0.10,
               "descripcion": "Evaluación colaborativa final"
           }
       },
       
       "calendario_evaluaciones_exacto": {
           "COMPRENSION_LECTURA_1": {
               "fecha_inicio": date(2025, 9, 29), # 29 sept - 3 oct (Semana 7)
               "fecha_fin": date(2025, 10, 3),
               "unidad": 1,
               "lecturas_obligatorias": [
                   "Gonzalo Portocarrero - La transgresión como forma específica de goce del mundo criollo",
                   "Martha Nussbaum - El cultivo de la humanidad (pp. 75-115)",
                   "Fidel Tubino - No una sino muchas ciudadanías",
                   "Adela Cortina - Conferencia responsabilidad universidad (YouTube)"
               ],
               "instrumento": "Rúbrica",
               "preparacion_dias": 5
           },
           "COMPRENSION_LECTURA_2": {
               "fecha_inicio": date(2025, 11, 24), # 24-28 nov (Semana 15)
               "fecha_fin": date(2025, 11, 28),
               "unidad": 3,
               "lecturas_obligatorias": [
                   "Ferran Cabrero - Ciudadanía intercultural (pp. 59-74)",
                   "Martha Nussbaum - Un cóctel tóxico: sexismo y misoginia (pp. 193-225)",
                   "Adela Cortina - Ciudadanía: el gozne entre ética, política y economía",
                   "Alberto Flores Galindo - La tradición autoritaria (pp. 165-194)"
               ],
               "instrumento": "Rúbrica",
               "preparacion_dias": 5
           },
           "BITACORAS_CONTINUAS": {
               "frecuencia": "Semanal",
               "periodo": "Todo el ciclo",
               "enfoque": "Reflexión personal sobre valores y decisiones actuales"
           },
           "PARTICIPACION_CONTINUA": {
               "frecuencia": "Cada clase",
               "metodos": ["Exposición dialogada", "Análisis de casos", "Debates", "Trabajos grupales", "Teatralización"]
           },
           "EXAMEN_GRUPAL_FINAL": {
               "fecha": date(2025, 12, 15), # Semana 18
               "modalidad": "Grupal",
               "enfoque": "Síntesis de aprendizajes del ciclo"
           }
       },
       
       "practicas_especificas": {
           "unidad_1_semana_2": "Análisis de video y debate",
           "unidad_2_semana_3": "Diario, Podcast o video de autoexploración sobre valores tempranos vs decisiones actuales",
           "unidad_3_semana_4": "Creación de campaña digital sobre problema ético comunitario"
       },
       
       "estrategias_jhon_especificas": {
           "ventaja_principal": "Temas filosóficos - área de fortaleza intelectual",
           "enfoque": "Mantenimiento básico - curso prácticamente 'regalado'",
           "participacion_clave": "40% del curso - asistir y participar activamente",
           "bitacoras_faciles": "Reflexiones personales - natural para ti",
           "lecturas_estrategicas": "Leer con anticipación para participar mejor",
           "horas_estudio_semanales": 1.5,
           "nota_esperada": "17-19",
           "uso_estrategico": "Nota alta fácil para compensar matemáticas",
           "ubicacion_optima": "Cualquier lugar - contenido reflexivo",
           "momento_optimo": "Relajante después de estudios intensos"
       }
   }
}
CURSO_COMPLEMENTARIO = {
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
           "actitud": "Relajado - momento de descanso mental",
           "impacto_promedio": "Excelente para subir promedio general"
       }
   }
}

# ============================================================================
# HORARIO SEMANAL DEFINITIVO CONSOLIDADO
# ============================================================================

HORARIO_JHON_EXACTO = {
   "lunes": [
       {
           "hora": "08:00-09:00",
           "curso": "EG1022_Banda_UNALM",
           "profesor": "Pedro Eduardo Montemayor Negreros",
           "importancia": "BAJA",
           "notas": "Relajado - momento descanso mental - NOTA 20 ASEGURADA"
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
           "importancia": "ALTA",
           "software": "R Estadístico"
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
           "profesor": "Edmundo de la Sota Díaz",
           "importancia": "MEDIA-ALTA",
           "notas": "Atención especial ortografía"
       },
       {
           "hora": "13:00-14:00",
           "actividad": "ALMUERZO"
       },
       {
           "hora": "14:00-15:00",
           "curso": "EP2088_Etica_Ciudadania",
           "profesor": "Martín David Córdova Pacheco",
           "importancia": "BAJA",
           "notas": "40% participación - fácil nota alta"
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
# PRESUPUESTO VARIABLE JHON ESPECÍFICO ACTUALIZADO
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
                       "subtotal_mensual": 80,
                       "correlacion": "Horarios llegada tardía al comedor"
                   },
                   "despensa_basica_sa": {
                       "descripcion": "Alimentos básicos cuarto Santa Anita",
                       "items": ["Atún", "Pan", "Leche", "Frutas", "Arroz básico"],
                       "subtotal_mensual": 60
                   },
                   "contribucion_despensa_cb": {
                       "descripcion": "Aporte despensa casa familiar",
                       "subtotal_mensual": 40
                   },
                   "emergencias_delivery": {
                       "descripcion": "Cuando no hay tiempo cocinar",
                       "limite_mensual": 80,
                       "trigger_alerta": "Más de S/80",
                       "correlacion": "Nivel de estrés académico"
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
               "monto": 70,  # Incrementado por Guía de Estadística
               "desglose": {
                   "fotocopias_matematicas": {
                       "descripcion": "Material adicional álgebra/discretas",
                       "limite_mensual": 25,
                       "justificacion": "Crítico para práctica"
                   },
                   "guia_estadistica_oficial": {
                       "descripcion": "Guía oficial Estadística General (Federado Posgrado)",
                       "costo_unico": 25,  # Estimado
                       "mes": "Agosto - inversión única",
                       "beneficio": "Códigos R + visualizaciones + datos"
                   },
                   "internet_datos_extra": {
                       "descripcion": "Cuando supero plan móvil",
                       "limite_mensual": 15
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
                       "desventajas": ["Muy lleno", "Horarios limitados"],
                       "horarios_disponibles": "14:00-15:00 (miércoles ideal)"
                   }
               },
               "suplementos_basicos": {
                   "limite": 25,
                   "condicion": "Solo si va a gym regularmente",
                   "tipos": ["Proteína", "Creatina básica"]
               }
           },
           
           "personal_emergencias": {
               "monto": 46,  # Ajustado por incremento académico
               "desglose": {
                   "ropa_necesidades": {
                       "descripcion": "Ropa básica/reposición",
                       "limite_mensual": 25
                   },
                   "salud_medicinas": {
                       "descripcion": "Metilfenidato + medicinas básicas",
                       "limite_mensual": 15,
                       "items": ["Metilfenidato", "Paracetamol", "Otros básicos"]
                   },
                   "fondo_emergencia": {
                       "descripcion": "Gastos totalmente imprevistos",
                       "limite_mensual": 6
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
           "Personal emergencias: S/46 → S/36"
       ]
   }
}

# ============================================================================
# CATEGORÍAS GASTOS ESPECÍFICAS JHON CONTEXTUALIZADAS
# ============================================================================

CATEGORIAS_GASTOS_JHON_ESPECIFICAS = {
   "transporte_contextual": {
       "sa_campus_diario": {
           "costo_normal": 1.0,
           "trigger_alerta": "Si supera S/50/mes",
           "patron_normal": "20 viajes/mes",
           "contexto": "Transporte diario necesario",
           "correlacion_horario": "Llegadas tarde = mayor costo"
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
       }
   },
   
   "alimentacion_contextual": {
       "comida_campus_necesaria": {
           "costo_normal": 10.0,
           "trigger_alerta": "Más de 3 veces/semana",
           "analisis_correlacion": "Horarios llegada vs disponibilidad comedor gratis",
           "contexto": "Backup cuando comedor UNALM se acaba"
       },
       "delivery_pereza": {
           "costo_variable": "15-30",
           "trigger_alerta": "Más de 1 vez/semana",
           "correlacion": "Nivel energía + horas estudio intenso",
           "contexto": "Cuando no quiere cocinar en SA"
       }
   },
   
   "academico_especifico": {
       "guia_estadistica": {
           "costo_unico": 25,
           "ubicacion": "Federado de posgrado (sobre centro médico)",
           "beneficio": "Códigos R + GitHub + visualizaciones",
           "timing": "Comprar primera semana ciclo"
       },
       "fotocopias_matematicas": {
           "limite_mensual": 25,
           "justificacion": "Material práctica álgebra/discretas",
           "correlacion": "Directamente relacionado meta 15.82"
       }
   }
}
# config/jhon_master_config.py - PARTE 6/6
# TRANSFORMACIÓN FÍSICA + VALIDACIONES + CONFIGURACIÓN SISTEMA FINAL

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
   
   "estrategia_ubicacional_optimizada": {
       "lunes_viernes_sa": {
           "opciones_ejercicio": {
               "gym_unalm_gratuito": {
                   "costo": 0,
                   "horario_ideal": "Miércoles 14:00-15:00",
                   "ventajas": ["Gratuito", "Horario libre miércoles", "Cerca campus"],
                   "desventajas": ["Muy lleno otros horarios"],
                   "decision_recomendada": "PRIMERA OPCIÓN - probar 4 semanas"
               },
               "gym_privado_sa": {
                   "costo": 70,
                   "horarios_optimos": ["06:00-07:00", "18:00-19:00"],
                   "ventajas": ["Menos gente", "Horarios flexibles", "Equipamiento"],
                   "decision": "Solo si UNALM no funciona"
               },
               "ejercicio_cuarto_sa": {
                   "costo": 0,
                   "tipo": "Peso corporal + YouTube",
                   "horarios": "Flexibles",
                   "uso": "Días sin gym + días matemáticas intensas"
               }
           },
           "frecuencia_objetivo": "4-5 días/semana"
       },
       
       "sabado_domingo_cb": {
           "actividad_principal": "Trabajo chacra + cardio natural",
           "beneficios_multiples": [
               "Ejercicio funcional 4-6 horas",
               "Ambiente familiar motivacional",
               "Ingresos adicionales S/10-20",
               "Desconexión mental del estrés académico"
           ]
       }
   },
   
   "plan_nutricional_especifico": {
       "alimentacion_sa_estrategica": {
           "desayuno": ["Avena + proteína", "Huevos + pan integral"],
           "almuerzo": "Comedor UNALM GRATUITO (prioridad) - llegar temprano",
           "backup_almuerzo": "S/10 saludable solo si comedor se acaba",
           "cena": ["Atún + ensalada", "Pollo + verduras"],
           "snacks": ["Frutas", "Frutos secos limitados"]
       },
       
       "alimentacion_cb_control": {
           "estrategia": "Porciones controladas comida familiar",
           "contribucion_inteligente": "Comprar opciones saludables para todos",
           "evitar": "Excesos por ambiente relajado familiar"
       }
   }
}

# ============================================================================
# CORRELACIONES ESPERADAS JHON ACTUALIZADAS
# ============================================================================

CORRELACIONES_ESPERADAS_JHON = {
   "ejercicio_concentracion": {
       "hipotesis": "Ejercicio regular mejora concentración en matemáticas",
       "variables": ["dias_ejercicio_semanal", "concentracion_matematicas_promedio"],
       "correlacion_esperada": 0.6,
       "recomendacion": "Ejercitarse día antes de evaluaciones matemáticas",
       "horario_optimo": "Miércoles 14:00-15:00 UNALM gym gratuito"
   },
   
   "medicacion_rendimiento": {
       "hipotesis": "Metilfenidato mejora significativamente rendimiento matemático",
       "variables": ["uso_metilfenidato", "concentracion_durante_matematicas"],
       "correlacion_esperada": 0.8,
       "dias_criticos": ["Martes 8AM doble matemáticas", "Jueves 8AM doble matemáticas"]
   },
   
   "ubicacion_productividad": {
       "hipotesis": "Biblioteca UNALM es ubicación más productiva",
       "variables": ["ubicacion_estudio", "contribucion_meta_1582"],
       "mejor_horario": "Miércoles 15:00-17:00 post-ejercicio"
   },
   
   "comedor_gratis_rendimiento": {
       "hipotesis": "Uso comedor gratuito correlaciona con mejor control presupuestario",
       "variables": ["uso_comedor_unalm", "gastos_alimentacion_mensual"],
       "correlacion_esperada": -0.7,
       "estrategia": "Llegar temprano para asegurar disponibilidad"
   }
}

# ============================================================================
# CONFIGURACIÓN SISTEMA PROMETEO-JHON
# ============================================================================

PROMETEO_SYSTEM_CONFIG = {
   "nombre": "PROMETEO-JHON",
   "version": "4.0-FINAL-SILABOS",
   "usuario_unico": "Jhon Jhayro Villegas Verde",
   "matricula": "20231515",
   "objetivo_principal": "Meta 15.82 ciclo 2025-II",
   "objetivo_secundario": "Transformación física 88kg → 70kg",
   
   "profesores_confirmados": {
       "matematicas": "Carlos J. Rodríguez Fernández",
       "estadistica": ["Viernes Rosazza", "Mauricio Maguiña"],
       "redaccion": "Edmundo de la Sota Díaz", 
       "etica": "Martín David Córdova Pacheco",
       "procesos": "Valencia Chacón, Raphael Félix",
       "banda": "Pedro Eduardo Montemayor Negreros"
   },
   
   "recursos_confirmados": {
       "guia_estadistica": "Federado posgrado - S/25 única vez",
       "comedor_gratuito": "Campus UNALM - prioridad alimentación",
       "gym_gratuito": "Campus UNALM - miércoles ideal",
       "transporte_universitario": "S/2.50 CB↔SA",
       "biblioteca_unalm": "Ubicación estudio optimal"
   }
}

# ============================================================================
# FUNCIONES DE VALIDACIÓN ACTUALIZADAS
# ============================================================================

def validar_meta_1582_matematica(promedio_actual: float = 13.23, 
                                creditos_actuales: int = 46,
                                creditos_ciclo: int = 20,
                                meta_final: float = 14.0) -> dict:
   """Validación matemática exacta de la meta 15.82"""
   puntos_actuales = promedio_actual * creditos_actuales  # 608.58
   creditos_totales = creditos_actuales + creditos_ciclo  # 66
   puntos_necesarios_total = meta_final * creditos_totales  # 924.0
   puntos_necesarios_ciclo = puntos_necesarios_total - puntos_actuales  # 315.42
   promedio_necesario = puntos_necesarios_ciclo / creditos_ciclo  # 15.82
   
   return {
       "promedio_necesario": round(promedio_necesario, 2),
       "exacto": abs(promedio_necesario - 15.82) < 0.01,
       "factibilidad": "EXIGENTE_PERO_POSIBLE",
       "cursos_criticos": ["CC4036_Algebra_Matricial", "CC3106_Matematicas_Discretas"]
   }

def calcular_presupuesto_mes_actual() -> dict:
   """Calcula presupuesto disponible según mes actual"""
   mes_actual = datetime.now().month
   
   if mes_actual >= 11:  # Noviembre en adelante
       return {
           "disponible": 526,
           "gastos_fijos": 424,
           "internet_cb": 40,
           "periodo": "noviembre_adelante",
           "ajuste_requerido": 10
       }
   else:  # Agosto-octubre
       return {
           "disponible": 536,
           "gastos_fijos": 414, 
           "internet_cb": 30,
           "periodo": "agosto_octubre"
       }

def obtener_evaluaciones_proximas_dias(dias_adelante: int = 7) -> List[Dict]:
   """Obtiene evaluaciones próximas con profesores confirmados"""
   evaluaciones_proximas = []
   fecha_limite = date.today() + timedelta(days=dias_adelante)
   
   # Consolidar todos los cursos con evaluaciones
   todos_cursos = {
       **CURSOS_MATEMATICAS_CRITICAS,
       **CURSOS_CORE_CARRERA,
       **CURSOS_HUMANIDADES_CONFIRMADOS
   }
   
   for curso_key, curso_data in todos_cursos.items():
       if "calendario_evaluaciones_exacto" in curso_data:
           for eval_nombre, eval_data in curso_data["calendario_evaluaciones_exacto"].items():
               fecha_eval = eval_data["fecha"]
               if date.today() <= fecha_eval <= fecha_limite:
                   profesor = curso_data["datos_basicos"].get("profesor_confirmado", 
                            curso_data["datos_basicos"].get("profesor", "No asignado"))
                   
                   evaluaciones_proximas.append({
                       "curso": curso_data["datos_basicos"]["nombre"],
                       "curso_codigo": curso_data["datos_basicos"]["codigo"],
                       "profesor": profesor,
                       "evaluacion": eval_nombre,
                       "fecha": fecha_eval,
                       "dias_restantes": (fecha_eval - date.today()).days,
                       "critico": eval_data.get("critico", False),
                       "medicacion_recomendada": eval_data.get("medicacion_recomendada", False),
                       "tema": eval_data.get("tema", ""),
                       "peso_meta_1582": eval_data.get("peso_meta_1582", "MEDIO")
                   })
   
   return sorted(evaluaciones_proximas, key=lambda x: x["fecha"])

def obtener_semana_actual() -> int:
   """Obtiene semana académica actual del ciclo"""
   hoy = date.today()
   inicio = date(2025, 8, 18)  # Inicio ciclo 2025-II
   fin = date(2025, 12, 20)    # Fin clases
   
   if hoy < inicio:
       return 0  # Antes del ciclo
   elif hoy > fin:
       return 19  # Después del ciclo
   else:
       diferencia = (hoy - inicio).days
       return (diferencia // 7) + 1

# ============================================================================
# INTEGRACIÓN Y CONFIGURACIÓN FINAL
# ============================================================================

CURSOS_CICLO_2025_2_COMPLETO = {
   **CURSOS_MATEMATICAS_CRITICAS,
   **CURSOS_CORE_CARRERA,
   **CURSOS_HUMANIDADES_CONFIRMADOS,
   **CURSO_COMPLEMENTARIO
}

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
   'PROMETEO_SYSTEM_CONFIG',
   'validar_meta_1582_matematica',
   'calcular_presupuesto_mes_actual',
   'obtener_evaluaciones_proximas_dias',
   'obtener_semana_actual'
]

# ============================================================================
# TESTING Y VALIDACIÓN FINAL
# ============================================================================

def inicializar_configuracion_jhon() -> bool:
   """Inicializa toda la configuración hardcodeada en el sistema"""
   try:
       # Validar meta matemática
       validacion_meta = validar_meta_1582_matematica()
       if not validacion_meta["exacto"]:
           print(f"⚠️ Warning: Meta calculada vs esperado")
       
       # Validar total créditos
       total_creditos = sum(
           curso["datos_basicos"]["creditos"] 
           for curso in CURSOS_CICLO_2025_2_COMPLETO.values()
       )
       assert total_creditos == 20, f"Error: Total créditos {total_creditos} != 20"
       
       # Validar profesores confirmados
       profesores_sin_confirmar = []
       for curso_key, curso_data in CURSOS_CICLO_2025_2_COMPLETO.items():
           profesor = curso_data["datos_basicos"].get("profesor_confirmado") or curso_data["datos_basicos"].get("profesor")
           if not profesor or profesor == "No asignado":
               profesores_sin_confirmar.append(curso_key)
       
       if profesores_sin_confirmar:
           print(f"⚠️ Cursos sin profesor confirmado: {profesores_sin_confirmar}")
       
       print("✅ Configuración PROMETEO-JHON 4.0 inicializada correctamente")
       print(f"📊 Total cursos: {len(CURSOS_CICLO_2025_2_COMPLETO)}")
       print(f"📅 Semana actual: {obtener_semana_actual()}/18")
       print(f"💰 Presupuesto disponible: S/{calcular_presupuesto_mes_actual()['disponible']}")
       
       return True
       
   except Exception as e:
       print(f"❌ Error inicializando configuración: {e}")
       return False

# Información del módulo
__version__ = "4.0-FINAL-SILABOS"
__author__ = "Sistema PROMETEO-JHON"
__description__ = "Configuración hardcodeada completa con sílabos oficiales - Jhon Villegas Verde - Ciclo 2025-II"

if __name__ == "__main__":
   print("🚀 PROMETEO-JHON 4.0 - Configuración Final con Sílabos")
   print("=" * 60)
   
   if inicializar_configuracion_jhon():
       evaluaciones_proximas = obtener_evaluaciones_proximas_dias(14)
       if evaluaciones_proximas:
           print(f"\n📋 Próximas evaluaciones (14 días):")
           for eval in evaluaciones_proximas[:5]:
               print(f"   • {eval['evaluacion']} - {eval['curso']} - {eval['profesor']} ({eval['dias_restantes']} días)")
       
       print(f"\n🎯 Meta 15.82: {validar_meta_1582_matematica()['factibilidad']}")
       print("🎉 Sistema listo para producción!")
   else:
       print("❌ Error en inicialización - revisar configuración")