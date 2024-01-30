#main()
#making robot objects, starting the simulation, and then updating each robot throughout the simulation.
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
client = RemoteAPIClient()
sim = client.require('sim')
import robot
from robot import Robots

def main():
    r0 = Robots(0)
    r1 = Robots(1)
    r2 = Robots(2)
    r3 = Robots(3)
    r4 = Robots(4)
    sim.setStepping(True)
    sim.startSimulation()
    while (t := sim.getSimulationTime()) < 30:
        print(f'Simulation time: {t:.2f} [s]')
        r0.update()
        r1.update()
        r2.update()
        r3.update()
        r4.update()
        sim.step()
    sim.stopSimulation()
if __name__ == '__main__':
    main()



