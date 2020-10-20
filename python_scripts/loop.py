service_data = { 'room': data['room'] }
options = { 'blocking': True }

for i in range(int(data['loop'])):
  hass.services.call(data['domain'], data['entity_id'], service_data, options)