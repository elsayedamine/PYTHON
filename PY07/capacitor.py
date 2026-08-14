from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with healing capability base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform(factory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with transform capability base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing(healing_factory)
    test_transform(transform_factory)


if __name__ == "__main__":
    main()
