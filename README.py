# student-record-manager
# A simple Python console application to manage student records using dictionary and file handling.


# Use file + dictionary + functions
# User can:

#  * Add student and marks
#  * Delete student
#  * View all students
#  * Save to file
#  def add_student(name, mark): ...
#  def delete_student(name): ...
#  def save_to_file(): ...

students ={}
N = 3 

def insert():
    for i in range(N):
        student ,mark = input('Enter the name of the student and marks : ').split()
        students[student] = mark
    print('Name and the marks are noted')

def delete():
    name_delete = input('Enther the name we need to delete from our data base : ').strip()
    if name_delete in students:
        del students[name_delete]
        print('deleted')
    
def save_file():
    upload = input('Do you want to save the names in file (yes/no):').strip().lower()
    if upload == 'yes':
        with open(r'Bosco.txt','+r') as file:
            for student,mark in students.items():
                file.write(f'{student}:{mark}')
        print('saved')
    else:
        print('Thanks for the news')

def question():
    while True:
        print('1 for print')
        print('2 for delete')
        print('3 for upload')
        print('4 for exit')
        choice = int(input('which option kindly select : '))

        if choice == 1:
            insert()
        elif choice == 2:
            delete()
        elif choice == 3:
            save_file()
        elif choice == 4:
            break

if __name__ == "__main__":
    question()
        
        
        
            

