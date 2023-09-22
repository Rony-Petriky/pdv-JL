import customtkinter as ctk
from tkinter import *
from CTkTable import *
from PIL import Image

#janela principal
janela = ctk.CTk()
#janela._set_appearance_mode("dark")
janela.title("PDV-JL")
janela.geometry("794x477")
janela.minsize(width=774, height=477)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=300)
janela.grid_columnconfigure(0, minsize=198)

janela.grid_rowconfigure(0, weight=1)
############################################################################

#fremes da esquerda e direita#################################################
fremeDireita= ctk.CTkFrame(master= janela, width=543 , height=441, fg_color="#343434", corner_radius=10)
#fremeDireita.pack_forget()
fremeDireita.grid(row=0, column=1,pady=10, padx=10, sticky="wsne")
fremeEsquerda= ctk.CTkFrame(master= janela, width=198 , height=457, fg_color="#343434")
fremeEsquerda.grid(row=0, column=0, sticky="wsne")

fremeBotaoMenu= ctk.CTkFrame(master= fremeEsquerda, width=198 , height=239, fg_color="transparent", corner_radius=10)
fremeBotaoMenu.grid(row=0, column=0, sticky="E")

fremeEsquerda.grid_columnconfigure(0, weight=1)
fremeEsquerda.grid_rowconfigure(0, weight=1)

#################################################################################

#funçoes dos botoes de menu######################################### 

def fremeVendas():
    fremeDireita.destroy()
    fremeDireitad= ctk.CTkFrame(master= janela, width=543 , height=441, fg_color="#343434", corner_radius=10)
#freme1.bind()
    fremeDireitad.grid(row=0, column=1,pady=10, padx=10, sticky="wsne")

    fremeVendas= ctk.CTkFrame(master=fremeDireitad, width=198 , height=457, fg_color="transparent", corner_radius=10)
    fremeVendas.grid(row=0, column=0, pady=10, padx=10, sticky="EW")
    tituloVendas = ctk.CTkLabel(master=fremeVendas,fg_color="transparent", text="Vendas", font=("Arial", 20))
    tituloVendas.grid(row=0, column=0, padx=20, pady=10, sticky="w")

    value = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

    table = CTkTable(master=fremeVendas, row=5, column=5, values=value)
    table.grid(row=1, column=0, padx=20, pady=20)
   

def fremeClientes():
    fremeDireita.destroy()
    fremeDireitad= ctk.CTkFrame(master= janela, width=543 , height=441, fg_color="#343434", corner_radius=10)
#freme1.bind()
    fremeDireitad.grid(row=0, column=1,pady=10, padx=10, sticky="wsne")

    fremeClientes= ctk.CTkFrame(master=fremeDireitad, width=198 , height=457, fg_color="transparent", corner_radius=10)
    fremeClientes.grid(row=0, column=0, pady=10, padx=10, sticky="EW")
    tituloClientes = ctk.CTkLabel(master=fremeClientes,fg_color="transparent", text="Clientes", font=("Arial", 20))
    tituloClientes.grid(row=0, column=0, padx=20, pady=10, sticky="nw")

def fremeProdutos():
    fremeDireita.destroy()
    fremeDireitad= ctk.CTkFrame(master= janela, width=543 , height=441, fg_color="#343434", corner_radius=10)
#freme1.bind()
    fremeDireitad.grid(row=0, column=1,pady=10, padx=10, sticky="wsne")
    fremeProdutos= ctk.CTkFrame(master=fremeDireitad, width=198 , height=457, fg_color="transparent", corner_radius=10)
    fremeProdutos.grid(row=0, column=0, pady=10, padx=10, sticky="EW")
    tituloProdutos = ctk.CTkLabel(master=fremeProdutos,fg_color="transparent", text="Produtoss", font=("Arial", 20))
    tituloProdutos.grid(row=0, column=0, padx=20, pady=10, sticky="nw")
def fremeStatus():
    fremeDireita.destroy()
    fremeDireitad= ctk.CTkFrame(master= janela, width=543 , height=441, fg_color="#343434", corner_radius=10)
#freme1.bind()
    fremeDireitad.grid(row=0, column=1,pady=10, padx=10, sticky="wsne")

    fremeStatus= ctk.CTkFrame(master=fremeDireitad, width=198 , height=457, fg_color="transparent", corner_radius=10)
    fremeStatus.grid(row=0, column=0, pady=10, padx=10, sticky="EW")
    tituloStatus = ctk.CTkLabel(master=fremeStatus,fg_color="transparent", text="Status", font=("Arial", 20))
    tituloStatus.grid(row=0, column=0, padx=20, pady=10, sticky="nw")
#######################################################################################

#imagens do menu##################################################################
imgVendas = ctk.CTkImage(light_image= Image.open("../img/vendas.png"),size=(38,38))
imgClientes = ctk.CTkImage(light_image= Image.open("../img/clientes.png"),size=(38,38))
imgProdutos = ctk.CTkImage(light_image= Image.open("../img/produtos.png"),size=(38,38))
imgstatus = ctk.CTkImage(light_image= Image.open("../img/status.png"),size=(38,38))
######################################################################################

#criaçao dos botoes##########################################################
butonVendas= ctk.CTkButton(master=fremeBotaoMenu, image= imgVendas, width=198, height=58, fg_color="#343434", 
                              hover_color="#4D4D4D",font=("Arial", 20), text="Vendas", command=fremeVendas)
butonClientes= ctk.CTkButton(master=fremeBotaoMenu, image=imgClientes, width=198, height=58, fg_color="#343434", 
                              hover_color="#4D4D4D", font=("Arial", 20), text="Clientes", command=fremeClientes)
butonProdutos= ctk.CTkButton(master=fremeBotaoMenu, image=imgProdutos, width=198, height=58, fg_color="#343434",
                              hover_color="#4D4D4D", font=("Arial", 20), text="Produtos", command=fremeProdutos)
butonStatus= ctk.CTkButton(master=fremeBotaoMenu, image=imgstatus, width=198, height=58, fg_color="#343434", 
                               hover_color="#4D4D4D", font=("Arial", 20), text="Status", command=fremeStatus)


butonVendas.grid_columnconfigure(0,weight=1)
butonClientes.grid_columnconfigure(0,weight=1)
butonProdutos.grid_columnconfigure(0,weight=1)
butonStatus.grid_columnconfigure(0,weight=1)


butonVendas.grid(row=0, column=0, sticky="EW")
butonClientes.grid(row=1, column=0, sticky="EW")
butonProdutos.grid(row=2, column=0, sticky="EW")
butonStatus.grid(row=3, column=0, sticky="EW")
###################################################################################################################

#freme4 = ctk.CTkFrame(master=janela, width=200, height=200).grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

def segmented_button_callback(value):
    print("segmented button clicked:", value)

'''segemented_button = ctk.CTkSegmentedButton(freme1, values=["Value 1", "Value 2", "Value 3","Value 4","Value 5"],
                                                     command=segmented_button_callback)
segemented_button.set("Value 2")
segemented_button.grid(row=0, column=2)
'''



def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="#2C2C2C")
    nova_janela.geometry("478x438")

#btn = ctk.CTkButton(master=janela, text='abrir', command=nova_tela).place(x=300, y=100)



janela.mainloop()