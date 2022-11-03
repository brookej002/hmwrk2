fname=input("Enter file name:")
Enter file name: sample2.txt
    writeFilmName= "UPPER" + fname
    file3 = opne(writeFileName, "L")
    Lines= file.readlines()
    for i in range (len(Lines)):
        t=Lines[i]
        file3.write(t.upper())
