 # Lab 1 — Creational Design Patterns



## Implemented patterns

- **Singleton** — `LibrarySingleton` ensures a single shared library instance used by the demo.
- **Factory Method** — `BookFactory.create_book(...)` returns different concrete `Book` types (`Ebook`, `PaperBook`) based on a simple kind string.
- **Builder** — `BookBuilder` lets the client construct a `Book` in steps (fluent API).
- **Prototype** — `Book.clone()` (uses `copy.deepcopy`) to duplicate book instances.

Each pattern is deliberately implemented in a compact, idiomatic way so the code is easy to read and extend.

## Domain & models

Core entity: Book

- `Book` (base)
	- attributes: `title: str`, `author: str`, `pages: int`
	- methods: `clone()` — returns a deep copy (Prototype)

- `Ebook(Book)`
	- extra: `file_format: str` (e.g. `epub`, `pdf`)

- `PaperBook(Book)`
	- extra: `hardcover: bool`

Simple class diagram (informal)

```
Book <|-- Ebook
Book <|-- PaperBook

Book: title, author, pages
Ebook: file_format
PaperBook: hardcover
```

## Files and responsibilities

| Path | Purpose |
|---|---|
| `lab1/models/book.py` | Domain models: `Book`, `Ebook`, `PaperBook` (+ `clone()` for Prototype) |
| `lab1/factory/book_factory.py` | Factory Method: create `Ebook` / `PaperBook` from a kind/params |
| `lab1/builder/book_builder.py` | `BookBuilder` fluent builder for incremental construction |
| `lab1/domain/library_singleton.py` | `LibrarySingleton` — single shared container for demo entries |
| `lab1/client.py` | Demo scenario wiring patterns together (Factory, Builder, Prototype) |
| `lab1/main.py` | Runner that executes the demo and prints the library contents |

The implementation intentionally keeps modules small and focused to make the patterns stand out.

## How to run

From the project root (macOS / zsh):

```bash
python3 -m lab1.main
```

or directly:

```bash
python3 lab1/main.py
```

The demo does the following in `lab1/client.py`:

1. Clears the singleton library.
2. Creates books using the Factory Method (`Ebook`, `PaperBook`).
3. Builds a `Book` via the Builder.
4. Clones an existing `Ebook` via Prototype and tweaks the title.
5. Adds all items to the `LibrarySingleton` and returns it for inspection.

## Example output

```
Library contents:
 - Ebook(title='Factory Patterns in Py', author='A. Dev', pages=120, format='pdf')
 - PaperBook(title='Understanding Patterns', author='B. Coder', pages=350, hardcover=True)
 - Book(title='Built Book', author='Builder Author', pages=200)
 - Ebook(title='Factory Patterns in Py (clone)', author='A. Dev', pages=120, format='pdf')
```

## Design notes and rationale

- Simplicity first: the project uses small, single-purpose modules so each pattern's code is easy to locate and understand.
- Prototype uses `copy.deepcopy` which is sufficient for this small domain. If domain objects hold external resources (files, sockets), implement a custom `clone()` that copies only safe attributes.
- The `BookBuilder` returns a plain `Book` by default. If you need complex variants, consider adding `EbookBuilder`/`PaperBookBuilder` or a `BookDirector` that selects a builder based on requirements.
- The Factory Method is intentionally minimal (string-based). In larger systems prefer enums or explicit factory classes for type-safety and discoverability.



