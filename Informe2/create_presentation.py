import sys
import os
import pptx
from pptx import Presentation
from pptx.util import Pt

TEMPLATE_PATH = "/media/tati/BACKUP1/REP Memoristas/Alexandra Navarro/Seminario/Presentación_Navarro.pptx"
OUTPUT_PATH = "/home/tati/Documentos/GitHub/TrabajoTitulo/Informe2/Presentacion_Fabian_Ibarra.pptx"

def set_shape_text_by_id(slide, shape_id, new_text, font_size=None, font_color=None, bold=None, font_name=None):
    target_shape = None
    for shape in slide.shapes:
        if shape.shape_id == shape_id:
            target_shape = shape
            break
            
    if not target_shape or not target_shape.has_text_frame:
        return
        
    tf = target_shape.text_frame
    
    # Store existing first run styling if available
    first_run = None
    if len(tf.paragraphs) > 0 and len(tf.paragraphs[0].runs) > 0:
        first_run = tf.paragraphs[0].runs[0]
        
    orig_font_name = font_name or (first_run.font.name if first_run and first_run.font else "Calibri")
    orig_font_size = font_size or (first_run.font.size if first_run and first_run.font else None)
    orig_bold = bold if bold is not None else (first_run.font.bold if first_run and first_run.font else None)
    orig_color = font_color
    if orig_color is None and first_run and first_run.font and first_run.font.color:
        try:
            if first_run.font.color.type == 1: # RGB
                orig_color = first_run.font.color.rgb
        except:
            pass

    # Clear paragraphs and insert new text line by line
    lines = new_text.split('\n')
    tf.clear()
    
    for idx, line in enumerate(lines):
        p = tf.add_paragraph() if idx > 0 else tf.paragraphs[0]
        p.text = line
        if len(p.runs) > 0:
            r = p.runs[0]
            if orig_font_name:
                r.font.name = orig_font_name
            if orig_font_size:
                r.font.size = orig_font_size
            if orig_bold is not None:
                r.font.bold = orig_bold
            if orig_color:
                try:
                    r.font.color.rgb = orig_color
                except:
                    pass

def main():
    prs = Presentation(TEMPLATE_PATH)
    
    # SLIDE 1: Portada
    s1 = prs.slides[0]
    set_shape_text_by_id(s1, 77, "Metodología basada en procesamiento de lenguaje natural para analizar la alineación curricular de Ingeniería Informática en Chile con estándares ACM/IEEE y necesidades de la industria", font_size=Pt(22), bold=True)
    set_shape_text_by_id(s1, 78, "Integrante: Fabián Ibarra Norambuena\nProfesor Guía: Manuel Villalobos Cid\nDepartamento de Ingeniería Informática - USACH", font_size=Pt(16))

    # SLIDE 2: Tabla de contenidos 1
    s2 = prs.slides[1]
    set_shape_text_by_id(s2, 95, "Tabla de contenidos", font_size=Pt(36))
    set_shape_text_by_id(s2, 105, "Contexto", font_size=Pt(18))
    set_shape_text_by_id(s2, 115, "Motivación", font_size=Pt(18))
    set_shape_text_by_id(s2, 125, "Revisión de la literatura", font_size=Pt(18))
    set_shape_text_by_id(s2, 135, "Brecha del conocimiento", font_size=Pt(18))
    set_shape_text_by_id(s2, 145, "Pregunta e Hipótesis", font_size=Pt(18))
    set_shape_text_by_id(s2, 155, "Objetivos", font_size=Pt(18))

    # SLIDE 3: Tabla de contenidos 2
    s3 = prs.slides[2]
    set_shape_text_by_id(s3, 166, "Tabla de contenidos", font_size=Pt(36))
    set_shape_text_by_id(s3, 176, "Enfoque y Metodología", font_size=Pt(18))
    set_shape_text_by_id(s3, 186, "Corpus y Modelamiento", font_size=Pt(18))
    set_shape_text_by_id(s3, 196, "Software y Hardware", font_size=Pt(18))
    set_shape_text_by_id(s3, 206, "Plan de Trabajo", font_size=Pt(18))

    # SLIDE 4: Contexto 1
    s4 = prs.slides[3]
    set_shape_text_by_id(s4, 217, "Contexto: Educación en Ingeniería Informática", font_size=Pt(30))
    set_shape_text_by_id(s4, 218, "Heterogeneidad estructural entre mallas curriculares de las distintas universidades en Chile.", font_size=Pt(15))
    set_shape_text_by_id(s4, 219, "Acelerada transformación tecnológica y evolución constante de las competencias requeridas por la industria TI.", font_size=Pt(15))
    set_shape_text_by_id(s4, 220, "Dificultad para evaluar de forma continua y manual el grado de alineación curricular ante estándares internacionales.", font_size=Pt(15))
    set_shape_text_by_id(s4, 222, "1. MALLAS CHILE", font_size=Pt(11), bold=True)
    set_shape_text_by_id(s4, 223, "2. ACM/IEEE", font_size=Pt(11), bold=True)
    set_shape_text_by_id(s4, 224, "3. LINKEDIN TI", font_size=Pt(11), bold=True)
    set_shape_text_by_id(s4, 225, "4. MODELO NLP", font_size=Pt(11), bold=True)
    set_shape_text_by_id(s4, 226, "5. ALINEACIÓN", font_size=Pt(11), bold=True)

    # SLIDE 5: Contexto 2
    s5 = prs.slides[4]
    set_shape_text_by_id(s5, 246, "Contexto: NLP y Representación Semántica", font_size=Pt(30))
    set_shape_text_by_id(s5, 247, "Los programas de estudio y descripciones de asignaturas contienen información no estructurada en lenguaje natural.", font_size=Pt(15))
    set_shape_text_by_id(s5, 248, "Los métodos tradicionales de revisión curricular son cualitativos, costosos y de baja frecuencia de actualización.", font_size=Pt(15))
    set_shape_text_by_id(s5, 250, "Técnicas avanzadas:\n• Sentence-Transformers\n• Embeddings densos\n• Clustering no supervisado", font_size=Pt(14))

    # SLIDE 6: Motivación
    s6 = prs.slides[5]
    set_shape_text_by_id(s6, 261, "Motivación", font_size=Pt(36))
    set_shape_text_by_id(s6, 262, "Integrar Minería de Textos + Sentence-Transformers + Clustering No Supervisado.", font_size=Pt(16))
    set_shape_text_by_id(s6, 263, "Heterogeneidad Curricular", font_size=Pt(14), bold=True)
    set_shape_text_by_id(s6, 264, "Brechas con la Industria", font_size=Pt(14), bold=True)
    set_shape_text_by_id(s6, 266, "PROPUESTA", font_size=Pt(14), bold=True)
    set_shape_text_by_id(s6, 267, "Esta metodología permitirá cuantificar las brechas curriculares, automatizar el análisis comparativo de mallas y apoyar la toma de decisiones informada en los procesos de rediseño curricular continuo en la Educación Superior.", font_size=Pt(15))

    # SLIDE 7: Revisión de la literatura
    s7 = prs.slides[6]
    set_shape_text_by_id(s7, 278, "Revisión de la literatura", font_size=Pt(36))
    set_shape_text_by_id(s7, 279, "• Directrices ACM/IEEE (CS2013 y CC2020) definen áreas de conocimiento y competencias clave en computación.\n• Estudios de alineación curricular previos se basan mayoritariamente en frecuencias (TF-IDF) o revisiones manuales.\n• Modelos de representaciones vectoriales densas (Sentence-BERT / BGE / E5) capturan similitud semántica contextual profunda.\n• Algoritmos de clustering no supervisado (K-Means, Jerárquico, DBSCAN) permiten identificar perfiles formativos implícitos.\n• Se requiere un marco de validación híbrido que combine métricas cuantitativas geométricas (Silhouette, Davies-Bouldin) y juicio de expertos.", font_size=Pt(15))

    # SLIDE 8: Brecha del conocimiento
    s8 = prs.slides[7]
    set_shape_text_by_id(s8, 289, "Brecha del conocimiento", font_size=Pt(36))
    set_shape_text_by_id(s8, 290, "Ausencia de metodologías cuantitativas y replicables en Chile para medir alineación curricular de forma automatizada.\n\nFalta de integración analítica continua entre estándares internacionales (ACM/IEEE) y la demanda laboral nacional real (LinkedIn).\n\nNecesidad de un marco de validación híbrido operacionalizable en un entorno de visualización interactivo para gestores académicos.", font_size=Pt(16))

    # SLIDE 9: Pregunta e Hipótesis
    s9 = prs.slides[8]
    set_shape_text_by_id(s9, 301, "Pregunta de investigación", font_size=Pt(30))
    set_shape_text_by_id(s9, 302, "¿En qué medida una metodología basada en procesamiento de lenguaje natural, representación semántica vectorial y agrupamiento no supervisado permite cuantificar con rigor y validar la alineación curricular de las carreras de Ingeniería Informática en Chile frente a los estándares ACM/IEEE y las necesidades del mercado laboral nacional?", font_size=Pt(15))
    set_shape_text_by_id(s9, 303, "Hipótesis", font_size=Pt(18), bold=True)
    set_shape_text_by_id(s9, 304, "Es posible construir representaciones vectoriales densas de los programas de estudio que capturen su afinidad semántica con directrices internacionales y requerimientos laborales, permitiendo a través de clustering no supervisado identificar perfiles formativos institucionales y cuantificar brechas curriculares de forma válida y consistente.", font_size=Pt(14))

    # SLIDE 10: Objetivo General
    s10 = prs.slides[9]
    set_shape_text_by_id(s10, 316, "Objetivo General", font_size=Pt(36))
    set_shape_text_by_id(s10, 317, "Desarrollar y evaluar una metodología sistemática basada en procesamiento de lenguaje natural, representación semántica vectorial y algoritmos de agrupamiento no supervisado (clustering) para analizar, agrupar y comparar el grado de alineación curricular de las carreras de Ingeniería Informática en Chile con respecto a los estándares de referencia internacional (ACM/IEEE CS2013 y CC2020) y a las competencias demandadas por el mercado laboral tecnológico nacional, cuantificando las brechas formativas mediante métricas de similitud semántica y validando los agrupamientos obtenidos mediante un marco de evaluación híbrido (cuantitativo y cualitativo).", font_size=Pt(15))

    # SLIDE 11: Objetivos específicos
    s11 = prs.slides[10]
    set_shape_text_by_id(s11, 328, "Objetivos específicos", font_size=Pt(36))
    set_shape_text_by_id(s11, 329, "1. Construir un corpus curricular y de mercado estructurado y normalizado (mallas nacionales, ACM/IEEE y ofertas de LinkedIn TI en Chile).\n\n2. Generar representaciones vectoriales densas (embeddings) mediante Sentence-Transformers y proyección dimensional (UMAP/t-SNE).\n\n3. Identificar perfiles formativos y medir la alineación curricular mediante clustering no supervisado (K-Means, DBSCAN) y similitud del coseno.\n\n4. Validar la calidad y estabilidad de los agrupamientos mediante un marco híbrido (métricas de Silhouette, Davies-Bouldin y juicio de expertos).\n\n5. Operacionalizar la metodología en un tablero de control (dashboard) interactivo de visualización para apoyo en la gestión académica.", font_size=Pt(13))

    # SLIDE 12: Enfoque y Metodología
    s12 = prs.slides[11]
    set_shape_text_by_id(s12, 339, "Enfoque y Metodología", font_size=Pt(36))
    set_shape_text_by_id(s12, 340, "• Enfoque cuantitativo, reproducible e impulsado por Minería de Textos y NLP.\n\n• Procesamiento analítico de textos no estructurados (programas de estudio y ofertas de trabajo).\n\n• Mapeo semántico tripartito: Mallas Curriculares vs Estándares ACM/IEEE vs Demandas de la Industria TI.\n\n• Soporte objetivo para la toma de decisiones informada en procesos de acreditación y rediseño curricular.", font_size=Pt(15))

    # SLIDE 13: Procedimiento Metodológico
    s13 = prs.slides[12]
    set_shape_text_by_id(s13, 354, "Procedimiento Metodológico", font_size=Pt(36))
    set_shape_text_by_id(s13, 357, "Metodología basada en 5 Fases Secuenciales de Desarrollo", font_size=Pt(18), bold=True)

    # SLIDE 14: Descripción del Corpus de Datos
    s14 = prs.slides[13]
    set_shape_text_by_id(s14, 369, "Descripción del Corpus de Datos", font_size=Pt(30))
    set_shape_text_by_id(s14, 372, "Fuentes de Información", font_size=Pt(18), bold=True)
    set_shape_text_by_id(s14, 374, "Corpus Curricular (Mallas nacionales + Estándares ACM/IEEE) y Mercado Laboral (LinkedIn TI Chile).", font_size=Pt(15))

    # SLIDE 15: Modelamiento Semántico
    s15 = prs.slides[14]
    set_shape_text_by_id(s15, 383, "Modelamiento y Agrupamiento Semántico", font_size=Pt(30))
    set_shape_text_by_id(s15, 386, "Representación Vectorial, Clustering y Métricas de Similitud", font_size=Pt(18), bold=True)

    # SLIDE 16: Software y Hardware
    s16 = prs.slides[15]
    set_shape_text_by_id(s16, 397, "Software y Hardware", font_size=Pt(36))
    set_shape_text_by_id(s16, 398, "Hardware de Trabajo\n• Sistema Operativo: Linux Ubuntu / macOS / Windows\n• Procesador: Intel® Core™ i7 / AMD Ryzen / Apple Silicon\n• Memoria RAM: 16 GB+ | Aceleración GPU para Embeddings", font_size=Pt(14))
    set_shape_text_by_id(s16, 399, "Software Crítico de Análisis\n• Python (v 3.11+)\n• Sentence-Transformers & PyTorch\n• scikit-learn & UMAP-learn\n• NLTK & spaCy (Preprocesamiento NLP)", font_size=Pt(14))
    set_shape_text_by_id(s16, 402, "Herramientas de Gestión y Visualización\n• Streamlit / Plotly (Dashboard Interactivo)\n• Git & GitHub (Control de versiones)\n• LaTeX (Redacción del Informe)", font_size=Pt(14))

    # SLIDE 17: Plan de Trabajo
    s17 = prs.slides[16]
    set_shape_text_by_id(s17, 415, "Plan de Trabajo", font_size=Pt(36))
    set_shape_text_by_id(s17, 418, "Definición de actividades", font_size=Pt(24))
    set_shape_text_by_id(s17, 434, "Fase 1: Extracción y Curaduría del Corpus", font_size=Pt(15), bold=True)
    set_shape_text_by_id(s17, 435, "Fase 2: Vectorización y Reducción Dimensional", font_size=Pt(15), bold=True)
    set_shape_text_by_id(s17, 436, "Fase 3: Clustering y Análisis de Alineación", font_size=Pt(15), bold=True)
    set_shape_text_by_id(s17, 437, "Fase 4: Validación Híbrida y Evaluación", font_size=Pt(15), bold=True)
    set_shape_text_by_id(s17, 438, "Fase 5: Dashboard y Documentación", font_size=Pt(15), bold=True)
    set_shape_text_by_id(s17, 439, "Consolidación de mallas informáticas chilenas, directrices ACM/IEEE y ofertas laborales LinkedIn TI.", font_size=Pt(13))
    set_shape_text_by_id(s17, 440, "Modelos de Embeddings, Métricas de Similitud, Clustering No Supervisado y Desarrollo del Dashboard Interactivo.", font_size=Pt(13))

    # SLIDE 18: Carta Gantt
    s18 = prs.slides[17]
    set_shape_text_by_id(s18, 450, "Plan de Trabajo", font_size=Pt(36))
    set_shape_text_by_id(s18, 453, "Carta Gantt", font_size=Pt(28))

    # SLIDE 19: Cierre
    s19 = prs.slides[18]
    set_shape_text_by_id(s19, 465, "¡Gracias por su atención!", font_size=Pt(50))
    set_shape_text_by_id(s19, 466, "¿Dudas o consultas?", font_size=Pt(28))

    # SLIDE 20: Bibliografía 1
    s20 = prs.slides[19]
    set_shape_text_by_id(s20, 477, "Bibliografía", font_size=Pt(36))
    set_shape_text_by_id(s20, 478, "ACM/IEEE Task Force. (2013). Computer Science Curricula 2013: Curriculum Guidelines for Undergraduate Degree Programs in Computer Science. ACM/IEEE Computer Society.\n\nCC2020 Task Force. (2020). Computing Curricula 2020: Paradigms for Global Computing Education. ACM/IEEE Computer Society.\n\nReimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. Proceedings of EMNLP-IJCNLP 2019, 3982-3992.\n\nMcInnes, L., Healy, J., & Melville, J. (2018). UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction. arXiv preprint arXiv:1802.03426.\n\nRousseeuw, P. J. (1987). Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. Journal of Computational and Applied Mathematics, 20, 53-65.", font_size=Pt(13))

    # SLIDE 21: Bibliografía 2
    s21 = prs.slides[20]
    set_shape_text_by_id(s21, 488, "Bibliografía", font_size=Pt(36))
    set_shape_text_by_id(s21, 489, "Davies, D. L., & Bouldin, D. W. (1979). A cluster separation measure. IEEE Transactions on Pattern Analysis and Machine Intelligence, 1(2), 224-227.\n\nPedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.\n\nEster, M., Kriegel, H. P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. Proceedings of KDD-96, 226-231.\n\nDevlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. NAACL-HLT 2019.", font_size=Pt(13))

    prs.save(OUTPUT_PATH)
    print(f"Presentation updated successfully with exact shape IDs at: {OUTPUT_PATH}")

if __name__ == '__main__':
    main()
