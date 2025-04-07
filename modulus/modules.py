#example
#by calculateing the simple interest
#function deffination
'''def simpleint():
    p=float(input("enter a principal amount:"))
    t=float(input("enter a time:"))
    r=float(input("enter  a rate of interest:"))
    print("-"*50)
    si=(p*t*r)/100
    print("-"*50)
    totalamount=p+si
    print("-"*50)
    print("simple interest details:")
    print("-" * 50)
    print("principal amount:{}".format(p))
    print("time:{}".format(r))
    print("rate of interest:{}".format(r))
    print("-" * 50)
    print("simple interest:{}".format(si))
    print("total amount to pay:{}".format(totalamount))
    print("-" * 50)
#main programme
simpleint()
'''

#big no
'''def s():
    a=int(input("enter a  no:"))
    b=int(input("enter a  no:"))
    if a>b or b<a:
        print("a is big",a)
    elif b>a or b>b:
        print("b is big:",b)
    else:
        print("thankyou")

#function call
s()'''




'''from mathsinfo import PI,E
print("val of PI={}".format(PI))
print("val of E={}".format(E))

'''

'''import cv2
from pyzbar.pyzbar import decode


def scan_qr_code(image_path):
    # Read the imagepip install qreader
    image = cv2.imread(image_path)

    # Decode the QR code
    decoded_objects = decode(image)

    if not decoded_objects:
        print("No QR code found.")
        return None

    for obj in decoded_objects:
        qr_data = obj.data.decode("utf-8")
        print("QR Code Data:", qr_data)
        return qr_data


# Example usage: Provide your QR code image path
qr_data = scan_qr_code("your_qr_code_image.png")'''




#scanner

'''import cv2
import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.clock import Clock
from pyzbar.pyzbar import decode

class QRScanner(BoxLayout):
    def __init__(self, **kwargs):
        super(QRScanner, self).__init__(**kwargs)
        self.orientation = 'vertical'
        # Create and add a Camera widget
        self.camera = Camera(play=True)
        self.camera.resolution = (640, 480)
        self.add_widget(self.camera)
        # Schedule the QR scanning function to run 10 times per second
        Clock.schedule_interval(self.scan_qr, 1.0 / 10.0)

    def scan_qr(self, dt):
        # Get the current texture from the Camera widget
        texture = self.camera.texture
        if not texture:
            return

        # Retrieve pixel data from the texture (RGBA format)
        width, height = texture.size
        pixel_data = texture.pixels  # returns a bytes object

        # Convert the pixel data to a NumPy array and reshape to (height, width, 4)
        img = np.frombuffer(pixel_data, dtype=np.uint8)
        img = img.reshape((height, width, 4))

        # Convert from RGBA to BGR format (as used by OpenCV) and discard the alpha channel
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

        # Use pyzbar to decode any QR codes in the frame
        decoded_objects = decode(img)
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            print("QR Code detected:", qr_data)
            # Optionally, you can update the UI or trigger an action based on the decoded data

class QRScannerApp(App):
    def build(self):
        return QRScanner()

if __name__ == '__main__':
    QRScannerApp().run()

'''


'''def a():
    a=int(input("enter a  no:"))
    b=int(input("enter a  no:"))
    if a>b and b<a:
        print("a is big:",a)
    elif b>a and a<b:
        print("b is big:",b)
    else:
        print("process completed")
#function calls
a()
'''


'''stateinfo="telengana"
capinfo=("hyd")

def hello(s):
    return("{},good morning from hello()--hyd module".format(s))

def show():
    print("iam from hyd module")
#hello()
show()'''

'''
#function deffination
def a():
    print("iam manikumar--1")
def b():
    print("iam manikumar--2")


#main function
a()
b()

'''

'''from hyd import stateinfo,capinfo,hello,show
print("state name=",stateinfo)
print("capital name=",capinfo)
hello("rossum")
show()'''



#function deffination
'''def a():
    r = range(11)
    for v in r:
        print(v, end=" ")
#main functon
a()
'''


def mani():
    rollno=int(input("please enter roll no:"))
    if rollno>=0:
        print("it is a correct hallticket number")
    else:
        print("rong hallticket number please try again")

    name=input("enter name:")
    s1=int(input("enter a sub-1 marks:"))
    s2=int(input("enter a sub-2 marks:"))
    s3=int(input("enter a sub-3 marks:"))
    s4=int(input("enter a sub-4 marks:"))
    s5=int(input("enter a sub-5 marks:"))
    s6=int(input("enter a sub-6 marks:"))
    total=s1+s2+s3+s4+s5+s6
    print("student total marks:",total)
    percentage=total/6
    print("student average percentage:",percentage)
    if s1<=35 or s2<=35 or s3<=35 or  s4<=35 or s5<=35 or s6<=35:

    #total=s1+s2+s3+s4+s5+s6
    #print(total)
        print("student are fail")
    else:
        print("student are pass")
#main function
mani()












