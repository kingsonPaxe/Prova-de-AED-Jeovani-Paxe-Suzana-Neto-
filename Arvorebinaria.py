from Libs import *
from Arvorebinaria import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")




ctk.set_default_color_theme("dark-blue")


class No:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        self.root = None  # Inicializa a raiz como None por padrão
        if node:
            self.root = node
        elif data:
            self.root = No(data)

    def em_ordem_erd(self, node=None):
        if self.root is None:
            return []
        if node is None:
            node = self.root
        percurso = []
        if node.left:
            percurso += self.em_ordem_erd(node.left)
        percurso.append(node.data)
        if node.right:
            percurso += self.em_ordem_erd(node.right)
        return percurso

    def pos_ordem_edr(self, node=None):
        if self.root is None:
            return []
        if node is None:
            node = self.root
        percurso = []
        if node.left:
            percurso += self.pos_ordem_edr(node.left)
        if node.right:
            percurso += self.pos_ordem_edr(node.right)
        percurso.append(node.data)
        return percurso

    def pre_ordem(self, node=None):
        if self.root is None:
            return []
        if node is None:
            node = self.root
        percurso = [node.data]
        if node.left:
            percurso += self.pre_ordem(node.left)
        if node.right:
            percurso += self.pre_ordem(node.right)
        return percurso

    def altura(self, node=None):
        if self.root is None:
            return -1
        if node is None:
            node = self.root
        altura_esquerda = 0
        altura_direita = 0
        if node.left:
            altura_esquerda = self.altura(node.left)
        if node.right:
            altura_direita = self.altura(node.right)
        return max(altura_esquerda, altura_direita) + 1

    def imprimir_arvore(self, node=None, level=0, prefix="Root"):
        if self.root is None:
            return
        if node is None:
            node = self.root
        print(" " * (level * 4) + prefix + ": " + str(node.data))
        if node.left:
            self.imprimir_arvore(node.left, level + 1, "L---")
        if node.right:
            self.imprimir_arvore(node.right, level + 1, "R---")

class ArvoreBinariaBusca(BinaryTree):
    def inserir(self, valor):
        parent = None
        x = self.root
        node = No(valor)
        while x:
            parent = x
            if valor < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = node
        elif valor < parent.data:
            parent.left = node
        else:
            parent.right = node
    
    
    ##########################################################
    def remover(self, valor):
        return self._remover_recursivo(self.root, valor)

    def _remover_recursivo(self, node, valor):
        if node is None:
            return None

        if valor < node.data:
            node.left = self._remover_recursivo(node.left, valor)
        elif valor > node.data:
            node.right = self._remover_recursivo(node.right, valor)
        else:
            # Caso 1: Nó sem filhos
            if node.left is None and node.right is None:
                return None
            # Caso 2: Nó com um filho
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Caso 3: Nó com dois filhos
            menor_direita = self._encontrar_menor(node.right)
            node.data = menor_direita.data
            node.right = self._remover_recursivo(node.right, menor_direita.data)

        return node

    def _encontrar_menor(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    

####################################################3  CTkCanvas

class TreeVisualizer(ctk.CTkFrame):
    def __init__(self, master=None, tree=None):
        super().__init__(master)
        # self.master = master
        self.tree = tree
        # self.master.title("Visualização da Árvore Binária")
        self.canvas_width = 1000
        self.canvas_height =600
        
        #Criando o menuBar
    
    
        self.create_widgets()

        
    def create_widgets(self):        
        self.canvas = ctk.CTkCanvas(self)
        self.canvas.pack(expand=True, fill=ctk.BOTH)
        
        scrollbar = tk.Scrollbar(self.canvas, orient=ctk.VERTICAL)
        scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)
        scrollbar.config(command=self.canvas.yview)
        
        
        
        # Frame para entrada de dados
        input_frame = ctk.CTkFrame(self,fg_color='#292b31')
        input_frame.pack()

        self.entry_valor = ctk.CTkEntry(input_frame,placeholder_text='Insira um valor na árvore',width=180,  font=("", 12))
        self.entry_valor.pack(side=ctk.LEFT, pady=10)       
        btn_inserir = ctk.CTkButton(input_frame, text="Inserir", command=self.inserir_valor, font=("",14))
        btn_inserir.pack(side=ctk.LEFT,padx=10)
        ## botao remover nó
        btn_remover= ctk.CTkButton(input_frame, text="remover", command=self.remover_valor, font=("",14))
        btn_remover.pack(side=ctk.LEFT, padx=10)


        # Frame para exibição dos percursos
        percurso_frame = ctk.CTkFrame(self)
        percurso_frame.pack()


        self.txt_em_ordem = ctk.CTkTextbox(percurso_frame,fg_color='#292b31', width=450,height=100,wrap=ctk.WORD, font=("", 18))
        self.txt_em_ordem.pack(side=ctk.LEFT, padx=10, pady=10)
        
        
        self.txt_pre_ordem = ctk.CTkTextbox(percurso_frame,fg_color='#292b31', width=450, height=100, wrap=ctk.WORD,font=("", 18))
        self.txt_pre_ordem.pack(side=ctk.LEFT, padx=10,pady=10)
        
        self.txt_pos_ordem = ctk.CTkTextbox(percurso_frame,fg_color='#292b31', width=450, height=100, wrap=ctk.WORD,font=("", 18))
        self.txt_pos_ordem.pack(side=ctk.LEFT, padx=10,pady=10)
       

        
        self.draw_tree()

    def draw_tree(self):
        self.canvas.delete("all")  # Limpa o canvas antes de redesenhar
        if self.tree.root:
            self.draw_node(self.tree.root, self.canvas_width // 2, 50, self.canvas_width // 4)
        
        # Atualiza as áreas de texto dos percursos
        em_ordem = self.tree.em_ordem_erd()
        self.txt_em_ordem.delete("1.0", ctk.END)
        self.txt_em_ordem.insert(ctk.END, "Em Ordem (ERD):\n" + ", ".join(map(str, em_ordem)))

        pre_ordem = self.tree.pre_ordem()
        self.txt_pre_ordem.delete("1.0", ctk.END)
        self.txt_pre_ordem.insert(ctk.END, "Pré-Ordem:\n" + ", ".join(map(str, pre_ordem)))
        
        pos_ordem = self.tree.pos_ordem_edr()
        self.txt_pos_ordem.delete("1.0", ctk.END)
        self.txt_pos_ordem.insert(ctk.END, "Pós-Ordem (EDR):\n" + ", ".join(map(str, pos_ordem)))

        
    def draw_node(self, node, x, y, h_space):
        if node.left:
            x_left = x - h_space
            y_left = y + 20
            self.canvas.create_line(x, y, x_left, y_left, width=2)
            self.draw_node(node.left, x_left, y_left, h_space // 2)
        
        if node.right:
            x_right = x + h_space
            y_right = y + 100
            self.canvas.create_line(x, y, x_right, y_right, width=2)
            self.draw_node(node.right, x_right, y_right, h_space // 2)

             # Draw node
        radius = 20
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="lightblue")
        self.canvas.create_text(x, y, text=str(node.data), font=("Arial", 12))

    def inserir_valor(self):
        valor = self.entry_valor.get()
        if valor == '':
            print('Adiciona um elemento na lista')
            tkinter.messagebox.showwarning("Mensagem de Erro", "Adiciona um elemento na árvore")
            

        elif valor.isdigit():
            valor = int(valor)
            self.tree.inserir(valor)
            self.draw_tree()
            self.entry_valor.delete(0,"end")
        else:
            print("Valor inválido. Insira um número inteiro.")
    # remover nó
    def remover_valor(self):
        valor = self.entry_valor.get()  
        if valor == '':
            print('Adiciona um elemento na lista')
            tkinter.messagebox.showwarning("Mensagem de Erro", "Adiciona um elemento na caixa de texto")
            
        elif valor.isdigit():
            valor = int(valor)
            self.tree.remover(valor)
            self.draw_tree()
            self.entry_valor.delete(0,"end")


        else:
                print(f"O valor {valor} não foi encontrado na árvore.")
        #else:
        #    print("Valor inválido. Insira um núgitmero inteiro.")
    

        
        
      
def main():
    arvore = ArvoreBinariaBusca()
    root = ctk.CTk()
    app = TreeVisualizer(master=root, tree=arvore)
    app.pack(expand=True, fill=ctk.BOTH)
    root.mainloop()

if __name__ == "__main__":
    main()
