# -*- coding: utf-8 -*-
import pytest
from gilded_rose import Item, GildedRose


class TestGildedRose:

    # --- ítem normal ---
    def test_normal_quality_decreases_by_1(self):
        items = [Item("Normal Item", 10, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 19
        assert items[0].sell_in == 9

    def test_normal_quality_decreases_by_2_after_sell_date(self):
        items = [Item("Normal Item", 0, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 18

    def test_quality_never_goes_below_zero(self):
        items = [Item("Normal Item", 5, 0)]
        GildedRose(items).update_quality()
        assert items[0].quality == 0

    # --- AGED_BRIE ---
    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", 5, 10)]
        GildedRose(items).update_quality()
        assert items[0].quality == 11

    def test_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", 5, 50)]
        GildedRose(items).update_quality()
        assert items[0].quality == 50

    # --- Sulfuras ---
    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        GildedRose(items).update_quality()
        assert items[0].quality == 80
        assert items[0].sell_in == 0

    # --- Backstage passes ---
    def test_backstage_quality_increases_normally(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 21

    def test_backstage_quality_plus2_near_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 22

    def test_backstage_quality_plus3_close_to_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 23

    def test_backstage_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 0

    # --- Conjured ---
    def test_conjured_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 18

    def test_conjured_degrades_4_per_day_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 16

    def test_conjured_quality_never_goes_below_zero(self):
        items = [Item("Conjured Mana Cake", 5, 1)]
        GildedRose(items).update_quality()
        assert items[0].quality == 0

    # --- Conjured (TDD) ---
    def test_conjured_item_degrades_twice_as_fast_before_sell_date(self):
        items = [Item("Conjured Mana Cake", 5, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 18  # degrada 2 por día

    def test_conjured_item_degrades_four_times_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 20)]
        GildedRose(items).update_quality()
        assert items[0].quality == 16  # degrada 4 tras sell date

    def test_conjured_quality_never_below_zero(self):
        items = [Item("Conjured Mana Cake", 5, 1)]
        GildedRose(items).update_quality()
        assert items[0].quality == 0