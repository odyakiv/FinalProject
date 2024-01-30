from tkinter import INSERT

from flask import Flask, render_template, request, flash,g
import sqlite3
app = Flask(__name__)


app = Flask(__name__)
app.config['DATABASE'] = 'products.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

def create_table():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS
                
items(
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        price INTEGER,
                        weight TEXT,
                        description TEXT,
                        lint TEXT,
                        category TEXT
                )
        ''')
        db.commit()

if __name__ == '__main__':
        create_table()







app = Flask(__name__)
items = [
    (1, "Гамбургер", 60, "96 г/g | 253 ккал/kcal", "Біфштекс із натуральної яловичини, цибуля, шматочок маринованого огірка, заправлені гірчицею і кетчупом, у запашній булочці з пшеничного борошна.", "https://mcdonaldsmenu.ru/image/cache/catalog/photo/764668645-gamburger-600x600.png","Бургер" ),
    (2, "Чізбургер", 72, "117 г/g | 298 ккал/kcal", "Біфштекс із натуральної яловичини, шматочок сиру “Чеддер”, шматочок маринованого огірка та цибуля, заправлені гірчицею і кетчупом, у булочці з пшеничного борошна.", "https://s7d1.scene7.com/is/image/mcdonalds/Best_CHEESEBURGER-1:product-header-desktop?wid=829&hei=455&dpr=off","Бургер"),
    (3, "Бігмак", 92, "229 г/g | 526 ккал/kcal", "Два біфштекси з натуральної яловичини, цибуля, маринований огірок, сир “Чеддер”, свіжий салат, заправлені спеціальним соусом, у булочці з насінням сезаму.", "https://s7d1.scene7.com/is/image/mcdonalds/Best_BIGMAC-1:product-header-desktop?wid=829&hei=455&dpr=off","Бургер"),
    (4, "Біг Тейсті", 154, "325 г/g | 790 ккал/kcal", "Натуральна яловичина у поєднанні зі свіжими овочами та плавленим сиром “Емменталь”.", "https://s7d1.scene7.com/is/image/mcdonalds/Best_BIG_TASTY-1:product-header-desktop?wid=829&hei=455&dpr=off","Бургер"),

    (5, "Кока-Кола мала", 35, "250 мл/ml | 102 ккал/kcal", "Всесвітньо відомий освіжаючий напій.", "https://s7d1.scene7.com/is/image/mcdonalds/Cola_250ml:product-header-desktop?wid=829&hei=455&dpr=off","Напої"),
    (6, "Фанта мала", 35, "250 мл/ml | 102 ккал/kcal", "Всесвітньо відомий освіжаючий напій.", "https://s7d1.scene7.com/is/image/mcdonalds/Fanta_250ml:product-header-desktop?wid=829&hei=455&dpr=off","Напої"),
    (7, "Спрайт малий", 35, "250 мл/ml | 102 ккал/kcal", "Всесвітньо відомий освіжаючий напій.", "https://s7d1.scene7.com/is/image/mcdonalds/Sprite_250ml:product-header-desktop?wid=829&hei=455&dpr=off","Напої"),
    (8, "Кава Лате класік", 48, "295 мл/ml | 130 ккал/kcal", "Лате – кавовий напій, який містить молоко. Особливістю цієї кави є те, що, на відміну від капучино, у лате молока значно більше.", "https://s7d1.scene7.com/is/image/mcdonalds/CoffeeLatteLarge:product-header-desktop?wid=830&hei=458&dpr=off","Напої"),
    (9, "Кава Капучино класік", 48, "245 мл/ml | 130 ккал/kcal245", "Капучино – це мікс еспресо та гарячого молока у рівних пропорціях. Особливістю цієї кави є смачна молочна пінка, яка утворюється завдяки поєднанню пари та молока.", "https://s7d1.scene7.com/is/image/mcdonalds/CoffeeCapuccinoLarge:product-header-desktop?wid=830&hei=458&dpr=off","Напої"),
    (10, "Чай чорний", 30, "300 мл/ml | 0 ккал/kcal", "Оригінальний чорний чай.", "https://s7d1.scene7.com/is/image/mcdonalds/TeaBlack:product-header-desktop?wid=829&hei=455&dpr=off"),

    (11, "Піца Франческо", 190, "490 г/g", "Основа томатна, моцарела, мисливські ковбаски, бекон, цибуля маринована, помідор, сир чедер, зелень, часниковий соус, орегано.", "https://images.deliveryhero.io/image/menus-glovo/products/8272943bec6e3b9244d361afcf26e67ae0f10c2c99327bbcc20904697aa31417?t=W3siYXV0byI6eyJxIjoibG93In19LHsicmVzaXplIjp7IndpZHRoIjo2MDB9fV0=","Піца"),
    (12, "Піца Барбекю", 225, "490 г/g", "Соус BBQ, мікс сирів, маринована цибуля, Печериці, огірок, Пепероні, Мисливські ковбаски, зелена цибуля, соус Світ Чилі.", "https://images.deliveryhero.io/image/menus-glovo/products/26be6872b00ab62886fdc50b59c9500305459a8f62280ebd1815639417447321?t=W3siYXV0byI6eyJxIjoibG93In19LHsicmVzaXplIjp7IndpZHRoIjo2MDB9fV0=","Піца"),
    (13, "Піца Чотири сири", 189, "490 г/g", "Cир Блю чіз, сир Гауда, сир Голландський, сир Моцарелла, вершковий соус.", "https://images.deliveryhero.io/image/menus-glovo/products/a9164a9b9cf59dbc6cbeea0be9b8023325d5ca331771f42cfd8a781b606d5a94?t=W3siYXV0byI6eyJxIjoibG93In19LHsicmVzaXplIjp7IndpZHRoIjo2MDB9fV0=","Піца"),
    (14, "Піца Карбонара", 179, "490 г/g", "30 см 490 грам Бекон, шинка, печериці, сир Моцарелла, маринована цибуля, оливки, соус вершковий.", "https://images.deliveryhero.io/image/menus-glovo/products/655a37c74c4aeaf3ff58c65b780e0220f42fd31e16a5940856bee8eb7e39a83a?t=W3siYXV0byI6eyJxIjoibG93In19LHsicmVzaXplIjp7IndpZHRoIjo2MDB9fV0=","Піца"),
    (15, "Піца Мисливська", 149, "490 г/g", "30 см 440 грам Мисливські ковбаски, салямі, солоний огірок, цибуля маринована, моцарелла, фірмовий соус. Для справжніх мисливців за смаком. Спробуй!.", "https://images.deliveryhero.io/image/menus-glovo/products/f9d3a48ca7e39297953b0f2efa5219cf34698ab067cff540fdf177b3473eb3ea?t=W3siYXV0byI6eyJxIjoibG93In19LHsicmVzaXplIjp7IndpZHRoIjo2MDB9fV0=","Піца"),

    (16, "Соус Баффало", 20, "40 г/g | 40 ккал/kcal", "Гострий соус із кисло-солодкими нотками, прянощами додасть характеру твоїм улюбленим стравам.", "https://s7d1.scene7.com/is/image/mcdonalds/New_Sauce_BUFFALO:product-header-desktop?wid=829&hei=455&dpr=off","Соус"),
    (17, "Соус Хабанеро", 20, "40 г/g | 120 ккал/kcal", "Пікантний перець Хабанеро, солодка паприка й прянощі.", "https://s7d1.scene7.com/is/image/mcdonalds/New_Sauce_BUFFALO:product-header-desktop?wid=829&hei=455&dpr=off","Соус"),
    (18, "Соус із сиром Дорблю", 20, "40 г/g | 100 ккал/kcal", "Ніжний соус із вишуканим вершковим смаком сиру Дорблю — ідеальне доповнення до хрумких снеків.", "https://s7d1.scene7.com/is/image/mcdonalds/New_Sauce_DOR_BLU:nutrition-calculator-tile","Соус"),
    (19, "Соус Барбекю", 15, "25 г/g | 38 ккал/kcal",  "https://s7d1.scene7.com/is/image/mcdonalds/SauceBBQ:product-header-desktop?wid=830&hei=458&dpr=off","Соус"),
    (20, "Кетчуп", 15, "28 г/g | 29 ккал/kcal",  "https://s7d1.scene7.com/is/image/mcdonalds/Ketchup:product-header-desktop?wid=830&hei=458&dpr=off","Соус"),
    (21, "Майонез", 15, "25 г/g | 119 ккал/kcal",  "https://s7d1.scene7.com/is/image/mcdonalds/Mayonnaise-2:nutrition-calculator-tile","Соус"),
    (22, "Соус Гірчичний", 15, "25 г/g | 55 ккал/kcal",  "https://s7d1.scene7.com/is/image/mcdonalds/Mustard:product-header-desktop?wid=830&hei=456&dpr=off","Соус"),

    (23, "Рол Філадельфія з лососем", 299, "400 г/g", "270 г Рис, лосось, крем сир, авокадо, огірок, норі", "https://images.deliveryhero.io/image/menus-glovo/products/3ce7954f9b437198db9ebeadf56d326b0be48382c76e59a9725e1c94ca25e8a3?t=W3siYXV0byI6eyJxIjoibG93In19LHsicmVzaXplIjp7IndpZHRoIjo2MDB9fV0=","Роли"),
    (24, "Рол Каліфорнія з крабовим", 249, "400 г/g", "230 г Рис, крабовий мікс, авокадо, огірок, ікра тобіко, норі.", "https://x100-venus-hub.gumlet.io/SKU/SUSHI-MASTER/%D0%9A%D0%B0%D0%BB%D1%96%D1%84%D0%BE%D1%80%D0%BD%D1%96%D1%97/BEFA2531-3068-11ED-ACA4-2DE1140535B7-1969%D1%851100_0029_%D0%9A%D0%B0%D0%BB%D0%B8%D1%84%D0%BE%D1%80%D0%BD%D0%B8%D1%8F-%D1%81-%D0%BA%D1%80%D0%B0%D0%B1%D0%BE%D0%B2%D1%8B%D0%BC-%D0%BC%D0%B8%D0%BA%D1%81%D0%BE%D0%BC-%D0%B2-%D0%B8%D0%BA%D1%80%D0%B5.png?w=1000&format=jpeg&mode=fit","Роли"),
    (25, "4 сири рол", 145, "245 г/g", "Рис, сир вершковий, сир Моцарелла, сир твердий, сир тостовий обпалений, бальзамічний соус.", "https://tita.com.ua/wp-content/uploads/2020/10/4-%D1%81%D0%B8%D1%80%D0%B8.jpg","Роли"),
    (26, "Чікен рол", 175, "265 г/g", "Рис, куряче філе, огірок, болгарський перець, сир вершковий, соус горіховий, кунжут, сухарі Панко.", "https://tita.com.ua/wp-content/uploads/2020/10/%D1%87%D1%96%D0%BA%D0%B5%D0%BD-%D1%80%D0%BE%D0%BE%D0%BB.jpg","Роли")

]


@app.route('/')
def food_street():
    return render_template('food_street.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/burger/<int:burger_id>')
def burger(burger_id):
    return render_template('burger.html', burger_id=burger_id)

@app.route('/drink/<int:drink_id>')
def drink(drink_id):
    return render_template('drink.html', drink_id=drink_id)

@app.route('/sous/<int:sous_id>')
def sous (sous_id):
    return render_template('sous.html', sous_id=sous_id)

@app.route('/pizza/<int:pizza_id>')
def pizza(pizza_id):
    return render_template('pizza.html', pizza_id=pizza_id)

@app.route('/roles/<int:roles_id>')
def roles(roles_id):
    return render_template('roles.html', roles_id=roles_id)


@app.route('/zakas/<int:zakas_id>')
def zakas(zakas_id):
    return render_template('zakas.html', zakas_id=zakas_id)

@app.route('/end/<int:end_id>')
def end(end_id):
    return render_template('end.html', end_id=end_id)

@app.route('/login/<int:login_id>')
def login(login_id):
    return render_template('login.html', login_id=login_id)

@app.route('/login2/<int:login2_id>')
def login2(login_id):
    return render_template('login2.html', login_id=login_id)


@app.route("/product/<item_id>")
def product_page(item_id):
    item = items[int(item_id)-1]
    return render_template("product.html", item=item)






app.run(debug=True)