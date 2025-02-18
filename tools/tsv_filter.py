# filter a tsv file based on a list of allowed extentions

allowed_ext = [".pdf", ".png", ".jpeg",  ".jpg", ".txt", ".odt"]
input_f = open("output.tsv", "r").readlines()
print(input_f)

for line in input_f:
	for ext in allowed_ext:
		if ext in line:
			open("output_filtered.tsv", "a").write(line)
