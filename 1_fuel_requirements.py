from functools import reduce

MODULES_MASSES = [
    82406, 83106, 120258, 142695, 50629, 117793, 81165, 83442, 70666, 94355, 64069, 72830, 88813, 148762, 90723, 121206, 57713,
    116892, 82470, 101686, 83768, 92160, 91532, 136997, 142382, 120050, 81062, 106227, 112071, 102275, 54033, 109059, 91772,
    63320, 81872, 52925, 92225, 60053, 110402, 97125, 87404, 54970, 66662, 83979, 88474, 91361, 69272, 61559, 56603, 96324, 66226,
    95278, 105643, 139141, 116838, 130717, 97708, 108371, 73652, 100518, 98295, 63127, 50486, 121157, 109721, 110874, 124791,
    147116, 127335, 65889, 76769, 100596, 79740, 125860, 120185, 73861, 97700, 147169, 106781, 71891, 64744, 107113, 59274,
    77680, 101891, 69848, 98922, 147825, 128315, 55221, 119892, 87492, 75814, 80350, 131504, 81095, 57344, 63765, 143915, 126768
]


# Part 1
# Core
def fuel_for_mass(mass):
    required_fuel = int(mass / 3) - 2
    return required_fuel if required_fuel > 0 else 0


def fuel_for_christmas_sledge(module_masses):
    return sum(map(fuel_for_mass, MODULES_MASSES))


def better_fuel_for_christmas_sledge(module_masses):
    return reduce(
        lambda fuel_a, fuel_b: fuel_a + fuel_b, map(
            lambda mass: int(mass / 3) - 2, module_masses
        )
    )


# Tests
def test_fuel_for_mass():
    assert fuel_for_mass(12) == 2
    assert fuel_for_mass(14) == 2
    assert fuel_for_mass(1969) == 654
    assert fuel_for_mass(100756) == 33583


def test_fuel_for_christmas_sledge():
    assert fuel_for_christmas_sledge(module_masses=MODULES_MASSES) == 3147032


def test_better_fuel_for_christmas_sledge():
    assert better_fuel_for_christmas_sledge(module_masses=MODULES_MASSES) == 3147032


# Part 2
# Core
def fuel_for_total_mass(mass):
    fuel = 0
    fuel_for_fuel = 0
    required_fuel = fuel_for_mass(mass=mass)
    fuel += required_fuel
    if required_fuel > 0:
        fuel_for_fuel = fuel_for_total_mass(mass=required_fuel)
        if fuel_for_fuel > 0:
            fuel += fuel_for_fuel
    return fuel


def fuel_for_total_christmas_sledge(module_masses):
    return sum(map(fuel_for_total_mass, MODULES_MASSES))


# Tests
def test_fuel_for_total_mass():
    assert fuel_for_total_mass(14) == 2
    assert fuel_for_total_mass(1969) == 966
    assert fuel_for_total_mass(100756) == 50346


# Exec
# print(fuel_for_christmas_sledge(module_masses=MODULES_MASSES))
print(better_fuel_for_christmas_sledge(module_masses=MODULES_MASSES))
print(fuel_for_total_christmas_sledge(module_masses=MODULES_MASSES))