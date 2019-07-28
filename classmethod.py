class Class:
    @classmethod
    def class_meth(self,param):
        # method with self
        print('1'+ param)

    @staticmethod
    def satatic_meth(param):
        # without "self"
        print('2 '+ param)

obj = Class()
# But what if vise versa?
# we need decorators
Class.class_meth(' Hi')
obj.satatic_meth(' yo')

""" If,for some reasons,you need to call a regular class method as a static
 method(in other words,you do not have an object to pass to "self"),
 use the @classmethod decorator to ask Python to genrate correct
arguments when calling the method. Python will substitute the class type to
"self".And for the opposite case, use @staticmethod to limit the
"self" parameter, which makes able to call a method on a class instead
 of an object. Be careful and think about the "self" value in this case if you
 use such approach"""
