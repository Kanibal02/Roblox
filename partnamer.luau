local meshes = location
local customName = "Name"

for _, descendant in ipairs(meshes) do
	if descendant:IsA("MeshPart") then
		descendant.Name = customName
	end
end
