import sys
import os

from algorithms.routingalg_factory import RoutingAlgFactory

current_path = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.append(os.path.join(current_path, '..', ''))

ga = RoutingAlgFactory.get_routing_alg('GENETIC')
route = ga.execute_routing()
route.print_route()
