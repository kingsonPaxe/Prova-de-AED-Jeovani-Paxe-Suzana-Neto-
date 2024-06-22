from Libs import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Configurando a tela
        self.geometry("1000x600")
        # self.resizable(0,0)
        self.title('Simulação de uma ED')
        
        self.fila = fila()
        self.gf = nx.Graph()
        self.labels = [] # onde vai armazenar a quantidade de lables
        self.columns = 15 # Numero maximos de colunas para mudar de linha
    
        # Minha barra de navegacao
        self.MenuBar()

    #Criando o menuBar
    def MenuBar(self):
        self.menuBar = ctk.CTkTabview(self, fg_color='#292b31')
        self.menuBar.pack(expand = True, fill = "both")

        self.tb_fila = self.menuBar.add('Fila')
        self.tb_grafos = self.menuBar.add('Grafos')
        self.tb_arvore = self.menuBar.add('Árvore')
        
        #Chamando cada Tela
        self.MenuBarGrafos()
        self.MenuBarFila()
    #Criando a Tela Fila
    def MenuBarFila(self):
        self.input = ctk.CTkEntry(self.tb_fila, placeholder_text='Insira um valor na lista',font=('', 12))
        self.input.pack(pady=10)
        self.btn_push = ctk.CTkButton(self.tb_fila, text='Adicionar', command=self.push, font=('', 12))
        self.btn_push.pack(pady=10)

        self.btn_pop = ctk.CTkButton(self.tb_fila, text='Eliminar', command=self.pop,font=('', 12))
        self.btn_pop.pack(pady=10)

        self.output = ctk.CTkScrollableFrame(self.tb_fila, fg_color = "#EFF3F6")
        self.output.pack(pady=10, padx=10,expand=True, fill='both')
        

        # Criando outro frame para o ver o tamaho da lable
        self.frame = ctk.CTkFrame(self.tb_fila,height=50, width=1000, fg_color='#292b31',corner_radius=0)
        self.frame.pack(pady=10)

        self.btn_size = ctk.CTkButton(self.tb_fila, text='Ver tamanho', command=self.view_size)
        self.btn_size.pack(pady=10)

    def push(self):

        self.data = self.input.get()
        if self.data == '':
            print('Adiciona um elemento na lista')
            messagebox.showwarning("Mensagem de Erro", "Adiciona um elemento na lista")


        elif self.data:
            self.fila.push(self.data)
            self.addLable()
            print(self.fila.data)
            self.input.delete(0, "end")

    
    def pop(self):
        if self.fila.isEmpty():
            print('Lista vazia')
            messagebox.showwarning("Mensagem de Erro", "Lista vazia")
        else:
            self.fila.pop()
            print(self.fila.data)
            self.deleteLable()

    def addLable(self):
        lable_text = f"{self.data}"
        self.label = ctk.CTkLabel(self.output, text=f"{lable_text}", font=('',18), fg_color='#2a4c63', height=50, width=50 )
        self.labels.append(self.label)

        # Mudando as colunas
        self.update_lables()

    def deleteLable(self):
        if len(self.labels) > 0:
            primeiro_label = self.labels[0]
            primeiro_label.destroy()  # Exemplo: destruir a label no Tkinter

            # Removendo a primeira label da lista
            self.labels.pop(0)
    # change de columns
    def update_lables(self):
        for i, label in enumerate(self.labels):
            row = i // self.columns
            col = i % self.columns
            label.grid(row=row, column=col, pady= 5, padx=5)
            

    #Ver o tamanho da fila
    def view_size(self):
        self.size_list =  ctk.CTkLabel(self.frame, text= f'A lista possui {self.fila.size()} elementos', fg_color='#292b31', font=('', 17), height=50, width=50)
        self.size_list.place(y = 10, x=390)
        print(self.fila.size())

    # ************************************** Tela dos Grafos **************************************
    def MenuBarGrafos(self):
        self.input1 = ctk.CTkEntry(self.tb_grafos, placeholder_text= 'No 1 ')
        self.input1.pack(pady=10)

        self.input2 = ctk.CTkEntry(self.tb_grafos, placeholder_text='No 2',font=('', 12))
        self.input2.pack(pady=10)
        self.btn_arestras = ctk.CTkButton(self.tb_grafos, text='Add aresta', command=self.add_aresta, font=('', 12))
        self.btn_arestras.pack(pady=10)

        # A parte onde vai ficar o resultado do grafos
        self.graph_frame = ctk.CTkScrollableFrame(self.tb_grafos, fg_color="white")
        self.graph_frame.pack(padx=20, pady=20, fill = 'both', expand= True)

        self.figura,self.ax = plt.subplots(figsize=(5,4)) # configurando o tamanho da figura
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(side=ctk.TOP, fill = 'both', expand= True)
        self.atualizar_grafo()

        self.protocol("WM_DELETE_WINDOW", self.on_closing) # garantir que a interface estara fechada

    def add_aresta(self):
        node1 = self.input1.get()
        node2 = self.input2.get()

        if node1 and node2:
            self.gf.add_edge(node1, node2)
            self.input1.delete(0, "end")
            self.input2.delete(0, "end")
            self.atualizar_grafo()
    
    def atualizar_grafo(self):
        self.ax.clear()
        pos = nx.spring_layout(self.gf)
        nx.draw(self.gf, pos, with_labels=True, ax=self.ax) # responsavel por fazer as ligacoes
        self.canvas.draw()

    # fechar a interface
    def on_closing(self):
        self.destroy()
        plt.close('all')

if __name__=="__main__":
    app = App()
    app.mainloop()