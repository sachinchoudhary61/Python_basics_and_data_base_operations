# Demonstrating the work of the ___enter__ and __exit__ methods
class C:
    def some_work(self):
        print("Hello,there!")
    def __enter__(self):
        print("Enter")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT")

o = C()
with o:
    # as soon as you have "with"
    # you need __enter__ and __exit__

    o.some_work()

