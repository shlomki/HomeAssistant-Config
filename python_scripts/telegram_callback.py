options = { 'blocking': True }

#Get params
callback_query_id = data['callback_query_id']
callback_data = data['callback_data']
callback_data = callback_data.split(':')
action = callback_data[0].replace('/', '')
entity_id = callback_data[1]

#Turn on / turn off
hass.services.call('homeassistant', action, { 'entity_id': entity_id }, options)

#Send callback that confirms new state
entity_data = hass.states.get(entity_id)
new_state = entity_data.state
entity_name = entity_data.attributes['friendly_name']
message = 'OK, ' + entity_name + ' is now ' + new_state
hass.services.call('telegram_bot', 'answer_callback_query', { 'callback_query_id': callback_query_id, 'message': message }, options)
