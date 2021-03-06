## 脥ndice

1. [馃摑 Introducci贸n](#Introducci贸n)
2. [鉁堬笍 Gesti贸n del Tr谩fico A茅reo](#Gesti贸n_Del_Tr谩fico_A茅reo)
3. [馃洭 Configuraci贸n de las pistas](#Configuraci贸n_De_Las_Pistas)
4. [馃洬 Aeropuerto Adolfo Su谩rez Madrid-Barajas](#Aeropuerto_Adolfo_Su谩rez_Madrid-Barajas)
5. [鉁? Objetivos del proyecto](#Objetivos_Del_Proyecto)
6. [馃摎 Conjunto y Modelo de Datos](#Conjunto_Y_Modelo_De_Datos)
7. [馃 Modelos de Aprendizaje Autom谩tico](#Modelos_De_Aprendizaje_Autom谩tico)
8. [鈴? Prueba Inicial de Modelos](#Prueba_Inicial_De_Modelos)
9. [馃尣 Bosques Aleatorios](#Bosques_Aleatorios)
10. [馃彉 K-Vecinos m谩s Cercanos](#K-Vecinos_M谩s_Cercanos)
11. [馃搱 Regresi贸n Log铆stica](#Regresi贸n_Log铆stica)
12. [馃 Redes Neuronales](#Redes_Neuronales)
13. [馃洜 Optimizaci贸n de los modelos](#Optimizaci贸n_De_Los_Modelos)
14. [馃尣 Bosques Aleatorios](#Bosques_Aleatorios)
15. [馃彉 K-Vecinos m谩s Cercanos](#K-Vecinos_M谩s_Cercanos)
16. [馃搱 Regresi贸n Log铆stica](#Regresi贸n_Log铆stica)
17. [馃 Redes Neuronales](#Redes_Neuronales)
18. [馃ぜ鈥嶁檧锔? Comparativa de la mejora entre el modelo Base y el modelo optimizado](#Comparativa_De_La_Mejora_Entre_El_Modelo_Base_Y_El_Modelo_Optimizado)
19. [馃挴 Evaluaci贸n de los modelos](#Evaluaci贸n_De_Los_Modelos)
20. [馃彌 Arquitectura L贸gica de la herramienta](#Arquitectura_L贸gica_De_La_Herramienta)
21. [鈿欙笍 Estructura del Proyecto](#Estructura_Del_Proyecto)
22. [馃摲 Capturas de pantalla](#Capturas_De_Pantalla)
23. [馃敋 Conclusiones y Trabajo Futuro](#Conclusiones_Y_Trabajo_Futuro)
24. [馃敋 Conclusiones](#Conclusiones)
25. [馃敭 Trabajo Futuro](#Trabajo_Futuro)

Repositorio del proyecto fin de grado: **Selecci贸n y Optimizaci贸n de algoritmos para la predicci贸n de configuraciones en aeropuertos** Link a la web con la memoria oficial: [UVaDoc](https://uvadoc.uva.es/handle/10324/41331)

# 馃摑 Introducci贸n <a name="Introducci贸n"></a>
## 鉁堬笍 Gesti贸n del Tr谩fico A茅reo <a name="Gesti贸n_Del_Tr谩fico_A茅reo"></a>
* En los 煤ltimos a帽os el n煤mero de transacciones a茅reas ha crecido de manera exponencial y se espera que esta cifra siga aumentando a lo largo de los pr贸ximos a帽os.
* Para poder albergar esta cantidad de vuelos, los aeropuertos han de disponer de una buena infraestructura (n煤mero de pistas, orientaci贸n, accesos, etc) y contar con una buena **gesti贸n del tr谩fico a茅reo.**

**Gesti贸n del Tr谩fico A茅reo: La gesti贸n del tr谩fico a茅reo comprende todas aquellas acciones e interacciones que se llevan a cabo para ayudar a una aeronave a trasladarse de un aer贸dromo de origen a otro de destino de una forma segura.**

## 馃洭 Configuraci贸n de las pistas <a name="Configuraci贸n_De_Las_Pistas"></a>

En este proyecto nos vamos a centrar en las pistas y en su configuraci贸n. *Una pista es una superficie rectangular destinada a la realizaci贸n de las maniobras de aterrizaje y despegue por parte de las aeronaves.*

Dependiendo de su relevancia pueden ser de dos tipos:
* **Pista principal:** Pista que se utiliza de forma usual en el aeropuerto
siempre y cuando las condiciones para su uso sean adecuadas.
* **Pista Secundaria:** Pista auxiliar que se utiliza cuando la pista
principal no se encuentre disponible ya sea por motivos meteorol贸gicos o por motivos log铆sticos.

**La configuraci贸n de las pistas hace referencia al n煤mero, orientaci贸n y agrupamiento de las pistas dentro de un aeropuerto.** Los principales tipos de configuraci贸n de las pistas son los siguientes:

* **Pistas Simples:** Consta de una 煤nica pista en la que se llevan a cabo las operaciones de aterrizaje o de despegue.
* **Pistas Paralelas:** Combinaci贸n de dos o m谩s pistas simples.
* **Pistas que se cortan:** Combinaci贸n de dos o m谩s pistas simples de manera que existe una intersecci贸n entre ambas.
* **Pistas en V abierta:** Combinaci贸n de dos pistas simples en direcciones opuestas que no llegan a cortarse nunca.

### 馃洬 Aeropuerto Adolfo Su谩rez Madrid-Barajas <a name="Aeropuerto_Adolfo_Su谩rez_Madrid-Barajas"></a>

Es el aeropuerto m谩s grande de Espa帽a y el 5潞 m谩s grande de Europa. Dispone de 4 pistas dispuestas en paralelo 2 a 2 (14L, 14R, 18L, 18R, 32L, 32R, 36L, 36R).

Las pistas se encuentran distribuidas en 2 configuraciones distintas (Ver Figura 1):

* **Configuraci贸n Norte:** Aterrizajes (32L y 32R); Despegues (36L y 36R).
* **Configuraci贸n Sur:** Aterrizajes (18L y 18R); Despegues (14L y 14R).

![Configuracion Norte](assets/ConfiguracionNORTE.jpg)
![Configuracion Sur](assets/ConfiguracionSUR.jpg)
**Figura 1: Configuraci贸n de pistas del aeropuerto de Madrid-Barajas.**


## 鉁? Objetivos del proyecto <a name="Objetivos_Del_Proyecto"></a>
Los objetivos fijados para este proyecto son:
* **Procesamiento y an谩lisis** de los datos de los vuelos.
* **Prueba y optimizaci贸n** de modelos de aprendizaje autom谩tico.
* **Evaluaci贸n y selecci贸n** del modelo de aprendizaje autom谩tico final.
* **Dise帽o e implementaci贸n** de un *dashboard* de visualizaci贸n e interacci贸n con el modelo de aprendizaje autom谩tico.

# 馃摎 Conjunto y Modelo de Datos <a name="Conjunto_Y_Modelo_De_Datos"></a>

El conjunto de datos utilizado se encuentra constituido por registros individuales de operaciones de aterrizaje y despegue llevadas a cabo en el Aeropuerto de Barajas durante los a帽os 2018 y 2019. Consta de 733.825 registros de vuelos, de los cu谩les 346.198 (aproximadamente el 47,17%) pertenecen a operaciones realizadas durante el a帽o 2018, mientras que 387.627 (52,83 %) corresponden al a帽o 2019. Adem谩s se dispone de informaci贸n relativa al vuelo, la meteorolog铆a en el momento de realizar la maniobra y los datos de la aeronave en dicho momento.

El diagrama de clases en el que se encuentran estructuradas las distintas caracter铆sticas que conforman el conjunto de datos es el siguiente:

![Diagrama de Clases](assets/Diagrama-Clases.png)
**Figura 2: Diagrama de Clases de los datos del proyecto.**

# 馃 Modelos de Aprendizaje Autom谩tico <a name="Modelos_De_Aprendizaje_Autom谩tico"></a>

Para la prueba de los modelos de aprendizaje autom谩tico, se han generado cuatro subconjuntos de datos distintos:
* **FULL:** Todas las caracter铆sticas y *Target* multicolumna.
* **FNORM:** Todas las caracter铆sticas y *Target* normalizado.
* **RELATED:** Todas las caracter铆sticas **relacionadas** y *Target* multicolumna.
* **RNORM:** Todas las caracter铆sticas **relacionadas** y *Target* normalizado.

Estos subconjuntos han sido probados en los siguientes modelos de aprendizaje autom谩tico en su configuraci贸n base de [scikit-learn](https://scikit-learn.org/stable/):
* **Bosques Aleatorios.**
* **K-Vecinos M谩s Cercanos.**
* **Regresi贸n Log铆stica.**
* **Redes Neuronales.**

## 鈴? Prueba Inicial de modelos <a name="Prueba_Inicial_De_Modelos"></a>
### 馃尣 Bosques Aleatorios <a name="Bosques_Aleatorios"></a>
Modelo basado en Bosques Aleatorios:
* **N煤mero de 谩rboles:** Variable.
* **Profundidad:** Sin l铆mite.
* **M铆nimo de ejemplos para dividir nodo interno:** 2.
* **M铆nimo de ejemplos por nodo hoja:** 1.

![Bosques Aleatorios Inicial](assets/randomForest-global.png)
**Figura 3: Precisi贸n del modelo basado en Bosques Aleatorios con la configuraci贸n base.**

### 馃彉 K-Vecinos M谩s Cercanos <a name="K-Vecinos_M谩s_Cercanos"></a>
Modelo basado en K-Vecinos M谩s Cercanos:
* **N煤mero de vecinos:** Variable.
* **Pesos:** Uniforme.
* **Distancia:** *Minkowski*.

![KNN Inicial](assets/knn-global.png)
**Figura 4: Precisi贸n del modelo basado en K-Vecinos m谩s Cercanos con la configuraci贸n base.**

### 馃搱 Regresi贸n Log铆stica <a name="Regresi贸n_Log铆stica"></a>
Modelo basado en Regresi贸n Log铆stica:
* **Algoritmo de Resoluci贸n:** Variable.
* **Penalizador:** *l2*.

![RL Inicial](assets/logistic_regression-global-def.png)
**Figura 5: Precisi贸n del modelo basado en Regresi贸n Log铆stica con la configuraci贸n base.**

### 馃 Redes Neuronales <a name="Redes_Neuronales"></a>

Modelo basado en Redes Neuronales:
* **Configuraci贸n:** (100).
* **Activaci贸n:** Variable.
* **Algoritmo de Resoluci贸n:** *Adam*.
* **Factor Aprendizaje:** 0,001.
* **Tipo Factor Aprendizaje:** Constante.

![RRNN Inicial](assets/neural_network-activation-global.png)
**Figura 6: Precisi贸n del modelo basado en Redes Neuronales con la configuraci贸n base.**

## 馃洜 Optimizaci贸n de los modelos <a name="Optimizaci贸n_De_Los_Modelos"></a>

### 馃尣 Bosques Aleatorios <a name="Bosques_Aleatorios"></a>

![Bosques Aleatorios Profundidad](assets/Random_Forest_Max-Depth.png)
**Figura 7: Precisi贸n del modelo basado en Bosques Aleatorios modificando el par谩metro "Profundidad".**
![Bosques Aleatorios Ejemplos Dividir Nodo](assets/Random_Forest_Min-Samples-Split.png)
**Figura 8: Precisi贸n del modelo basado en Bosques Aleatorios modificando el par谩metro "M铆nimo de ejemplos antes de dividir un nodo interno".**
![Bosques Aleatorios Ejemplos Dividir Nodo Hoja](assets/Random_Forest_Min-Samples-Leaft.png)
**Figura 9: Precisi贸n del modelo basado en Bosques Aleatorios modificando el par谩metro "M铆nimo de ejemplos antes de dividir un nodo hoja".**

![Bosques Aleatorios Mejora](assets/comparativaRF.png)
**Figura 10: Comparativa entre los par谩metros por defecto y los par谩metros optimizados.**

### 馃彉 K-Vecinos M谩s Cercanos <a name="K-Vecinos_M谩s_Cercanos"></a>
![KNN Asignacion Distancia](assets/knnDISTANCIA.png)
**Figura 11: Precisi贸n del modelo basado en K-Vecinos m谩s Cercanos modificando el par谩metro "Tipo de Distancia".**

![KNN Asignacion Pesos](assets/knn5-distance.png)
**Figura 12: Precisi贸n del modelo basado en K-Vecinos m谩s Cercanos modificando el par谩metro "F贸rmula para calcular la distancia".**

![KNN Mejora](assets/comparativaKNN.png)
**Figura 13: Comparativa entre los par谩metros por defecto y los par谩metros optimizados.**

### 馃搱 Regresi贸n Log铆stica <a name="Regresi贸n_Log铆stica"></a>

![RL Optimizada](assets/logistic_regression-global.png)
**Figura 14: Comparativa entre los par谩metros por defecto y los par谩metros optimizados.**

### 馃 Redes Neuronales <a name="Redes_Neuronales"></a>

![RNN Capas y Neuronas](assets/neural_network-layers-global.png)
**Figura 15: Precisi贸n del modelo basado en Redes Neuronales modificando el par谩metro "N煤mero de Capas".**

![RNN Configuraci贸n](assets/neural_network-configuration.png)
**Figura 16: Precisi贸n del modelo basado en Redes Neuronales modificando el par谩metro "N煤mero de Neuronas por capa".**

![RNN Learning Rate](assets/neural_network-learning_rate-global.png)
**Figura 17: Precisi贸n del modelo basado en Redes Neuronales modificando el par谩metro "Factor de Aprendizaje".**

![RNN Epocas](assets/Neural_Network_Validation-Curve.png)
**Figura 18: Precisi贸n del modelo basado en Redes Neuronales modificando el par谩metro "N煤mero de 脡pocas".**

![RRNN Mejora](assets/comparativaRRNN.png)
**Figura 19: Comparativa entre los par谩metros por defecto y los par谩metros optimizados.**

### 馃ぜ鈥嶁檧锔? Comparativa de la mejora entre el modelo base y el modelo optimizado <a name="Comparativa_De_La_Mejora_Entre_El_Modelo_Base_Y_El_Modelo_Optimizado"></a>

![Mejora Global](assets/comparativaGlobal.png)
**Figura 20: Comparativa de precisi贸n entre los modelos base y los modelos optimizados.**

# 馃挴 Evaluaci贸n de los modelos <a name="Evaluaci贸n_De_Los_Modelos"></a>

La evaluaci贸n se ha llevado a cabo utilizando la t茅cnica de la validaci贸n cruzada. Para ello se divide el conjunto de entrenamiento en *k* subconjuntos iguales, de tal forma que en cada una de las *i* iteraciones (*i=1 ... k*), se utilizar谩 el subconjunto *i* como conjunto de prueba y los *k-1* restantes como subconjuntos de entrenamiento.

**Cuanto menor sea la diferencia entre la precisi贸n obtenida con el conjunto de entrenamiento y la del conjunto de prueba, mejor ser谩 el modelo.**

![Comparativa Train Test](assets/cv1.png)
**Figura 21: Comparativa de precisi贸n mediante validaci贸n cruzada entre los modelos optimizados.**
![Comparativa entre los modelos](assets/cv2.png)
**Figura 22: Comparativa de m茅tricas (precision, recall y F1) mediante validaci贸n cruzada entre los modelos optimizados.**

# 馃彌 Arquitectura l贸gica de la herramienta <a name="Arquitectura_L贸gica_De_La_Herramienta"></a>

La arquitectura l贸gica de la herramienta es la siguiente:
![Estructura logica](assets/ArquitecturaLogica.jpg)
**Figura 23: Arquitectura l贸gica de la herramienta software.**

# 鈿欙笍 Estructura del proyecto <a name="Estructura_Del_Proyecto"></a>
El repositorio se encuentra estructurado de la siguiente forma:

````
.
鈹溾攢鈹? app/ # Herramienta software
鈹?   鈹溾攢鈹? data/ # Datos para generar las visualizaciones
鈹?   鈹溾攢鈹? img/ # Im谩genes de la herramienta
鈹?   鈹溾攢鈹? modules/ # M贸dulos para realizar diferentes tareas en la herramienta (carga de datos, inferencia del modelo, generaci贸n de gr谩ficos, etc)
鈹?   鈹斺攢鈹? app.py # Script principal para el despliegue de la herramienta
鈹溾攢鈹? assets/ # Im谩genes del README
鈹溾攢鈹? Documentacion Tecnica/ # Memoria y presentaci贸n del proyecto en PDF
鈹溾攢鈹? Notebooks/ # Ficheros .ipynb adicionales
鈹溾攢鈹? README.md
鈹斺攢鈹? requirements.txt # Dependencias python para ejecutar la herramienta
````

# 馃摲 Capturas de pantalla <a name="Capturas_De_Pantalla"></a>
![Dashboard Datos](assets/dash-datos.png)
**Figura 24: Visualizaci贸n de los datos en el Dashboard.**

![Dashboard Metricas](assets/dash-metrics.png)
**Figura 25: Visualizaci贸n de los m茅tricas de los modelos en el Dashboard.**

![Dashboard Evaluacion](assets/dash-evaluacion.png)
**Figura 26: Inferencia de la configuraci贸n de las pistas en base a la meteorolog铆a utilizando el Dashboard.**


# 馃敋 Conclusiones y Trabajo Futuro <a name="Conclusiones_Y_Trabajo_Futuro"></a>

## 馃敋 Conclusiones <a name="Conclusiones"></a>
Las conclusiones que se han obtenido tras la realizaci贸n del proyecto son:

* Los resultados obtenidos a lo largo de las distintas etapas de prueba y optimizaci贸n de los modelos de aprendizaje autom谩tico han sido muy buenos a pesar de que la elecci贸n de las pistas es una decisi贸n complicada en la que influyen muchos factores externos.
* Diferencia de precisi贸n de los modelos con los distintos subconjunto de datos (se consigue una media de un 2,84% m谩s utilizando todas las caracter铆sticas que 煤nicamente las que tienen relaci贸n con la configuraci贸n).
* Gran homogeneidad y robustez del modelo final para clasificar nuevos vuelos teniendo en cuenta la complejidad del problema a tratar.

## 馃敭 Trabajo Futuro <a name="Trabajo_Futuro"></a>
Las posibles l铆neas de trabajo futuro que se abren tras la finalizaci贸n del proyecto son:

* **Aplicaci贸n del modelo en otros aeropuertos:** Una l铆nea de trabajo consiste en evaluar los resultados del modelo en otros aeropuertos con otras caracter铆sticas (distinto n煤mero de pistas, mayor variedad en las configuraciones, diferente climatolog铆a, etc), para analizar su comportamiento en distintas circunstancias.
* **Utilizaci贸n de modelos basados en Aprendizaje Profundo:** Por lo general este tipo de modelos arrojan mejores resultados que los modelos tradicionales, por lo que analizar y evaluar distintos modelos basados en Aprendizaje Profundo para resolver esta problem谩tica, es una l铆nea de trabajo futuro a investigar.
