class Test:
    a = 100
    b = 200

    @classmethod
    def test_classmethod(cls, n):
        return cls.a <= n and cls.b <= n

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.test_classmethod(x) and self.test_classmethod(y):
            self.x = x
            self.y = y
    def return_data(self):
        print(self.x, self.y)

    @staticmethod
    def test_staticmethod(x,y):
        return x+y

