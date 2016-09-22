import vrep
import time


def apply_wheel_velocities(
        forward_back_vel=0.0, left_right_vel=0.0, rot_vel=0.0):
    # Apply the desired wheel velocities:
    ret = vrep.simxSetJointTargetVelocity(
        clientID, wheel_joints[0],
        -forward_back_vel - left_right_vel - rot_vel,
        vrep.simx_opmode_blocking)
    ret = vrep.simxSetJointTargetVelocity(
        clientID, wheel_joints[1],
        -forward_back_vel + left_right_vel - rot_vel,
        vrep.simx_opmode_blocking)
    ret = vrep.simxSetJointTargetVelocity(
        clientID, wheel_joints[2],
        -forward_back_vel - left_right_vel + rot_vel,
        vrep.simx_opmode_blocking)
    ret = vrep.simxSetJointTargetVelocity(
        clientID, wheel_joints[3],
        -forward_back_vel + left_right_vel + rot_vel,
        vrep.simx_opmode_blocking)


def main():
    # Move a little
    apply_wheel_velocities(
        forward_back_vel=0.5,
        left_right_vel=0.5,
        rot_vel=0.5)
    time.sleep(2)
    # Stop
    apply_wheel_velocities()

    #import pdb
    #pdb.set_trace()


print 'Program started'
vrep.simxFinish(-1)  # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
if clientID != -1:
    print 'Connected to remote API server'
    ret = vrep.simxStartSimulation(clientID, vrep.simx_opmode_blocking)

    # Get joints (motors) from vrep
    # front left, rear left, rear right, front right
    wheel_joints = [-1, -1, -1, -1]
    ret, wheel_joints[0] = vrep.simxGetObjectHandle(
        clientID, 'rollingJoint_fl', vrep.simx_opmode_blocking)
    ret, wheel_joints[1] = vrep.simxGetObjectHandle(
        clientID, 'rollingJoint_rl', vrep.simx_opmode_blocking)
    ret, wheel_joints[2] = vrep.simxGetObjectHandle(
        clientID, 'rollingJoint_rr', vrep.simx_opmode_blocking)
    ret, wheel_joints[3] = vrep.simxGetObjectHandle(
        clientID, 'rollingJoint_fr', vrep.simx_opmode_blocking)
    ret, youBot = vrep.simxGetObjectHandle(
        clientID, 'youBot', vrep.simx_opmode_blocking)
    ret, youBotRef = vrep.simxGetObjectHandle(
        clientID, 'youBot_ref', vrep.simx_opmode_blocking)
    ret, tip = vrep.simxGetObjectHandle(
        clientID, 'youBot_positionTip', vrep.simx_opmode_blocking)
    ret, target = vrep.simxGetObjectHandle(
        clientID, 'youBot_positionTarget', vrep.simx_opmode_blocking)

    main()

    ret = vrep.simxStopSimulation(clientID, vrep.simx_opmode_blocking)
    vrep.simxFinish(clientID)
else:
    print 'Failed connecting to remote API server'
print 'Program ended'
