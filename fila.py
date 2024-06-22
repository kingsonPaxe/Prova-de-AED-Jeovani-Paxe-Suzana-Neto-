class fila:
    def __init__(self):
        self.data = []


    def isEmpty(self):
        return self.data == []
    
    def size(self):
        print(len(self.data))
        return len(self.data)
        
    # Enfileirar(Equeue)...

    def push(self, valor):
        self.data.append(valor)
    
    # Desenfilerar (Dequeue)...

    def pop(self):
        self.data.pop(0)

    

if __name__ == '__main__':

    f = fila()
    f.push(10)
    f.push(20)
    f.push(30)
    f.push(30)


    print(f.data)
    f.pop()
    print(f.data)
    print(f.size())
    print(f.isEmpty())