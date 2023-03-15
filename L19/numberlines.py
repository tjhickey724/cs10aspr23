def number_lines(infilename,outfilename):
    infile = open(infilename,'r')
    lines = infile.readlines()
    infile.close()

    outfile = open(outfilename,'w')
    count=1
    for line in lines:
        linenumber = str(count)+": "
        outfile.write(linenumber+line)
        count += 1
    outfile.close()

infile = input("What is the source file: ")
outfile = input("What is the target file? ")
number_lines(infile,outfile)
