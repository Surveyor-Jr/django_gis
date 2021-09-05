from geopy import distance
point_a = (41.00, 41.00)
point_b = (45.00, 45.00)
print(distance.distance(point_a, point_b).km)