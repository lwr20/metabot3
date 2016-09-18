# metabot3

- `/scene` - contains the VREP scene
- `metabot3.py` - an example robot control file
- `remoteApi.dll` - files needed to work with V-REP API (windows)
- `remoteApi.so` - files needed to work with V-REP API (linux)
- `vrep.py` - python wrapper for V-REP API
- `vrepConst.py` - constants for V-REP API

Files `remoteApi.dll`, `remoteApi.so`, `vrep.py` and `vrepConst.py` 
should be copied/linked from V-REP installation folder.

##Install V-REP

- Download from http://www.coppeliarobotics.com/downloads.html
- Copy the following into the repo directory:
    - Copy from `<install root>/V-REP3/V-REP_PRO_EDU/programming/remoteApiBindings/python/python`
        - `vrep.py`
        - `vrepConst.py`
    - Copy from `<install root>/V-REP3/V-REP_PRO_EDU/programming/remoteApiBindings/lib/lib`
        - `/64Bit/remoteApi.dll` (if on windows64)
        - `/64Bit/remoteApi.so` (if on linux64)

## Running
- Start V-REP
- Open `scene/metabot3.ttt` file 
- Start Simulation by press on "Play" button or from menu "Simulation", "Start simulation".

###Start robot control script
- In console:
- `python metabot3.py` 

## Useful links
- API overview 
    - http://www.coppeliarobotics.com/helpFiles/en/remoteApiOverview.htm
- Python API docs 
    - http://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm
- Video tutorial
    - https://www.youtube.com/watch?v=SQont-mTnfM
