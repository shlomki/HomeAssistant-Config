# Welcome to shlomki's Home Assistant Config!

Hi! My name is Shlomi, after spending quite some time with Home Assistant I decided it would be nice to share some of my nice automations and ideas with you, so I've uploaded my HA configuration here.
Feel free to browse.

# Disclaimer
This code was written for my own personal needs, most of it was customized in ways which might not fit your own needs and might not work for you as it does for me. However, you can still use it as a good starting point and build on top of it. Use at your own risk. Good luck!

# Screenshots

## Tablet
A dashboard for quick control of lights, AC and other devices, in all areas of the house. The idea is to allow the control of many types of devices with just one tap.

![Home Screen - Tablet](https://github.com/shlomki/HomeAssistant-Config/blob/main/examples/tablet_homescreen.png?raw=true)

## Mobile:
Designed to be more minimalistic, and provide access to different devices around the house grouped by device type, rather than by room.

![Home Screen- Mobile](https://github.com/shlomki/HomeAssistant-Config/blob/main/examples/mobile_homescreen.png?raw=true)
![Power](https://github.com/shlomki/HomeAssistant-Config/blob/main/examples/power.png?raw=true)
![Lights](https://github.com/shlomki/HomeAssistant-Config/blob/main/examples/lights.png?raw=true)
![Air Conditioning](https://github.com/shlomki/HomeAssistant-Config/blob/main/examples/air_conditioning.png?raw=true)
![Guest Mode](https://github.com/shlomki/HomeAssistant-Config/blob/main/examples/guest_mode.png?raw=true)
![Shower](https://github.com/shlomki/HomeAssistant-Config/blob/main/examples/shower.png?raw=true)
![Rooms](https://github.com/shlomki/HomeAssistant-Config/blob/main/examples/rooms.png?raw=true)
![Windows](https://github.com/shlomki/HomeAssistant-Config/blob/main/examples/windows.png?raw=true)

# Directory Structure

## / Root Directory

This is the base directory for the configuration. The files are:

 - **lovelace** - All of my UI.
 - **packages** - This is where most of the logic is stored, you should definitely look at this folder.
 - **python_scripts** - A few helper scripts I've written that I use in my automations regularly. These scripts do slightly more complicated logic that's too much for yaml to handle.
 - **ui_lovelace_minimalist/custom_cards** - Some of my own button-card templates, and some customizations on top of UI Lovelace Minimalist.

## /packages Directory - The good stuff!

 - **Automations** - Anything that happens by itself, automagically.
 - **Climate** - Configurations regarding HVAC units, fans.
 - **Devices** - Other devices such as Cameras, Broadlink controllers, Shelly relays, TVs, etc.
 - **Lights** - Anything regarding the lights around the house.
 - **Services** - External services and helpers such as telegram, Google Maps, etc.
