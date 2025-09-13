# Dictionary creation

student = {
          'ishu':94,
          'siddhartha':93,
          'atul':92,
          'sandeep':96,
          'ajeet':97,
}
n = input("Enter the student's name: ")
if n in student:
    print(f"{n}'s marks: ",student[n])
else:
    print(f"Student not found. ")