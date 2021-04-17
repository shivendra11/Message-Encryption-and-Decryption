


def prime_check(p):
    a=p.get()
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return False
    return True




def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            r=e
            e=b
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        return(gcd,t,s)
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        return s%r


# In[3]:


def encrypt(pub_key,n_text):
    e,n=pub_key
#     x=[]
    x=''
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x+=str(c)
            x+=','
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x+=str(c)
            x+=','
        elif(i.isspace()):
            spc=400
            x+=str(400)
            x+=','
    x = x[:-1]
    return x

def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',')
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x





from tkinter import *
import base64

#initialize window
root = Tk()
root.geometry('550x450')
root.resizable(0,0)

#title of the window
root.title("Message Encode and Decode")



#label

Label(root, text ='RSA based ENCODING and DECODING', font = 'arial 20 bold').pack()
Label(root, text ='of a Message', font = 'arial 20 bold').pack()


#define variables

Text = StringVar() # store the variable
# private_key = StringVar() #store the public key 
# public_key = StringVar() #store the public key 
mode = StringVar() #mode
Result = StringVar() #resul
prime1 = IntVar()
prime2 = IntVar()

#function to set mode
def Mode():
    
    # module to check no is prime or not
    check_p = prime_check(prime1)
    check_q = prime_check(prime2)
    if(((check_p==False)or(check_q==False))):
        Result.set("Entered Valued is not prime!!! Try Again")
        return 
    
    # further calculation or public private key pair
    n = prime1.get() * prime2.get()
    r= (prime1.get()-1)*(prime2.get()-1)
    for i in range(2,r):
        if(egcd(i,r)==1):
            e=i
    eugcd(e,r)
    d = mult_inv(e,r)
    public = (e,n) #public key
    private = (d,n) #private key
    # validating mode
    if(mode.get() == 'e'):
        Result.set(encrypt(public,Text.get()))
    elif(mode.get() == 'd'):
        Result.set(decrypt(private,Text.get()))
    else:
        Result.set('Invalid Mode')
        return



#Function to exit window
        
def Exit():
    root.destroy()


#Function to reset
def Reset():
    Text.set("")
    mode.set("")
    Result.set("")
    prime1.set("")
    prime2.set("")


#################### Label and Button #############
#prime number
Label(root, font= 'arial 12 bold', text='enter two prime number').place(x= 60,y=80)
Label(root, font= 'arial 12 bold', text='first number').place(x= 60,y=110)
Entry(root, font = 'arial 10', textvariable = prime1, bg = 'ghost white',borderwidth=5).place(x=290, y = 110)
Label(root, font= 'arial 12 bold', text='second number').place(x= 60,y=140)
Entry(root, font = 'arial 10', textvariable = prime2, bg = 'ghost white',borderwidth=5).place(x=290, y = 140)


#Message
Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=180)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white',borderwidth=5).place(x=290, y = 180)

#key
#Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
#Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)


#mode
Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 220)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white',borderwidth=5).place(x=290, y = 220)



#result
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white',borderwidth=5).place(x=290, y = 260)

######result button
Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 260)


#reset button
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=60, y = 330)

#exit button
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=290, y = 330)
root.mainloop()






