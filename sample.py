import cognitive_face as CF
import faces as face

KEY = '06add3ffb377418fa5a4ed59d3d4325c'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

img_url = 'http://i.imgur.com/8ydax81.jpg'
result = CF.face.detect(img_url)

faceNumber = result[0][u'faceId']

# This compares our known faceId to our group
whoIsShe = CF.face.identify([ faceNumber ], 'my_anthem', 1)

recognizedId = whoIsShe[0][u'candidates'][0][u'personId']

print '-----------------'

print whoIsShe[0][u'candidates'][0][u'personId']

if recognizedId == face.RACHEL:
  print "we found it!"
  print "It's Rachel"
elif recognizedId == face.TIERNEY:
  print "we found it!"
  print "It's Tierney!"
elif recognizedId == face.ANNIE:
  print "we found it!"
  print "It's Annie!"
else:
   print "I don't know her"

