

class Hacker():
    def __init__(self):
        print("here is a hacker")
       
               # to do!!
    def __call__(self):
        print("what's up")
    def len(self):
        return self.hackers
    def __len__(self):
        self.hackers = 1

        return self.hackers

    def __repr__(self):
        return "hackcu hackers"
f = Hacker()

f()

print(len(f))
print(f)