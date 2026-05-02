AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
CONJURED = "Conjured Mana Cake"

MAX_QUALITY = 50
MIN_QUALITY = 0
BACKSTAGE_THRESHOLD_1 = 10
BACKSTAGE_THRESHOLD_2 = 5


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater:
    """Clase base — comportamiento por defecto: ítem normal."""

    def __init__(self, item):
        self.item = item

    def update(self):
        raise NotImplementedError


class NormalItemUpdater(ItemUpdater):
    def update(self):
        self.item.sell_in -= 1
        degradation = 2 if self.item.sell_in < 0 else 1
        self.item.quality = max(MIN_QUALITY, self.item.quality - degradation)


class AgedBrieUpdater(ItemUpdater):
    def update(self):
        self.item.sell_in -= 1
        improvement = 2 if self.item.sell_in < 0 else 1
        self.item.quality = min(MAX_QUALITY, self.item.quality + improvement)


class SulfurasUpdater(ItemUpdater):
    def update(self):
        pass  # Sulfuras nunca cambia


class BackstagePassUpdater(ItemUpdater):
    def update(self):
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = MIN_QUALITY
        elif self.item.sell_in < BACKSTAGE_THRESHOLD_2:
            self.item.quality = min(MAX_QUALITY, self.item.quality + 3)
        elif self.item.sell_in < BACKSTAGE_THRESHOLD_1:
            self.item.quality = min(MAX_QUALITY, self.item.quality + 2)
        else:
            self.item.quality = min(MAX_QUALITY, self.item.quality + 1)


class ConjuredUpdater(ItemUpdater):
    def update(self):
        self.item.sell_in -= 1
        degradation = 4 if self.item.sell_in < 0 else 2
        self.item.quality = max(MIN_QUALITY, self.item.quality - degradation)


class UpdaterFactory:
    """Selecciona el updater correcto según el nombre del ítem."""

    _registry = {
        AGED_BRIE: AgedBrieUpdater,
        SULFURAS: SulfurasUpdater,
        BACKSTAGE_PASSES: BackstagePassUpdater,
        CONJURED: ConjuredUpdater,
    }

    @classmethod
    def for_item(cls, item):
        updater_class = cls._registry.get(item.name, NormalItemUpdater)
        return updater_class(item)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            UpdaterFactory.for_item(item).update()