import re
import base64

def generate_random_name(counter):
    """Generates a random variable name like 'v1', 'v2', etc."""
    return f"v{counter}"

def encode_string(s):
    """Encodes a string using base64."""
    return base64.b64encode(s.encode()).decode()

def obfuscate_lua_code(lua_code):
    # Regular expression to match local variables and function parameters
    local_var_pattern = r'\blocal\s+([a-zA-Z_]\w*)'   # Matches local variables
    func_param_pattern = r'function\s*\(.*?\)'        # Matches function parameters
    string_pattern = r'\"(.*?)\"'                     # Matches string literals
    
    # Dictionary to map original variable names to obfuscated names
    variable_mapping = {}
    counter = 1

    # Obfuscate local variables
    matches = re.findall(local_var_pattern, lua_code)
    for match in matches:
        if match not in variable_mapping:
            variable_mapping[match] = generate_random_name(counter)
            counter += 1
    
    # Obfuscate function parameters
    func_param_matches = re.findall(r'function\s*\((.*?)\)', lua_code)
    for params in func_param_matches:
        param_list = params.split(',')
        for param in param_list:
            param = param.strip()
            if param not in variable_mapping and param:  # avoid empty params
                variable_mapping[param] = generate_random_name(counter)
                counter += 1
    
    # Replace all occurrences of the original variables with obfuscated names
    for original_var, obfuscated_var in variable_mapping.items():
        lua_code = re.sub(rf'\b{original_var}\b', obfuscated_var, lua_code)

    # Obfuscate string literals
    lua_code = re.sub(string_pattern, lambda m: f'get_decoded_string("{encode_string(m.group(1))}")', lua_code)
    
    # Add the decoding function at the top of the Lua script
    decoding_function = """
local function get_decoded_string(encoded)
    local b='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    encoded = string.gsub(encoded, '[^'..b..'=]', '')
    return (encoded:gsub('.', function(x)
        if (x == '=') then return '' end
        local r,b='',b:find(x)-1
        for i=6,1,-1 do r=r..(b%2^i-b%2^(i-1)>0 and '1' or '0') end
        return r;
    end):gsub('%d%d%d?%d?%d?%d?%d?%d?', function(x)
        if (#x ~= 8) then return '' end
        local c=0
        for i=1,8 do c=c+(x:sub(i,i)=='1' and 2^(8-i) or 0) end
        return string.char(c)
    end))
end
    """
    
    lua_code = decoding_function + lua_code
    
    # Remove newlines and extra spaces to compress to a single line
    lua_code = ' '.join(lua_code.split())
    
    return lua_code

def obfuscate_file(input_file, output_file):
    # Read the input Lua code
    with open(input_file, 'r') as file:
        lua_code = file.read()

    # Obfuscate the Lua code
    obfuscated_code = obfuscate_lua_code(lua_code)

    # Write the obfuscated code to the output file
    with open(output_file, 'w') as file:
        file.write(obfuscated_code)

    print(f"Obfuscation complete! Output saved to {output_file}")

# File paths for input and output
input_file = 'input.txt'
output_file = 'output.txt'

# Run the obfuscator
obfuscate_file(input_file, output_file)
