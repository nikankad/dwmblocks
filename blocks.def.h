// #define PATH(name)			"/home/yigit/.local/bin/status-bar/"name
//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
	// {"", "/home/USER/.config/dwmblocks/scripts/network.sh",	2,		0},

	{"", "/home/USER/.config/dwmblocks/scripts/spotify.sh",1,		6},
	// {"", "/home/USER/.config/dwmblocks/scripts/memory.sh",	10,		0},
	{"", "/home/USER/.config/dwmblocks/scripts/bitcoin.py",	600,		5},
	{"", "/home/USER/.config/dwmblocks/scripts/volume.sh",	0,		4},
	{"", "/home/USER/.config/dwmblocks/scripts/weather.py",	3600,		3},
	// {"", "/home/USER/.config/dwmblocks/scripts/packages.sh",	7200,		0},
	{"", "/home/USER/.config/dwmblocks/scripts/wifi.sh",5,		2},
	{"", "/home/USER/.config/dwmblocks/scripts/time.sh",1,		1},

};

//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim[] = " ";
static unsigned int delimLen = 5;
