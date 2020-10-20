options = { 'blocking': True }
enableLog = False

#Params
fan_name = data['name']
requested_speed = data['speed']

#Entity IDs
fan_entity_id = "fan." + fan_name
fan_speed_script_entity_id = fan_name + "_speed"
fan_input_select_speed_entity_id = "input_select." + fan_name + "_speed"

#Vars
fan_input_select_state = hass.states.get(fan_input_select_speed_entity_id)
if enableLog:
    logger.debug(fan_input_select_state)
speed_list = fan_input_select_state.attributes['options']
current_speed = fan_input_select_state.state

if (requested_speed in speed_list):

    if enableLog:
        logger.debug("start. current_speed: " + current_speed + " requested_speed: " + requested_speed)

    while (current_speed != requested_speed):

        #Go to next speed
        hass.services.call('script', fan_speed_script_entity_id, { }, options)
        hass.services.call('input_select', 'select_next', { 'entity_id': fan_input_select_speed_entity_id }, options)
        current_speed = hass.states.get(fan_input_select_speed_entity_id).state
        
        if enableLog:
            logger.debug("loop. current_speed: " + current_speed + " requested_speed: " + requested_speed)


else:
    if enableLog:
        logger.debug(requested_speed + " is not an option of " + fan_entity_id)
