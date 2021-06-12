from sklearn.metrics.pairwise import haversine_distances
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from math import radians
import numpy as np

np.set_printoptions(precision=2)


def get_routes_for_vehicles(coordinates, num_vehicles, solution_strategy=routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC):
    data = create_data_model(coordinates, num_vehicles)
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    dimension_name = 'Distance'
    routing.AddDimension(transit_callback_index, 0, 1000, True, dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)

    distance_dimension.SetGlobalSpanCostCoefficient(100)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = solution_strategy

    solution = routing.SolveWithParameters(search_parameters)

    return get_routes(data, manager, routing, solution)


def get_distance_matrix(coordinates):
    coord_rads = []
    for coord in coordinates:
        coord_in_radius = [radians(_) for _ in coord]
        coord_rads.append(coord_in_radius)
    result = haversine_distances(coord_rads)
    result = result * (6371000 / 1000)
    return result


def create_data_model(coordinates, num_vehicles):
    data = {'distance_matrix': get_distance_matrix(coordinates), 'num_vehicles': num_vehicles, 'depot': 0}
    return data


def get_routes(data, manager, routing, solution):
    routes = []

    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        route_distance = 0
        vehicle_route = []

        while not routing.IsEnd(index):
            vehicle_route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)

        routes.append((vehicle_route, route_distance))

    return routes


if __name__ == '__main__':
    coordinates = [[52.363770, 4.939501],
                   [52.362086, 4.933954],
                   [52.357606, 4.923147],
                   [52.354836, 4.914628],
                   [52.352205, 4.896861],
                   [52.355210, 4.883085],
                   [52.349787, 4.891582],
                   [52.340275, 4.903481],
                   [52.341144, 4.946311],
                   [52.339915, 4.961417]]
    routes = get_routes_for_vehicles(coordinates, num_vehicles=3)
    print(routes)
