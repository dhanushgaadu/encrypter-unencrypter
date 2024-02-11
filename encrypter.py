import random
import time
class encrypter:
    def __init__(self):
        self.dic={}
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
    def scankey(self)->dict:
        with open("key.txt","r") as r:
            line = r.readlines()
            line = ["".join(l.split("\n")) for l in line]
            self.dic.update({h[0]:h[2] for h in line})
            return self.dic
    def encoder(self,d_msg)->str:
        e_msg=[]
        self.scankey()
        for j in d_msg:
            if j in self.dic.keys():
                e_msg.append(self.dic[j])
        return"".join(e_msg)
    def decoder(self,e_msg)->str:
        u_msg=[]
        dic=self.scankey()
        for k in e_msg:
            for i,j in dic.items():
                if j==k:
                    u_msg.append(i)
        return "".join(u_msg)
    
    def chooser(self)->int:
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
        self.file()
        try:
            if h==1:
                t0=time.time()
                with open("unencrypted.txt","r") as ue:
                    r=ue.read()
                    with open("encrypted.txt","w") as e:
                        e.write(self.encoder(r))
                print('''\nDONE\n
check the encrpyted.txt\n\n''')
                print(f"\nexecuted in {time.time()-t0} seconds\n")
                print("""\nfollow @thisguyisdhanush on instagram : )\n""")
            elif h==2:
                u_msg=self.inp()
                t0=time.time()
                print("encrpyted message:-"+str(self.encoder(u_msg)))
                print(f"\nexecuted in {time.time()-t0} seconds\n")
                print("""\n\nfollow @thisguyisdhanush on instagram : )\n""")
            elif h==3:
                t0=time.time()
                with open("encrypted.txt","r") as ue:
                    r=ue.read()
                    with open("unencrypted.txt","w") as e:
                        e.write(self.decoder(r))
                print('''\nDONE\n
check the unencrpyted.txt''')
                print(f"\nexecuted in {time.time()-t0} seconds\n")
                print("""\nfollow @thisguyisdhanush on instagram : )\n""")
            elif h==4:
                e_msg=input("enter encrypted word :")
                t0=time.time()
                print("decrypted message:-"+str(self.decoder(e_msg)))
                print(f"\nexecuted in {time.time()-t0} seconds\n")
                print("""\n\nfollow @thisguyisdhanush on instagram : )\n""")
            elif h==5:
                t0=time.time()
                self.keygen()
                print("""\n
Key is generated successfully : )""")
                print(f"\nexecuted in {time.time()-t0} seconds\n")
                print("""\nfollow @thisguyisdhanush on instagram : )\n""")
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
def reccurse():
    print("""enter 1 to encrypt contents of unencryptedt.txt -> encrypted.txt
enter 2 to encrypt a message in the terminal itself 
enter 3 to unencrypt contents of encryptedt.txt -> unencrypted.txt
enter 4 to unencrypt a message in the terminal itself 
enter 5 to generate a new key""")
    encrypter().main()
    if input("press enter to run again \n")=="":
        reccurse()
    else:
        pass
if __name__=="__main__":    
    reccurse()
