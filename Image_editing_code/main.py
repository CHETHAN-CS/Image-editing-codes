
import os


def mainmenu():
    print("I have written the basic code to do following operations on a image")
    print("-----------------MENU---------------------")
    print("1. Remove background from an Image")
    print("2. Greyscalling the Image")
    print("3. Enhance Contrast and brightness of Image")
    print("4. Remove dust spots in image")
    print("5. Merging images")
    print("----------------------------------------------")
    choice = input("Enter your choice(1-5) : ")
    if (int(choice) == 1):
        os.system('python rmbg.py')
        loop = input("do you want to try again ? (y/n): ")
        if(loop == 'y'):
            mainmenu()
        else:
            exit()
    elif (int(choice) == 2):
        os.system('python greyscaleimg.py')
        loop = input("do you want to try again ? (y/n)")
        if(loop == 'y'):
            mainmenu()
        else:
            exit()
    elif (int(choice) == 3):
        os.system('python cont.py')
        loop = input("do you want to try again ? (y/n)")
        if(loop == 'y'):
            mainmenu()
        else:
            exit()
    elif (int(choice) == 4):
        os.system('python rmdust.py')
        loop = input("do you want to try again ? (y/n)")
        if(loop == 'y'):
            mainmenu()
        else:
            exit()
    elif (int(choice) == 5):
        os.system('python merging.py')
        loop = input("do you want to try again ? (y/n)")
        if(loop == 'y'):
            mainmenu()
        else:
            exit()
    else:
        print("wrong choice....")
        loop = input("do you want to try again ? (y/n)")
        if(loop == 'y'):
            mainmenu()
        else:
            exit()

mainmenu()



