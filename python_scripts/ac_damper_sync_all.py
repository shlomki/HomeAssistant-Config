
options = { 'blocking': True }
rooms = ["living_room", "office", "guests", "riley", "bedroom"]
for room in rooms:
  hass.services.call('python_script', "ac_damper" , { 'room': room, 'action': 'sync' }, options)