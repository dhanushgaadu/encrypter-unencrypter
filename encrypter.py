import random
class encrypter:
    def __init__(self):
        self.dic={}
    print("\nNOTE:- WHILE ENCRYPTING THE KEY WILL BE RANDOMIZED\n")
    print("note :- run only once !!!")
    def keygen(self):
        abc=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_`+=}|~[]{\./?,<>:;!@#$%^&*()")
        abc.append(" ")
        k=set()
        while(len(abc)!=len(k)):
            k.add(random.choice(abc))
            if len(k) == len(abc):
                k=list(k)
        self.dic.update({abc[x]:y for x,y in enumerate(k)})
        with open("key.txt","w") as w:
            for i in self.dic.items():
                w.writelines((":".join(list(i)))+"\n")
    def encoder(self,d_msg):
        self.keygen()
        e_msg=[]
        for j in d_msg:
            if j in self.dic.keys():
                e_msg.append(self.dic[j])
        return"".join(e_msg)
    def decoder(self,e_msg):
        u_msg=[]
        with open("key.txt","r") as r:
            line = r.readlines()
            line = ["".join(l.split("\n")) for l in line]
            for j in e_msg:
                for h in line:
                    if j==h[2]:
                        u_msg.append(h[0])
        return"".join(u_msg)
    def chooser(self):
        try:
            x=int(input("\nenter a option :"))
        except ValueError:
            print('''\nplease enter an integer value \n
                  maybe you are re running your program :)\n
                  to re run press ctrl+c on terminal and re run the program ;)\n''')
            self.chooser()
        return x
    def inp(self):
        try:
            u=input("\nEnter word to be encrypted :")
        except ValueError:
            print('\nPlease enter string type input ')
            self.inp()
        return u
    def main(self):
        h=self.chooser()
        try:
            if h==1:
                with open("unencrypted.txt","r") as ue:
                    r=ue.read()
                    with open("encrypted.txt","w") as e:
                        e.write(self.encoder(r))
                print('''\nDONE\n
            check the encrpyted or unencrypted file\n\n''')
            elif h==2:
                u_msg=self.inp()
                print("encrpyted message=",self.encoder(u_msg))
            elif h==3:
                with open("encrypted.txt","r") as ue:
                    r=ue.read()
                    with open("unencrypted.txt","w") as e:
                        e.write(self.decoder(r))
            elif h==4:
                e_msg=self.inp()
                print(self.decoder(e_msg))
            else:
                raise ValueError
        except ValueError:
            print('\nInvalid Option Entered Try Again\n')
            self.main()
    def file(self):
        try:
            open("unencrypted.txt","x")
            open("encrypted.txt","x")
            open("key.txt","x")
        except FileExistsError:
            pass
print('''\nEnter 1 to encrypt a file data and store into another file :) \n
Enter 2 to encrypt the unecrypted word input and print in terminal \n
Enter 3 to unencrpyt a file data and store into another file\n
enter 4 to unencrpt a encrpypted word input and print in terminal\n''')
encrypter().file()
encrypter().main()
