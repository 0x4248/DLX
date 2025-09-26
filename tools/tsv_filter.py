# filter a tsv file based on a list of allowed extentions
# for example if i wanted only .png files but not .md this can help

allowed_ext = [".pdf", ".png", ".jpeg",  ".jpg", ".txt", ".odt"]
input_f = open("output.tsv", "r").readlines()
print(input_f)

for line in input_f:
	for ext in allowed_ext:
		if ext in line:
			open("output_filtered.tsv", "a").write(line)
