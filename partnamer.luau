-- without render fidelity

local meshes = location
local customName = "Name"

for _, descendant in ipairs(meshes) do
	if descendant:IsA("MeshPart") then
		descendant.Name = customName
	end
end


-- with render fidelity

local meshes = location
local customName = "Name"

for _, descendant in ipairs(meshes) do
	if descendant:IsA("MeshPart") then
		descendant.Name = customName
		if descendant.RenderFidelity == Enum.RenderFidelity.Automatic or 
			descendant.RenderFidelity == Enum.RenderFidelity.Performance then
			descendant.RenderFidelity = Enum.RenderFidelity.Precise
		end
	end
end
