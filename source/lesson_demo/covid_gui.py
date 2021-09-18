import tkinter as tk
from tkinter import ttk
from covid import Covid


class CovidGUI:
    list_countries = {
            0: 'Chọn một quốc gia',
            1: 'Vietnam',
            2: 'Australia',
            3: 'Italy',
            4: 'Russia',
            5: 'United Kingdom',
            6: 'US',
            7: 'Japan',
            8: 'India',
            9: 'Laos'
        }

    def __init__(self, covid):
        self.covid = covid

        window = tk.Tk()  # Khởi tạo window Tk
        window.title("Số liệu ca lây nhiễm Covid")
        window.geometry("800x250")
        window.resizable(0, 0)
        window.rowconfigure(0, minsize=50, weight=1)  # Cấu hình cho row và column
        window.rowconfigure(1, minsize=200, weight=1)
        window.columnconfigure(0, minsize=600, weight=1)

        font_01 = ("Courier", 13, "bold")
        font_02 = ("Courier", 12, "bold")

        frm_top = tk.Frame(window)  # Khởi tạo Frame, trong window được phân tách thành nhiều Frame khác nhau để quản lý
        frm_top.grid(column=0, row=0)
        combo_country = ttk.Combobox(frm_top, values=list(self.list_countries.values()), font=font_01)
        combo_country.grid(column=0, row=0, padx=10, pady=10)
        combo_country.current(0)
        # bind() để bắt và xử lý sự kiện thay đổi giá trị của Combobox
        combo_country.bind("<<ComboboxSelected>>", self.change_combo_selected)

        frm_bot = tk.Frame(window)
        frm_bot.grid(column=0, row=1)
        frm_bot_world = tk.Frame(frm_bot)
        frm_bot_world.grid(column=0, row=0, padx=5, pady=5)
        frm_bot_world.rowconfigure([0, 1, 2, 3], minsize=30)
        frm_bot_world.columnconfigure(0, minsize=100)
        frm_bot_world.columnconfigure(1, minsize=200)

        frm_bot_country = tk.Frame(frm_bot)
        frm_bot_country.grid(column=1, row=0, padx=5, pady=5)
        frm_bot_country.rowconfigure([0, 1, 2, 3], minsize=30)
        frm_bot_country.columnconfigure(0, minsize=100)
        frm_bot_country.columnconfigure(1, minsize=200)

        lb_world = tk.Label(frm_bot_world, text="Thế giới", foreground="blue", font=font_01)
        lb_world.grid(column=0, row=0, sticky="nw")

        lb_total = tk.Label(frm_bot_world, text="Tổng số ca:")
        lb_total.grid(column=0, row=1, sticky='e')
        et_total = tk.Entry(frm_bot_world, width=20, justify='right', font=font_02)
        et_total.grid(column=1, row=1)
        et_total.insert(0, f'{self.covid.get_total_confirmed_cases()}')

        lb_recover = tk.Label(frm_bot_world, text="Phục hồi:")
        lb_recover.grid(column=0, row=2, sticky='e')
        et_recover = tk.Entry(frm_bot_world, width=20, justify='right', font=font_02)
        et_recover.grid(column=1, row=2)
        et_recover.insert(5, f'{self.covid.get_total_recovered()}')

        lb_active = tk.Label(frm_bot_world, text="Đang điều trị:")
        lb_active.grid(column=0, row=3, sticky='e')
        et_active = tk.Entry(frm_bot_world, width=20, justify='right', font=font_02)
        et_active.grid(column=1, row=3)
        et_active.insert(5, f'{self.covid.get_total_active_cases()}')

        lb_death = tk.Label(frm_bot_world, text="Tử vong:")
        lb_death.grid(column=0, row=4, sticky='e')
        et_death = tk.Entry(frm_bot_world, width=20, justify='right', font=font_02, foreground='red')
        et_death.grid(column=1, row=4)
        et_death.insert(5, f'{self.covid.get_total_deaths()}')

        self.lb_country = tk.Label(frm_bot_country, text="Chưa chọn quốc gia!", foreground="blue", font=font_01)
        self.lb_country.config(width=19)
        self.lb_country.grid(column=0, row=0, sticky="nw")

        lb_total_c = tk.Label(frm_bot_country, text="Tổng số ca:")
        lb_total_c.grid(column=0, row=1, sticky='e')
        self.et_total_c = tk.Entry(frm_bot_country, width=20, justify='right', font=font_02)
        self.et_total_c.grid(column=1, row=1)

        lb_recover_c = tk.Label(frm_bot_country, text="Phục hồi:")
        lb_recover_c.grid(column=0, row=2, sticky='e')
        self.et_recover_c = tk.Entry(frm_bot_country, width=20, justify='right', font=font_02)
        self.et_recover_c.grid(column=1, row=2)

        lb_active_c = tk.Label(frm_bot_country, text="Đang điều trị:")
        lb_active_c.grid(column=0, row=3, sticky='e')
        self.et_active_c = tk.Entry(frm_bot_country, width=20, justify='right', font=font_02)
        self.et_active_c.grid(column=1, row=3)

        lb_death_c = tk.Label(frm_bot_country, text="Tử vong:")
        lb_death_c.grid(column=0, row=4, sticky='e')
        self.et_death_c = tk.Entry(frm_bot_country, width=20, justify='right', font=font_02, foreground='red')
        self.et_death_c.grid(column=1, row=4)

        window.mainloop()

    def change_combo_selected(self, event):
        combo = event.widget
        self.et_total_c.delete(0, tk.END)
        self.et_recover_c.delete(0, tk.END)
        self.et_active_c.delete(0, tk.END)
        self.et_death_c.delete(0, tk.END)
        if combo.current() == 0:
            self.lb_country['text'] = 'Chưa chọn quốc gia!'
        else:
            country_name = combo.get()
            self.lb_country['text'] = country_name
            country_data = self.covid.get_status_by_country_name(country_name.lower())
            self.et_total_c.insert(0, f"{country_data['confirmed']}")
            self.et_recover_c.insert(0, f"{country_data['recovered']}")
            self.et_active_c.insert(0, f"{country_data['active']}")
            self.et_death_c.insert(0, f"{country_data['deaths']}")


if __name__ == "__main__":
    covid = Covid()
    covid_gui = CovidGUI(covid)

