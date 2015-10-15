
function contains(table, element)
  for key,value in pairs(table) do
    if value == element then
      return true
    end
  end
  return false
end

function split(source, delimiters)
	local elements = {}
	local pattern = '([^'..delimiters..']+)'
	string.gsub(source, pattern, function(value) elements[#elements + 1] =     value;  end);
	return elements
end
