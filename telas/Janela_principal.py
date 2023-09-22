import customtkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from CTkTable import *
from PIL import Image
from tktooltip import ToolTip
from tkcalendar import Calendar, DateEntry

class JanelaPrincipal(customtkinter.CTk):
    def __init__(self, values, commandpesbotao, comandoImprimirCsv):
        super().__init__()

#########################################JANELA PRINCIPAL###########################################
        self.title("PDV-JL")
        self.geometry("1050x477")
        self.minsize(width=1050, height=477)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=300)
        self.grid_columnconfigure(0, minsize=198)

        self.grid_rowconfigure(0, weight=1)

        self.values = values
        self.commandpesbotao = commandpesbotao
        self.comandoImprimirCsv = comandoImprimirCsv

############################################## fremes principais ####################################
        self.fremeDireita= customtkinter.CTkFrame(master= self, width=543 , height=441, fg_color="#343434", corner_radius=10)
        #fremeDireita.pack_forget()
        self.fremeDireita.grid(row=0, column=1,pady=10, padx=10, sticky="wsne")
        self.fremeEsquerda= customtkinter.CTkFrame(master= self, width=198 , height=457, fg_color="#343434")
        self.fremeEsquerda.grid(row=0, column=0, sticky="wsne")

        self.fremeBotaoMenu= customtkinter.CTkFrame(master= self.fremeEsquerda, width=198 , height=239, fg_color="transparent", corner_radius=10)
        self.fremeBotaoMenu.grid(row=0, column=0, sticky="E")

        self.fremeEsquerda.grid_columnconfigure(0, weight=1)
        self.fremeEsquerda.grid_rowconfigure(0, weight=1)

############################################# imagens do menu ##########################################
        self.imgVendas = customtkinter.CTkImage(light_image= Image.open("../pdv-jL/img/vendas.png"),size=(38,38))
        self.imgClientes = customtkinter.CTkImage(light_image= Image.open("../pdv-jL/img/clientes.png"),size=(38,38))
        self.imgProdutos = customtkinter.CTkImage(light_image= Image.open("../pdv-jL/img/produtos.png"),size=(38,38))
        self.imgstatus = customtkinter.CTkImage(light_image= Image.open("../pdv-jL/img/status.png"),size=(38,38))

############################################# BOTOES DE MENU ##############################################
        self.butonVendas= customtkinter.CTkButton(master=self.fremeBotaoMenu, image= self.imgVendas, width=198, height=58, fg_color="#343434", 
                              hover_color="#4D4D4D",font=("Arial", 20), text="Vendas", command=self.fremeVendas)
        self.butonClientes= customtkinter.CTkButton(master=self.fremeBotaoMenu, image=self.imgClientes, width=198, height=58, fg_color="#343434", 
                              hover_color="#4D4D4D", font=("Arial", 20), text="Clientes", command=self.fremeClientes)
        self.butonProdutos= customtkinter.CTkButton(master=self.fremeBotaoMenu, image=self.imgProdutos, width=198, height=58, fg_color="#343434",
                              hover_color="#4D4D4D", font=("Arial", 20), text="Produtos", command=self.fremeProdutos)
        self.butonStatus= customtkinter.CTkButton(master=self.fremeBotaoMenu, image=self.imgstatus, width=198, height=58, fg_color="#343434", 
                               hover_color="#4D4D4D", font=("Arial", 20), text="Status", command=self.fremeStatus)


        self.butonVendas.grid_columnconfigure(0,weight=1)
        self.butonClientes.grid_columnconfigure(0,weight=1)
        self.butonProdutos.grid_columnconfigure(0,weight=1)
        self.butonStatus.grid_columnconfigure(0,weight=1)


        self.butonVendas.grid(row=0, column=0, sticky="EW")
        self.butonClientes.grid(row=1, column=0, sticky="EW")
        self.butonProdutos.grid(row=2, column=0, sticky="EW")
        self.butonStatus.grid(row=3, column=0, sticky="EW")
        el = self.elementos()

    def elementos(self):
        #self.fremeDireita.grid_rowconfigure(0, weight=1)
        self.felementos= customtkinter.CTkFrame(master=self.fremeDireita, width=0 , height=0, fg_color="transparent", corner_radius=10)
        self.felementos.grid(row=0, column=0, pady=10, padx=10, sticky="wsne")   
     

    def fremeVendas(self):
        self.felementos.destroy()
        self.elementos()
        self.fremeDireita.grid_columnconfigure(0,weight=1)
        self.felementos.grid_columnconfigure(0, weight=1)
        self.fremeDireita.grid_rowconfigure(0, weight=1)
        self.felementos.grid_rowconfigure(1, weight=1)



        self.felementos.columnconfigure(1, minsize=100)

        tituloVendas = customtkinter.CTkLabel(master=self.felementos,fg_color="transparent", text="Vendas", font=("Arial", 20))
        tituloVendas.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.inicio = customtkinter.CTkLabel(master=self.felementos,fg_color="transparent", text="inicio", font=("Arial", 12))
        self.inicio.grid(row=0, column=0, padx=(135,0),  sticky="wn")
        
        self.calinicio = DateEntry(master=self.felementos, width=10, background="#267EC3",date_pattern="dd-mm-yyyy")
        self.calinicio.set_date("01-01-2023") 
        self.calinicio.grid(row=0, column=0, padx=(135,0), pady=(20,0), sticky="wn")

        self.fim = customtkinter.CTkLabel(master=self.felementos,fg_color="transparent", text="fim", font=("Arial", 12))
        self.fim.grid(row=0, column=0, padx=(265,0),  sticky="wn")

        style = ttk.Style()
# style.theme_use('clam') # -> uncomment this line if the styling does not work
        style.configure('my.DateEntry',
        fieldbackground='light green',
        background='dark green',
        foreground='dark blue',
        arrowcolor='white')

        
        self.calfim = DateEntry(master=self.felementos, width=10, background="#267EC3",date_pattern="dd-mm-yyyy")
       
        #cal2.set_date("01-01-2023") 
        self.calfim.grid(row=0, column=0, padx=(265,0), pady=(20,0), sticky="wn")

        imgabrir_cadastro = customtkinter.CTkImage(light_image= Image.open("../pdv-jL/img/abrir_cadastro.png"),size=(30,30))
        self.imgiconcadastro = customtkinter.CTkButton(master=self.felementos, width=60, image= imgabrir_cadastro, fg_color="#343434", 
                              hover_color="#4D4D4D", text=None, command=self.nova_tela)
        self.imgiconcadastro.grid(row=0, column=1, padx=20,ipadx=None, sticky="E")

        imgabrir_csv = customtkinter.CTkImage(light_image= Image.open("../pdv-jL/img/csv.png"),size=(30,30))
        imgiconcsv = customtkinter.CTkButton(master=self.felementos, width=60, image= imgabrir_csv, fg_color="#343434", 
                              hover_color="#4D4D4D", text=None, command=self.abrir_arquivo)
        imgiconcsv.grid(row=0, column=1, padx=100,ipadx=None, sticky="E")


        scroltable = customtkinter.CTkScrollableFrame(master=self.felementos, fg_color="#4D4D4D", corner_radius=10)
        #fremeDireita.columnconfigure(0,weight=1)
        scroltable.columnconfigure(0, weight=1)
        scroltable.rowconfigure(0, weight=1)

        #scroltable.columnconfigure(0, maxsize=600)

        scroltable.grid(row=1, column=0, pady=10, padx=10, columnspan=2, sticky="nEws")

        values = self.values
        table = CTkTable(master=scroltable, hover=True, hover_color="#000000", pady=5, colors=["#267EC3","#267EC3"], header_color="#000000", values=values)
        table.grid(row=0, column=0, sticky="nW")

        self.pesBotao = customtkinter.CTkButton(master=self.felementos, width=55, height=16, fg_color="#000000", 
                              hover_color="#267EC3", text="pesquisar", command=self.commandpesbotao)
        #cancelarbotao.rowconfigure(0,weight=1)
        #cancelarbotao.columnconfigure(0,weight=1)
        self.pesBotao.grid(row=0, column=0, ipady=2, padx=(365,0), pady=(20,0), sticky="wn")
    

    def pegarData(self):
        datainicio = self.calinicio.get_date()
        datefim = self.calfim.get_date()
        return datainicio, datefim

    def fremeClientes(self):
        self.felementos.destroy()
        self.elementos()

        tituloClientes = customtkinter.CTkLabel(master=self.felementos,fg_color="transparent", text="Clientes", font=("Arial", 20))
        tituloClientes.grid(row=0, column=0, padx=20, pady=10, sticky="nw")

    def fremeProdutos(self):
        self.felementos.destroy()
        self.elementos()
 
        tituloProdutos = customtkinter.CTkLabel(master=self.felementos,fg_color="transparent", text="Produtoss", font=("Arial", 20))
        tituloProdutos.grid(row=0, column=0, padx=20, pady=10, sticky="nw")

    def fremeStatus(self):
        self.felementos.destroy()
        self.elementos()

        tituloStatus = customtkinter.CTkLabel(master=self.felementos,fg_color="transparent", text="Status", font=("Arial", 20))
        tituloStatus.grid(row=0, column=0, padx=20, pady=10, sticky="nw")

    def abrir_arquivo(self):
        file_name = filedialog.askopenfilename(initialdir ="C:", title="Escolha um arquivo", filetypes=(("CSV Files","*.csv"),))
        if file_name:
            self.comandoImprimirCsv(file_name)

    def nova_tela(self):
        self.nova_janela_cadastro_cliente = customtkinter.CTkToplevel(self, fg_color="#2C2C2C")
        self.nova_janela_cadastro_cliente.geometry("478x438")
        self.nova_janela_cadastro_cliente.resizable(width=False, height=False)
        #self.nova_janela_cadastro_cliente.rowconfigure(0,weight=1)
        self.nova_janela_cadastro_cliente.columnconfigure(0, weight=1)
        #self.nova_janela_cadastro_cliente.rowconfigure(1, weight=1)
        #self.nova_janela_cadastro_cliente.rowconfigure(2, weight=1)
        self.nova_janela_cadastro_cliente.grid_rowconfigure(4, weight=1)
        self.nova_janela_cadastro_cliente.grid_rowconfigure(5, weight=1)


        self.nova_janela_cadastro_cliente.transient(self)
        self.nova_janela_cadastro_cliente.focus_force()
        self.nova_janela_cadastro_cliente.grab_set()
        #self.nova_janela_cadastro_cliente.overrideredirect(True)

        
        def cancelar():
            self.nova_janela_cadastro_cliente.destroy()
        
        self.cancelarBotao = customtkinter.CTkButton(master=self.nova_janela_cadastro_cliente, width=55, height=16, fg_color="#343434", 
                              hover_color="#267EC3", text="finalizar", command=cancelar)
        self.proxBotao = customtkinter.CTkButton(master=self.nova_janela_cadastro_cliente, width=55, height=16, fg_color="#343434", 
                              hover_color="#267EC3", text="proximo", command=cancelar)
        #cancelarbotao.rowconfigure(0,weight=1)
        #cancelarbotao.columnconfigure(0,weight=1)
        self.cancelarBotao.grid(row=6, column=0, pady=(0,10), padx=(110,10), sticky="es")
        self.proxBotao.grid(row=6, column=0, pady=(0,10), padx=(10,85), sticky="es")

        nomeLabel = customtkinter.CTkLabel(master=self.nova_janela_cadastro_cliente, fg_color="transparent", 
                         text="Nome do cliente", font=("Arial", 12))
        nomeLabel.grid(row=0, column=0, padx=(10,0), pady=(41,0), sticky="wn")

        nomebox = customtkinter.CTkEntry(master=self.nova_janela_cadastro_cliente, width=325, height=16,
                                     placeholder_text="Digiteo o nome do cliente" )
        ToolTip(nomebox, msg="Somente clientes cadastrados!")
        nomebox.grid(row=0, column=0, padx=(110,0), pady=(41,0), sticky="wn")

        produtoLabel = customtkinter.CTkLabel(master=self.nova_janela_cadastro_cliente, fg_color="transparent", 
                         text="Produto", font=("Arial", 12))
        produtoLabel.grid(row=1, column=0, padx=(10,0), pady=(44,0), sticky="wn")
        produtobox = customtkinter.CTkEntry(master=self.nova_janela_cadastro_cliente, width=184, height=16,
                                    placeholder_text="Digite o produto")
        ToolTip(produtobox, msg="Somente produtos cadastrados!")
        produtobox.grid(row=1, column=0, padx=(110,0), pady=(49,0), sticky="wn")

        quantidadeLabel = customtkinter.CTkLabel(master=self.nova_janela_cadastro_cliente, fg_color="transparent", 
                         text="Quantidade", font=("Arial", 12))
        quantidadeLabel.grid(row=1, column=0, padx=(0,65), pady=(44,0), sticky="en")
        produtoEntry = customtkinter.CTkEntry(master=self.nova_janela_cadastro_cliente, width=49, height=16, placeholder_text="Q/")
        produtoEntry.grid(row=1, column=0, padx=(0,5), pady=(48,0), sticky="en")

        formaLabel = customtkinter.CTkLabel(master=self.nova_janela_cadastro_cliente, fg_color="transparent", 
                         text="Forma de pag/", font=("Arial", 12))
        formaLabel.grid(row=2, column=0, padx=(10,0), pady=(44,0), sticky="wn")

        optioforma = customtkinter.CTkOptionMenu(master=self.nova_janela_cadastro_cliente, height=16,
                        values=["Pagamento a vista", "Pagamento a prazo"])
        optioforma.grid(row=2, column=0, padx=(110,0), pady=(49,0), sticky="wn")

        radio_var = customtkinter.IntVar(value=0)
        radiocartao = customtkinter.CTkRadioButton(master=self.nova_janela_cadastro_cliente, width=50, variable=radio_var, radiobutton_height=16, radiobutton_width=16, text="Cartâo",
                                            value=1)
       
        radiodinheiro = customtkinter.CTkRadioButton(self.nova_janela_cadastro_cliente, width=50, variable=radio_var, radiobutton_height=16, radiobutton_width=16, text="Dinheiro",
                                              value=2)
        radiocartao.grid(row=2, column=0, padx=(0,5), pady=(49,0), sticky="en")
        radiodinheiro.grid(row=2, column=0, padx=(0,90), pady=(49,0), sticky="en")

        statusLabel = customtkinter.CTkLabel(master=self.nova_janela_cadastro_cliente, fg_color="transparent", 
                         text="Status do pedido", font=("Arial", 12))
        statusLabel.grid(row=3, column=0, padx=(10,0), pady=(44,0), sticky="wn")

        optiostatus = customtkinter.CTkOptionMenu(master=self.nova_janela_cadastro_cliente, height=16,
                        values=["Agendamento Pag/", "Personalizaçâo", "Preparaçâo da arte", "Pedido Pronto"])
        optiostatus.grid(row=3, column=0, padx=(110,0), pady=(49,0), sticky="wn")

        porcentagemLabel = customtkinter.CTkLabel(master=self.nova_janela_cadastro_cliente, fg_color="transparent", 
                         text="%", font=("Arial", 12))
        porcentagemLabel.grid(row=3, column=0, padx=(0,150), pady=(44,0), sticky="en")
        porcentagemEntry = customtkinter.CTkEntry(master=self.nova_janela_cadastro_cliente, width=49, height=16, placeholder_text="%")
        porcentagemEntry.grid(row=3, column=0, padx=(0,90), pady=(48,0), sticky="en")

        fremeTabela= customtkinter.CTkFrame(master= self.nova_janela_cadastro_cliente, width=322 , height=85, fg_color="#D9D9D9", corner_radius=10)
        fremeTabela.grid_rowconfigure(0, weight=1)
        fremeTabela.grid_columnconfigure(0, weight=1)
        fremeTabela.grid(row=4, column=0, padx=10, pady=5, sticky="wns", rowspan=3)

        tabelaLabel = customtkinter.CTkLabel(master=fremeTabela, fg_color="transparent", text_color="#000000", 
                         text="Q/            Produto              desc/               Valor            Final", font=("Arial", 12))
        tabelaLabel.grid(row=0, column=0, padx=5, sticky="n")

        rsLabel = customtkinter.CTkLabel(master=self.nova_janela_cadastro_cliente, fg_color="transparent", 
                         text="R$", font=("Arial", 12))
        rsLabel.grid(row=4, column=0, padx=(0,125), pady=(0,0), sticky="ne")

        fremepreco= customtkinter.CTkFrame(master= self.nova_janela_cadastro_cliente, width=95 , height=46, fg_color="#4D4D4D", corner_radius=5)
        fremepreco.grid(row=5, column=0, padx=(0,50), pady=(0,40), sticky="ne")



    