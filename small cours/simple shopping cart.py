import tkinter as tk


class SimpleShoppingCart(tk.Tk):

    def __init__(self):
        super().__init__()
        self.lst_market = ['car', 'turtle', 'house', 'pupok', 'lobok', 'babina', 'stamina', 'konina', 'r9bina']
        self.title('shopping cart')
        self.geometry('640x480')
        self.iconphoto(False, tk.PhotoImage(file='img/shopping-cart.png'))

        self.market_list_frame = tk.LabelFrame(text='market')
        self.market_options_frame = tk.LabelFrame(text='options')
        self.user_cart_frame = tk.LabelFrame(text='cart')
        self.market_box = tk.Listbox(self.market_list_frame, selectmode=tk.EXTENDED)
        self.user_cart_box = tk.Listbox(self.user_cart_frame, selectmode=tk.EXTENDED)
        self.btn_add_to_card = tk.Button(self.market_options_frame, text='add to card', command=self.add_to_card)
        self.btn_remove_from_card = tk.Button(self.market_options_frame, text='remove from card',
                                              command=self.del_from_card)
        self.scroll_market = tk.Scrollbar(self.market_list_frame, command=self.market_box.yview)
        self.scroll_cart = tk.Scrollbar(self.user_cart_frame, command=self.user_cart_box.yview)

        self.market_list_frame.pack(side='left', anchor='n')
        self.market_options_frame.pack(side='left', anchor='n')
        self.user_cart_frame.pack(side='left', anchor='n')
        self.market_box.pack(side='left')
        self.scroll_market.pack(side='left', fill='y')
        self.user_cart_box.pack(side='left')
        self.scroll_cart.pack(side='left', fill='y')
        self.btn_add_to_card.pack(fill='x')
        self.btn_remove_from_card.pack(fill='x')
        for item in self.lst_market:
            self.market_box.insert(tk.END, item)

    def add_to_card(self):
        for item_index in self.market_box.curselection():
            self.user_cart_box.insert(tk.END, self.lst_market[item_index])

    def del_from_card(self):
        selected_items = list(self.user_cart_box.curselection())
        self.user_cart_box.delete(selected_items[0], selected_items[-1])


if __name__ == '__main__':
    root = SimpleShoppingCart()
    root.mainloop()
