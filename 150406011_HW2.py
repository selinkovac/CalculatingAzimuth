


import math


def azimuth(x1,y1, x2,y2):
    dy=y2-y1
    dx=x2-x1
    azimuth=((200/math.pi)*abs(math.atan(dy/dx)))
    
    if (y2-y1)>0 and (x2-x1)>0:
       print "Azimuth angle between two points is:",(200/math.pi)*(math.atan(dy/dx)),"grad"  
       print "Azimuth angle between two points is:",(180/math.pi)*(math.atan(dy/dx)),"degree"
       print "It's in the I. region." 
    elif (y2-y1)>0 and (x2-x1)<0:
        print "Azimuth angle between two points is:",((200/math.pi)*(math.atan(dy/dx)))+200,"grad"
        print"Azimuth angle between two points is:",(180/math.pi)*(math.atan(dy/dx))+180,"degree"
        print "It's in the II. region."
    elif (y2-y1)<0 and (x2-x1)<0:
        print "Azimuth angle between two poins is:",((200/math.pi)*(math.atan(dy/dx)))+200,"grad"
        print"Azimuth angle between two points is:",(180/math.pi)*(math.atan(dy/dx))+180,"degree"
        print "It's in the III. region."
    elif (y2-y1)<0 and (x2-x1)>0:
        print "Azimuth angle between two points is:",((200/math.pi)*(math.atan(dy/dx)))+400,"grad"
        print"Azimuth angle between two points is:",(180/math.pi)*(math.atan(dy/dx))+360,"degree"
        print "It's in the IV.region."
print "SK1= (5000,5000)","SK2= (6077.87,5219.51)"
(azimuth(5000,5000,6077.87,5219.51))
print "SK3= (5000,5000)","SK4= (4138.13,5416.20)"
(azimuth(5000,5000,4138.13,5416.20))
print "SK5= (5000,5000)","SK6= (4878.42,4013.97)"
(azimuth(5000,5000,4878.42,4013.97))
print "SK7= (5000,5000)","SK8= (5791.44,4576.97)"
(azimuth(5000,5000,5791.44,4576.97))

