local sensor = {} 
sensor.__index = sensor 

function sensor.new(name,type,pins,unit)
  local self = setmetatable({}, sensor)
  self.name = name
  self.type = type
  self.pins = pins
  self.unit = unit
  return self
end

function sensor.set_name(self, newval)
  self.name = newval
end

function sensor.set_pins(self, newpins)
  self.type = newtype
end

function sensor.set_pins(self, newpins)
  self.pins = newpins
end

function sensor.get_name(self)
  return self.name
end

function sensor.get_type(self)
  return self.type
end

function sensor.get_pins(self)
  return self.pins
end



return sensor