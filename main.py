from libscan import Explorer
from libscan.renderers.graphviz_renderer import GraphvizRenderer


def main():
    explorer = Explorer()

    for mod in ["libscan", "math", "random", "pathlib"]:
        tree = explorer.scan(mod, max_depth=4)
        renderer = GraphvizRenderer()
        output = renderer.render(tree, f"output/{mod}_tree", format="svg")

        print("Generated:", output)


if __name__ == "__main__":
    main()