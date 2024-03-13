#!/usr/bin/python3

"""

This utility is for use with kick assembler, it takes the breakpoint information from the kick .vs file
and adds it to the x16 emulator as part of the debug option

The launcher variable should contain the execution path for the emulator;
for example 

for Linux/MacOS

/Applications/x16emu/x16emu 

or for window

c:\\dev\\xemu.exe

options are the list of options you wish to start the emualtor with; see the xemu documentation for a full list

appName is the name of the program you are compiling 

scriptName is the script that will be created to execute the emulator - this will be a .bat file for windows and usuall a 
           .sh file for linux or mac

Note: for linux / mac you may need to add a chmod command to the build script to make the script executable

"""

appName    = 'main'
launcher   = '/Applications/x16emu/x16emu'
options    = '-run -scale 2 -ram 2048'
scriptName = "run.sh"

handle = open(appName+".vs","r")

lines = {} 
for param in handle:

    values = param.split(" ")
    lines[values[0]]=values[1]

handle.close()

handle = open (scriptName,"w")
commandLine = launcher + f' -prg {appName}.prg ' + options + f' -debug {lines["break"]}'
handle.write ( commandLine)
handle.close()


