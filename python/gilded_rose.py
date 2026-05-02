AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"

MAX_QUALITY = 50
MIN_QUALITY = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == AGED_BRIE:
                self._update_aged_brie(item)
            elif item.name == SULFURAS:
                pass  # Sulfuras nunca cambia
            elif item.name == BACKSTAGE_PASSES:
                self._update_backstage_pass(item)
            else:
                self._update_normal_item(item)

    def _update_normal_item(self, item):
        item.sell_in -= 1
        degradation = 2 if item.sell_in < 0 else 1
        item.quality = max(MIN_QUALITY, item.quality - degradation)

    def _update_aged_brie(self, item):
        item.sell_in -= 1
        improvement = 2 if item.sell_in < 0 else 1
        item.quality = min(MAX_QUALITY, item.quality + improvement)

    def _update_backstage_pass(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = MIN_QUALITY
        elif item.sell_in < 5:
            item.quality = min(MAX_QUALITY, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(MAX_QUALITY, item.quality + 2)
        else:
            item.quality = min(MAX_QUALITY, item.quality + 1)