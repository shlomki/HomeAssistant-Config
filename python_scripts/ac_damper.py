options = { 'blocking': True }
enableLog = False

#Params
room = data['room']
action = data['action']

if ('speed' in data) :
  requested_speed = data['speed']
else: 
  requested_speed = 'None'

#Entity IDs
damper_speed_entity_id = "input_select.ac_damper_" + room
damper_state_entity_id = "input_boolean.ac_damper_" + room
last_ac_mode_entity_id = "input_text.last_ac_mode"

#Vars
damper_state = hass.states.get(damper_state_entity_id).state

def turn_damper_on():
  hass.services.call('input_boolean', "turn_on" , { 'entity_id': damper_state_entity_id, }, options)
  if enableLog:
    logger.debug("Turn on entity_id: " + damper_state_entity_id)

  last_ac_mode = hass.states.get(last_ac_mode_entity_id).state
  speed = hass.states.get(damper_speed_entity_id).state

  if (speed == 'SmartAuto'): 
    speed = "low"
  elif (speed == 'Quick'):
    speed = "high"

  command_entity_id = "ac_damper_" + speed.lower() + "_" + last_ac_mode
  
  if enableLog:
    logger.debug("Run script: script." + command_entity_id + " in room: " + room)
  hass.services.call('script', command_entity_id , { 'room' : room } , options)

if (action == 'set_speed'):
  #Just save the new speed
  if enableLog:
    logger.debug("Set entity_id: " + damper_speed_entity_id + " to: " + requested_speed)
  hass.services.call('input_select', "select_option" , { 'entity_id': damper_speed_entity_id, 'option': requested_speed }, options)

  if (damper_state == 'on'):
    turn_damper_on()

if (action == 'turn_on') and (requested_speed == 'None'): #This is done to ignore turning on the damper when changing speed when it's off
  turn_damper_on()

if (action == 'turn_off') :
  if enableLog:
    logger.debug("Turn off entity_id: " + damper_state_entity_id)
  hass.services.call('input_boolean', "turn_off" , { 'entity_id': damper_state_entity_id }, options)
  
  if enableLog:
    logger.debug("Run script: script.ac_damper_off" + " in room: " + room)
  hass.services.call('script', 'ac_damper_off' , { 'room' : room } , options)

if (action == 'sync') :
  hass.services.call('input_boolean', "turn_on" , { 'entity_id': 'input_boolean.ac_damper_oscillating' }, options)
  if (damper_state == 'on') :
    last_ac_mode = hass.states.get(last_ac_mode_entity_id).state
    damper_speed = hass.states.get(damper_speed_entity_id).state
    command_entity_id = "ac_damper_" + damper_speed.lower() + "_" + last_ac_mode

  else :
    command_entity_id = "ac_damper_off"
  
  if enableLog:
    logger.debug("Run script: script." + command_entity_id + " in room: " + room)
  hass.services.call('script', command_entity_id , { 'room' : room } , options)
  hass.services.call('input_boolean', "turn_off" , { 'entity_id': 'input_boolean.ac_damper_oscillating' }, options)

  #Update current temp
  #hass.services.call('python_script', 'update_ac_room_temp', { 'room': room }, options)

