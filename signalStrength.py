# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:33:15 2016

@author: rajat
"""

import subprocess

interface = "wlan0"
name = []
signal_level = []


def match(line, keyword):
    """If the first part of line (modulo blanks) matches keyword,
    returns the end of that line. Otherwise returns None"""
    line = line.lstrip()
    length = len(keyword)
    if line[:length] == keyword:
        return line[length:]
    else:
        return None


def main():
    proc = subprocess.Popen(["iwlist", interface, "scan"],
                            stdout=subprocess.PIPE, universal_newlines=True)
    out, err = proc.communicate()
    for line in out.split("\n"):
        name_line = match(line, "ESSID")
        signal_line = match(line, "Quality=")
        if name_line is not None:
            name.append(name_line[2:-1].rstrip())
        if signal_line is not None:
            signal_level.append(signal_line.split(
                "Signal level=")[1][:-5].rstrip())
            # print(name.rstrip())

    print(name)
    print(signal_level)

main()
