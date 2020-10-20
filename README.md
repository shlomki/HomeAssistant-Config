# Welcome to shlomki/HomeAssistant-Config!

Hi! My name is Shlomi, I'm not expert in Home Assistant but I do have some nice automations and ideas to share with you, so I've uploaded my HA configuration here.
Feel free to browse.


# Directory Structure

## / Root Directory

This is the base directory for the configuration. The files are:

 - **custom_components** - This is where I store third party components that I've edited to fit my needs.
 - **packages** - This is where most of the logic is stored, you should definitely look at this folder.
 - **python_scripts** - A few helper scripts I've written that I use in my automations regularly. These scripts do slightly more complicated logic that's too much for yaml to handle.

## /packages Directory - The good stuff!

 - **Automations** - Anything that happens by itself, automagically.
 - **Climate** - Configurations regarding AC HVAC units, fans.
 - **Devices** - Other devices such as Cameras, Broadlink controllers, Shelly relays, TVs, etc.
 - **Lights** - Anything regarding the lights around the house.
 - **Services** - External services and helpers such as telegram, Google Maps, etc.
 - **Windows** - Controlling windows, shutters, curtains.
