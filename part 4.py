#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution
#student id: 200220185 #UoW no: w1953145
#Date: 14.12.2022

#for the use of histogram
progress_count=retriever_count=trailer_count=excluded_count=total_count=0

#lists for part 3
p=[]
t=[]
r=[]
e=[]
stid=[]

#dictionary for part 4
dictionary={}

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
                p.append('Progress - '+str(pass_credits)+', '+str(defer_credits)+', '+str(fail_credits))
            elif pass_credits==100:
                print ('Progress(module trailer)')
                trailer_count+=1
                t.append('Progress (module trailer) - '+str(pass_credits)+', '+str(defer_credits)+', '+str(fail_credits))
            elif fail_credits>=80:
                print ('Exclude')
                excluded_count+=1
                e.append('Excluded - '+str(pass_credits)+', '+str(defer_credits)+', '+str(fail_credits))
            else:
                print ('Do not progress - module retriever')
                retriever_count+=1
                r.append('Module retriever - '+str(pass_credits)+', '+str(defer_credits)+', '+str(fail_credits))
        finally:
            total_count+=1
        return (progress_count,retriever_count,trailer_count,excluded_count,total_count)      
            
#id
def id_f():
    global idno
    idno=input('\nEnter student id: ')
    if idno not in stid:
        stid.append(idno)
    else:
        print('Enter again. Student id must be unique')
        id_f()

#main execution
while True:
    id_f()
    main()
    #repeat or quit with user input
    print ('\n\nWould you like to enter another set of data?')
    repeat_quit=str(input("Enter 'y; for yes or 'q' to quit and view results: "))
    if repeat_quit=='q':
        break

#part 3
#writing in the file, part3.txt
file=open('part3.txt','w')
import linecache
def part_three(count,list_p):
    for i in range(count):
        write=file.write(str(list_p[i]))
        newline=file.write('\n')

#print('\nPart 3:')
part_three(progress_count,p)
part_three(trailer_count,t)
part_three(retriever_count,r)
part_three(excluded_count,e)

#reading and printing from the file, part3.txt
file.close()
f=open('part3.txt','r')

#part 4
for tot in range (total_count):
    line=linecache.getline('part3.txt',tot+1)
    dictionary[stid[tot]]=line
print(dictionary)
print('\nPart 4:')
for k,v in dictionary.items():
    print(k,':',v,end=' ')
        
f.close()

'''
References
https://www.sololearn.com/discuss/2864450/why-is-there-a-extra-none-in-output
https://pynative.com/python-search-for-a-string-in-text-files/
https://stackoverflow.com/questions/33161448/getting-only-element-from-a-single-element-list-in-python
https://stackoverflow.com/questions/56381066/how-to-open-a-file-in-both-read-and-append-mode-at-the-same-time-in-one-variable/56381383#56381383
https://www.geeksforgeeks.org/how-to-read-specific-lines-from-a-file-in-python/
https://docs.python.org/3/library/linecache.html
'''


  




















        
        
