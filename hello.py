#!/usr/bin/env python
from gimpfu import *

def greeting(img, layer):
	pdb.gimp_text_fontname(img, None,
			10, 10, "Hello, World!",
			-1, False, 50.0, 0, "Sans")

register(
	"python_fu_greeting",
	"Greet the world",
	"Write \"Hello, World!\" on the current layer",
	"Tomaz Solc",
	"Open source (BSD 3-clause license)",
	"2018",
	"<Image>/Filters/Demo/Greeting",
	"*",
	[],
	[],
	greeting)

main()
