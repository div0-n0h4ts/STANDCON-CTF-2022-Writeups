# Flag: STANDCON22{_r3v_py7h0n_byt3c0d3}

flag_prefix = "STANDCON22{"
flag_mid = ""
flag_suffix = "}"


derived_key = [ "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a" ]
expected_output = ">\x13R\x17>\x11\x18V\tQ\x0f>\x03\x18\x15R\x02Q\x05R"


# Fact used:
# a ^ b = c
# b = c ^ c

# derived_key ^ flag = expected_output
# flag = derived_key ^ expected_output

inp_a = "".join(derived_key).encode("utf-8")
inp_b = expected_output.encode("utf-8")


for i, j in zip(inp_a, inp_b):
    flag_mid += chr(i ^ j)

flag = flag_prefix + flag_mid + flag_suffix

print ("Flag:", flag)