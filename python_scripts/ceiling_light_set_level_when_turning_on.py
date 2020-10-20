options = { 'blocking': True }

#Find room name
entity_id = data['entity_id']
room = entity_id
room = room.replace('group.', '')
room = room.replace('light.', '')
room = room.replace('_dimmable_lights', '')
room = room.replace('_main', '')
room = room.replace('_entrance', '')
room = room.replace('_hallway', '')

#Set input number "input_number.{ROOM}_light_level" to 18 (max brightness)
input_number_entity = "input_number." + room + "_light_level"
hass.services.call('input_number', 'set_value', { 'entity_id': input_number_entity, 'value': 18 }, options)