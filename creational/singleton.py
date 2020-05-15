class Singleton_Lazy:
    __instance = None
    
    def __init__(self):
        if not Singleton_Lazy.__instance:
            print("I have already got an instance.")
        else:
            print("I don't yet have an instance.")
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton_Lazy()
        return cls.__instance

sl1 = Singleton_Lazy()
sl2 = Singleton_Lazy()

print(f"sl1: {sl1}")
print(f"sl2: {sl2}")

class Singleton_Strict:
    name = "testezinhotopo"
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton_Strict, cls).__new__(cls)
        return cls.instance

ss1 = Singleton_Strict()
ss2 = Singleton_Strict()

print(f"ss1: {ss1}\nss2: {ss2}")