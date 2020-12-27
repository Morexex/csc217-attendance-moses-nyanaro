def csc_217_formated(csc_217_IT.txt)

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
                #check the name does not excist in unique_names
                if student_name not in unique_names:
                     outfile.write(student_name)
                     unique_names.add(student_name)

    return outfile
csc_217_formatted('csc_217_IT.txt')