import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Calculador de Horas Trabalhadas"
    page.scroll = "adaptive"

    # Criando os campos de texto
    entrada = ft.TextField(label="Entrada (ex: 07:00)", value="07:00")
    ini_almoço = ft.TextField(label="Saída Almoço (ex: 12:00)", value="12:00")
    fim_almoço = ft.TextField(label="Volta Almoço (ex: 14:00)", value="14:00")
    saida = ft.TextField(label="Saída Final (ex: 17:00)", value="17:00")
    
    resultado = ft.Text(size=25, weight="bold")

    def calcular_horas(e):
        try:
            # Converte as strings para o formato de hora
            fmt = "%H:%M"
            h1 = datetime.strptime(entrada.value, fmt)
            h2 = datetime.strptime(ini_almoço.value, fmt)
            h3 = datetime.strptime(fim_almoço.value, fmt)
            h4 = datetime.strptime(saida.value, fmt)

            # Cálculo: (Almoço - Entrada) + (Saída - Volta Almoço)
            turno_manha = h2 - h1
            turno_tarde = h4 - h3
            total_trabalhado = turno_manha + turno_tarde

            # Extraindo horas e minutos do total
            segundos = total_trabalhado.total_seconds()
            horas = int(segundos // 3600)
            minutos = int((segundos % 3600) // 60)

            resultado.value = f"Total: {horas} horas e {minutos} minutos"
            resultado.color = "green" # Usando string em vez de ft.colors para evitar erro
        except Exception as erro:
            resultado.value = "Formato inválido! Use HH:MM"
            resultado.color = "red"
        
        page.update()

    # Montando a tela
    page.add(
        ft.Text("Minha Jornada de Trabalho", size=30),
        entrada,
        ini_almoço,
        fim_almoço,
        saida,
        ft.ElevatedButton("Calcular Total", on_click=calcular_horas),
        ft.Divider(),
        resultado
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)