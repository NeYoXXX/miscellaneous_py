class A(object):
    num = 100

def print_b(self):
    print(self.num)

@staticmethod
def print_static():
    print("----haha-----")

@classmethod
def print_class(cls):
    print(cls.num)

B = type("B", (A,), {"print_b": print_b, "print_static": print_static, "print_class": print_class})
b = B()
b.print_b()
b.print_static()
b.print_class()

# 结果
# 100
# ----haha-----
# 100

'''
元类就是用来创建类的“东西”。你创建类就是为了创建类的实例对象，不是吗？但是我们已经学习到了Python中的类也是对象。

元类就是用来创建这些类（对象）的，元类就是类的类，你可以这样理解为：

MyClass = MetaClass() # 使用元类创建出一个对象，这个对象称为“类”
my_object = MyClass() # 使用“类”来创建出实例对象
你已经看到了type可以让你像这样做：

MyClass = type('MyClass', (), {})
这是因为函数type实际上是一个元类。type就是Python在背后用来创建所有类的元类。
现在你想知道那为什么type会全部采用小写形式而不是Type呢？好吧，我猜这是为了和str保持一致性，str是用来创建字符串对象的类，而int是用来创建整数对象的类。
type就是创建类对象的类。你可以通过检查__class__属性来看到这一点。
Python中所有的东西，注意，我是指所有的东西——都是对象。
这包括整数、字符串、函数以及类。它们全部都是对象，而且它们都是从一个类创建而来，这个类就是type。

'''