sno=int(input("enter student no                           : "))
sname=input("enter student name                      : ")
s1=int(input("c programming marks                 : "))
s2=int(input("java marks                                      : "))
s3=int(input("python                                             : "))
s4=int(input("operating system                          : "))
s5=int(input("data structures                              : "))
s6=int(input("data base management system : "))
total=s1+s2+s3
avg=total/3
if avg>=90:
    print("O grade")
elif avg>=80:
    print("A grade")
elif avg>=70:
    print("b grade")
elif avg>=60:
    print("c grade")
elif avg>=50:
    print("d grade")
elif avg>=40:
    print("pass")
else:
    print("fail")
