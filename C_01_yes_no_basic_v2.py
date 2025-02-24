
def yes_no(question):
    while True:

      want_instructions =input("would you like to veiw the intructions?") .lower()
        if want_instructions == "yes" or want_instructions == "y":
            print ("you said yes")
             break
        elif want_instructions == "no" or want_instructions == "n":
            print ("you said no")
         break
        else:
            print("please enter yes / no")
             continue


print("we done")
