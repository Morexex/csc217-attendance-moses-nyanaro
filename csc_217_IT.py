def csc_217_IT(csc_217_IT.txt)

    #importing IT.txt file
    import IT.txt


    #keep track of unique names
    unique_names=set()

    # using write mode
    with open('IT.txt','a')as outfile:

        #iterate over the list
        for file in filenames:

           #open IT.txt file in read mode
            for student_name in open(file):

                # creating a function to differentiate between IT and computer science user_names

                 student_name={'admission_number',',',' ','name'}
                    print(student_name)
                #check the name does not exist in unique_names
                if student_name not in unique_names:
                     outfile.write(student_name)
                     unique_names.add(student_name)
     #add and remove duplicates
     s = set()
     s.add(file_csc_217_IT.txt)
s.append(duplicates)
print(s)
print(f"the set has{len(s)}elements")

    return outfile
csc_217_formatted('csc_217_IT_wk1_final.txt')