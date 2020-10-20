room = data['room']
packet = data['packet']

script_service_data = { 'entity_id': 'remote.' + room, 'command': 'b64:' + packet }
options = { 'blocking': True }

hass.services.call('remote', 'send_command', script_service_data, options)
