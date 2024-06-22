local parts = Part Location Here -- Location of where your parts are located like a folder or model
local customName = "Your Name of all parts" -- Name which you will name all of the parts

for _, descendant in ipairs(parts) do
	if descendant:IsA("TYPE OF YOUR PART!!") then
		descendant.Name = customName
	end
end
