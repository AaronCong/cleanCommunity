from codes.persist.models.User import User
import heapq
import math
def searchDumper(user):
    userLon, userLat = user.apt_lon, user.apt_lat
    helperList = User.query.filter(User.status == 2).all()
    distance = []
    for helper in helperList:
        x = userLon - helper.cur_lon
        y = userLat - helper.cur_lat
        distance.append({'helperName':helper.uname,'helperID':helper.id,'distance': math.sqrt(x**2+y**2),'img':helper.img})
    closest = heapq.nsmallest(5, distance, key=lambda x:x['distance'])
    return closest