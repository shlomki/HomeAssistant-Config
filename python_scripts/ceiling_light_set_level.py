options = { 'blocking': True }

room = data['room']
input_number_entity = "input_number." + room + "_light_level"
input_boolean_entity = "input_boolean." + room + "_script_running"

if hass.states.get(input_boolean_entity).state != "on":
  hass.services.call('input_boolean', 'turn_on', { 'entity_id': input_boolean_entity }, options)
  
  current_brightness_level = int(float(hass.states.get(input_number_entity).state))
  new_brightness_level =  round(int(data['new_brightness_level']) / 14.1666)
  difference = new_brightness_level - current_brightness_level
  script_service_data = { 'room': room }
  
  if (new_brightness_level == 18):
    hass.services.call('script', "ceiling_light_brightness_highest" , script_service_data, options) 
    hass.services.call('input_number', 'set_value', { 'entity_id': input_number_entity, 'value': 18 }, options)
  elif (new_brightness_level == 0):
    hass.services.call('script', "ceiling_light_brightness_lowest" , script_service_data, options)
    hass.services.call('input_number', 'set_value', { 'entity_id': input_number_entity, 'value': 0 }, options)
  else:
    entity = ""
    if difference <= 0:
      entity = "ceiling_light_brightness_down"
      step = -1
    else:
      entity = "ceiling_light_brightness_up"
      step = 1
    
    for i in range(current_brightness_level, new_brightness_level + step, step):
      hass.services.call('script', entity, script_service_data, options) 
      hass.services.call('input_number', 'set_value', { 'entity_id': input_number_entity, 'value': i }, options)
  
  hass.services.call('input_boolean', 'turn_off', { 'entity_id': input_boolean_entity }, options)
