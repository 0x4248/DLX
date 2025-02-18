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

import requests
from bs4 import BeautifulSoup
import os

try:
    os.mkdir("downloads")
except FileExistsError:
    pass

url = input("Enter the URL: ")
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all(class_="link")

    for item in items:
        a = item.find("a")
        href = a["href"]
        title = a.text
        if "(Europe)" in title or "(USA)" in title:
            if "Demo" not in title:
                open("out.csv", "a").write(f"{title}\t{url + href}\n")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
