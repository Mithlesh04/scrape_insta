import cv2

# url = "https://instagram.fdel18-1.fna.fbcdn.net/v/t51.2885-19/s320x320/231585681_790852348256104_5034569828741661124_n.jpg?_nc_ht=instagram.fdel18-1.fna.fbcdn.net&_nc_ohc=FxYNtcK37jIAX-nc5oM&edm=ABfd0MgBAAAA&ccb=7-4&oh=84ebcc0f1fcab2012972d29b5c1935dc&oe=61138046&_nc_sid=7bff83"

def faceDetect(imagePath):
    try : 
        # faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=4,
            minSize= (20,20)
        )

        # for (x, y, w, h) in faces:
        #     cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)
        #     cv2.imshow("Faces found", image)
        # cv2.waitKey(0)
        return format(len(faces))
    except : 
        return 0


# f = faceDetect("./users/7181088_1628462581379543400/instagram/post/234658560_3917832628343738_4281428504250253704_n.jpg")
# print("Found faces = {0}".format(f))
# downloadImg(url,'./photos/')