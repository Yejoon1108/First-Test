class Champions:
    def __init__(self,name,hp,mp,spd,dmg):
        self.name=name
        self.hp=hp
        self.mp=mp
        self.spd=spd
        self.dmg=dmg
        print("{0} 를 선택하셨습니다.\n"
              "체력 : {1}\n"
              "마나 : {2}\n"
              "이동속도 : {3}\n"
              "공격력 : {4}\n".format(self.name,self.hp,self.mp,self.spd,self.dmg))
    def move(self,location):
        print("{0}의 속도로 {1}의 방향으로 이동 중.".format(self.spd,location))

    def kill(self,target):
        self.hp+=100
        print("{0}을 처치하여 {1}의 체력이 100 증가하였습니다. 현재체력 : {2}".format(target,self.name,self.hp))

초가스 = Champions("초가스",4000,2350,325,100)
초가스.move("3시")
초가스.kill("오공")