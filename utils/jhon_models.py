# jhon_models.py - Modelos especÃ­ficos Jhon
# utils/jhon_models.py
# Modelos específicos PROMETEO-JHON
# Tablas hardcodeadas para contexto único de Jhon Villegas Verde

from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Boolean, Text, Time, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import date, datetime, time
import enum
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Importar Base desde config
from config.database import Base

# ============================================================================
# ENUMS ESPECÍFICOS JHON
# ============================================================================

class UbicacionJhonEnum(enum.Enum):
    """Ubicaciones granulares específicas de Jhon"""
    # Carabayllo específicas
    CB_CUARTO = "cb_cuarto"
    CB_SALA_FAMILIAR = "cb_sala_familiar"
    CB_CHACRA_TRABAJANDO = "cb_chacra_trabajando"
    CB_VIAJE_SA = "cb_viaje_sa"
    
    # Santa Anita específicas
    SA_CUARTO = "sa_cuarto"
    SA_VIAJE_CAMPUS = "sa_viaje_campus"
    SA_VIAJE_CB = "sa_viaje_cb"
    
    # Campus UNALM específicas
    CAMPUS_BIBLIOTECA = "campus_biblioteca"
    CAMPUS_AULA = "campus_aula"
    CAMPUS_LABORATORIO = "campus_laboratorio"
    CAMPUS_CAFETERIA = "campus_cafeteria"
    CAMPUS_EXTERIOR = "campus_exterior"
    
    # Otros contextos
    NOVIA_CASA = "novia_casa"
    TRANSPORTE_PUBLICO = "transporte_publico"

class CursoJhonEnum(enum.Enum):
    """Cursos específicos ciclo 2025-II"""
    CC4036_ALGEBRA_MATRICIAL = "cc4036_algebra_matricial"
    CC3106_MATEMATICAS_DISCRETAS = "cc3106_matematicas_discretas"
    EP2085_ESTADISTICA_GENERAL = "ep2085_estadistica_general"
    EP2095_INGENIERIA_PROCESOS = "ep2095_ingenieria_procesos"
    EP1052_REDACCION_ARGUMENTACION = "ep1052_redaccion_argumentacion"
    EP1XXX_ETICA_CIUDADANIA = "ep1xxx_etica_ciudadania"
    EG1022_BANDA_UNALM = "eg1022_banda_unalm"

class TriggerImpulsivoJhonEnum(enum.Enum):
    """Triggers específicos de impulsos de Jhon"""
    FRUSTRACION_POST_MATEMATICAS = "frustracion_post_matematicas"
    ANSIEDAD_META_1582 = "ansiedad_meta_1582"
    SOLEDAD_SA_NOCTURNA = "soledad_sa_nocturna"
    CANSANCIO_POST_CHACRA = "cansancio_post_chacra"
    PROCRASTINACION_ABURRIMIENTO = "procrastinacion_aburrimiento"
    LLEGUE_TARDE_ESTRES = "llegue_tarde_estres"
    RECIBIR_DINERO_TIA = "recibir_dinero_tia"
    PRESION_EVALUACION_CRITICA = "presion_evaluacion_critica"
    NO_IDENTIFICADO = "no_identificado"

class CategoriaGastoJhonEnum(enum.Enum):
    """Categorías específicas de gastos contextuales para Jhon"""
    # Transporte específico
    TRANSPORTE_SA_CAMPUS_DIARIO = "transporte_sa_campus_diario"
    TRANSPORTE_CB_SA_UNIVERSITARIO = "transporte_cb_sa_universitario"
    TRANSPORTE_SA_CB_UNIVERSITARIO = "transporte_sa_cb_universitario"
    TRANSPORTE_EMERGENCIA_TARDANZA = "transporte_emergencia_tardanza"
    TRANSPORTE_TAXI_UBER = "transporte_taxi_uber"
    
    # Alimentación contextual
    COMIDA_CAMPUS_NECESARIA = "comida_campus_necesaria"
    COMIDA_CHATARRA_ARREPENTIMIENTO = "comida_chatarra_arrepentimiento"
    SUPERMERCADO_DESPENSA_SA = "supermercado_despensa_sa"
    SUPERMERCADO_DESPENSA_CB = "supermercado_despensa_cb"
    DELIVERY_PEREZA = "delivery_pereza"
    
    # Académico específico
    ACADEMICO_FOTOCOPIAS_MATEMATICAS = "academico_fotocopias_matematicas"
    ACADEMICO_INTERNET_DATOS_EXTRA = "academico_internet_datos_extra"
    ACADEMICO_SOFTWARE_EDUCATIVO = "academico_software_educativo"
    ACADEMICO_MATERIALES_ESPECIALES = "academico_materiales_especiales"
    
    # Servicios fijos
    SERVICIOS_ALQUILER_SA = "servicios_alquiler_sa"
    SERVICIOS_INTERNET_CB = "servicios_internet_cb"
    SERVICIOS_PLAN_MOVIL = "servicios_plan_movil"
    SERVICIOS_VPN_MEGA = "servicios_vpn_mega"
    
    # Transformación física
    FISICO_GIMNASIO_PRIVADO = "fisico_gimnasio_privado"
    FISICO_SUPLEMENTOS_BASICOS = "fisico_suplementos_basicos"
    FISICO_ROPA_DEPORTIVA = "fisico_ropa_deportiva"
    FISICO_NUTRICION_ESPECIALIZADA = "fisico_nutricion_especializada"
    
    # Salud específica TDAH
    SALUD_METILFENIDATO = "salud_metilfenidato"
    SALUD_CONSULTA_MEDICA = "salud_consulta_medica"
    SALUD_OTROS_MEDICAMENTOS = "salud_otros_medicamentos"
    SALUD_FARMACIA_GENERAL = "salud_farmacia_general"
    
    # Impulsos específicos
    IMPULSO_MARIHUANA_TRIMESTRAL = "impulso_marihuana_trimestral"
    IMPULSO_SUSCRIPCIONES_INNECESARIAS = "impulso_suscripciones_innecesarias"
    IMPULSO_TECNOLOGIA_NO_ESENCIAL = "impulso_tecnologia_no_esencial"
    
    # Personal y emergencias
    PERSONAL_ROPA_NECESARIA = "personal_ropa_necesaria"
    EMERGENCIAS_IMPREVISTAS = "emergencias_imprevistas"
    
    # Otros
    OTROS_DESCRIPCION_LIBRE = "otros_descripcion_libre"

# ============================================================================
# TABLA MASTER - CONFIGURACIÓN ÚNICA JHON
# ============================================================================

class JhonProfileMaster(Base):
    """Tabla única con contexto hardcodeado completo de Jhon"""
    __tablename__ = 'jhon_profile_master'
    
    id = Column(Integer, primary_key=True, default=1)  # Solo un registro
    
    # DATOS ACADÉMICOS ACTUALES
    matricula = Column(String, default="20231515")
    universidad = Column(String, default="Universidad Nacional Agraria La Molina")
    carrera = Column(String, default="Estadística Informática")
    facultad = Column(String, default="Economía y Planificación")
    ciclo_actual = Column(String, default="2025-II")
    creditos_acumulados = Column(Integer, default=46)
    promedio_actual = Column(Float, default=13.23)
    meta_promedio_final = Column(Float, default=14.0)
    meta_ciclo_2025_2 = Column(Float, default=15.82)
    ranking_facultad = Column(String, default="133 de 251")
    ranking_carrera = Column(String, default="42 de 88")
    
    # DATOS FÍSICOS ACTUALES
    peso_inicial = Column(Float, default=88.0)  # ACTUALIZADO
    peso_meta = Column(Float, default=70.0)
    altura = Column(Float, default=1.70)
    imc_inicial = Column(Float, default=30.5)
    imc_meta = Column(Float, default=24.2)
    
    # CONFIGURACIÓN FINANCIERA
    ingreso_mensual_base = Column(Float, default=950.0)
    gastos_fijos_agosto_octubre = Column(Float, default=414.0)
    gastos_fijos_noviembre_adelante = Column(Float, default=424.0)
    presupuesto_variable_agosto_octubre = Column(Float, default=536.0)
    presupuesto_variable_noviembre_adelante = Column(Float, default=526.0)
    
    # CONFIGURACIÓN DISPOSITIVOS
    dispositivo_principal = Column(String, default="Poco X6 5G")
    sistema_operativo = Column(String, default="Android 15")
    plan_datos = Column(String, default="Ilimitado")
    
    # TIMESTAMPS
    fecha_inicio_sistema = Column(DateTime, default=datetime.utcnow)
    ultima_actualizacion = Column(DateTime, onupdate=datetime.utcnow)
    ciclo_academico_actual = Column(String, default="2025-II")

    def __repr__(self):
        return f"<JhonProfile(matricula={self.matricula}, promedio={self.promedio_actual})>"

# ============================================================================
# BIENESTAR ESPECÍFICO JHON
# ============================================================================

class BienestarJhon(Base):
    """Bienestar específico con campos hardcodeados para Jhon"""
    __tablename__ = 'bienestar_jhon'
    
    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False, unique=True)
    
    # CAMPOS BÁSICOS OBLIGATORIOS
    energia_nivel = Column(Integer, nullable=False)  # 1-5
    animo_nivel = Column(Integer, nullable=False)    # 1-5
    sueno_horas = Column(Float, nullable=False)      # 0-12
    
    # UBICACIÓN GRANULAR ESPECÍFICA JHON
    ubicacion_principal_dia = Column(String, nullable=False)  # UbicacionJhonEnum
    ubicacion_registro = Column(String, nullable=False)       # UbicacionJhonEnum
    
    # TDAH ESPECÍFICO
    concentracion_sin_medicacion = Column(Integer, default=3)  # 1-5
    tomo_metilfenidato = Column(Boolean, default=False)
    if_medicacion_hora = Column(Time, nullable=True)
    if_medicacion_motivo = Column(String, nullable=True)  # "PC Álgebra", "Examen Discretas"
    if_medicacion_efecto_percibido = Column(Integer, nullable=True)  # 1-5
    concentracion_con_medicacion = Column(Integer, nullable=True)  # 1-5
    
    # PRESIÓN META 15.82 ESPECÍFICA
    presion_matematicas_hoy = Column(Integer, default=3)        # Álgebra + Discretas
    presion_redaccion_ortografia = Column(Integer, default=3)   # Por debilidad ortografía
    presion_tiempo_ciclo = Column(Integer, default=3)           # "No me alcanza tiempo"
    confianza_meta_15_82_hoy = Column(Integer, default=3)       # Confianza específica meta
    ansiedad_evaluaciones_proximas = Column(Integer, default=3) # Por calendario evaluaciones
    
    # CONTROL COMPORTAMIENTOS ESPECÍFICOS JHON
    tiempo_lol_minutos = Column(Integer, default=0)
    tiempo_pornografia_minutos = Column(Integer, default=0)
    tiempo_estudio_productivo_total = Column(Integer, default=0)
    tiempo_youtube_educativo = Column(Integer, default=0)
    tiempo_redes_sociales = Column(Integer, default=0)
    
    # CONTEXTO UBICACIONAL ESPECÍFICO
    if_sa_soledad_nivel = Column(Integer, nullable=True)        # Solo si está en SA
    if_sa_extrano_familia = Column(Boolean, nullable=True)
    if_sa_productividad_cuarto = Column(Integer, nullable=True) # 1-5
    if_cb_apoyo_familia_hoy = Column(Boolean, nullable=True)    # Solo si está en CB
    if_cb_distraccion_familia = Column(Boolean, nullable=True)
    if_cb_ambiente_estudio = Column(Integer, nullable=True)     # 1-5
    if_campus_productividad = Column(Integer, nullable=True)    # Solo si estuvo en campus
    if_campus_concentracion_aulas = Column(Integer, nullable=True) # 1-5
    
    # TRABAJO CHACRA (DOMINGOS)
    if_trabajo_chacra_hoy = Column(Boolean, default=False)
    if_chacra_horas_trabajadas = Column(Float, nullable=True)
    if_chacra_cansancio_fisico = Column(Integer, nullable=True)     # 1-5
    if_chacra_impacto_lunes_predicho = Column(Integer, nullable=True) # 1-5
    if_chacra_satisfaccion = Column(Integer, nullable=True)         # 1-5
    
    # RUTINA SEMANAL CB↔SA
    if_viaje_cb_sa_hoy = Column(Boolean, default=False)
    if_viaje_sa_cb_hoy = Column(Boolean, default=False)
    if_viaje_cansancio = Column(Integer, nullable=True)           # 1-5
    if_viaje_productivo_transporte = Column(Boolean, nullable=True) # ¿Estudió en viaje?
    
    # REFLEXIÓN DIARIA
    principal_logro_hoy = Column(String, nullable=True)
    principal_frustracion_hoy = Column(String, nullable=True)
    nivel_satisfaccion_dia = Column(Integer, default=3)          # 1-5
    plan_manana = Column(String, nullable=True)
    
    # TIMESTAMP
    timestamp_registro = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<BienestarJhon(fecha={self.fecha}, energia={self.energia_nivel})>"

# ============================================================================
# ESTUDIO ESPECÍFICO JHON
# ============================================================================

class EstudioJhon(Base):
    """Estudio específico con cursos hardcodeados y contexto meta 15.82"""
    __tablename__ = 'estudio_jhon'
    
    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    timestamp_inicio = Column(DateTime, nullable=False)
    timestamp_fin = Column(DateTime, nullable=False)
    
    # CURSO ESPECÍFICO (7 opciones hardcodeadas)
    curso = Column(String, nullable=False)  # CursoJhonEnum
    
    # DATOS BÁSICOS SESIÓN
    duracion_minutos = Column(Integer, nullable=False)
    ubicacion_estudio = Column(String, nullable=False)  # UbicacionJhonEnum
    
    # CONCENTRACIÓN Y TDAH
    concentracion_inicio = Column(Integer, nullable=False)   # 1-5
    concentracion_durante = Column(Integer, nullable=False)  # 1-5
    concentracion_final = Column(Integer, nullable=False)    # 1-5
    con_medicacion_metilfenidato = Column(Boolean, default=False)
    logre_hiperfoco = Column(Boolean, default=False)
    nivel_distracciones = Column(Integer, default=3)        # 1-5 (1=muchas, 5=ninguna)
    
    # ESPECÍFICO MATEMÁTICAS (Álgebra + Discretas)
    if_matematicas_tema_especifico = Column(String, nullable=True)  # "Determinantes", "Grafos"
    if_matematicas_dificultad_tema = Column(Integer, nullable=True) # 1-5
    if_matematicas_frustracion = Column(Integer, nullable=True)     # 1-5
    if_matematicas_youtube_ayuda = Column(Boolean, nullable=True)
    if_matematicas_avance_real = Column(Boolean, nullable=True)
    if_matematicas_necesita_repaso = Column(Boolean, nullable=True)
    if_matematicas_confianza_pc = Column(Integer, nullable=True)    # 1-5
    
    # ESPECÍFICO REDACCIÓN (debilidad ortografía)
    if_redaccion_uso_corrector = Column(Boolean, nullable=True)
    if_redaccion_mejora_ortografia = Column(Boolean, nullable=True)
    if_redaccion_tiempo_extra_revisar = Column(Integer, nullable=True) # minutos
    if_redaccion_satisfaccion_texto = Column(Integer, nullable=True)   # 1-5
    if_redaccion_tipo_texto = Column(String, nullable=True)           # "Ensayo", "Práctica"
    
    # ESPECÍFICO ESTADÍSTICA (fortaleza)
    if_estadistica_uso_r = Column(Boolean, nullable=True)
    if_estadistica_uso_python = Column(Boolean, nullable=True)
    if_estadistica_facilidad_conceptos = Column(Integer, nullable=True) # 1-5
    
    # ESPECÍFICO INGENIERÍA PROCESOS
    if_procesos_trabajo_grupal = Column(Boolean, nullable=True)
    if_procesos_avance_proyecto = Column(String, nullable=True)  # "Primer avance", etc.
    if_procesos_uso_software_bpmn = Column(Boolean, nullable=True)
    
    # HERRAMIENTAS ESPECÍFICAS USADAS
    uso_python = Column(Boolean, default=False)
    uso_r = Column(Boolean, default=False)
    uso_youtube_educativo = Column(Boolean, default=False)
    uso_corrector_ortografico = Column(Boolean, default=False)
    uso_calculadora_cientifica = Column(Boolean, default=False)
    uso_wolfram_symbolab = Column(Boolean, default=False)
    
    # EVALUACIÓN ESPECÍFICA CONTRIBUCIÓN META 15.82
    contribucion_meta_1582 = Column(Integer, nullable=False)  # 1-5
    preparacion_evaluacion_proxima = Column(Boolean, default=False)
    evaluacion_proxima_nombre = Column(String, nullable=True) # "PC1 Álgebra"
    dias_para_evaluacion = Column(Integer, nullable=True)
    
    # SATISFACCIÓN Y RESULTADOS
    satisfaccion_sesion = Column(Integer, nullable=False)     # 1-5
    objetivos_sesion_cumplidos = Column(Boolean, nullable=False)
    principal_concepto_aprendido = Column(String, nullable=True)
    principal_duda_pendiente = Column(String, nullable=True)
    
    # LIMITACIONES TÉCNICAS ESPECÍFICAS
    limitaciones_laptop_sa = Column(Boolean, default=False)
    interrupciones_familia_cb = Column(Boolean, default=False)
    interrupciones_ruido_sa = Column(Boolean, default=False)
    problema_internet = Column(Boolean, default=False)

    def __repr__(self):
        return f"<EstudioJhon(fecha={self.fecha}, curso={self.curso}, duracion={self.duracion_minutos}min)>"

# ============================================================================
# GASTOS ESPECÍFICOS JHON
# ============================================================================

class GastosJhon(Base):
    """Gastos con categorías específicas Jhon y análisis impulsos"""
    __tablename__ = 'gastos_jhon'
    
    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    monto = Column(Float, nullable=False)
    
    # CATEGORÍAS ESPECÍFICAS JHON
    categoria = Column(String, nullable=False)  # CategoriaGastoJhonEnum
    descripcion_especifica = Column(String, nullable=True)  # Para categoría "OTROS"
    
    # CONTROL IMPULSIVIDAD ESPECÍFICO JHON
    es_gasto_impulsivo = Column(Boolean, default=False)
    if_impulsivo_trigger = Column(String, nullable=True)  # TriggerImpulsivoJhonEnum
    if_impulsivo_momento_emocional = Column(String, nullable=True)  # "Post PC difícil"
    if_impulsivo_arrepentimiento_nivel = Column(Integer, nullable=True)  # 1-5
    if_impulsivo_podria_evitarse = Column(Boolean, nullable=True)
    
    # CONTEXTO PRESUPUESTARIO ESPECÍFICO
    afecta_presupuesto_variable = Column(Boolean, default=True)
    afecta_categoria_academica = Column(Boolean, default=False)
    afecta_categoria_fisica = Column(Boolean, default=False)
    es_gasto_fijo_mensual = Column(Boolean, default=False)
    
    # UBICACIÓN Y CONTEXTO DETALLADO
    ubicacion_gasto = Column(String, nullable=False)  # UbicacionJhonEnum
    es_gasto_planificado = Column(Boolean, default=False)
    metodo_pago = Column(String, nullable=True)  # "Efectivo", "Tarjeta", "Transfer"
    
    # ESPECÍFICOS POR TIPO DE GASTO
    if_transporte_motivo_especifico = Column(String, nullable=True)  # "Llegué tarde", "Lluvia"
    if_transporte_distancia = Column(String, nullable=True)         # "SA-Campus", "CB-SA"
    if_comida_tipo_especifico = Column(String, nullable=True)       # "Necesaria", "Chatarra"
    if_comida_hambre_emocional = Column(Boolean, nullable=True)
    if_academico_curso_relacionado = Column(String, nullable=True)  # "Álgebra", "Discretas"
    if_academico_urgencia = Column(Integer, nullable=True)          # 1-5
    if_fisico_contribuye_meta = Column(Boolean, nullable=True)
    if_salud_medicacion_exacta = Column(String, nullable=True)      # "Metilfenidato 10mg"
    
    # ANÁLISIS AUTOMÁTICO
    patron_similar_ultimos_dias = Column(Boolean, default=False)    # Detectado automáticamente
    patron_correlacion_evaluaciones = Column(Boolean, default=False) # Post-exámenes
    patron_correlacion_ubicacion = Column(Boolean, default=False)   # SA vs CB
    
    # IMPACTO EN METAS
    impacto_meta_financiera = Column(String, nullable=True)  # "BAJO", "MEDIO", "ALTO"
    porcentaje_presupuesto_mensual = Column(Float, nullable=True)  # Calculado automáticamente

    def __repr__(self):
        return f"<GastosJhon(fecha={self.fecha}, monto=S/{self.monto}, categoria={self.categoria})>"

# ============================================================================
# FÍSICO ESPECÍFICO JHON
# ============================================================================

class FisicoJhon(Base):
    """Transformación física específica 88kg → 70kg"""
    __tablename__ = 'fisico_jhon'
    
    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False, unique=True)
    
    # MÉTRICAS BÁSICAS
    peso_kg = Column(Float, nullable=True)  # Solo domingos
    energia_fisica = Column(Integer, nullable=False)     # 1-5 diario
    fuerza_percibida = Column(Integer, nullable=False)   # 1-5 diario
    resistencia_percibida = Column(Integer, nullable=False) # 1-5 diario
    como_me_veo_espejo = Column(Integer, nullable=False) # 1-5 diario
    confianza_fisica = Column(Integer, nullable=False)   # 1-5 diario
    nivel_motivacion = Column(Integer, nullable=False)   # 1-5 diario
    
    # MEDIDAS CORPORALES (lunes/jueves)
    medida_pecho_cm = Column(Float, nullable=True)      # Solo L/J
    medida_cintura_cm = Column(Float, nullable=True)    # Solo L/J
    medida_cuello_cm = Column(Float, nullable=True)     # Solo L/J
    medida_brazo_cm = Column(Float, nullable=True)      # Opcional L/J
    medida_muslo_cm = Column(Float, nullable=True)      # Opcional L/J
    
    # ACTIVIDAD FÍSICA
    hizo_ejercicio_hoy = Column(Boolean, default=False)
    if_ejercicio_tipo = Column(String, nullable=True)    # "Gym", "Chacra", "Cardio"
    if_ejercicio_ubicacion = Column(String, nullable=True) # "Gym SA", "Casa CB"
    if_ejercicio_duracion_minutos = Column(Integer, nullable=True)
    if_ejercicio_intensidad = Column(Integer, nullable=True)  # 1-5
    if_ejercicio_satisfaccion = Column(Integer, nullable=True) # 1-5
    
    # ESPECÍFICO GYM
    if_gym_grupos_musculares = Column(String, nullable=True)  # "Pecho, Tríceps"
    if_gym_peso_utilizado = Column(String, nullable=True)     # "15kg mancuernas"
    if_gym_series_completadas = Column(String, nullable=True) # "3x12, 3x10"
    if_gym_crowding_nivel = Column(Integer, nullable=True)    # 1-5 (lleno vs vacío)
    
    # ESPECÍFICO CHACRA DOMINGOS
    if_chacra_trabajo_hoy = Column(Boolean, default=False)
    if_chacra_equivale_ejercicio = Column(Boolean, nullable=True)
    if_chacra_tipo_trabajo = Column(String, nullable=True)    # "Sembrar", "Cosechar"
    if_chacra_cansancio_fisico = Column(Integer, nullable=True) # 1-5
    
    # ALIMENTACIÓN ESPECÍFICA
    comidas_saludables_cantidad = Column(Integer, default=3)  # 0-5
    comidas_chatarra_cantidad = Column(Integer, default=0)    # 0-3
    litros_agua_aprox = Column(Float, default=2.0)            # 0-5
    control_antojos_nivel = Column(Integer, default=3)        # 1-5
    suplementos_tomados = Column(String, nullable=True)       # "Proteína", "Creatina"
    
    # HAMBRE EMOCIONAL ESPECÍFICA
    hambre_emocional_hoy = Column(Boolean, default=False)
    if_hambre_trigger_especifico = Column(String, nullable=True) # "Post-matemáticas"
    if_hambre_alimentos_buscados = Column(String, nullable=True) # "Dulces", "Frituras"
    if_hambre_controlada = Column(Boolean, nullable=True)
    
    # IMPACTO EN RENDIMIENTO ACADÉMICO
    if_ejercicio_concentracion_post = Column(Integer, nullable=True)  # 1-5
    if_ejercicio_energia_post = Column(Integer, nullable=True)        # 1-5
    if_ejercicio_animo_post = Column(Integer, nullable=True)          # 1-5
    calidad_sueno_esperada_hoy = Column(Integer, default=3)           # 1-5
    
    # PROGRESO ESPECÍFICO META 70KG
    progreso_percibido_semana = Column(String, nullable=True)  # "AVANCE", "ESTABLE", "RETROCESO"
    principal_logro_fisico = Column(String, nullable=True)
    principal_reto_fisico = Column(String, nullable=True)
    ajuste_plan_necesario = Column(String, nullable=True)
    motivacion_proxima_semana = Column(Integer, default=3)    # 1-5
    
    # CORRELACIÓN CON OTROS MÓDULOS
    correlacion_humor_ejercicio = Column(Integer, nullable=True)      # 1-5
    correlacion_estudio_energia = Column(Integer, nullable=True)      # 1-5
    correlacion_gastos_impulsos = Column(Boolean, nullable=True)      # ¿Gasta más cuando no hace ejercicio?

    def __repr__(self):
        return f"<FisicoJhon(fecha={self.fecha}, peso={self.peso_kg}kg, ejercicio={self.hizo_ejercicio_hoy})>"

# ============================================================================
# CONFIGURACIÓN CURSOS JHON
# ============================================================================

class ConfiguracionCursoJhon(Base):
    """Configuración específica cursos con capacidad de actualización"""
    __tablename__ = 'configuracion_curso_jhon'
    
    id = Column(Integer, primary_key=True)
    curso_codigo = Column(String, nullable=False, unique=True)  # "CC4036"
    curso_nombre = Column(String, nullable=False)
    
    # CONFIGURACIÓN BÁSICA
    creditos = Column(Integer, nullable=False)
    profesor_principal = Column(String, nullable=False)
    email_profesor = Column(String, nullable=True)
    dificultad_jhon = Column(Integer, nullable=False)  # 1-5
    ansiedad_nivel_jhon = Column(String, nullable=False) # "BAJO", "MEDIO", "ALTO"
    tipo_curso = Column(String, nullable=False)  # "Matemática Crítica", "Core Carrera"
    
    # SISTEMA EVALUACIÓN (JSON)
    sistema_evaluacion = Column(JSON, nullable=False)  # Estructura completa evaluaciones
    calendario_evaluaciones = Column(JSON, nullable=False)  # Fechas específicas
    estrategias_jhon = Column(JSON, nullable=True)  # Estrategias específicas para Jhon
    
    # ESTADO ACTUALIZACIÓN
    status_configuracion = Column(String, default="pendiente_silabo")  # "estimado", "confirmado"
    fuente_datos = Column(String, default="inferencia")  # "silabo_oficial", "estimacion"
    fecha_ultima_actualizacion = Column(DateTime, default=datetime.utcnow)
    requiere_actualizacion = Column(Boolean, default=True)
    
    # ALERTAS ESPECÍFICAS
    alertas_habilitadas = Column(JSON, nullable=True)  # Tipos de alertas para este curso
    recordatorios_medicacion = Column(Boolean, default=False)  # Solo matemáticas
    
    # CORRELACIONES
    impacto_promedio_general = Column(Float, nullable=True)  # Peso en promedio 15.82
    criticidad_meta = Column(String, default="MEDIA")  # "BAJA", "MEDIA", "ALTA", "CRÍTICA"

    def __repr__(self):
        return f"<ConfiguracionCursoJhon(codigo={self.curso_codigo}, dificultad={self.dificultad_jhon})>"

# ============================================================================
# CORRELACIONES AUTOMÁTICAS JHON
# ============================================================================

class CorrelacionJhon(Base):
    """Correlaciones automáticas específicas entre módulos"""
    __tablename__ = 'correlaciones_jhon'
    
    id = Column(Integer, primary_key=True)
    fecha_calculo = Column(DateTime, default=datetime.utcnow)
    
    # VARIABLES CORRELACIONADAS
    variable_x = Column(String, nullable=False)  # "ejercicio_semanal"
    variable_y = Column(String, nullable=False)  # "concentracion_matematicas"
    
    # RESULTADO ESTADÍSTICO
    coeficiente_correlacion = Column(Float, nullable=False)
    significancia_estadistica = Column(Boolean, nullable=False)
    n_observaciones = Column(Integer, nullable=False)
    
    # INTERPRETACIÓN ESPECÍFICA JHON
    interpretacion_textual = Column(Text, nullable=False)
    recomendacion_accion = Column(Text, nullable=True)
    impacto_meta_1582 = Column(String, nullable=True)  # "POSITIVO", "NEGATIVO", "NEUTRO"
    
    # VALIDEZ
    periodo_analisis_inicio = Column(Date, nullable=False)
    periodo_analisis_fin = Column(Date, nullable=False)
    confianza_resultado = Column(String, nullable=False)  # "ALTA", "MEDIA", "BAJA"
    
    # SEGUIMIENTO
    validada_por_jhon = Column(Boolean, nullable=True)
    util_para_jhon = Column(Boolean, nullable=True)
    aplicada_en_rutina = Column(Boolean, default=False)

    def __repr__(self):
        return f"<CorrelacionJhon({self.variable_x} → {self.variable_y}, r={self.coeficiente_correlacion:.3f})>"

# ============================================================================
# ALERTAS ESPECÍFICAS JHON
# ============================================================================

class AlertaJhon(Base):
    """Sistema de alertas específico para contexto Jhon"""
    __tablename__ = 'alertas_jhon'
    
    id = Column(Integer, primary_key=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_programada = Column(DateTime, nullable=False)
    fecha_mostrada = Column(DateTime, nullable=True)
    
    # CLASIFICACIÓN ALERTA
    tipo_alerta = Column(String, nullable=False)  # "evaluacion", "medicacion", "presupuesto"
    prioridad = Column(String, nullable=False)    # "BAJA", "MEDIA", "ALTA", "CRÍTICA"
    categoria_vida = Column(String, nullable=False) # "academico", "fisico", "financiero"
    
    # CONTENIDO ESPECÍFICO
    titulo = Column(String, nullable=False)
    mensaje = Column(Text, nullable=False)
    accion_sugerida = Column(String, nullable=True)
    
    # CONTEXTO ESPECÍFICO JHON
    curso_relacionado = Column(String, nullable=True)  # "CC4036", "CC3106"
    ubicacion_recomendada = Column(String, nullable=True)  # "Biblioteca", "SA"
    medicacion_sugerida = Column(Boolean, default=False)
    
    # ESTADO
    mostrada = Column(Boolean, default=False)
    accion_tomada = Column(Boolean, default=False)
    feedback_utilidad = Column(Integer, nullable=True)  # 1-5
    
    # GENERACIÓN AUTOMÁTICA
    generada_automaticamente = Column(Boolean, default=True)
    regla_generacion = Column(String, nullable=True)  # "3_dias_antes_PC"
    datos_contexto = Column(JSON, nullable=True)  # Datos adicionales

    def __repr__(self):
        return f"<AlertaJhon(tipo={self.tipo_alerta}, prioridad={self.prioridad}, mostrada={self.mostrada})>"

# ============================================================================
# CALENDAR ACADÉMICO HARDCODEADO
# ============================================================================

class CalendarioAcademicoJhon(Base):
    """Calendario académico específico ciclo 2025-II"""
    __tablename__ = 'calendario_academico_jhon'
    
    id = Column(Integer, primary_key=True, default=1)  # Solo un registro
    
    # INFORMACIÓN CICLO HARDCODEADA
    ciclo = Column(String, default='2025-II')
    fecha_inicio_ciclo = Column(Date, default=date(2025, 8, 18))
    fecha_fin_clases = Column(Date, default=date(2025, 12, 20))
    duracion_semanas = Column(Integer, default=18)
    
    # FECHAS CRÍTICAS ESPECÍFICAS (JSON)
    fechas_criticas = Column(JSON)  # JSON con fechas importantes
    
    # CONFIGURACIÓN ESPECÍFICA JHON
    timezone = Column(String, default='America/Lima')
    regla_madrugada = Column(Time, default=time(2, 0))
    backup_automatico_habilitado = Column(Boolean, default=True)
    
    # TIMESTAMPS
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    ultima_sincronizacion = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<CalendarioAcademico(ciclo={self.ciclo}, semanas={self.duracion_semanas})>"

# ============================================================================
# EVALUACIONES CALENDARIZADAS
# ============================================================================

class EvaluacionCalendarizada(Base):
    """Evaluaciones específicas con fechas exactas hardcodeadas"""
    __tablename__ = 'evaluaciones_calendarizadas'
    
    id = Column(Integer, primary_key=True)
    
    # IDENTIFICACIÓN
    curso_codigo = Column(String, nullable=False)  # "CC4036"
    evaluacion_nombre = Column(String, nullable=False)  # "PC1", "EXAMEN_PARCIAL"
    evaluacion_tipo = Column(String, nullable=False)  # "PC", "EXAMEN", "TRABAJO"
    
    # FECHAS ESPECÍFICAS
    fecha_evaluacion = Column(Date, nullable=False)
    semana_academica = Column(Integer, nullable=False)  # 1-18
    dias_preparacion_recomendados = Column(Integer, default=3)
    
    # CONTENIDO Y DIFICULTAD
    tema_principal = Column(String, nullable=True)  # "Determinantes", "Grafos"
    dificultad_esperada = Column(Integer, default=3)  # 1-5
    criticidad_meta_1582 = Column(String, default="MEDIA")  # "BAJA", "MEDIA", "ALTA", "CRÍTICA"
    
    # RECOMENDACIONES ESPECÍFICAS JHON
    medicacion_recomendada = Column(Boolean, default=False)
    ubicacion_estudio_recomendada = Column(String, nullable=True)
    horas_estudio_sugeridas = Column(Integer, nullable=True)
    
    # ESTADO
    notificacion_enviada = Column(Boolean, default=False)
    preparacion_iniciada = Column(Boolean, default=False)
    evaluacion_completada = Column(Boolean, default=False)
    nota_obtenida = Column(Float, nullable=True)
    
    # METADATA
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    activa = Column(Boolean, default=True)

    def __repr__(self):
        return f"<EvaluacionCalendarizada({self.curso_codigo}-{self.evaluacion_nombre}, {self.fecha_evaluacion})>"

# ============================================================================
# FUNCIONES HELPER PARA MODELOS
# ============================================================================

def get_ubicaciones_jhon():
    """Retorna lista de ubicaciones específicas de Jhon"""
    return [e.value for e in UbicacionJhonEnum]

def get_cursos_jhon():
    """Retorna lista de cursos ciclo 2025-II"""
    return [e.value for e in CursoJhonEnum]

def get_categorias_gastos_jhon():
    """Retorna lista de categorías de gastos específicas"""
    return [e.value for e in CategoriaGastoJhonEnum]

def get_triggers_impulsos_jhon():
    """Retorna lista de triggers de impulsos específicos"""
    return [e.value for e in TriggerImpulsivoJhonEnum]

# ============================================================================
# VALIDACIONES ESPECÍFICAS JHON
# ============================================================================

def validar_promedio_meta_1582(promedio_actual: float, creditos_actuales: int, 
                               creditos_nuevos: int, meta_final: float = 14.0) -> dict:
    """
    Valida matemáticamente la meta 15.82
    """
    puntos_actuales = promedio_actual * creditos_actuales
    creditos_totales = creditos_actuales + creditos_nuevos
    puntos_necesarios_total = meta_final * creditos_totales
    puntos_necesarios_nuevos = puntos_necesarios_total - puntos_actuales
    promedio_necesario = puntos_necesarios_nuevos / creditos_nuevos
    
    return {
        "promedio_necesario": round(promedio_necesario, 2),
        "factible": promedio_necesario <= 20.0,
        "riesgo": "ALTO" if promedio_necesario > 16.0 else "MEDIO" if promedio_necesario > 14.0 else "BAJO"
    }

def validar_ubicacion_coherente(ubicacion_principal: str, ubicacion_registro: str) -> bool:
    """
    Valida que las ubicaciones sean coherentes
    """
    # Ubicaciones que pueden registrar desde cualquier lado
    ubicaciones_flexibles = [
        UbicacionJhonEnum.TRANSPORTE_PUBLICO.value,
        UbicacionJhonEnum.NOVIA_CASA.value
    ]
    
    if ubicacion_registro in ubicaciones_flexibles:
        return True
    
    # Validaciones específicas de coherencia
    coherencia_map = {
        UbicacionJhonEnum.CB_CUARTO.value: [UbicacionJhonEnum.CB_CUARTO.value, UbicacionJhonEnum.CB_SALA_FAMILIAR.value],
        UbicacionJhonEnum.SA_CUARTO.value: [UbicacionJhonEnum.SA_CUARTO.value],
        UbicacionJhonEnum.CAMPUS_BIBLIOTECA.value: [UbicacionJhonEnum.CAMPUS_BIBLIOTECA.value, UbicacionJhonEnum.CAMPUS_AULA.value]
    }
    
    return ubicacion_registro in coherencia_map.get(ubicacion_principal, [ubicacion_principal])

def calcular_peso_meta_progreso(peso_inicial: float, peso_actual: float, peso_meta: float) -> dict:
    """
    Calcula progreso específico meta 70kg
    """
    perdida_total_necesaria = peso_inicial - peso_meta  # 18kg
    perdida_actual = peso_inicial - peso_actual
    progreso_porcentaje = (perdida_actual / perdida_total_necesaria) * 100
    peso_restante = peso_actual - peso_meta
    
    return {
        "progreso_porcentaje": max(0, round(progreso_porcentaje, 1)),
        "peso_perdido": round(perdida_actual, 1),
        "peso_restante": round(peso_restante, 1),
        "imc_actual": round(peso_actual / (1.70 ** 2), 1),
        "meta_alcanzada": peso_actual <= peso_meta
    }

# ============================================================================
# CONFIGURACIÓN PARA TESTS
# ============================================================================

# Datos de ejemplo para testing
JHON_TEST_DATA = {
    "profile_master": {
        "matricula": "20231515",
        "creditos_acumulados": 46,
        "promedio_actual": 13.23,
        "peso_inicial": 88.0,
        "meta_ciclo_2025_2": 15.82
    },
    "ubicaciones_frecuentes": [
        UbicacionJhonEnum.SA_CUARTO.value,
        UbicacionJhonEnum.CAMPUS_BIBLIOTECA.value,
        UbicacionJhonEnum.CB_CUARTO.value
    ],
    "cursos_criticos": [
        CursoJhonEnum.CC4036_ALGEBRA_MATRICIAL.value,
        CursoJhonEnum.CC3106_MATEMATICAS_DISCRETAS.value
    ],
    "categorias_gastos_frecuentes": [
        CategoriaGastoJhonEnum.TRANSPORTE_SA_CAMPUS_DIARIO.value,
        CategoriaGastoJhonEnum.COMIDA_CAMPUS_NECESARIA.value,
        CategoriaGastoJhonEnum.ACADEMICO_FOTOCOPIAS_MATEMATICAS.value
    ]
}

if __name__ == "__main__":
    # Test básico de validaciones
    print("🧪 Testing modelos PROMETEO-JHON...")
    
    # Test validación meta 15.82
    resultado_meta = validar_promedio_meta_1582(13.23, 46, 20, 14.0)
    print(f"Meta 15.82: {resultado_meta['promedio_necesario']} - Riesgo: {resultado_meta['riesgo']}")
    
    # Test progreso físico
    progreso_fisico = calcular_peso_meta_progreso(88.0, 88.0, 70.0)
    print(f"Progreso físico: {progreso_fisico['progreso_porcentaje']}% - IMC: {progreso_fisico['imc_actual']}")
    
    # Test coherencia ubicaciones
    coherente = validar_ubicacion_coherente(
        UbicacionJhonEnum.SA_CUARTO.value, 
        UbicacionJhonEnum.SA_CUARTO.value
    )
    print(f"Ubicaciones coherentes: {coherente}")
    
    print("✅ Tests básicos completados")