# 2) Реализовать метакласс, позволяющий создавать всегда один и тот же объект класса

class Meta(type):
    example = None

    def __call__(self):
        if self.example is None:
            self.example = super().__call__()
        return self.example


class MyClass(metaclass=Meta):
    pass


obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
obj_4 = MyClass()

print(obj_1 is obj_4)
print(obj_2 is obj_3)
print(obj_3 is obj_4)
print(obj_2 is obj_3)
