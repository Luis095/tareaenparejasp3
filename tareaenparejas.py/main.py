from binary_search_tree import BinarySearchTree

def main():
    # Crea una instancia de BinarySearchTree
    bst = BinarySearchTree()

    # Inserta valores en el árbol
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)

    # Busca un valor en el árbol
    print(bst.search(5))  # Debería imprimir True
    print(bst.search(4))  # Debería imprimir False

if __name__ == '__main__':
    main()
