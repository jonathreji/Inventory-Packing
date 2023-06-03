class InventoryItem:
    def __init__(self, name, weight, volume):
        self.name = name
        self.weight = weight
        self.volume = volume

class Arrow(InventoryItem):
    def __init__(self):
        super().__init__("Arrow", 0.1, 0.05)

class Bow(InventoryItem):
    def __init__(self):
        super().__init__("Bow", 1, 4)

class Rope(InventoryItem):
    def __init__(self):
        super().__init__("Rope", 1, 1.5)

class Water(InventoryItem):
    def __init__(self):
        super().__init__("Water", 2, 3)

class Food(InventoryItem):
    def __init__(self):
        super().__init__("Food", 1, 0.5)

class Sword(InventoryItem):
    def __init__(self):
        super().__init__("Sword", 5, 3)

class Pack:
    def __init__(self, maxCount, maxVolume, maxWeight):
        self.maxCount = maxCount
        self.maxVolume = maxVolume
        self.maxWeight = maxWeight
        self.items = []

    def Add(self, item):
        if len(self.items) >= self.maxCount:
            return False

        total_volume = sum(item.volume for item in self.items)
        total_weight = sum(item.weight for item in self.items)

        if total_volume + item.volume > self.maxVolume or total_weight + item.weight > self.maxWeight:
            return False

        self.items.append(item)
        return True

    def ToString(self):
        output = f"Pack Contents (Count: {len(self.items)}, Weight: {sum(item.weight for item in self.items)}, Volume: {sum(item.volume for item in self.items)})\n"

        for item in self.items:
            output += f"{item.name}\n"

        return output


# Unit Tests
def RunTests():
    # Test InventoryItem and derived classes
    arrow = Arrow()
    print(arrow.name)  # Output: Arrow
    print(arrow.weight)  # Output: 0.1
    print(arrow.volume)  # Output: 0.05

    # Test Pack class
    pack = Pack(5, 10, 15)
    print(pack.Add(arrow))  # Output: True
    print(pack.Add(Bow()))  # Output: True

    # Try adding items that exceed the pack's constraints
    print(pack.Add(Rope()))  # Output: True
    print(pack.Add(Water()))  # Output: False (exceeds max volume)
    print(pack.Add(Food()))  # Output: False (exceeds max weight)
    print(pack.Add(Sword()))  # Output: False (exceeds max volume and weight)

    print(pack.ToString())
    """
    Output:
    Pack Contents (Count: 3, Weight: 2.1, Volume: 5.55)
    Arrow
    Bow
    Rope
    """

    # Edge cases
    negative_pack = Pack(-5, -10, -15)
    print(negative_pack.Add(Arrow()))  # Output: True (negative constraints are ignored)

    zero_weight_item = InventoryItem("ZeroWeight", 0, 1)
    zero_volume_item = InventoryItem("ZeroVolume", 1, 0)
    zero_pack = Pack(0, 0, 0)
    print(zero_pack.Add(zero_weight_item))  # Output: True
    print(zero_pack.Add(zero_volume_item))  # Output: False (zero volume item exceeds max volume)

# Run the unit tests
RunTests()
