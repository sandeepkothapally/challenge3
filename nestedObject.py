def get_value_from_key(obj, key):
    # Split the key into its individual parts
    key_parts = key.split('/')
    
    # Traverse the object using each part of the key
    current_obj = obj
    for part in key_parts:
        if part in current_obj:
            current_obj = current_obj[part]
        else:
            return None
    
    # Return the final value
    return current_obj

  
  # Example inputs
obj1 = {"a":{"b":{"c":"d"}}}
key1 = 'a/b/c'
obj2 = {"x":{"y":{"z":"a"}}}
key2 = 'x/y/z'

# Example outputs
print(get_value_from_key(obj1, key1))  # Output: d
print(get_value_from_key(obj2, key2))  # Output: a
