import cognitive_face as CF
import faces as face

KEY = '06add3ffb377418fa5a4ed59d3d4325c'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

img_url = 'http://i.imgur.com/36Q3rNy.jpg'
result = CF.face.detect(img_url)

#this returns that the user group IS shown as my_anthem
group = CF.person_group.get('my_anthem')

faceNumber = result[0][u'faceId']

identifyPerson = CF.person.lists('my_anthem')


# This call isn't working why 
whoIsShe = CF.face.identify(faceNumber, 'my_anthem', 1)

print '-----------------'

print faceNumber

print '-----------------'

print group

print '-----------------'

print whoIsShe


