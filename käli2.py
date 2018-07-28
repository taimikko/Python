from tkinter import *
class Pommikäyttöliittymä:
    def __init__(self):
      self.__pääikkuna = Tk()
      self.__bang_kuva = PhotoImage(file="bang.gif")
      self.__bomb_kuva = PhotoImage(file="bomb.gif")
      self.__boom_kuva = PhotoImage(file="boom.gif")
      self.__pommi_label = Label(self.__pääikkuna, image=self.__bomb_kuva, height=110, background="white")
      self.__räjäytä_button = Button(self.__pääikkuna, image=self.__bang_kuva, command=self.räjäytä)
      self.__lataa_button = Button(self.__pääikkuna, text="lataa", command=self.lataa, state=DISABLED, background="white")
      self.__lopeta_button = Button(self.__pääikkuna, text="lopeta", command=self.lopeta, background="white")
      self.__pommi_label.pack(fill=BOTH)
      self.__räjäytä_button.pack()
      self.__lataa_button.pack(fill=BOTH)
      self.__lopeta_button.pack(fill=BOTH)
      self.__pääikkuna.mainloop()
    def räjäytä(self):
      self.__pommi_label.configure(image=self.__boom_kuva)
      self.__räjäytä_button.configure(state=DISABLED)
      self.__lataa_button.configure(state=NORMAL)
    def lataa(self):
      self.__pommi_label.configure(image=self.__bomb_kuva)
      self.__räjäytä_button.configure(state=NORMAL)
      self.__lataa_button.configure(state=DISABLED)
    def lopeta(self):
      self.__pääikkuna.destroy()
def main():
  käyttöliittymä = Pommikäyttöliittymä()
main()