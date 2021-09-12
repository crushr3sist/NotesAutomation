import os
# print(os.getcwd())

def editCreation():

    addorrem = input("would you like to add or remove? a or r\n:")
    if addorrem == "r":
        for anything in subjects:
            which = input("which subjects would you like to remove?\n:")
            which.push(subjects)
            isThatIt = input("have you deleted all the incorrect subjects")
            if isThatIt == "yes":
                break
            else:
                which = input("which subjects would you like to remove?\n:")
                which.remove(subjects)
                isThatIt = input("have you deleted all the incorrect subjects")
    else:
        for edit in range(0,amountOfSubjects):
            which = input("which subject/s would you like to add?\n:")

def creator():
    dirCheck = input(rf"would you like to save to Documents? or to Desktop folder? |doc|desk|:")
    if dirCheck == "doc":
        userCheck = input(rf"please go to C:\Users and type in your user name accuratly:")
        userDir = rf"C:\Users\{userCheck}\Documents" 
        os.chdir(userDir)
        try:
            os.mkdir(userDir)
        except OSError:
            print ("Creation of the directory %s failed" % userDir)
        else:
            print ("Successfully created the directory %s " % userDir)

    elif dirCheck == "desk":
        userCheck = input(r"please go to C:\Users and type in your user name accurately:")
        userDir = rf"C:\Users\{userCheck}\Desktop" 
        os.chdir(userDir)
        try:
            os.mkdir(userDir)
        except OSError:
            print ("Creation of the directory %s failed" % userDir)
        else:
            print ("Successfully created the directory %s " % userDir)

    for i in range(0, amountOfSubjects):
        f = open(f"{subjects[i]}"+suffix,"w")
    print("Your note files have been created!")
    print(f"please go to:{userDir}, there will be a folder called 'school notes. All your files will be there")

def main():
    for i in range(0,amountOfSubjects):
        subjectInp = input(f"enter subject {i}:")
        subjects.append(subjectInp)
    for k in subjects:
        print(subjects)
        option = input("do you want to edit this list? y or n\n:")
        if option == "y":
            editCreation()
        if option == "n":
            creator()
            break

suffix = ".docx"
subjects = []
folderName = "school Notes"

if __name__ == '__main__':
    print("how many subjects do you have:")
    amountOfSubjects = int(input())
    main()


    #TODO functionality  
    '''
    allow user to delete array elements with either the element name it self 
    or the elements position in the array
#///                                                                                  ///#
    show the person the array after every change
#///                                                                                  ///#
    ask the person if they would like to either remove or add a subject into the array
#///                                                                                  ///#
    '''

# TODO save the files in a folder in the documents folder
#///                                                     ///#
# TODO print the directory for the user
#///                                                     ///#
