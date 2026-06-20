from libscan import Explorer


def print_tree(node, indent=0):
    print("    " * indent + f"{node.kind.name}: {node.name}")

    for child in node.children:
        print_tree(child, indent + 1)


def main():
    explorer = Explorer()

    tree = explorer.scan("math")

    print_tree(tree)


if __name__ == "__main__":
    main()