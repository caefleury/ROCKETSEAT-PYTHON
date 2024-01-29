import pytest
from characters import Character, Hero, Enemy


def test_character_details():
    character = Character(name="Test Character", life=50, level=10)
    details = character.show_details()
    assert "Nome: Test Character" in details
    assert "Vida: 50" in details
    assert "Nível: 10" in details


def test_hero_details():
    hero = Hero(name="Test Hero", life=100, level=20,
                special_attack="Test Special Attack")
    details = hero.show_details()
    assert "Nome: Test Hero" in details
    assert "Vida: 100" in details
    assert "Nível: 20" in details
    assert "Habilidade: Test Special Attack" in details


def test_enemy_details():
    enemy = Enemy(name="Test Enemy", life=75, level=15, type="Test Type")
    details = enemy.show_details()
    assert "Nome: Test Enemy" in details
    assert "Vida: 75" in details
    assert "Nível: 15" in details
    assert "Tipo: Test Type" in details
