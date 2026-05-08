# Revisión SOLID -Yahir Hernandez

## S — Single Responsibility
Cada clase tiene una sola razón de cambio.
- GildedRose: orquesta la actualización, no conoce reglas de negocio.
- Cada XxxUpdater: encapsula las reglas de un solo tipo de ítem.
- UpdaterFactory: selecciona el updater correcto. Solo cambia si hay
  un nuevo tipo que registrar.

## O — Open/Closed
El sistema está abierto para extensión y cerrado para modificación.
Para agregar "Conjured" solo se necesitó:
1. Crear ConjuredUpdater con su lógica.
2. Registrarlo en UpdaterFactory._registry.
No se modificó GildedRose ni ningún updater existente.

## L — Liskov Substitution
Cada ItemUpdater puede sustituir a la clase base sin alterar
el comportamiento esperado por GildedRose. El método update()
siempre actualiza correctamente sell_in y quality del item.

## I — Interface Segregation
No aplica directamente (no hay interfaces múltiples), pero cada
updater expone solo el método update() que GildedRose necesita.

## D — Dependency Inversion
GildedRose depende de la abstracción ItemUpdater (a través de
UpdaterFactory), no de las implementaciones concretas.
Esto permite añadir nuevos tipos sin tocar el orquestador.

## Señal de éxito
GildedRose.update_quality() NO contiene ningún if relacionado
con el nombre del ítem. Toda la lógica condicional vive en
UpdaterFactory y en las clases concretas de updater.