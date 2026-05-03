# Reflexión — Añadir Conjured en legacy vs refactorizado - Yahir Hernández

## En el código legacy original
Para agregar Conjured se habría necesitado:
1. Entrar al método update_quality() de ~40 líneas con 5 niveles
   de if anidados.
2. Encontrar el lugar correcto dentro de la lógica sin romper
   el comportamiento de los otros ítems.
3. Riesgo alto: cualquier error en el anidamiento afecta a
   Normal, Aged Brie, Backstage y Sulfuras simultáneamente.
4. Sin tests, no hay forma de saber si algo se rompió.

## En el código refactorizado (Strategy + Factory)
Para agregar Conjured solo se necesitó:
1. Crear ConjuredItemUpdater con su lógica propia (5 líneas).
2. Registrarlo en UpdaterFactory._registry (1 línea).
3. No se tocó GildedRose ni ningún otro updater.
4. Los 10 tests existentes siguieron en verde sin cambios.

## Conclusión
La refactorización previa redujo el riesgo de añadir
funcionalidad nueva de ALTO a MÍNIMO. El patrón Strategy
implementa el principio Open/Closed: el sistema está cerrado
para modificación y abierto para extensión.

-Yahir Hernández