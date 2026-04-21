# Análisis Gilded Rose — Módulo 1

## Paso 1.2 — Preguntas sobre los requisitos

**¿Cuántos tipos de ítems hay?**
5 tipos: Normal, Aged Brie, Sulfuras, Backstage passes, Conjured.
Cada uno tiene reglas distintas de actualización.

**¿Qué significa sellIn y quality?**
sellIn = días restantes para vender. quality = valor del ítem.
Límites: quality entre 0 y 50. Sulfuras excepción: siempre 80.

**¿Cuál es la restricción más importante sobre Item?**
No se puede modificar la clase Item ni su lista items.
Simula código de terceros intocable.

**¿Qué nuevo ítem hay que implementar?**
Conjured. Degrada el doble de rápido que un ítem normal.

*-------------*

## Paso 1.3 — Code smells identificados

- [x] Método demasiado largo (update_quality sin separación)
- [x] Condicionales anidados (profundidad 4-5)
- [x] Strings literales repetidos ("Aged Brie", "Sulfuras"...)
- [x] Números mágicos (50, 80, 10, 5 sin nombre)
- [x] Falta de abstracción (toda la lógica en un método)

**Línea para Conjured:** dentro del else del if principal (~línea 30)
**Riesgo:** alto, fácil romper otros comportamientos por los ifs anidados

**Clases que usa GildedRose:** Item (name, sellIn, quality)

**¿Qué pasa si quality es negativa?**
R: No hay validación de entrada. Puede seguir bajando.

**¿Qué pasa con nombre desconocido?**
R: Se trata como ítem normal (else implícito).