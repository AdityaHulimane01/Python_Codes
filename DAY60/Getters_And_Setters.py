class MyClass:
    def __init__(self, value):
        # Internal (protected) attribute.
        # By convention, a single underscore means:
        # "Do not access this directly from outside the class."
        self._value = value

    def show(self):
        # Normal method that prints the internal value
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        # GETTER
        # This method is accessed like an attribute, not like a function.
        # obj.ten_value returns 10 times the internal value.
        # You use a getter when you want controlled read access.
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        # SETTER
        # This method runs when someone assigns:
        # obj.ten_value = something
        # We do NOT store new_value directly.
        # We convert it back to the internal representation.
        # This enforces consistency and hides internal logic.
        self._value = new_value / 10


# Object creation
obj = MyClass(10)   # Here 10 is default value

# This does NOT directly change _value.
# It calls the setter, which divides by 10 internally.

# obj.ten_value = 67    # Default value 10 is overrided here by setter

# This calls the getter.
# It multiplies the internal value by 10.
print(obj.ten_value)

# Shows the actual internal stored value
obj.show()
