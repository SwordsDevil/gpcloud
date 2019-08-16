#object mutul
#2019/08/15
import random

class Player:
    BUFF = random.randint(0, 100)
    def __init__(self,blood,attack,energy,depletion):
        self.blood = blood
        self.attack = attack
        self.energy = energy
        self.depletion = depletion

    def attackOpera(self,instance):
        instance.blood -= self.attack +self.BUFF
        self.energy -= self.depletion

    def getInfo(self):
        print('''player's info
        blood:{}
        energy:{}'''.format(self.blood,self.energy))

class Monster:
    BUFF = random.randint(0, 100)
    def __init__(self,blood,attack,equipment):
        self.blood = blood
        self.attack = attack
        self.equipment = equipment

    def attackOpera(self,instance):
        instance.blood -= self.attack + self.BUFF

    def getInfo(self):
        print('''monster's info
        blood:{}'''.format(self.blood))

    def getEquip(self):
        ZB = self.equipment[random.randint(0,len(self.equipment)-1)]
        return ZB

player = Player(blood=3000,attack=280,energy=200,depletion=5)
monster = Monster(blood=7500,attack=200,equipment=['青龙偃月刀','方天画戟','金箍棒','倚天剑'])
for i in range(30):
    player.attackOpera(monster)
    if random.randint(0,9) % 2 == 0:
        monster.attackOpera(player)
    if monster.blood <= 0 and player.blood > 0:
        print('player is alive:{}'.format(player.blood))
        print(monster.getEquip())
        break
    elif player.blood <0 and monster.blood>0:
        print('monster is alive:{}'.format(monster.blood))
        print('you dead!!')
        break
    elif player.blood <0 and monster.blood <0:
        print('player is dead:{}'.format(player.blood))
        print('monster is dead:{}'.format(monster.blood))
        print('player and monster perish together')
        break
else:
    if monster.blood > 0:
        print('player is alive:{}'.format(player.blood))
        print('monster is alive:{}'.format(monster.blood))
        print('you failed!!')
