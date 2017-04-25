import cognitive_face as CF
import faces as face

KEY = '06add3ffb377418fa5a4ed59d3d4325c'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

img_url = 'http://i.imgur.com/36Q3rNy.jpg'
result = CF.face.detect(img_url)

faceNumber = result[0][u'faceId']

#identifyPerson = CF.face.identify(faceNumber, 'my_anthem')

print '-----------------'

print faceNumber

print '-----------------'

#print identifyPerson
