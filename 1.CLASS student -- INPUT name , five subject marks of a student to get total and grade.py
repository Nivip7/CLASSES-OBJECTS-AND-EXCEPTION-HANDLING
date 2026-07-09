class student:
    def __init__(self):
        self.name = input("name:")
        self.mark = []
    def add_marks(self):
        for i in range(5):
            m=float(input("enter your marks:"))
            self.mark.append(m)
    def display(self):
        t=0
        for i in self.mark:
            t+=i
        avg=t/5
        if avg >=90:
            grade='A'
        elif avg >=80:
            grade = 'B'
        elif avg >=70:
            grade='C'
        elif avg >=60:
            grade = 'D'
        else:
            grade='F'
        print("\nNAME:",self.name,"\nMARKS:",self.mark,"\nGRADE:",grade,"\nTOTAL MARKS:",t,"\nAVG:",avg)
s=student()
s.add_marks()
s.display()
