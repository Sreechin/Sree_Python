#encapsulation helps to hide the internal state 
# of an object from the outside world and only 
# expose a controlled interface. This can be 
# achieved through the use of access modifiers 
# like protected (_) and private (__).

class E:
    def __init__(self):
        self.attr1=1
        self._attr2=2 #Protected attribute '_' with underscore

        self.__attr3=3 # Private attribute '__' with duble underscope

e=E()

print(e.attr1)
print(e._attr2)
print(e.__attr3)