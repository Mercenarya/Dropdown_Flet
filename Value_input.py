import flet as ft

def main(page: ft.Page):
    VALUE = ft.TextField(label="Total value",value=0)
    INCOME = ft.TextField(label="Income",value=0)
    def customize(e):
       if CUSTOM_PRICE.value == "VND":
           Value_Convert_2
       elif CUSTOM_PRICE.value == "US Dollar":
           Value_Convert
       page.update()
    CUSTOM_PRICE = ft.Dropdown(
       on_change=customize,
       options=[
           ft.dropdown.Option("US Dollar"),
           ft.dropdown.Option("VND"),
       ],
       width=200,
      
   )
    Dollar_value = 0.000040
    Value_update = ft.Text("0.0"+"$",size=40,color="lightGreen")
    Income_update = ft.Text("0.0"+"$", size=40, color="lightGreen")
    Custom_price = ft.Text(size=40)
    
    total_value_result = ft.Text("0.0"+"$",size=40,color="lightGreen")
    def Value_Convert(e):
       Value_update.value = str(round(int(VALUE.value)*Dollar_value,1))+"$"
       Income_update.value = str(round(int(INCOME.value)*Dollar_value,1))+"$"
       total_value = round((int(INCOME.value)+int(VALUE.value))*Dollar_value,1)
       total_value_result.value = str(total_value)+"$"
       Custom_price.value = f"{CUSTOM_PRICE.value}",
       page.update()
    def Value_Convert_2(e):
       Value_update.value = str(round(int(VALUE.value)))+"VND"
       Income_update.value = str(round(int(INCOME.value))) + "VND"
       total_value = round((int(INCOME.value)+int(VALUE.value)))
       total_value_result.value = str(total_value)+"VND"
       Custom_price.value = f"{CUSTOM_PRICE.value}"
       page.update()
            
    def Close_dlg(e):
        Input_Form.open = False
        page.update()
    def Open_dlg(e):
       page.dialog = Input_Form
       Input_Form.open = True
       page.update()
    Input_Form = ft.AlertDialog(
       modal=True,
       title=ft.Text("FMDA"),
       content=ft.Column(
           controls=[
                VALUE,
                INCOME,
           ],
           height=500,
       ),
       actions=[
           ft.TextButton("Confirm",on_click=Value_Convert),
           ft.TextButton("Cancel",on_click=Close_dlg)
       ]
   )
    view = ft.Column(
        controls=[
            ft.ElevatedButton("Add",on_click=Open_dlg),
            CUSTOM_PRICE,
            ft.Text("Reserves"),
            Value_update,
            ft.Text("Income"),
            Income_update,
            ft.Text("Total"),
            total_value_result
        ]
    )
    page.add(view)
    page.update()
ft.app(target = main)