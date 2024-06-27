import tkinter as tk
from tkinter import ttk

class BookRatingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Minhas Leituras e Avaliações")

        self.book_ratings = {}  # Dicionário para armazenar as avaliações dos livros

        # Cria as abas
        self.tab_control = ttk.Notebook(self.root)
        self.tab_books = ttk.Frame(self.tab_control)
        self.tab_opinions = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_books, text="Livros Lidos")
        self.tab_control.add(self.tab_opinions, text="Opiniões")

        self.tab_control.pack(expand=1, fill="both")

        # Aba "Livros Lidos"
        self.create_books_tab()

        # Aba "Opiniões"
        self.create_opinions_tab()

    def create_books_tab(self):
        self.books_listbox = tk.Listbox(self.tab_books)
        self.books_listbox.pack()

        self.add_book_entry = tk.Entry(self.tab_books)
        self.add_book_entry.pack()

        self.add_book_button = tk.Button(self.tab_books, text="Adicionar Livro", command=self.add_book)
        self.add_book_button.pack()

        self.rating_scale = tk.Scale(self.tab_books, from_=0, to=5, orient="horizontal", label="Avaliação")
        self.rating_scale.pack()

        self.rate_button = tk.Button(self.tab_books, text="Atribuir Nota", command=self.rate_book)
        self.rate_button.pack()

    def create_opinions_tab(self):
        self.opinions_text = tk.Text(self.tab_opinions)
        self.opinions_text.pack()

    def add_book(self):
        book_name = self.add_book_entry.get()
        if book_name:
            self.books_listbox.insert(tk.END, book_name)
            self.book_ratings[book_name] = -1  # Inicialmente, sem classificação
            self.add_book_entry.delete(0, tk.END)

    def rate_book(self):
        selected_book = self.books_listbox.get(tk.ACTIVE)
        if selected_book:
            rating = self.rating_scale.get()
            self.book_ratings[selected_book] = rating
            self.rating_scale.set(0)  # Resseta a escala para 0
            print(f"Avaliação para {selected_book}: {rating} / 5")

    def update_opinions_tab(self):
        opinions_text = ""
        for book, rating in self.book_ratings.items():
            opinions_text += f"{book}: {rating if rating != -1 else 'Sem avaliação'} / 5\n"
        self.opinions_text.delete("1.0", tk.END)  # Limpa o texto anterior
        self.opinions_text.insert(tk.END, opinions_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookRatingApp(root)
    root.mainloop()