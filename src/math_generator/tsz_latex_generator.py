'''
Created by: Tsz Hey
Created on: 13.09.2022

Wrapper for programmically generating latex documents.
'''
import os
import sys

class Doc:
    def __init__(self, filepath):
        self.filepath = filepath

    def erase(self):
        if os.path.isfile(self.filepath):
            os.remove(self.filepath)


    def add(self, text):
        with open(self.filepath, 'a') as f:
            f.write(text)
            f.write("\n")

    def add_section(self, text):
        section_arr = [r"\section", "{", text, "}"]
        section_text = ''.join(section_arr)
        self.add(rf"{section_text}")

    def add_newpage(self):
        self.add(r"\newpage")
    def add_geometry(self, geometry_options):
        self.add(r"\usepackage{geometry}")
        self.add(r"\geometry{")
        for option in geometry_options:
            self.add(rf"{option},")
        self.add(r"}")
