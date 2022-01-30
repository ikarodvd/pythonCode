import cv2, os

def find(name, path):
    for root,dirs,files in os,walk(path):
        if (name in files) or (name in dirs):
            print ('O diretório/arquivo {} encontra-se em: {}'.format(name,root))
            return os.path.join(root, name)
    return find (name, os.path.dirname(path))

cv2path = os.path.dirname(cv2._file_)
haar_path = find ('haarcascades',cv2path)
xml_name = 'haarcascade_frontalface_alt2.xml'
xml_path = os.path.join(haar_path, xml_name)

clf = cv2.CascadeClassifier (xml_path)

cap = cv2.VideoCapture(0)

while (not cv2.waitKey(20)& 0xFF == ord('q')):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = clf.detectMultiScale(gray)

    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0))

        cv2.imshow('frame',frame)


cap.release()

cv2.destroyWindows()
cv2.waitKey(1)