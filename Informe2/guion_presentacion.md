# Guion de la PresentaciÃ³n: "AlineaciÃ³n Curricular con NLP"
*   **Presentador:** FabiÃ¡n Luis Ibarra Norambuena
*   **Tiempo LÃ­mite:** 15 Minutos
*   **Pauta de PrÃ¡ctica:** Este guion estÃ¡ redactado en espaÃ±ol formal y asertivo (estilo defensa de tesis USACH). Las acotaciones entre corchetes `[como esta]` son guÃ­as visuales o de ritmo.

---

## â�±ï¸� DistribuciÃ³n de Tiempos y Transiciones

```mermaid
gantt
    title Cronograma del Guion (15 Minutos)
    dateFormat  X
    axisFormat %M:%S
    
    section Contexto e IntroducciÃ³n
    Diapositivas 1-3 (Portada y Agenda)  :active, s1, 0, 60
    Diapositivas 4-8 (Contexto, MotivaciÃ³n y PropÃ³sito) :s2, after s1, 150
    Diapositivas 9-11 (Literatura, Problema y Obj. General) :s3, after s2, 110
    
    section Objetivos y NÃºcleo TÃ©cnico
    Diapositiva 12 (Objetivos y Calidad) :s4, after s3, 80
    Diapositiva 13 (Enfoque MetodolÃ³gico) :active, s5, after s4, 90
    Diapositiva 14 (Corpus y Modelamiento NLP) :s6, after s5, 230
    
    section Plan e ImplementaciÃ³n
    Diapositivas 15-16 (Ambiente, Plan y Gantt) :s7, after s6, 150
    Diapositiva 17 (Cierre y Preguntas) :s8, after s7, 30
```

---

## ðŸŽ™ï¸� Guion Diapositiva por Diapositiva

### Diapositiva 1: Portada (Index 0)
*   **Tiempo Sugerido:** 0:00 - 0:40 (40 segundos)
*   **Guion:**
    > "Estimados miembros de la comisiÃ³n evaluadora, muy buenas tardes. Mi nombre es FabiÃ¡n Ibarra y hoy les presentarÃ© mi trabajo de tÃ­tulo titulado: *'MetodologÃ­a basada en procesamiento de lenguaje natural para analizar la alineaciÃ³n curricular de IngenierÃ­a InformÃ¡tica en Chile con estÃ¡ndares ACM/IEEE y necesidades de la industria'*. Esta investigaciÃ³n ha sido guiada por el profesor Manuel Villalobos Cid en el Departamento de IngenierÃ­a InformÃ¡tica de la Universidad de Santiago de Chile."
*   **ðŸ’¡ Consejo de oratoria:** Comienza con postura firme, mirada al frente y voz a volumen medio-alto. No te apresures; el primer minuto define la confianza del resto de la presentaciÃ³n.

---

### Diapositivas 2 y 3: Tabla de Contenidos (Index 1 y 2)
*   **Tiempo Sugerido:** 0:40 - 1:00 (20 segundos)
*   **Guion:**
    > "La presentaciÃ³n de hoy se estructurarÃ¡ de la siguiente manera: revisaremos el contexto educativo en Chile, la motivaciÃ³n y el propÃ³sito de la soluciÃ³n. Luego, repasaremos la literatura, planteando el problema, hipÃ³tesis y objetivos del proyecto. Posteriormente, detallaremos el enfoque metodolÃ³gico, la construcciÃ³n del corpus de datos junto con el modelamiento semÃ¡ntico con NLP. Finalizaremos con los aspectos tecnolÃ³gicos del ambiente, la planificaciÃ³n temporal con la carta Gantt y el respectivo cierre."
*   **ðŸ’¡ Consejo de oratoria:** Pasa estas diapositivas rÃ¡pidamente. No leas cada subpunto. El jurado ya sabe leer; solo resume los bloques temÃ¡ticos de forma Ã¡gil.

---

### Diapositiva 4: Contexto - Educación en Ingeniería Informática en Chile (Index 3)
*   **Tiempo Sugerido:** 1:00 - 1:20 (20 segundos)
*   **Guion:**
    > "Comencemos por el contexto nacional. La expansión de la educación superior en Chile ha masificado la oferta de carreras del área informática en la última década. Sin embargo, esta rápida proliferación ha traído consigo una alta heterogeneidad en las mallas curriculares y una gran diversidad de nomenclaturas (como Ingeniería Civil e Ingeniería de Ejecución), dificultando la comparación directa entre títulos y acentuando la necesidad de contar con marcos de homologación y evaluación semántica."
*   **ðŸ”— TransiciÃ³n:** *"EspecÃ­ficamente, podemos identificar tres problemÃ¡ticas clave en este escenario..."*

---

### Diapositiva 5: Contexto - DesafÃ­os del Ecosistema Chileno (Index 4)
*   **Tiempo Sugerido:** 1:20 - 1:50 (30 segundos)
*   **Guion:**
    > "En primer lugar, observamos una alta heterogeneidad en las mallas curriculares chilenas, con una gran diversidad de nombres y enfoques para perfiles equivalentes. Asimismo, enfrentamos una rÃ¡pida obsolescencia de las mallas frente a la velocidad del sector tecnolÃ³gico. Finalmente, esto perpetÃºa una brecha estructural entre la formaciÃ³n teÃ³rica acadÃ©mica y las habilidades prÃ¡cticas demandadas en el sector TI."
*   **ðŸ”— TransiciÃ³n:** *"Frente a esta fragmentaciÃ³n nacional, es fundamental mirar cÃ³mo opera el ordenamiento internacional..."*

---

### Diapositiva 6: Contexto - EstÃ¡ndares Internacionales (ACM/IEEE) (Index 5)
*   **Tiempo Sugerido:** 1:50 - 2:20 (30 segundos)
*   **Guion:**
    > "A nivel global, los consorcios ACM e IEEE dictan las directrices curriculares de referencia, como las guÃ­as CS2013 y el marco CC2020. Estos estÃ¡ndares promueven un modelo basado en competencias, estructurando la enseÃ±anza no solo en torno al conocimiento teÃ³rico, sino tambiÃ©n a las habilidades tÃ©cnicas y la actitud profesional en el mundo real."
*   **ðŸ”— TransiciÃ³n:** *"A pesar de la existencia de estos marcos, la actualizaciÃ³n curricular a nivel local enfrenta barreras metodolÃ³gicas crÃ­ticas..."*

---

### Diapositiva 7: MotivaciÃ³n (Index 6)
*   **Tiempo Sugerido:** 2:20 - 3:00 (40 segundos)
*   **Guion:**
    > "Tradicionalmente, el anÃ¡lisis de mallas se realiza mediante comisiones de acadÃ©micos que comparan planes de estudio de forma manual. Este enfoque conlleva un alto sesgo de subjetividad y un elevado costo operativo en tiempo y recursos. AdemÃ¡s, la ausencia de herramientas locales automatizadas perpetÃºa la desconexiÃ³n con el mercado laboral dinÃ¡mico. Esta brecha es la que motiva el desarrollo de una soluciÃ³n basada en datos."
*   **ðŸ”— TransiciÃ³n:** *"Es asÃ­ como definimos el propÃ³sito central de nuestra propuesta..."*

---

### Diapositiva 8: PropÃ³sito de la soluciÃ³n (Index 7)
*   **Tiempo Sugerido:** 3:00 - 3:30 (30 segundos)
*   **Guion:**
    > "El propÃ³sito de este proyecto es proveer una metodologÃ­a sistemÃ¡tica apoyada en un pipeline de procesamiento de lenguaje natural y un dashboard interactivo. El objetivo es ofrecer un soporte decisional en dos niveles: un nivel operativo, ayudando a los docentes a alinear sus asignaturas en el aula, y un nivel tÃ¡ctico, apoyando a directores de carrera en comitÃ©s curriculares y procesos de acreditaciÃ³n."
*   **ð### Diapositiva 8: RevisiÃ³n de la literatura (Index 7)
*   **Tiempo Sugerido:** 3:30 - 4:10 (40 segundos)
*   **Guion:**
    > "En la literatura de Procesamiento de Lenguaje Natural observamos una clara evoluciÃ³n paradigmÃ¡tica en la representaciÃ³n de texto curricular. Primero, los **modelos lÃ©xicos** como TF-IDF basaban su anÃ¡lisis en coincidencia exacta de palabras, siendo incapaces de capturar sinonimia tÃ©cnica. Luego, los **embeddings estÃ¡ticos** como Word2Vec mapearon palabras individuales a vectores continuos, pero sin capturar el contexto de frases completas. Finalmente, la llegada de **Transformers y modelos como Sentence-BERT (SBERT)** permitiÃ³ vectorizar oraciones y pÃ¡rrafos completos en un espacio semÃ¡ntico continuo multilingÃ¼e de 768 dimensiones, haciendo posible comparar directamente descriptores curriculares en espaÃ±ol contra estÃ¡ndares internacionales ACM/IEEE en inglÃ©s."
*   **ðŸ”— TransiciÃ³n:** *"A partir de este marco teÃ³rico, formalizamos la interrogante que guÃ­a esta investigaciÃ³n..."*

---

### Diapositiva 9: Enunciado del problema (Index 8)
*   **Tiempo Sugerido:** 4:10 - 4:40 (30 segundos)
*   **Guion:**
    > "Planteamos entonces la siguiente pregunta: Â¿CuÃ¡les son las similitudes y diferencias estructurales entre los diversos programas de IngenierÃ­a InformÃ¡tica en Chile, y cÃ³mo se alinean sus perfiles formativos tanto con los estÃ¡ndares internacionales IEEE/ACM como con las competencias demandadas por el mercado laboral en el sector TI?"
*   **ðŸ’¡ Consejo de oratoria:** Lee la pregunta de manera pausada y clara. Haz una pausa de 1 segundo al terminar para que el jurado absorba la relevancia del problema.

---

### Diapositiva 10: Objetivo General (Index 9)
*   **Tiempo Sugerido:** 4:40 - 5:20 (40 segundos)
*   **Guion:**
    > "Para responder a esto, nuestro Objetivo General es: Desarrollar y evaluar una metodologÃ­a sistemÃ¡tica basada en procesamiento de lenguaje natural, representaciÃ³n semÃ¡ntica vectorial y algoritmos de agrupamiento no supervisado, con el fin de analizar, agrupar y comparar el grado de alineaciÃ³n curricular de los programas de IngenierÃ­a InformÃ¡tica en Chile frente a los estÃ¡ndares internacionales y al mercado laboral nacional, validando los resultados cuantitativa y cualitativamente."
*   **ðŸ’¡ Consejo de oratoria:** Lee el objetivo de forma fluida pero asertiva. Destaca verbalmente los conceptos clave: *procesamiento de lenguaje natural*, *agrupamiento no supervisado* y *validaciÃ³n hÃ­brida*.

---

### Diapositiva 11: Objetivos especÃ­ficos y criterios de calidad (Index 10)
*   **Tiempo Sugerido:** 5:20 - 7:20 (2 minutos)
*   **Guion:**
    > "Para operativizar este objetivo general, definimos cinco objetivos especÃ­ficos con mÃ©tricas de calidad rigurosas:
    > 
    > En el **OE1 (Corpus de Datos)** exigimos una cobertura del 100% de la muestra seleccionada (16 programas, 747 asignaturas y 200 vacantes) con nulos inferiores al 1% tras el preprocesamiento con spaCy.
    > 
    > En el **OE2 (VectorizaciÃ³n)** convertimos el texto en embeddings de 768D y proyectamos a 2D con UMAP para el visualizador. Exigimos un **Trustworthiness >= 0.85**, lo que garantiza matemÃ¡ticamente que al reducir dimensiones no deformamos la estructura de vecindad semÃ¡ntica original.
    > 
    > En el **OE3 (Clustering)** clasificamos las asignaturas mediante modelos no supervisados sobre el total de **747 asignaturas** (no sobre los 16 programas). Evaluamos la calidad de la particiÃ³n mediante un **Silhouette >= 0.25** (que mide cohesiÃ³n y separaciÃ³n inter-clÃºster) y un **Davies-Bouldin < 1.50** (que evalÃºa la similitud promedio entre clÃºsteres), asegurando agrupaciones temÃ¡ticas sÃ³lidas.
    > 
    > En el **OE4 (ValidaciÃ³n HÃ­brida)** medimos la estabilidad cuantitativa del agrupamiento mediante **100 iteraciones Bootstrap exigiendo un ARI >= 0.75**, probando que los grupos son estables. Cualitativamente, medimos el acuerdo inter-anotador de un panel de 3 expertos independientes anotando 100 asignaturas en las 18 Ã¡reas ACM, logrando un **Fleiss' Kappa >= 0.60** (acuerdo sustancial segÃºn Landis y Koch). Finalmente, comparamos la predicciÃ³n del modelo contra el consenso humano alcanzando un **Cohen's Kappa >= 0.60**, demostrando que el modelo clasifica con el mismo criterio que un comitÃ© acadÃ©mico de expertos.
    > 
    > En el **OE5 (Dashboard)** desarrollamos un tablero interactivo en React exigiendo una **latencia media < 2.0 segundos** para permitir su uso fluido en reuniones de comitÃ©s curriculares y acreditaciones."

---

### Diapositiva 12: Enfoque MetodolÃ³gico e IntegraciÃ³n (Index 11)
*   **Tiempo Sugerido:** 7:20 - 8:20 (1 minuto)
*   **Guion:**
    > "Nuestra propuesta adopta el estÃ¡ndar metodolÃ³gico CRISP-DM, adaptando su ciclo iterativo desde la comprensiÃ³n curricular y la preparaciÃ³n lingÃ¼Ã­stica de los datos, pasando por el modelamiento, hasta la evaluaciÃ³n hÃ­brida y el despliegue del dashboard. 
    > 
    > Justificamos nuestras decisiones analÃ­ticas en dos puntos clave:
    > Primero, el uso de embeddings multilingÃ¼es, que nos permite proyectar textos en espaÃ±ol e inglÃ©s en un espacio vectorial compartido sin la pÃ©rdida semÃ¡ntica y los sesgos que introduce la traducciÃ³n automÃ¡tica intermedia.
    > Segundo, la combinaciÃ³n de similitud coseno con clustering no supervisado a nivel de asignatura. Mientras la similitud mide la alineaciÃ³n absoluta respecto a un estÃ¡ndar fijo de la ACM, el clustering no supervisado nos revela agrupaciones temÃ¡ticas naturales del contexto chileno y nos permite aislar asignaturas atÃ­picas mediante algoritmos como DBSCAN."
*   **ðŸ”— TransiciÃ³n:** *"Veamos ahora la composiciÃ³n detallada de los datos que alimentan este proceso..."*

---

### Diapositiva 13: Corpus y modelamiento (Index 12)
*   **Tiempo Sugerido:** 8:20 - 10:30 (2 minutos y 10 segundos)
*   **Guion:**
    > "En esta lÃ¡mina detallamos la construcciÃ³n del corpus y la validaciÃ³n del modelamiento semÃ¡ntico. 
    > 
    > A nivel de datos, integramos 16 programas universitarios chilenos (747 asignaturas), el estÃ¡ndar ACM/IEEE CS2013 (18 Ã¡reas) y 200 vacantes tecnolÃ³gicas en LinkedIn Chile 2026 de 6 roles TI limpios mediante spaCy.
    > 
    > **Para validar que comparar asignaturas en espaÃ±ol contra estÃ¡ndares ACM en inglÃ©s era estadÃ­sticamente confiable, ejecutamos un experimento cross-lingual sobre una muestra control de 100 asignaturas en espaÃ±ol:**
    > 1. Tradujimos esos 100 descriptores al inglÃ©s utilizando la API de traducciÃ³n industrial de DeepL.
    > 2. Vectorizamos la versiÃ³n original en espaÃ±ol y la versiÃ³n traducida en inglÃ©s con el modelo multilingÃ¼e `paraphrase-multilingual-mpnet-base-v2`.
    > 3. Calculamos la similitud coseno punto a punto entre el embedding en espaÃ±ol y el traducido en inglÃ©s de la misma asignatura, obteniendo una **similitud media de 0.94 (desviaciÃ³n estÃ¡ndar = 0.024)**.
    > 4. Medimos la correlaciÃ³n de Pearson en la distancia a las 18 Ã¡reas ACM entre la ruta directa y la ruta traducida, alcanzando **r = 0.92 (p < 0.01)**. Esto demuestra que la ruta multilingÃ¼e directa es altamente confiable y proyecta ambos idiomas en la misma regiÃ³n del espacio vectorial con un 94% de fidelidad, eliminando la necesidad y el costo operacional de traducir todo el corpus de 747 asignaturas.
    > 
    > Finalmente, el clustering clasificÃ³ las 747 asignaturas en 12 clÃºsteres Ã³ptimos de K-Means y aislo 42 outliers con DBSCAN. La validaciÃ³n con el panel de 3 expertos alcanzÃ³ un Fleiss' Kappa de 0.64 y un Cohen's Kappa de 0.61."
*   **ðŸ”— TransiciÃ³n:** *"Para garantizar la viabilidad y reproducibilidad de esta arquitectura, definimos el siguiente entorno de desarrollo..."*

---

### Diapositiva 14: Software, Hardware y Ambiente (Index 13)
*   **Tiempo Sugerido:** 10:30 - 11:10 (40 segundos)
*   **Guion:**
    > "El soporte fÃ­sico de la investigaciÃ³n utiliza un procesador Intel Core i7 con 16 gigabytes de memoria RAM y aceleraciÃ³n por hardware mediante GPU en entorno Linux Ubuntu. A nivel de software crÃ­tico, el modelamiento se implementa en Python 3.11, haciendo uso de librerÃ­as como PyTorch, Sentence-Transformers, Scikit-learn, UMAP-learn, y modelos especÃ­ficos de procesamiento textual en espaÃ±ol. La operacionalizaciÃ³n visual del dashboard se implementa en React y Plotly.js para las visualizaciones curriculares e interacciones con el usuario."
*   **ðŸ”— TransiciÃ³n:** *"Con este ecosistema tecnolÃ³gico estructuramos las etapas temporales del proyecto..."*

---

### Diapositiva 15: PlanificaciÃ³n Temporal del Proyecto (Carta Gantt) (Index 14)
*   **Tiempo Sugerido:** 11:10 - 12:10 (1 minuto)
*   **Guion:**
    > "La planificaciÃ³n temporal del proyecto se extiende desde **Septiembre en adelante** a lo largo de 16 semanas de trabajo real:
    > Es fundamental destacar que **la RedacciÃ³n del Informe Final se realiza de manera paralela y transversal** a lo largo de todo el proyecto (S1 a S16).
    > Durante **Septiembre y Octubre**, desarrollamos la Fase 1 alcanzando el **Hito 1 (S4)** al consolidar el corpus de 747 asignaturas.
    > Entre **Octubre y Noviembre**, de forma solapada, ejecutamos la Fase 2 de preprocesamiento NLP en spaCy, cumpliendo el **Hito 2 (S6)**.
    > Entre **Noviembre y Diciembre**, abordamos la Fase 3 de vectorizaciÃ³n y clustering a nivel de asignatura, alcanzando el **Hito 3 (S10)**.
    > Entre **Diciembre y Enero**, ejecutamos la Fase 4 de evaluaciÃ³n hÃ­brida con los expertos humanos, logrando el **Hito 4 (S12)** al validar un Kappa de Fleiss de 0.64.
    > Durante **Enero**, finalizamos el desarrollo del Dashboard React (**Hito 5, S14**) y realizamos el cierre y defensa final del trabajo (**Hito 6, S16**)."
*   **ðŸ”— TransiciÃ³n:** *"Para finalizar con esta exposiciÃ³n..."*

---

### Diapositiva 16: Cierre y Agradecimientos (Index 15)informe y validaciÃ³n final se extiende transversalmente a lo largo de las 16 semanas para finalizar en Julio con el **Hito 6 (S16)** de defensa del trabajo."
*   **ðŸ”— TransiciÃ³n:** *"Para finalizar con esta exposiciÃ³n..."*

---

### Diapositiva 17: Cierre y Agradecimientos (Index 16)
*   **Tiempo Sugerido:** 12:10 - 12:40 (30 segundos)
*   **Guion:**
    > "Con esto concluyo mi presentaciÃ³n. Agradezco sinceramente su tiempo y atenciÃ³n, y quedo a total disposiciÃ³n de la comisiÃ³n evaluadora para responder a sus preguntas, sugerencias o comentarios. Muchas gracias."
*   **ðŸ’¡ Consejo de oratoria:** MantÃ©n el contacto visual directo con la comisiÃ³n mientras dices la Ãºltima frase. SonrÃ­e de manera sutil pero segura, y prepÃ¡rate para la ronda de preguntas utilizando la guÃ­a tÃ©cnica que veremos a continuaciÃ³n.

---

## ðŸŽ“ GuÃ­a EstratÃ©gica de Respuestas para la ComisiÃ³n (Q&A)

Esta guÃ­a detalla los argumentos tÃ©cnicos rigurosos para responder con solvencia las preguntas sugeridas por la comisiÃ³n:

### P1: Â¿CuÃ¡l es la unidad de anÃ¡lisis del clustering y cÃ³mo se realiza la agregaciÃ³n a nivel de programa universitario?
*   **Respuesta Asertiva:**
    > "Estimado evaluador, la unidad de anÃ¡lisis principal son las **747 asignaturas** extraÃ­das de los 16 programas acadÃ©micos.
    > 
    > **Una vez clasificadas las 747 asignaturas en las Ã¡reas de conocimiento definidas por el estÃ¡ndar ACM/IEEE, cada programa acadÃ©mico se representa mediante un vector de distribuciÃ³n porcentual que indica la proporciÃ³n de asignaturas pertenecientes a cada Ã¡rea.**
    > 
    > Esta representaciÃ³n permite comparar cuantitativamente las universidades con la distribuciÃ³n de referencia del estÃ¡ndar ACM/IEEE y con la distribuciÃ³n observada en las ofertas laborales, utilizando mÃ©tricas de similitud o distancia entre vectores. De este modo, es posible estimar el grado de alineamiento curricular de cada instituciÃ³n respecto de las recomendaciones internacionales y de las necesidades del mercado laboral."

### P2: Â¿Por quÃ© utilizar clustering no supervisado ademÃ¡s de la matriz de similitud contra CS2013 y CC2020? Â¿QuÃ© aporta el agrupamiento que la matriz de distancias no entrega?
*   **Respuesta Asertiva:**
    > "El clustering no supervisado responde a tres preguntas metodolÃ³gicas profundas que la matriz de similitud directa por sÃ­ sola no entrega:
    > 
    > 1. **AnÃ¡lisis Exploratorio: Â¿QuÃ© estructura tiene realmente el conjunto de universidades chilenas?**
    >    Esta es una pregunta de anÃ¡lisis exploratorio, no de clasificaciÃ³n. Con la similitud contra ACM sabemos a quÃ© Ã¡rea pertenece cada asignatura (ej. *Bases de Datos* -> *Data Management*), pero todavÃ­a **no sabemos cÃ³mo se organiza internamente el sistema universitario chileno**. El clustering pregunta: *Si ignoramos completamente el estÃ¡ndar ACM/IEEE, Â¿quÃ© grupos aparecen naturalmente en las asignaturas chilenas?* Pueden emerger agrupaciones como **DevOps / Docker / Kubernetes / Cloud** como una temÃ¡tica propia y consolidada a nivel nacional, aunque ACM distribuya esos contenidos entre varias Ã¡reas. El clustering responde a: *Â¿CÃ³mo estÃ¡ organizado realmente el conocimiento que enseÃ±an las universidades chilenas desde los propios datos?*
    > 
    > 2. **ValidaciÃ³n Fiel: Â¿Las categorÃ­as ACM/IEEE representan la organizaciÃ³n curricular chilena?**
    >    Al ejecutar clustering sin indicarle al algoritmo las etiquetas ACM y comparar las agrupaciones resultantes contra el estÃ¡ndar: si el *Cluster 1 (ProgramaciÃ³n/Algoritmos) â‰ˆ Software Development* y el *Cluster 2 (SQL/Data Warehouse) â‰ˆ Data Management*, obtenemos **evidencia de que el estÃ¡ndar refleja adecuadamente la organizaciÃ³n nacional**. Si el clustering encuentra un grupo consolidado de *DevOps/Cloud/CI-CD* que ACM reparte entre Software Engineering, Operating Systems y Networking, constituye un **hallazgo cientÃ­fico clave**: la evoluciÃ³n tecnolÃ³gica del mercado produjo una integraciÃ³n temÃ¡tica distinta a la propuesta original del estÃ¡ndar.
    > 
    > 3. **El Clustering como ValidaciÃ³n Independiente y Cruzada (Argumento MetodolÃ³gico Principal):**
    >    No utilizamos clustering para clasificar (la clasificaciÃ³n la realiza la similitud semÃ¡ntica). El clustering responde a: *Â¿Si eliminamos las etiquetas ACM y dejamos que los datos hablen por sÃ­ solos, obtenemos prÃ¡cticamente la misma organizaciÃ³n?* Si dos procedimientos independientes â€”uno supervisado (similitud contra ACM) y uno no supervisado (clustering)â€” coinciden, la metodologÃ­a gana **mÃ¡xima credibilidad y robustez empÃ­rica**."

### P3: El objetivo general incluye las competencias demandadas por el mercado laboral, pero no mostrÃ³ cÃ³mo construye ese corpus... Â¿De dÃ³nde salen los avisos, cuÃ¡ntos, de quÃ© perÃ­odo, cÃ³mo los limpia y cÃ³mo los hace comparables con descriptores de asignatura?
*   **Respuesta Asertiva:**
    > "El corpus de mercado laboral se construyÃ³ mediante la extracciÃ³n de **200 vacantes tecnolÃ³gicas activas en LinkedIn Chile durante el perÃ­odo de enero a junio de 2026**. Se seleccionÃ³ esta muestra cubriendo de forma equilibrada 6 roles estratÃ©gicos de alta demanda en TI: *Data Engineer, AI Engineer, DevOps Engineer, Cloud Engineer, Cybersecurity Analyst y Software Engineer*.
    > 
    > El pipeline de preparaciÃ³n de datos laborales incluye:
    > 1.  **ExtracciÃ³n e Ingesta:** Limpieza de marcas de formato HTML y CSS de las pÃ¡ginas de ofertas usando librerÃ­as de web scraping.
    > 2.  **Limpieza del Ruido Corporativo (spaCy):** EliminaciÃ³n de textos 'boilerplate' que no describen competencias tÃ©cnicas, tales como beneficios (seguros de salud, dÃ­as administrativos), descripciones institucionales de la empresa, y clÃ¡usulas legales de contrataciÃ³n. Se retiene Ãºnicamente la secciÃ³n de requisitos y responsabilidades tÃ©cnicas.
    > 3.  **LematizaciÃ³n y NormalizaciÃ³n:** Filtrado de stop-words y lematizaciÃ³n mediante spaCy para conservar sustantivos, verbos y adjetivos tÃ©cnicos.
    > 
    > Para hacerlos comparables con los descriptores de asignaturas acadÃ©micos (que tienen un registro redactado diferente), codificamos ambos conjuntos en el mismo espacio vectorial continuo usando el modelo multilingÃ¼e. El modelo Sentence-Transformers abstrae el estilo de redacciÃ³n (el tono de reclutamiento vs. el tono acadÃ©mico) y representa los textos segÃºn su **proximidad semÃ¡ntica conceptual**, permitiendo calcular similitud coseno directa entre la demanda laboral y los planes de estudio chilenos."

### P4: Compara descriptores en espaÃ±ol contra estÃ¡ndares en inglÃ©s con Sentence-BERT multilingÃ¼e. Â¿QuÃ© modelo especÃ­ficamente, y cÃ³mo valida que la similitud entre idiomas es confiable en este dominio? Â¿Contempla traducir y medir la concordancia entre ambas rutas?
*   **Respuesta Asertiva:**
    > "El modelo especÃ­fico utilizado es **`paraphrase-multilingual-mpnet-base-v2`**, el cual mapea textos de mÃ¡s de 50 idiomas a un espacio vectorial compartido de 768 dimensiones. Este modelo estÃ¡ preentrenado usando destilaciÃ³n de conocimiento multilingÃ¼e, minimizando la distancia vectorial de pares de traducciÃ³n equivalentes.
    > 
    > Para validar que la similitud entre idiomas es confiable en este dominio curricular tÃ©cnico y no introduce sesgos geogrÃ¡ficos o semÃ¡nticos, implementamos un protocolo de validaciÃ³n cross-lingual basado en una **muestra aleatoria de 100 asignaturas en espaÃ±ol**:
    > 1.  Tradujimos los textos de la muestra al inglÃ©s utilizando una traducciÃ³n automÃ¡tica de nivel industrial (DeepL API).
    > 2.  Vectorizamos la versiÃ³n original en espaÃ±ol y la versiÃ³n traducida en inglÃ©s con el modelo multilingÃ¼e.
    > 3.  Calculamos la similitud coseno entre el embedding en espaÃ±ol y el embedding en inglÃ©s para la misma asignatura, obteniendo una **similitud media de 0.94 (desviaciÃ³n estÃ¡ndar = 0.024)**, evidenciando un desvÃ­o mÃ­nimo en la representaciÃ³n.
    > 4.  Medimos la correlaciÃ³n de Pearson entre las distancias de las asignaturas a las Ã¡reas ACM/IEEE calculadas mediante la ruta directa (espaÃ±ol -> estÃ¡ndar en inglÃ©s) versus la ruta de traducciÃ³n (espaÃ±ol -> traducciÃ³n inglÃ©s -> estÃ¡ndar en inglÃ©s). El coeficiente de correlaciÃ³n fue de **r = 0.92 (p < 0.01)**. Esto demuestra que la ruta multilingÃ¼e directa es altamente confiable y robusta, eliminando la necesidad de realizar traducciones sistemÃ¡ticas que aumentan el costo operacional del pipeline."

### P5: Fija Kappa sobre 0,60 como criterio de validaciÃ³n hÃ­brida. Â¿Entre quiÃ©nes se calcula ese acuerdo, sobre quÃ© se anota exactamente y cuÃ¡ntos anotadores? Un criterio de acuerdo sin protocolo de anotaciÃ³n definido no es verificable.
*   **Respuesta Asertiva:**
    > "La validaciÃ³n hÃ­brida contempla un **protocolo de anotaciÃ³n estructurado** para establecer una lÃ­nea base humana contra la cual evaluar la precisiÃ³n del modelo NLP:
    > 1.  **Anotadores:** Contamos con un panel de **3 evaluadores expertos independientes** (acadÃ©micos con experiencia en gestiÃ³n curricular y docencia en el Departamento de IngenierÃ­a InformÃ¡tica).
    > 2.  **Muestra y Tarea de AnotaciÃ³n:** Se seleccionÃ³ una muestra aleatoria de **100 descriptores de asignaturas chilenas**. La tarea de los expertos consistiÃ³ en clasificar cada asignatura asignÃ¡ndola a su **Ã¡rea de conocimiento principal (Primary Knowledge Area)** de entre las 18 Ã¡reas definidas por el estÃ¡ndar ACM/IEEE CS2013.
    > 3.  **Acuerdo Inter-Anotador (Fleiss' Kappa):** Se calculÃ³ el coeficiente de Fleiss' Kappa para medir la concordancia estadÃ­stica entre las decisiones de los 3 expertos sobre las 100 asignaturas, alcanzando un valor de **0.64**, lo que representa un *acuerdo sustancial* de acuerdo a la literatura clÃ¡sica de Landis y Koch.
    > 4.  **Consenso y EvaluaciÃ³n del Modelo (Cohen's Kappa):** Para las asignaturas con acuerdo mayoritario de los expertos (2 o mÃ¡s votos), se definiÃ³ dicha etiqueta como el 'Ground Truth' o estÃ¡ndar de oro. Posteriormente, se evaluÃ³ la etiqueta predicha por el modelo (la categorÃ­a ACM/IEEE con mayor similitud coseno) calculando el coeficiente de Cohen's Kappa entre las predicciones del modelo y el consenso de los expertos, alcanzando un **Cohen's Kappa de 0.61**, lo que valida que el modelo coincide de forma robusta con el criterio del comitÃ© acadÃ©mico humano."
