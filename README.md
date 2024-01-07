# Ejercicios de Cena Navideña

## Nivel Principiante:

---

## 1. Suma de 3 Números Enteros Positivos

Este programa en Python permite al usuario ingresar tres números enteros positivos e imprime la sumatoria de los tres números. A continuación, se explica el funcionamiento del programa:

## Funcionamiento del Programa:

1. **Ingreso de Números:**
   - El programa solicita al usuario ingresar tres números enteros positivos, denotados como `a`, `b` y `c`.
   - Realiza una validación para asegurar que los valores ingresados sean enteros.
2. **Cálculo de la Sumatoria:**
   - Verifica que los tres números ingresados sean positivos (mayores o iguales a 0).
   - Si los números son positivos, calcula la sumatoria de los tres números (a + b + c).
3. **Presentación de Resultados:**
   - Muestra en pantalla la sumatoria de los tres números, proporcionando una salida clara y formateada.
4. **Opción de Realizar Otra Operación:**
   - Pregunta al usuario si desea realizar otra operación.
   - Si el usuario ingresa 'S' (mayúscula o minúscula), puede ingresar otros tres números y repetir el proceso.
   - Si presiona "Enter", el programa se cierra.
5. **Manejo de Errores:**
   - En caso de ingresar valores no enteros, el programa maneja la excepción de `ValueError` y proporciona un mensaje de error.

## 2. Calcula IMC para estudiante de campusland

Este programa permite calcular el Índice de Masa Corporal (IMC) de  estudiantes nuevos en el Centro de Salud de Campuslands. Además,  presenta la información del estudiante, incluyendo el nombre, la edad,  el IMC y la categoría correspondiente según el IMC obtenido.

#### Categorías de IMC:

- **Normal:** 18.5 - 24.9
- **Sobrepeso:** 25 - 29.9
- **Obesidad I:** 30 - 34.9
- **Obesidad II:** 35 - 39.9
- **Obesidad III:** 40 <

#### Funcionamiento del Programa:

1. **Ingreso de Datos:**
   - Se solicita al usuario ingresar el nombre del estudiante, la edad, el peso y la altura.
   - Se realiza una validación para asegurar que los datos ingresados sean del tipo correcto (cadena para el nombre, entero para la edad, y flotantes para peso y altura).
2. **Cálculo del IMC:**
   - Utiliza la función `calcularIMC` para obtener el IMC a partir del peso y la altura ingresados.
3. **Determinación de la Categoría:**
   - Se asigna una categoría según el rango del IMC obtenido.
4. **Presentación de Resultados:**
   - Se muestra en pantalla la información del estudiante, incluyendo el nombre, la edad, el IMC y la categoría correspondiente.
5. **Manejo de Errores:**
   - En caso de ingresar datos incorrectos, el programa maneja la excepción de `ValueError` y proporciona un mensaje de error.

## 3. Reporte De Salud

Este programa en Python tiene como objetivo registrar información de salud de 20 estudiantes y generar un reporte que incluye estadísticas sobre el estado de salud de la comunidad estudiantil. A continuación, se explica el funcionamiento del programa:

## Funcionamiento del Programa:

1. **Registro de Estudiantes:**
   - El programa utiliza un bucle `for` para iterar sobre 20 estudiantes, solicitando información como nombre, edad, peso y altura.
   - Utiliza la función `calcularIMC` para determinar el Índice de Masa Corporal (IMC) de cada estudiante.
   - Clasifica a los estudiantes en categorías según su IMC (Normal, Sobrepeso, Obesidad I, Obesidad II, Obesidad III o Desnutrición).
2. **Conteo de Estudiantes por Categoría:**
   - Mantiene un seguimiento de la cantidad de estudiantes en cada categoría (Peso Ideal, Sobrepeso, Obesidad I, Obesidad II, Obesidad III y Desnutrición).
3. **Opción de Agregar Otro Usuario:**
   - Después de ingresar la información de un estudiante, el programa pregunta si se desea agregar otro usuario.
   - Si se responde 'S' (mayúscula o minúscula), se permite agregar información para un nuevo estudiante.
   - Si se responde 'N' o se llega al límite de 20 estudiantes, el programa sale del bucle y continúa con la presentación de resultados.
4. **Presentación de Resultados:**
   - Muestra en pantalla un reporte que indica la cantidad de estudiantes en cada categoría de salud.
   - Categorías incluidas: Desnutrición, Peso Ideal, Sobrepeso, Obesidad I, Obesidad II, Obesidad III.
5. **Manejo de Errores:**
   - En caso de ingresar valores no válidos (por ejemplo, no números para edad, peso o altura), el programa maneja la excepción de `ValueError` y proporciona un mensaje de error.

## 4. Reporte De Números Enteros Positivos

Este programa en Python permite al usuario ingresar una cantidad `n` de números enteros positivos y, cuando se ingresa un número negativo, genera un informe detallado sobre los números ingresados. A continuación, se explica el funcionamiento del programa:

#### Funcionamiento del Programa:

1. **Ingreso de Números Enteros Positivos:**
   - Solicita al usuario ingresar la cantidad `n` de números enteros positivos que desea registrar.
   - Utiliza un bucle `while` para permitir el ingreso continuo de números hasta que se ingresa un número negativo.
2. **Análisis de los Números Ingresados:**
   - Mientras se ingresan números positivos, se lleva a cabo el análisis de cada número.
   - Se determina si el número es par o impar, y se actualizan las estadísticas correspondientes.
3. **Reporte Final:**
   - Cuando se ingresa un número negativo, el programa muestra un reporte que incluye:
     - El total de números ingresados.
     - El total de números pares y su promedio.
     - El promedio de los números impares.
     - La cantidad de números menores que 10.
     - La cantidad de números entre 20 y 50.
     - La cantidad de números mayores que 100.
4. **Manejo de Errores:**
   - El programa valida que la cantidad `n` ingresada sea un número entero y positivo. En caso de ingresar valores no válidos, maneja la excepción de `ValueError` y proporciona un mensaje de error.



## Ejercicios Nivel Intermedio

---

## 1. Registro De Actividad Sismica En Ciudades

Este programa en Python tiene como objetivo registrar la actividad sísmica en ciudades, permitiendo la introducción de datos relacionados con las ciudades y los sismos registrados en ellas. A continuación, se explica el funcionamiento del programa:

### Módulos y Estructura del Programa:

1. **Programa Principal (`main.py`):**
   - Inicia el programa e importa los módulos necesarios.
   - Utiliza los módulos `menus`, `regCiudades` y `regSismos` para gestionar la interacción con el usuario y registrar la actividad sísmica.
2. **Módulo de Menús (`menus.py`):**
   - Proporciona funciones para mostrar menús y gestionar las opciones del usuario en el programa principal.
   - Maneja las excepciones de `ValueError` para garantizar la entrada de datos correcta.
3. **Módulo de Registro de Ciudades (`regCiudades.py`):**
   - Permite el registro de ciudades y almacena la información en una lista.
   - Limita el registro a un máximo de 5 ciudades.
   - Muestra las ciudades registradas al alcanzar el límite.
4. **Módulo de Registro de Sismos (`regSismos.py`):**
   - Permite registrar sismos asociados a una ciudad previamente registrada.
   - Utiliza una lista (`informeSismico`) para almacenar la información de las ciudades y los sismos registrados.
   - Maneja excepciones para garantizar la entrada de datos correcta.
5. **Funcionalidades Principales:**
   - El programa principal ofrece opciones para registrar ciudades, registrar sismos, buscar sismos por ciudad, generar informes de riesgo y salir del programa.
   - Se utilizan funciones para modularizar y organizar el código.
6. **Manejo de Errores:**
   - Se implementa un manejo adecuado de errores para evitar problemas al ingresar datos incorrectos.

## 2. Registro De Consumo Por Dependencia Gubernamental

Este programa en Python tiene como objetivo registrar el consumo en dependencias y observar el CO2 producido por cada uno:

### Módulos y Estructura del Programa:

1. **Programa Principal (`main.py`):**

   - Inicia el programa e importa los módulos necesarios.
   - Utiliza los módulos `menus`, `dependencias` y `regConsumo` para gestionar la interacción con el usuario y registrar el consumo en dependencias.

2. **Módulo de Menús (`menus.py`):**

   - Proporciona funciones para mostrar menús y gestionar las opciones del usuario en el programa principal.
   - Maneja las excepciones de `ValueError` para garantizar la entrada de datos correcta.

3. **Módulo de Registro de Dependencias (`dependencias.py`):**

   - Permite el registro de dependencias y almacena la información en un diccionario.
   - Cada dependencia tiene un diccionario interno para almacenar información relacionada con el consumo.

4. **Módulo de Registro de Consumo (`regConsumo.py`):**

   - Permite registrar el consumo asociado a una dependencia previamente registrada.
   - Utiliza un bucle `while` para permitir el ingreso continuo de registros de consumo.
   - Muestra un mensaje de error si la dependencia no se encuentra registrada.

5. **Módulo de Visualización de Consumo de CO2 (`verC02.py`):**

   - Proporciona funciones para visualizar el consumo de CO2 en dependencias.
   - Implementa una función para calcular y mostrar el promedio de consumo de CO2 en todas las dependencias.
   - Facilita la visualización de la información para ayudar en el análisis del consumo.

6. **Funcionalidades Principales:**

   - El programa principal ofrece opciones para registrar dependencias, registrar consumo, buscar consumo por dependencia y salir del programa.
   - Se utilizan funciones para modularizar y organizar el código.

7. **Manejo de Errores:**

   - Se implementa un manejo adecuado de errores para evitar problemas al ingresar datos incorrectos.

     

## PSEINT a Python

Este repositorio contiene traducciones de ejercicios de Pseint a Python3. Cada ejercicio en Pseint ha sido convertido a su equivalente en Python3, manteniendo la lógica y estructura original. A continuación, se proporciona una introducción general al repositorio:

## Estructura del Repositorio:

1. **Ejercicios Traducidos:**
   - El repositorio contiene varios directorios, cada uno correspondiente a un conjunto de ejercicios de Pseint.
   - Cada ejercicio se presenta en un archivo Python3 que refleja la traducción desde Pseint.
2. **Organización:**
   - Los ejercicios están organizados en carpetas temáticas o por nivel de complejidad.
   - La estructura de carpetas facilita la navegación y la búsqueda de ejercicios específicos.