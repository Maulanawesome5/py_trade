class Hero:
    __jumlah = 0

    def __init__(self, name: str, health: float, attPower: float, armor: float):
        # Inisialisasi nilai
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        # Update nilai
        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax
        Hero.__jumlah += 1

    @property
    def info(self):
        return f"Lv. {self.__level} {self.__name}" +\
            f"\nHP: {self.__health}/{self.__healthMax} | EXP: {self.__exp} " +\
            f"| AP: {self.__attPower} | DP: {self.__armor}"

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, val):
        self.__exp += val
        if self.__exp >= 100:
            print(f"{self.__name} level up!")
            self.__level += 1
            self.__exp -= 100
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self, enemy):
        self.gainExp = 50


melisa = Hero("Melisa", 100, 5, 10)
mirana = Hero("Mirana", 100, 7, 8)

for i in range(10):
    melisa.attack(mirana)
    mirana.attack(melisa)

print(melisa.info)
print(mirana.info)
