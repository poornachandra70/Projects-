class Calculator:
    def calculate(self, a, b):
        return a + b


class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        return a * b


normal = Calculator()
advanced = AdvancedCalculator()

print("Normal Calculator:", normal.calculate(10, 5))
print("Advanced Calculator:", advanced.calculate(10, 5))