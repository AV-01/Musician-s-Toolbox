import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Musician's Toolbox", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        # self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        # self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        # self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        # self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        all_song_names = []
        with open('name_of_all_music.txt', 'r') as f:
            for line in f:
                all_song_names.append(line)
        self.optionmenu = customtkinter.CTkOptionMenu(master=self.sidebar_frame, values=all_song_names, command=self.load_song)
        self.optionmenu.grid(row=5, column=0, padx=0, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Music Name")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(text="Save",master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=self.save_song)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.goals_frame = customtkinter.CTkFrame(self)
        self.goals_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_goals_group = customtkinter.CTkLabel(master=self.goals_frame, text="Genre of music:")
        self.label_goals_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.goals_frame, variable=self.radio_var, value=0,text="Jazz")
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.goals_frame, variable=self.radio_var, value=1,text="Rock")
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.goals_frame, variable=self.radio_var, value=2,text="Pop")
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_4 = customtkinter.CTkRadioButton(master=self.goals_frame, variable=self.radio_var, value=2,text="Blues")
        self.radio_button_4.grid(row=4, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_5 = customtkinter.CTkRadioButton(master=self.goals_frame, variable=self.radio_var, value=2,text="Country")
        self.radio_button_5.grid(row=5, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_6 = customtkinter.CTkRadioButton(master=self.goals_frame, variable=self.radio_var, value=2,text="Rap")
        self.radio_button_6.grid(row=5, column=2, pady=10, padx=20, sticky="n")
        #
        # # create slider and progressbar frame
        # self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        # self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        # self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        # self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        # self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        # self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        # self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        # self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")
        #
        # # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Thing to add: ")
        self.scrollable_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        switch1 = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Instruments")
        switch1.grid(row=1, column=0, padx=10, pady=(0, 20))
        switch2 = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Chorus")
        switch2.grid(row=2, column=0, padx=10, pady=(0, 20))
        switch3 = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Sheet Music")
        switch3.grid(row=3, column=0, padx=10, pady=(0, 20))
        switch4 = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Other band members")
        switch4.grid(row=4, column=0, padx=10, pady=(0, 20))

        self.textbox1 = customtkinter.CTkTextbox(self, width=250)
        self.textbox1.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.textbox1.insert("0.0", "Notes:\n\n")

        self.appearance_mode_optionemenu.set("Dark")
        self.textbox.insert("0.0", "Lyrics:\n\n")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def save_song(self):
        with open('name_of_all_music.txt', 'a') as f:
            song_name = self.entry.get()
            print(song_name)
            f.write(f'{song_name}\n')
        print("Saved!")
        all_song_names = []
        with open('name_of_all_music.txt', 'r') as f:
            for line in f:
                all_song_names.append(line)
        self.optionmenu.configure(values=all_song_names)
        song_name = self.entry.get()
        with open(f'{song_name}_lyrics.txt', 'w') as f:
            f.write(self.textbox.get("0.0","100000.0"))
        with open(f'{song_name}_notes.txt', 'w') as f:
            f.write(self.textbox1.get("0.0","100000.0"))
            # print(self.textbox1.get("0.0","10000.0"))

    def load_song(self,song_name1):
        song_name = song_name1.replace("\n","")
        print("load in"+song_name)
        all_lyrics = []
        self.textbox.delete("0.0", "100000.0")
        self.textbox1.delete("0.0", "100000.0")
        with open(f'{song_name}_lyrics.txt', 'r') as f:
            for line in f:
                all_lyrics.append(line)
        self.textbox.insert("0.0", "\n".join(all_lyrics))
        all_notes = []
        with open(f'{song_name}_notes.txt', 'r') as f:
            for line in f:
                all_notes.append(line)
        self.textbox1.insert("0.0", "".join(all_notes))


if __name__ == "__main__":
    app = App()
    app.mainloop()