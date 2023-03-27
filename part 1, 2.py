#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution
#student id: 200220185 #UoW no: w1953145
#Date: 14.12.2022

#for the use of histogram
progress_count=retriever_count=trailer_count=excluded_count=total_count=0

#lists for part 2
list_ptwo=[]

#main function
def main():
    global progress_count,retriever_count,trailer_count,excluded_count,total_count
    #obtaining and validating pass credits
    while True:
        try:
            pass_credits=int(input('\nPlease enter your credits at pass : '))
            if 0<=pass_credits<=120 and pass_credits%20==0:
                break
            else:
                print('\nOut of range')
        except ValueError:
            print('\nInteger required')
        
    #obtaining and validating defer credits
    while True:
        try:
            defer_credits=int(input('Please enter your credits at defer : '))
            if 0<=defer_credits<=120 and defer_credits%20==0:
                break
            else:
                print('\nOut of range')
        except ValueError:
            print('\nInteger required')
    #obtaining and validating fail credits
    while True:
        try:
            fail_credits=int(input('Please enter your credits at fail : '))
            if 0<=fail_credits<=120 and fail_credits%20==0:
                break
            else:
                print('\nOut of range')
        except ValueError:
            print('\nInteger required')

    #checking for the total
    if pass_credits+defer_credits+fail_credits!=120:
        print('\nTotal incorrect')
    else:
        #progression outcomes
        try:
            if pass_credits==120:
                print ('Progress')
                progress_count+=1
                list_ptwo.append(['Progress -',pass_credits,',',defer_credits,',',fail_credits])
            elif pass_credits==100:
                print ('Progress(module trailer)')
                trailer_count+=1
                list_ptwo.append(['Progress (module trailer) -',pass_credits,',',defer_credits,',',fail_credits])
            elif fail_credits>=80:
                print ('Exclude')
                excluded_count+=1
                list_ptwo.append(['Excluded -',pass_credits,',',defer_credits,',',fail_credits])
            else:
                print ('Do not progress - module retriever')
                retriever_count+=1
                list_ptwo.append(['Module retriever -',pass_credits,',',defer_credits,',',fail_credits])
        finally:
            total_count+=1
    return (progress_count,retriever_count,trailer_count,excluded_count,total_count)

#histogram loop
def hisotogram(h):
    while h>0:
        print('*',end=' ')
        h-=1

#printing histogram
def print_histogram():
    print('\n---------------------------------------------------------------')
    print('Histogram')
    print('Progress ',progress_count,'  : ',end='')
    hisotogram(progress_count)
    print('\nTrailer ',trailer_count,'   : ',end='')
    hisotogram(trailer_count)
    print('\nRetriever ',retriever_count,' : ',end='')
    hisotogram(retriever_count)
    print('\nExcluded ',excluded_count,'  : ',end='')
    hisotogram(excluded_count)
    print('\n')
    print(total_count,' outcomes in total.')
    print('---------------------------------------------------------------')

#student or staff choice
def selection_menu():
    global choice
    print ("Enter:\n   '0' -> for student version \n   '1' -> for staff version with histogram \n   '2' -> for part 2 with staff version")
    choice=int(input('\nEnter to proceed: '))
    return (choice)

#part 2
#try with def part_two(*list) and calling the function with many parameters; all the lists
def part_two(outcome):
    for i in range(total_count):
        if outcome in list_ptwo[i]:
            print (*list_ptwo[i])

#student or staff validation and execution
def selection():
    if choice==0:
        main()
    elif choice==1:
        while True:
            main()
            #repeat or quit with user input
            print ('\n\nWould you like to enter another set of data?')
            repeat_quit=str(input("Enter 'y; for yes or 'q' to quit and view results: "))
            if repeat_quit=='q':
                break
        print_histogram()
    elif choice==2:
        while True:
            main()
            #repeat or quit with user input
            print ('\n\nWould you like to enter another set of data?')
            repeat_quit=str(input("Enter 'y; for yes or 'q' to quit and view results: "))
            if repeat_quit=='q':
                break
        print ('\npart 2:')
        part_two('Progress -')
        part_two('Progress (module trailer) -')
        part_two('Module retriever -')
        part_two('Excluded -')
    else:
        print("\nEnter '0', '1', or '2' to proceed!")
        choice_menu()
        choice()

selection_menu()
selection()
