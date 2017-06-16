def main():
    fileName=input("enter file name:")
    infile=open(fileName,'r')
    sum=0.0
    count=0
    line=infile.readline()
    while line!="":
        for xStr in line.split(","):
            sum=sum+eval(xStr)
            count=count+1
        line=infile.readline()
    print(" The average of the numbers is ", sum/count)
main()