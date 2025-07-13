#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import sys, time, os
from os import listdir
from os.path import join

os.system('cls')

class HID_SCRIPT_APPENDER: 

    def __init__(self, base_dir = 'C:/Users/edanr/Desktop/Code/Python/HID/' ):
        self.base_dir = base_dir
        self.script_dir = join(self.base_dir, "HID_Scripts/")
        self.output_file = join(self.base_dir, 'output.js')
        self.available_scripts = listdir(self.script_dir)
    
    def display_scripts(self):
        for idx, filename in enumerate(self.available_scripts, start=1):\
            print(f"({idx} {filename})")
        time.sleep(0.7)

    def get_user_selection(self):
        selected_snippets = input("\nEnter the indices you want to compound in order (comma separated): " + "\n\n")
        print("\n")
        selected_snippets = [int(idx.strip()) - 1 for idx in selected_snippets.split(',') if idx.strip().isdigit()]
        return selected_snippets

    def merge_selection(self, selected_snippets):
        open(self.output_file, 'w').close()
        with open(self.output_file, 'w', encoding='utf-8') as output_file:
            for idx in selected_snippets:
                script_path = join(self.script_dir, self.available_scripts[idx])
                with open(script_path, 'r', encoding='utf-8') as reading_file:
                    content = reading_file.read()
                    output_file.write(content)
                print(f"Appending: {self.available_scripts[idx]}")
                time.sleep(0.7)
            print(f"\nOutput written to: {self.output_file}\n\n\n")
            time.sleep(1)
            sys.exit()

class CONVERTER:
    
    def __init__(self, base_dir = 'C:/Users/edanr/Desktop/Code/Python/HID/' ):

        usr_input_file = input("Input File: ")
        time.sleep(1)
        usr_output_file = input("Output File: " )

        self.base_dir = base_dir
        self.input_file = join(base_dir, usr_input_file)
        self.output_file =  join(base_dir, usr_output_file)

        self.string = "STRING"
        self.delay = "DELAY"
        self.press = ["ENTER", "SHIFT", "CTRL", "LEFTARROW", "RIGHTARROW"]
        self.comment = "REM"


    def convert(self):
        with open(self.input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print("Reading File..."); time.sleep(0.7)

        with open(self.output_file, 'w', encoding='utf-8') as f:
            print("Translating File..."); time.sleep(0.7)
            for line in lines:

                if any(keyword in line for keyword in [self.string] + self.press + [self.delay]):

                    if self.string in line:
                        index = line.find(self.string) + len(self.string)
                        content_after = line[index:].strip()
                        new_line =  f"type('{content_after}')\n"
                        f.write(new_line)

                    elif self.delay in line:
                        index = line.find(self.delay) + len(self.delay)
                        content_after = line[index:].strip()
                        new_line =  f"delay('{content_after}')\n"
                        f.write(new_line)

                    elif any(key in line for key in self.press):
                        content_key = line.rstrip('\n')
                        new_line = f"press('{content_key}')\n"
                        f.write(new_line)

                    elif self.comment or "" in line:
                        new_line = "\n"
                        f.write(new_line)

                    else:
                        new_line = line.rstrip('\n') + " // Unmodified line\n"
                        f.write(new_line)
        sys.exit()

def main():

    resp = int(input("\nTool (0) CONVERTER or (1) APPENDER: "))
    print("")

    if not resp:
        os.system('cls')
        manager = CONVERTER()
        manager.convert()

    elif resp:
        os.system('cls')
        manager = HID_SCRIPT_APPENDER()
        time.sleep(3)
        manager.display_scripts()
        time.sleep(2)
        selected_snippets = manager.get_user_selection()
        time.sleep(1)
        manager.merge_selection(selected_snippets)

    else: 
        os.system('cls')
        sys.exit()

main()
