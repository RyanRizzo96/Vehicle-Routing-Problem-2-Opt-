import csv
from haversine import haversine
import matplotlib.pyplot as plt
import numpy as np
import random


def cost(cost_mat, route):
    return cost_mat[np.roll(route, 1), route].sum()  # shifts route array by 1 in order to look at pairs of cities


def two_opt(cost_mat, route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # changes nothing, skip then
                new_route = route[:]    # Creates a copy of route
                new_route[i:j] = route[j - 1:i - 1:-1]  # this is the 2-optSwap since j >= i we use -1
                if cost(cost_mat, new_route) < cost(cost_mat, best):
                    best = new_route
                    improved = True
                    route = best
    return best


def read_two_column_file(file_name):
    with open(file_name, 'r') as f_input:
        csv_input = csv.reader(f_input, delimiter=' ', skipinitialspace=True, )
        long = []
        lat = []
        for col in csv_input:
            x = float(col[0])  # converting to float
            y = float(col[1])
            long.append(x)
            lat.append(y)

    long = np.array(long)
    lat = np.array(lat)
    print(len(lat))

    return long, lat


def display_points(long, lat, best, distance):
    plt.figure()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.ylabel('latitude (°)')
    plt.xlabel('longitude (°)')
    plt.title('Total Distance travelled: %f km' % distance)
    plt.scatter(lat, long)
    plt.orientation = u'vertical'
    plt.grid('True')
    plt.plot(lat[best], long[best])
    plt.show()


def main():
    long, lat = read_two_column_file('latlong.txt')

    points = []
    for i in range(len(lat)):
        coords = tuple([lat[i], long[i]])
        points.append(coords)

    print(points)

    hav = []
    for i in range(len(lat)):
        for j in range(len(long)):
            hav.append(haversine(points[i], points[j]))

    cost_mat = np.reshape(hav, (len(lat), len(lat)))  # reshaping to 10 x 10 matrix
    print(cost_mat)

    for i in range(len(lat)):
        a = random.sample(range(0, len(lat)), len(lat))

    b = a[0]
    a.insert(len(a), b)

    # print(a)

    route = a
    # route = [2, 0, 3, 7, 5, 4, 6, 8, 9, 1, 10, 11, 13, 12, 14, 15, 16, 17, 18, 19, 22, 21, 20, 23, 24, 25, 26, 27, 53, 52, 51, 50, 28, 29, 30, 31, 32, 33, 34, 36, 35, 37, 38, 39, 40, 42, 41, 43, 44, 45, 46, 47,48, 49, 2]
    distance = (cost(cost_mat, route))

    best = two_opt(cost_mat, route)
    print(best)

    display_points(long, lat, best, distance)


main()

///////////////////////


import csv
from haversine import haversine
import matplotlib.pyplot as plt
import numpy as np
import random
from timeit import default_timer as timer


def cost(cost_mat, route):
    return cost_mat[np.roll(route, 1), route].sum()  # shifts route array by 1 in order to look at pairs of cities


def two_opt(lat, long, cost_mat, route):
    start = timer()
    best = route
    count = 0
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # changes nothing, skip then
                new_route = route[:]    # Creates a copy of route
                new_route[i:j] = route[j - 1:i - 1:-1]  # this is the 2-optSwap since j >= i we use -1
                if cost(cost_mat, new_route) < cost(cost_mat, best):
                    best = new_route
                    improved = True
                    route = best
                    # distance = (cost(cost_mat, route))
                    # display_points(long, lat, best, distance, count)
                    count += 1
    elapsed_time = timer() - start
    print(elapsed_time)
    return best


def read_two_column_file(file_name):
    with open(file_name, 'r') as f_input:
        csv_input = csv.reader(f_input, delimiter=' ', skipinitialspace=True, )
        long = []
        lat = []
        for col in csv_input:
            x = float(col[0])  # converting to float
            y = float(col[1])
            long.append(x)
            lat.append(y)

    long = np.array(long)
    lat = np.array(lat)
    # print(len(lat))

    return long, lat


def display_points(long, lat, best, distance):
    fig = plt.figure()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.ylabel('latitude (°)')
    plt.xlabel('longitude (°)')
    plt.title('Total Distance travelled: %f km' % distance)
    plt.scatter(lat, long)
    plt.orientation = u'vertical'
    # plt.grid('True')
    plt.plot(lat[best], long[best])
    # plt.savefig('/home/ryan/PycharmProjects/first_prog/mydir/{0}'.format(count), bbox_inches='tight')
    plt.show()
    # plt.hold(True)


def main():

    long, lat = read_two_column_file('latlong.txt')

    points = []
    for i in range(len(lat)):
        coords = tuple([lat[i], long[i]])
        points.append(coords)

    # print(points)

    hav = []
    for i in range(len(lat)):
        for j in range(len(long)):
            hav.append(haversine(points[i], points[j]))

    cost_mat = np.reshape(hav, (len(lat), len(lat)))  # reshaping to 10 x 10 matrix

    # for j in range(0, 6):   # Running 2-opt 6 times with same points but random points

    for i in range(len(lat)):
            a = random.sample(range(0, len(lat)), len(lat))

    b = a[0]
    a.insert(len(a), b)
    route = a
    print(route)

    distance = (cost(cost_mat, route))

    best = two_opt(lat, long, cost_mat, route)

    print(best)

    display_points(long, lat, best, distance)


main()


///////


def two_opt(connect_mat, route):
    start = timer()
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue  # changes nothing, skip then
                new_route = route[:]    # Creates a copy of route
                new_route[i:j] = route[j - 1:i - 1:-1]  # this is the 2-optSwap since j >= i we use -1
                if cost(connect_mat, new_route) < cost(connect_mat, best):
                    best = new_route    # change current route to best
                    improved = True     # this is a new route so we need to check if it can be improved
                    route = best        # save best_route to route

    elapsed_time = timer() - start
    print(elapsed_time)
    return best

