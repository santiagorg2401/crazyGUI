# crazyGUI

Graphical user interface for the [Crazyswarm](https://github.com/USC-ACTLab/crazyswarm) software ran in Python 3, this interface helps the user by grouping the most used tools such as the configuration files, [Cfclient](https://github.com/bitcraze/crazyflie-clients-python), etc.

## Dependencies.
For using crazyGUI you will need:
```console
pip3 install PyQt5
pip3 install cfclient
pip3 install numpy
pip3 install PyYAML
pip3 install QDarkStyle
pip3 install crazyKhoreia
```
## Installation.
1. Follow the steps for [Crazyswarm](https://github.com/USC-ACTLab/crazyswarm) in [installation](https://crazyswarm.readthedocs.io/en/latest/installation.html#installation) (Sidenote: for now, crazyGUI expects you to have crazyswarm inside a crazyflie folder like ~/crazyflie/crazyswarm/...).
2. Clone the repo:
```console
git clone https://github.com/santiagorg2401/crazyGUI.git
```

## Usage.
To use crazyGUI just run:
```console
python3 crazyGUI/crazyGUI.py
```
The GUI is organized by tabs, please select the tabs you are going to use in the section "Tabs" and then click the check boxes, the window will rearrange and resize automatically.

If you want to use the CrazyKhoreia tool with CrazySwarm, you may use the auto flight scripts in [ras_choreographies](https://github.com/santiagorg2401/ras_choreographies)

## Authors.
- [Santiago Restrepo García.](https://github.com/santiagorg2401)
