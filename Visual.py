import tkinter as tk
import selen

datas = {
}


class CarApp(tk.Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        
        super().__init__(className='imex-service')
        self.c = tk.Canvas(self ,background=self.get_rgb((50,50,50)) )
        self.c.pack()
        self.label_inn = tk.Label(self, text='ИНН')
        self.inn = tk.Entry(self, bg='white', fg='black')
        self.label_surname = tk.Label(self, text='Фамилия')
        self.surname = tk.Entry(self, bg='white', fg='black')
        self.label_name = tk.Label(self, text='Имя')
        self.name = tk.Entry(self, bg='white', fg='black')
        self.label_number_phone = tk.Label(self, text='Номер телефона')
        self.number_phone = tk.Entry(self, bg='white', fg='black')
        self.label_brand = tk.Label(self, text='Марка')
        self.brand = tk.Entry(self, bg='white', fg='black')
        self.label_model = tk.Label(self, text='Модель')
        self.model = tk.Entry(self, bg='white', fg='black')
        self.label_color = tk.Label(self, text='Цвет')
        self.color = tk.Entry(self, bg='white', fg='black')
        self.label_gos_number = tk.Label(self, text='Гос. номер')
        self.gos_number = tk.Entry(self, bg='white', fg='black')

        self.btn = tk.Button(text='Начать', command=self.saved_data)


        self.label_inn.pack()
        self.inn.pack()
        self.label_surname.pack()
        self.surname.pack()
        self.label_name.pack()
        self.name.pack()
        self.label_number_phone.pack()
        self.number_phone.pack()
        self.label_brand.pack()
        self.brand.pack()
        self.label_model.pack()
        self.model.pack()
        self.label_color.pack()
        self.color.pack()
        self.label_gos_number.pack()
        self.gos_number.pack()
        self.btn.pack()

    @classmethod
    def get_rgb(cls, rgb):
        return "#%02x%02x%02x" % rgb 


    def saved_data(self):
        datas['inn'] = self.inn.get()
        datas['surname'] = self.surname.get()
        datas['name'] = self.name.get()
        datas['number_phone'] = self.number_phone.get()
        datas['brand'] = self.brand.get()
        datas['model'] = self.model.get()
        datas['color'] = self.color.get()
        datas['gos_number'] = self.gos_number.get()
        selen.main(datas['inn'], datas['surname'], datas['name'], datas['number_phone'], datas['brand'], datas['model'], datas['color'], datas['gos_number'])
        self.close()

    def close(self):
        self.quit()
        
    

if __name__ == '__main__':
        app = CarApp()
        app.mainloop()
        
