class Province:
    country = "中国"

    def __init__(self, name):
        self.name = name

    @classmethod
    def show(cls):  # 类方法，由类调用，最少要有一个参数cls，调用的时候这个参数不用传值，自动将类名赋值给cls
        print(cls.country)
# 调用方法


# Province.show()


test = [1, 2, 3, 4]

for x, y in enumerate(test):
    print(test)