import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.master = master
        self.master.minsize(700, 150)
        self.master.maxsize(700, 150)

        # Default button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=8, column=2)

        # Entry box submit button
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.submitCustomText)
        self.btn.grid(row=8, column=3)

        # Creates text box label
        self.lbl_box = tk.Label(self.master, text='Enter custom text or click the default HTML button')
        self.lbl_box.grid(row=1, column=0, padx=(27, 0), pady=(10, 0), sticky=N + W)

        # Creates entry box
        self.txt_box = tk.Entry(self.master, text='')
        self.txt_box.grid(row=2, column=0, rowspan=4, columnspan=4, padx=(30, 40), pady=(0, 0), sticky=N + E + W)

    # Default buttons function
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # Submit buttons function
    def submitCustomText(self):
        var_text = self.txt_box.get() # Grabs entry from text box to use
        htmlText = "{}".format(var_text) # Applies entry to webpage
        htmlFile = open("index.html", "w") # Creates file to be opened
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>" # Generates files base
        htmlFile.write(htmlContent) # Writes out the file
        htmlFile.close()
        webbrowser.open_new_tab("index.html") # Opens the created file in a webpage


if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()
