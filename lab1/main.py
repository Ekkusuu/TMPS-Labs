"""Run the lab1 creational patterns demo."""

from lab1.client import demo


def main():
    lib = demo()
    print("\nLibrary contents:")
    for b in lib.list_books():
        print(" -", b)


if __name__ == "__main__":
    main()
