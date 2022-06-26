from tkinter import *
from tkinter import messagebox
import tkinter

def binario_para_decimal(string):
    decimal = 0
    inversa = string[::-1]

    for i in range(7):
        if inversa[i] == '1':
            decimal += 2 ** i

    return decimal


def checa_se_binario(string):
    p = set(string)
    s = {'0', '1'}

    if s == p or p == {'0'} or p == {'1'}:
        return True
    else:
        return False
fundo = "#F0fFFF"
fontePadrao = "Helvetica, 14"
fontetitle = "Helvetica, 16"
class Application:

    def __init__(self, master=None):
        #fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10 
        self.primeiroContainer["background"] = fundo
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["background"] = fundo
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["background"] = fundo
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer["background"] = fundo
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer["background"] = fundo
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="")
        self.titulo["background"] = fundo
        self.titulo["font"] = fontetitle  
        self.titulo.pack()

        self.entrada = Entry(self.segundoContainer)
        self.entrada["width"] = 30
        self.entrada["font"] = fontePadrao
        self.entrada["background"] = "#fff"
        self.entrada.pack(side=LEFT)

        self.selected = StringVar()
        self.radioCaracterToAscii = Radiobutton(self.terceiroContainer, command=self.atualiza_titulo)
        self.radioCaracterToAscii["text"] = "CARACTER ➠ ASCII"
        self.radioCaracterToAscii["value"] = "caracterToAscii"
        self.radioCaracterToAscii["variable"] = self.selected
        self.radioCaracterToAscii["font"] = fontePadrao
        self.radioCaracterToAscii["background"] = fundo
        self.radioCaracterToAscii.pack()
        self.radioCaracterToAscii.invoke()

        self.radioAsciiToCaracter = Radiobutton(self.terceiroContainer, command=self.atualiza_titulo)
        self.radioAsciiToCaracter["text"] = "ASCII ➠ Caracter"
        self.radioAsciiToCaracter["value"] = "asciiToCaracter"
        self.radioAsciiToCaracter["font"] = fontePadrao
        self.radioAsciiToCaracter["background"] = fundo
        self.radioAsciiToCaracter["variable"] = self.selected
        self.radioAsciiToCaracter.pack()

        self.converter = Button(self.quartoContainer, command=self.converter)
        self.converter["text"] = "CONVERTER"
        self.converter["font"] = fontePadrao
        self.converter["background"] = "#DAA520"
        self.converter["width"] = 12
        self.converter["relief"] = "groove"
        self.converter["border"] = "1.5px"
        # 'self.converter["command"] = self.converter'
        self.converter.pack()

        self.saida = Label(self.quintoContainer, text=f'''Decimal: \nBinário: ''')
        self.saida["font"] = fontePadrao
        self.saida["background"] = fundo
        self.saida.pack()

    def converter(self):
        if self.selected.get() == "caracterToAscii":
            self.caracter_ascii()
        elif self.selected.get() == "asciiToCaracter":
            self.ascii_caracter()

    def caracter_ascii(self):
        caracter = self.entrada.get()
        if len(caracter) == 1:
            decimal = ord(caracter)
            binario = bin(decimal).replace("0b", "")
            texto = f'''Decimal: {decimal}\nBinário: {binario}'''
        else:
            messagebox.showerror(title="Error", message= "INSIRA APENAS UM CARACTER")
            texto = f'''Decimal: N/A\nBinário: N/A'''
        self.saida["text"] = texto

    def ascii_caracter(self):
        if self.valida_ascii():
            valido_ascii = self.valida_ascii()

            caracter = chr(valido_ascii)
            texto = f'''Caracter: {caracter}\n'''
        else:
            messagebox.showerror(title="Error", message= "INSIRA APENAS 1 CARACTER")
            texto = f'''Caracter: N/A\n'''
        self.saida["text"] = texto

    def valida_ascii(self):
        ascii_inverificado = self.entrada.get()
        if len(ascii_inverificado) == 7:
            if checa_se_binario(ascii_inverificado):
                return binario_para_decimal(ascii_inverificado)
            else:
                return False
        elif ascii_inverificado.isdigit():
            if 0 <= int(ascii_inverificado) <= 127:
                return int(ascii_inverificado)
            else:
                return False
        else:
            return False

    def atualiza_titulo(self):
        if self.selected.get() == "caracterToAscii":
            self.titulo["text"] = "DIGITE UM CARACTER"
            if hasattr(self, 'ascii'):
                self.saida["text"] = f'''DECIMAL: \nBINÁRIO: '''
        elif self.selected.get() == "asciiToCaracter":
            self.titulo["text"] = "DIGITE O CÓDIGO ASCII"
            if hasattr(self, 'ascii'):
                self.saida["text"] = f'''CARACTER: \n'''


root = Tk()
root.configure(background = fundo)
root.title("CONVERSOR ASCII")
Application(root)
root.mainloop()
root.configure()
