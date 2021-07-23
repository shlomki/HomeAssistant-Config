options = { 'blocking': True }

#Get params
callback_query_id = data['callback_query_id']
callback_data = data['callback_data']
callback_data = callback_data.split(' ')
chat_id = data['chat_id']
file = callback_data[1]

#Turn on / turn off
hass.services.call('script', 'notify_photo', { 'file': file, 'target': chat_id, 'message': 'Photo' }, options)

#Send callback that confirms new state
message = 'OK, photo sent.'
hass.services.call('telegram_bot', 'answer_callback_query', { 'callback_query_id': callback_query_id, 'message': message }, options)

