# SPDX-License-Identifier: GPL-3.0
# DLX
#
# Bulk download tool
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
#
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

import os
import requests

f = open("links.csv")
f = f.read().split("\n")

for i in f:
	filename = i.split("\t")[0]
	url = i.split("\t")[1]
	if os.path.exists(f"downloads/{filename}"):
		print(f"{filename} already exists")
		continue
	print(f"Downloading {filename}")
	with open(f"downloads/{filename}", "wb") as f:
		os.system(f'wget -O "downloads/{filename}" "{url}"')

print("Done")