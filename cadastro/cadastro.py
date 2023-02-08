from textwrap import fill
import tkinter as tk
from tkinter import Tk, ttk
from tkinter.tix import COLUMN
from turtle import width
import tkintermapview
import tksheet
import sv_ttk

contador=0
#('protocol','name','bairro','end','end_n','pedido_obs','pedido_situ')

#id
#id_user
#id_solicitante
#data_created
#data_updated
#data_finalizado
#SITUA��O
#protocolo
#nome_solicitante
#telefone_solicitante
#endere�o_pedido
#bairro_pedido
#referencia
#tipo_pedido
#observa��o
#foto
#localiza��o

pedido_id=contador
id_user=0
id_solicitante=20
pedido_year_created="23"
pedido_data_created="2023-02-08"
pedido_date_updated=""
pedido_data_finalizado=""
pedido_name_solicitante="Dona Fatima"
pedido_situacao="NAO ATENDIDO"
pedido_tipo=0
pedido_telefone="(65)9.9915-5117"
pedido_bairro="jardim celeste"
pedido_end="rua das seriemas"
pedido_n="115"
pedido_obs="perto da av talhamares"
pedido_foto=""
pedido_protocolo=f'{pedido_tipo}{id_solicitante}{pedido_id}{pedido_year_created}'


def get_pedidos_entry():
    global contador;
    contador=contador+1
    pedido_protocolo=contador
    pedido_name=name_entry.get()
    pedido_telefone=telefone_entry.get()
    pedido_bairro=bairro_entry.get()
    pedido_end=end_entry.get()
    pedido_n=numero_entry.get()
    pedido_obs=obs_entry.get()
    pedido_status="NAO EXECUTADO"
    pedidos=[pedido_protocolo,
    pedido_bairro,
    pedido_name,
    pedido_end,
    pedido_n,
    pedido_obs,
    pedido_status]
    return pedidos

def insert_database(pedidos):
    tree.insert('',tk.END,values=pedidos)

def add_pedido():
    insert_database(get_pedidos_entry())


root=tk.Tk()
root.geometry("1400x900")
root.title("Sistema de pedidos")
root.state("zoomed")


#LEFT PANEL
left_panel=ttk.Frame(root,width=600,height=900)
left_panel.place(x=0,y=20)

#RIGHT PANEL
rigth_panel=ttk.Frame(root,width=500,height=800)
rigth_panel.place(x=560,y=20)
#FRAME 4
pedido_panel=ttk.Frame(left_panel,width=600,height=600)
pedido_panel.place(x=0,y=0)
#nome do solicitante
name_label=ttk.Label(pedido_panel,text="NOME DO  SOLICITANTE")
name_label.place(x=20,y=40)
name_entry=ttk.Entry(pedido_panel,width=30)
name_entry.place(x=220,y=30)

#cpf
cpf_label=ttk.Label(pedido_panel, text="CPF")
cpf_label.place(x=20,y=80)
cpf_entry=ttk.Entry(pedido_panel, width=30)
cpf_entry.place(x=220,y=70)

#bairro
bairro_label=ttk.Label(pedido_panel, text="BAIRRO")
bairro_label.place(x=20,y=120)
bairro_entry=ttk.Entry(pedido_panel, width=30)
bairro_entry.place(x=220,y=110)

#endere�o
end_label=ttk.Label(pedido_panel, text="ENDERECO")
end_label.place(x=20,y=160)
end_entry=ttk.Entry(pedido_panel, width=30)
end_entry.place(x=220,y=150)
#n�mero
numero_label=ttk.Label(pedido_panel, text="NUNERO")
numero_label.place(x=20,y=200)
numero_entry=ttk.Entry(pedido_panel, width=30)
numero_entry.place(x=220,y=190)
#telefone
telefone_label=ttk.Label(pedido_panel, text="TELEFONE")
telefone_label.place(x=20,y=240)
telefone_entry=ttk.Entry(pedido_panel, width=30)
telefone_entry.place(x=220,y=230)
#observa��o
obs_label=ttk.Label(pedido_panel, text="OBSERVACAO")
obs_label.place(x=20,y=280)
obs_entry=ttk.Entry(pedido_panel, width=30)
obs_entry.place(x=220,y=270)

#foto
foto_label=ttk.Label(pedido_panel, text="FOTO")
foto_label.place(x=20,y=320)
foto_entry=ttk.Entry(pedido_panel, width=30)
foto_entry.place(x=220,y=310)

#selecionar equipe
equipe_label=ttk.Label(pedido_panel,text="EQUIPE")

equipe_input=ttk.Menubutton(pedido_panel,text="Equipe")
equipe_input.place(x=120,y=340)
equipe_input.menu=tk.Menu(equipe_input)
equipe_input["menu"]=equipe_input.menu

equipes=['Equipe 1','Equipe 2','Equipe 3','Celio']
for equipe in equipes:
    equipe_input.menu.add_radiobutton(
        label=equipe,
        value=equipe,
        )
equipe_label.place(x=20,y=340)

#localiza��o

local_label=ttk.Label(root, text="LOCALIZACAO")
local_label.place(x=20,y=390)
map_widget=tkintermapview.TkinterMapView(left_panel,width=400,height=200,corner_radius=0)
map_widget.place(x=20,y=400)
marker_1 = map_widget.set_address("prefeitura,caceres,mato grosso")

#local_entry=ttk.Entry(root, width=30)
#local_entry.grid(column=1,row=8)


#bota inserir pedido

inserir_button=ttk.Button(left_panel,text="INSERIR PEDIDO",command=add_pedido)
inserir_button.place(x=20,y=640)

editar_button=ttk.Button(left_panel,text="EDITAR PEDIDO")
editar_button.place(x=160,y=640)

deletar_button=ttk.Button(left_panel,text="DELETAR PEDIDO")
deletar_button.place(x=300,y=640)

#FRAME 4

#FRAME 5
columns=('protocol','name','telefone','bairro','end','end_n','pedido_obs','pedido_situ')

tree = ttk.Treeview(root, columns=columns, show='headings',height=600)
tree.heading('protocol',text="Protocolo")
tree.heading('name',text="Nome do solicitante")
tree.heading('telefone',text="Telefone")
tree.heading('bairro',text="Bairro")
tree.heading('end',text="Endereco")
tree.heading('end_n',text="N.")
tree.heading('pedido_obs',text="Observacao")
tree.heading('pedido_situ',text="Situacao")
tree.column("# 1",anchor=tk.CENTER,width=70)
tree.column("# 2",anchor=tk.CENTER,stretch=tk.NO,width=140)
tree.column("# 3",anchor=tk.CENTER,stretch=tk.NO,width=140)
tree.column("# 4",anchor=tk.CENTER,stretch=tk.NO,width=220)
tree.column("# 5",anchor=tk.CENTER,stretch=tk.NO,width=40)
tree.column("# 6",anchor=tk.CENTER,stretch=tk.NO,width=180)
tree.column("# 7",anchor=tk.CENTER,stretch=tk.NO,width=80)

scrollbar = ttk.Scrollbar(rigth_panel,orient=tk.VERTICAL)
scrollbar.pack(side="left", fill="y")
scrollbottom=ttk.Scrollbar(rigth_panel)
scrollbottom.pack(side="bottom",fill="y")


tree.place(x=610,y=20)
#sv_ttk.set_theme("light")
root.mainloop()