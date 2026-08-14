from ex0 import FlameFactory, AquaFactory


def test_factory(factory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(flame_factory, aqua_factory) -> None:
    flame = flame_factory.create_base()
    aqua = aqua_factory.create_base()

    print(f"{flame.describe()} vs. {aqua.describe()} fight!")
    print(flame.attack())
    print(aqua.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    print("Testing factory")
    test_factory(flame_factory)

    print("Testing factory")
    test_factory(aqua_factory)

    print("Testing battle")
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
