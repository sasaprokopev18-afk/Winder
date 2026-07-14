import random
import time

class Player:
    def __init__(self):
        self.player_class = None
        self.level = 1
        self.exp = 0
        self.exp_next_level = 25
        self.hp = 0
        self.max_hp = 0
        self.physical_damage = 0
        self.magical_damage = 0
        self.coins = 0
        self.stats_bonus = {"phys": 0, "mag": 0, "hp": 0}

    def show_stats(self):
        print("\n--- СТАТИСТИКА ИГРОКА ---")
        print(f"Уровень: {self.level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Физ. урон: {self.physical_damage}")
        print(f"Маг. урон: {self.magical_damage}")
        print(f"Кошелек: {self.coins} монет")
        print("--------------------------\n")

# Инициализация игрока
p = Player()

def start_game():
    print("ОБУЧЕНИЕ: Перед вами Слизь (5 HP)!")
    # Имитация боя
    print("Вы победили слизь! Получено 1 EXP.")
    p.exp += 1
    
    print("\nВыберите оружие: [1] Деревянный меч (5 физ. урона) [2] Посох (6 маг. урона)")
    choice = input("Ваш выбор (1/2): ")
    
    print("\nВыберите класс: [1] Мечник (+20% урон, +5% хп) [2] Маг (+40% маг. урон) [3] Танк (+40% хп)")
    cls_choice = input("Ваш выбор (1/2/3): ")

    if cls_choice == '1':
        p.player_class = "мечник"
        p.hp = 10; p.max_hp = 10
        p.physical_damage = 5; p.magical_damage = 0
        p.stats_bonus["phys"] = 0.20; p.stats_bonus["hp"] = 0.05
    elif cls_choice == '2':
        p.player_class = "маг"
        p.hp = 5; p.max_hp = 5
        p.physical_damage = 0; p.magical_damage = 6
        p.stats_bonus["mag"] = 0.40
    elif cls_choice == '3':
        p.player_class = "танк"
        p.hp = 50; p.max_hp = 50
        p.physical_damage = 0; p.magical_damage = 0
        p.stats_bonus["hp"] = 0.40

    print("\nДобро пожаловать, дорогой приключенец!")
    main_menu()

def main_menu():
    while True:
        print("\n--- ГЛАВНОЕ МЕНЮ ---")
        print("[1] Статистика")
        print("[2] Подземелье")
        print("[3] Обмен монеток")
        print("[4] Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            p.show_stats()
            input("Нажмите Enter, чтобы вернуться...")
        elif choice == '2':
            dungeon_menu()
        elif choice == '3':
            exchange_system()
        elif choice == '4':
            break

def dungeon_menu():
    print("\n--- ПОДЗЕМЕЛЬЕ ---")
    print("[1] 1 уровень")
    if p.level >= 10:
        print("[2] 2 уровень")
    
    lvl = input("Выберите уровень: ")
    
    if lvl == '1':
        print("Вы входите в подземелье... Ждите 10 секунд...")
        time.sleep(10)
        run_event(1)
    elif lvl == '2' and p.level >= 10:
        run_event(2)
    else:
        print("Уровень недоступен!")

def run_event(level):
    roll = random.random() * 100
    
    if level == 1:
        if roll < 4: # Дракон
            print("ВЫ ВСТРЕТИЛИ БОССА: ДРАКОН!")
            battle("dragon")
        elif roll < 39: # Горилла
            print("Вы встретили Гориллу!")
            battle("gorilla")
        elif roll < 54: # Слизь
            print("Вы встретили Слизь!")
            battle("slime")
        elif roll < 69: # Сундук
            print("Вы нашли сундук!")
            p.coins += random.randint(15, 100)
        else:
            print("Здесь пусто...")
    
    elif level == 2:
        # Логика для 2 уровня (Гоблин, Гризли и т.д.)
        if roll < 2:
            print("Встречена Павшая Богиня!")
            battle("goddess")
        else:
            print("В подземелье 2 уровня вы никого не встретили...")

def battle(mob_type):
    # Упрощенная логика боя для примера
    if mob_type == "slime":
        print("Победа! +1 EXP, +монетки (шанс 15%)")
        p.exp += 1
        if random.random() < 0.15:
            coins = random.randint(15, 20)
            p.coins += coins
            print(f"Найдено монет: {coins}")
    # Добавьте остальные мобов по аналогии...

def exchange_system():
    print("\nПоложи свои монетки и получи рандомную стату!")
    try:
        amount = int(input("Сколько монет положить? (мин. 1000): "))
        if amount < 1000:
            print("Слишком мало!")
            return
        
        p.coins -= amount
        roll = random.random() * 100
        
        if roll < 45:
            val = random.randint(15, 35)
            p.physical_damage += val
            print(f"Вы получили Физ. урон +{val}!")
        elif roll < 94:
            val = random.randint(15, 35)
            p.magical_damage += val
            print(f"Вы получили Маг. силу +{val}!")
        else:
            val = random.randint(35, 70)
            p.max_hp += val
            p.hp += val
            print(f"Вы получили HP +{val}!")
            
    except ValueError:
        print("Введите число!")

# Запуск
start_game()
