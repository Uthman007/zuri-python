class Student:
    # [assignment] Skeleton class. Add your code here
    def change_name(self, name):
        self.name=name
        
    def change_age(self, age):
        self.age=age
        
    def add_track(self, track):
        self.track=track
        
    def get_score(self):
        self.score=score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()