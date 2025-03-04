from tkinter import *
import os
from tkinter import Frame
from tkinter import filedialog

'''
proj_stats.py
Responsible for project setup and holds information about important directories for the project. 
'''

REQ_PROJECT_DIR_LIST = (".settings", "Debug",
                        "Drivers", "Inc",
                        "Src", "startup")


class Proj_Stats:

    def __init__(self):
        self.projPath = ""
        self.isValidProj = False
        self.config_sampling_dir = None
        self.sample_dir = None
        self.openocdExe_dir = None

    @property
    def check_ready_for_config_creation(self):
        if len(self.config_sampling_dir.get()) == 0:
            return False
        if len(self.sample_dir.get()) == 0:
            return False

        return True

    def isValidProject(self, selPath):

        if len(selPath) == 0:
            return False

        isvalid = True
        reqDirs = [os.path.join(selPath, child) for child in REQ_PROJECT_DIR_LIST]

        dirlist = []
        dirlist = os.listdir(selPath)

        pathlist = [os.path.join(selPath, child) for child in dirlist]
        dirFilterObject = filter(os.path.isdir, pathlist)

        dirlist = list(dirFilterObject)

        # print("%s" % dirlist)
        # print("%s" % pathlist)

        for dirname in reqDirs:
            if (not (dirname in dirlist)):
                isvalid = False
                # print("%s was not found" % dirname)
                break

        return isvalid

    def get_config_dir(self):
        dir_path = filedialog.askdirectory(title="Select Configuration File Directory")

        if dir_path:
            self.config_sampling_dir.set(dir_path)

    def get_sample_data_dir(self):
        dir_path = filedialog.askdirectory(title="Select Sample Data Directory")

        if dir_path:
            self.sample_dir.set(dir_path)

    def get_opencd_exe_dir(self):
        dir_path = filedialog.askdirectory(title="Select openocd.exe Directory")

        if dir_path:
            self.openocdExe_dir.set(dir_path)

    def create_gui(self, master):
        '''
        Sets up gui elements that receive important project information.
        :param master: Tk root
        :return: Frame for "Directory Settings" tab.
        '''
        settingsFrame = Frame(master)
        settingsFrame.pack(fill="both")

        lf1 = LabelFrame(master=settingsFrame,
                         text="Configuration and Sampling List File Directory",
                         padx=10,
                         pady=5)
        lf1.pack(fill="both")

        lf2 = LabelFrame(master=settingsFrame,
                         text="Sampling Data Directory",
                         padx=10,
                         pady=5)
        lf2.pack(fill="both")

        lf3 = LabelFrame(master=settingsFrame,
                         text="OpenOCD Executable Directory",
                         padx=10,
                         pady=5)
        lf3.pack(fill="both")

        self.config_sampling_dir = StringVar()
        self.sample_dir = StringVar()
        self.openocdExe_dir = StringVar()

        entry1 = Entry(lf1, textvariable=self.config_sampling_dir)
        entry1.pack(anchor='w', expand=1, fill='x', side='left')
        button1 = Button(lf1, text="...", command=self.get_config_dir)
        button1.pack(anchor='e',side='left')

        entry2 = Entry(lf2, textvariable=self.sample_dir)
        entry2.pack(anchor='w', expand=1, fill='x', side='left')
        button2 = Button(lf2, text="...", command=self.get_sample_data_dir)
        button2.pack(anchor='e', side='left')

        entry3 = Entry(lf3, textvariable=self.openocdExe_dir)
        entry3.pack(anchor='w', expand=1, fill='x', side='left')
        button3 = Button(lf3, text="...", command=self.get_opencd_exe_dir)
        button3.pack(anchor='e', side='left')

        return settingsFrame

