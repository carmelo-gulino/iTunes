import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_album = None
        self.btn_crea_grafo = None
        self.txt_in_durata = None
        self.btn_analisi_comp = None
        self.btn_set_album = None
        self.txt_in_soglia = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Hello World", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW 1
        self.txt_in_durata = ft.TextField(label="Duarata")
        self.btn_crea_grafo = ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handle_crea_grafo)
        row1 = ft.Row([ft.Container(self.txt_in_durata, width=300),
                       ft.Container(self.btn_crea_grafo, width=300)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # ROW 2
        self.dd_album = ft.Dropdown(label="Album", on_change=self._controller.get_selected_album)
        self.btn_analisi_comp = ft.ElevatedButton(text="Analisi componente",
                                                  on_click=self._controller.handle_analisi_componente)
        row2 = ft.Row([ft.Container(self.dd_album, width=300),
                       ft.Container(self.btn_analisi_comp, width=300)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # ROW 3
        self.txt_in_soglia = ft.TextField(label="Soglia")
        self.btn_set_album = ft.ElevatedButton(text="Set di album", on_click=self._controller.handle_set_album)
        row3 = ft.Row([ft.Container(self.txt_in_soglia, width=300),
                       ft.Container(self.btn_set_album, width=300)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
