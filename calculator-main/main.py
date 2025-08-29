#Импорт
from flask import Flask, render_template, request
import os
app = Flask(__name__)
# Настроим путь (должен быть полный) для сохранения файлов
UPLOAD_FOLDER = 'C:/Users/Admin/Desktop/John/calculator-main/static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def result_calculate(size, lights, device):
    #Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')
#Вторая страница
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

#Третья страница
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

#Расчет
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
#Форма
@app.route('/form')
def form():
    return render_template('form.html')

#Результаты формы
@app.route('/submit', methods=['POST'])
def submit_form():
    #Создай переменные для сбора информации
    name = request.form['name']
    address = request.form['address']
    email = request.form['email']
    date = request.form['date']
    myfile = request.files['myfile']
    # Здесь сохраняется файл в путь, сложенный из пути папки img и названия изображения
    img_adress = myfile.filename
    myfile.save(os.path.join(app.config['UPLOAD_FOLDER'], myfile.filename))
    # Здесь вы можете сохранить данные или отправить их по электронной почте
    return render_template('form_result.html', 
                           #Помести переменные
                           name=name,
                           address=address,
                           email=email,
                           date=date,
                           img_adress = img_adress
                           )

app.run(debug=True)