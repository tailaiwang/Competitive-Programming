# Compress a string based on run-length encoding
# e.g 'aaabbcccc' becomes 'a3b2c4'

def run_length_encode(input_str):
	output_str = ""
	if(len(input_str) == 0):
		return output_str
	elif(len(input_str) == 1):
		return (output_str + input_str + "1")
	
	cur_char_count = 1
	cur_char = input_str[0]
	
	for i in range(1, len(input_str)):
		if input_str[i] != cur_char:
			output_str += "(" +  (cur_char + " " + str(cur_char_count)) + ")"
			cur_char = input_str[i]
			cur_char_count = 1
		else:
			cur_char_count += 1
	
	return (output_str + "(" + cur_char + " " + str(cur_char_count) + ")")

print(run_length_encode("aaabbcccc"))

