local sensor = {} 
sensor.__index = sensor 

function sensor.new(name,type,pins)
  local self = setmetatable({}, sensor)
  self.name = name
  self.type = type
  self.pins = pins
  return self
end

function sensor.set_name(self, newval)
  self.name = newval
end

function sensor.get_name(self)
  return self.name
end

function sensor.get_type(self)
  return self.type
end

return sensor