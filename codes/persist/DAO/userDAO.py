from codes.persist.models.User import User

def searchDumper(user):
    userLon, userLat = user.apt_lon, user.apt_lat
    cleanerList = User.query.filter(User.status == 2).all()
    for cleaner in cleanerList:
