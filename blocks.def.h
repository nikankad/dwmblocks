//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
	// {"", "/home/user/.config/dwmblocks/scripts/network.sh",	2,		0},
	{"", "/home/user/.config/dwmblocks/scripts/song.sh",1,		0},

	{"", "/home/user/.config/dwmblocks/scripts/bitcoin.py",	180,		0},
	{"", "/home/user/.config/dwmblocks/scripts/memory.sh",	10,		0},
	{"", "/home/user/.config/dwmblocks/scripts/weather.py",	180,		0},
	{"", "/home/user/.config/dwmblocks/scripts/time.sh",1,		0},

};

//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim[] = " ";
static unsigned int delimLen = 5;