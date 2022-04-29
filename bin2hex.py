import os

os.chdir(".") # Change dir name

def bin2hex(filename):

	data = open(filename,"rb").read()

	fp = open(filename+".h","w+")

	data_length = len(data)

	for i in range(len(data)):

		if data[i] < 0x10:
			char_str = str(hex(data[i]))
			char_str = char_str[:2]+'0'+char_str[2:]
			fp.write(char_str+', ')
		else:
			fp.write(hex(data[i])+', ')

		next_line = (i+1)%16
		if next_line==0:
			fp.write('\n')
			
	fp.close()


if __name__ == '__main__':
	for file in os.listdir():
		if file.endswith(".bin"):
			print(file)
			bin2hex(file)
