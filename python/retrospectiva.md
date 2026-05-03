# Retrospectiva — Gilded Rose Kata - Yahir Hernández

## Preguntas grupales

**¿Qué parte fue la más incómoda?**
La parte más incómoda fue leer el código legacy por primera vez:
un solo método de ~40 líneas con condicionales anidados a 5
niveles sin ningún test de respaldo. No queda claro si
modificarlo directamente rompería algo.

**¿Hubo algún test que falló inesperadamente?**
Sí, al hacer Find & Replace para extraer las constantes,
el reemplazo también afectó los strings en los archivos de
tests, convirtiendo "Aged Brie" en AGED_BRIE dentro de los
Item(). Eso reveló que el scope del refactoring debe ser
cuidadoso y verificado archivo por archivo.

**¿Diferencia entre tests de caracterización y tests de TDD?**
Tests de caracterización: documentan el comportamiento ACTUAL
del código (puede ser incorrecto). Su objetivo es crear una red
de seguridad antes de refactorizar.
Tests de TDD: describen el comportamiento DESEADO de código
que aún no existe. Primero fallan (rojo), luego se implementa
el mínimo para hacerlos pasar (verde).

## Reflexión individual

**Estrategia seguida:**
1. Construir red de seguridad (10 tests de caracterización).
2. Refactorizar en micro-pasos verificados: constantes →
   métodos → Strategy pattern. Commit atómico tras cada paso.
3. Añadir Conjured mediante TDD solo después de completar
   la refactorización.

**¿Qué haría diferente?**
Usaría TextTest (Approval Testing) desde el inicio para tener
una cobertura de golden master más completa antes de tocar
nada. También extraería los umbrales del Backstage (5, 10)
como constantes desde el primer paso.

**¿Qué técnica aplico en mi proyecto actual?**
El patrón de extraer métodos con nombres descriptivos antes
de cualquier cambio de funcionalidad. En el IMS frontend,
cuando hay lógica condicional compleja en un componente,
primero extraer a funciones con nombre antes de añadir casos
nuevos reduce el riesgo de regresiones.

-Yahir Hernández