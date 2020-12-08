import time
import openravepy
import os
from init import initRobot
from init import simpleDynamicinputs, goforwardDynamicinputs
import robotType
from KalmanFilter import KF, EKF
from ParticleFilter import PF
from Sensor import *
from Astar import Astar
from PID import *

if not __openravepy_build_doc__:
    from openravepy import *
    from numpy import *


if __name__ == "__main__":
    path =  os.getcwd()

    env = Environment()
    env.SetViewer('qtcoin')
    collisionChecker = RaveCreateCollisionChecker(env,'ode')
    env.SetCollisionChecker(collisionChecker)

    env.Reset()

    handles = []
    # load a scene from ProjectRoom environment XML file
    # env_path = os.path.join(path, "map/testScene.env.xml")

    # test a scene with barriers
    # env_path = os.path.join(path, "map/testSceneWithLandMark.env.xml")
    env_path = os.path.join(path, "map/roomScene.env.xml")
    env.Load(env_path)

    robot = env.GetRobots()[0]
    initRobot(env, robot)

    ######################## Load a simpleDynamicRobot with a GPS sensor ########################
    ########################          Use KalmanFilter to predict        ########################
    # simplerobot = robotType.SimpleDynamicRobot(robot, [-6, -2, 0], env, sensor=GPS)
    # simplerobot.update(env, handles)
    # kf = KF(simplerobot)
    #
    # for ii in range(simpleDynamicinputs.shape[0]):
    #     simplerobot.input = simpleDynamicinputs[ii, :]
    #     simplerobot.predict(env)
    #     simplerobot.update(env, handles)
    #     kf.update(env, handles)
    #     time.sleep(0.05)

    ##################### Load a simpleDynamicRobot with a LandMark sensor  #####################
    ####################          Use ExtendedKalmanFilter to predict        ####################
    # simplerobot = robotType.SimpleDynamicRobot(robot, [-6, -2, 0], env, sensor=LandMark)
    # simplerobot.update(env, handles)
    # ekf = EKF(simplerobot)

    # for ii in range(simpleDynamicinputs.shape[0]):
    #     simplerobot.input = simpleDynamicinputs[ii, :]
    #     simplerobot.predict(env)
    #     simplerobot.update(env, handles)
    #     ekf.update(env, handles)
    #     time.sleep(0.05)

    ######################## Load a GoForwardDynamicRobot with a IMU sensor ########################
    ########################               Use EKF to predict               ########################
    # goforwardrobot = robotType.GoForwardDynamicRobot(robot, [1, 0, 0], env, sensor=IMU)
    # goforwardrobot.update(env, handles)
    # ekf = EKF(goforwardrobot)
    # for ii in range(goforwardDynamicinputs.shape[0]):
    #     goforwardrobot.input = goforwardDynamicinputs[ii, :]
    #     goforwardrobot.predict(env)
    #     goforwardrobot.update(env, handles)
    #     ekf.update(env, handles)
    #     time.sleep(0.025)

    ########################  Load a simpleDynamicRobot with a GPS sensor   ########################
    ########################               Use PF to predict                ########################
    # simplerobot = robotType.SimpleDynamicRobot(robot, [-6, -2, 0], env, sensor=GPS)
    # simplerobot.update(env, handles)
    # pf = PF(simplerobot,
    #         M = 1000, env = env, handles = handles,
    #         boundary = array([[-12, 12], [-12, 12]]))
    # for ii in range(simpleDynamicinputs.shape[0]):
    #     simplerobot.input = simpleDynamicinputs[ii, :]
    #     simplerobot.predict(env)
    #     simplerobot.update(env, handles)
    #     pf.update(env, handles)
    #     time.sleep(0.05)

    ########################  Load a simpleDynamicRobot with a (only onte landmark)LandMark sensor   ########################
    ######################################                 Use PF to predict                   ##############################
    # simplerobot = robotType.SimpleDynamicRobot(robot, [-6, -2, 0], env, sensor=LandMark)
    # simplerobot.update(env, handles)
    # pf = PF(simplerobot,
    #         M = 1000, env = env, handles = handles,
    #         boundary = array([[-12, 12], [-12, 12]]))
    # for ii in range(simpleDynamicinputs.shape[0]):
    #     simplerobot.input = simpleDynamicinputs[ii, :]
    #     simplerobot.predict(env)
    #     simplerobot.update(env, handles)
    #     pf.update(env, handles)
    #     # time.sleep(0.05)

    ######################## Load a GoForwardDynamicRobot with a IMU sensor ########################
    ########################               Use PF to predict                ########################
    # goforwardrobot = robotType.GoForwardDynamicRobot(robot, [-6, 2, 0], env, sensor=IMU)
    # goforwardrobot.update(env, handles)
    # pf = PF(goforwardrobot,
    #         M = 1000, env = env, handles = handles,
    #         boundary = array([[-12, 12], [-12, 12]]))fe
    # for ii in range(goforwardDynamicinputs.shape[0]):
    #     goforwardrobot.input = goforwardDynamicinputs[ii, :]
    #     goforwardrobot.predict(env)
    #     goforwardrobot.update(env, handles)
    #     pf.update(env, handles)
    #     # time.sleep(0.05)

    ####################### Load a GoForwardDynamicRobot with a Laser sensor ########################
    #######################               Use PF to predict                ########################
    # goforwardrobot = robotType.GoForwardDynamicRobot(robot, [1, 0, 0], env, sensor=Laser)
    # goforwardrobot.update(env, handles)
    # pf = PF(goforwardrobot,
    #         M = 100, env = env, handles = handles,
    #         boundary = array([[0, 10], [-0.5, 0.5], [-0.05, 0.05]]))
    # for ii in range(goforwardDynamicinputs.shape[0]):
    #     goforwardrobot.input = goforwardDynamicinputs[ii, :]
    #     goforwardrobot.predict(env)
    #     goforwardrobot.update(env, handles)
    #     pf.update(env, handles)
    #     # time.sleep(0.05)

    #######################                  A* search                    ########################
    ######################## Load a simpleDynamicRobot with a GPS sensor  ########################
    ########################          Use KalmanFilter to predict         ########################
    ########################                 Use PID control              ########################
    # #search path and calculate input
    goalconfig =[8, 0, pi/2]
    simplerobot = robotType.SimpleDynamicRobot(robot, [1, 0, 0], env, sensor=GPS, search_alg = Astar)
    raw_input("Press enter to start searching path...")
    print("searching the path......")
    searchpath = simplerobot.search_path(handles, goalconfig)
    targetinput = simplerobot.path2input(searchpath)
    
    simplerobot.update(env, handles)
    kf = KF(simplerobot)
    pid = PID(searchpath, kp = np.array([5e-2, 5e-2, 0]))
    for ii in range(targetinput.shape[0]):
        simplerobot.input = targetinput[ii, :] + pid.FeedBack(simplerobot.observation)
        simplerobot.predict(env)
        simplerobot.update(env, handles)
        kf.update(env, handles)
        time.sleep(0.05)

    #######################                  A* search                    ########################
    ######################## Load a simpleDynamicRobot with a GPS sensor  ########################
    ########################               Use PF to predict              ########################
    #search path and calculate input
    # goalconfig =[8, 0, pi/2]
    # simplerobot = robotType.SimpleDynamicRobot(robot, [1, 0, 0], env, sensor=GPS, search_alg = Astar)
    # raw_input("Press enter to start searching path...")
    # print("searching the path......")
    # searchpath = simplerobot.search_path(handles, goalconfig)
    # targetinput = simplerobot.path2input(searchpath)

    # simplerobot.update(env, handles)
    # pf = PF(simplerobot,
    #         M = 100, env = env, handles = handles,
    #         boundary = array([[0, 27], [-10, 10], [-0.05, 0.05]]))
    # for ii in range(targetinput.shape[0]):
    #     simplerobot.input = targetinput[ii, :]
    #     simplerobot.predict(env)
    #     simplerobot.update(env, handles)
    #     pf.update(env, handles)
    #     time.sleep(0.05)

    raw_input("Press enter to exit...")
    handles = None
    env.Destroy()