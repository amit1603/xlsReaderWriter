from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0
def my_function(s_lat, s_long, d_lat, d_long):
    lat1 = radians(float(s_lat))
    lon1 = radians(float(s_long))
    lat2 = radians(float(d_lat))
    lon2 = radians(float(d_long))
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance
