from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def process_requests(): #Создаю общую функцию (не понял для чего, но так нужно)
    
    #Сразу определяю статус ошибок
    error_message1=None
    error_message2=None
    error_message3=None

    if request.method == 'POST':
        form_type = request.form.get('form_type', '')


        # Функция для решения первого ДЗ
        if form_type == "form1":
            temperatureF = request.form.get('temperatureF', "")
            if not temperatureF or not temperatureF.isdigit():
                error_message1 = "Введите числовое значение температуры по Фаренгейту"
            else:
                temperatureC = (int(temperatureF) - 32) * 5 / 9
                return render_template("form.html", temperatureC=int(temperatureC), error_message1=error_message1)


        # Функция для решения второго ДЗ
        elif form_type == "form2":
            money_usd = request.form.get('money_usd')
            if not money_usd or not money_usd.isdigit():
                error_message2 = "Введите числовое значение суммы в долларах"
            else:
                money_usd = int(money_usd)
                money_rub = money_usd * 70.38
                money_eur = money_rub / 100
                return render_template("form.html", money_eur=int(money_eur), error_message2=error_message2)


        # Функция для решения третьего ДЗ
        elif form_type == "form3":
            status_weather = (request.form.get("status_weather", "")).lower()
            if status_weather=="":
                error_message3 = "Введите состояние погоды"
            else:
                if status_weather=="солнечная":
                    recommendation  ="Возьми с собой очки.\nХорошего дня!"
                else:
                    recommendation  ="Возьми с собой зонт.\nХорошего дня!"
               
            
                return render_template("form.html", recommendation = recommendation, error_message3=error_message3)



    # Если это GET-запрос или неизвестный тип формы
    return render_template("form.html", error_message1=error_message1, error_message2=error_message2, error_message3=error_message3)

if __name__ == '__main__':
    app.run(debug=True)
