from random import *
#일반유닛
class Unit:
    def __init__(self, name, hp, speed): #__init__ 생성자라는 부분임.
        #객체란 클래스로부터 만들어지는 요소
        self.name = name #이런것들을 멤버변수라고함
        self.hp = hp    #결국 멤버변수란 클래스 내에서 정의된것
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):

         print("{0} : {1} 방향으로 이동합니다 [속도 {2}]"\
                .format(self.name, location, self.speed))
    def dmged(self, dmg):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, dmg))
        self.hp -= dmg
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 마린1 = Unit("마린", 40, 5)
# 마린2 = Unit("마린", 40, 5)
# 탱크1 = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스",80,5)
# print("유닛 이름 : {0}, 공격력: {1}".format(wraith1.name,wraith1.dmg)) #외부에서도 쓸수있음
#
# #마인드컨트롤
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True #객체에 추가로 변수를 할당가능
#
# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

#메소드
#메소드 앞엔 다 self 를 붙여줘야함

class ATK_Unit(Unit): #괄호안의 class를 상속한다는 뜻
    def __init__(self, name, hp, speed, dmg): # 기본적으로 상속하려는 클래스의 함수가져오기
        Unit.__init__(self,name,hp,speed)
        self.dmg = dmg
    def attack(self,location): # 그럼 저기서 할당받은 self.name 의 값을 쓴다는것

        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location,self.dmg))

class marine(ATK_Unit):
    def __init__(self):
        ATK_Unit.__init__(self,"마린",40,1,5)

    def stimpack(self):
        if self.hp>10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))

        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

class tank(ATK_Unit):
    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        ATK_Unit.__init__(self,"탱크",150,1,35)
        self.seize_mode = False

    def set_seize_mode(self):
        if tank.seize_developed == False:
            return #기본 값

        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.dmg *= 2
            self.seize_mode = True #시즈모드가 아닐때 > 시즈모드
        #시즈모드일때 > 시즈 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.dmg /=2
            self.seize_mode = False




#공중 유닛
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    #비행능력
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class fly_ATK(ATK_Unit, flyable):
    def __init__(self, name, hp, dmg, flying_speed):
        ATK_Unit.__init__(self, name, hp, 0, dmg) #지상 스피드 0처리
        flyable.__init__(self, flying_speed)

    def move(self, location): #무브를 오버라이딩한다.

        self.fly(self.name, location)

class Wraith(fly_ATK):
    def __init__(self):
        fly_ATK.__init__(self,"레이스",80,20,5)
        self.clocked = False #클로킹이 해제상태

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked=False

        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

#실제게임 진행
game_start()

#마린 3기 생성
m1 = marine()
m2 = marine()
m3 = marine()
#탱크 2기 생성
t1 = tank()
t2 = tank()

#레이스 1기 생성
w1 = Wraith()

#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩 탱크 : 시즈모드 , 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, marine): #지금 만들어진 객체의 클래스를 확인하는 것
        unit.stimpack()
    elif isinstance(unit, tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

#전국 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.dmged(randint(5,21)) #공격은 랜덤으로받음

# 게임 종료
game_over()


#다중상속 unit 이 부모, atk_unit 이 지금 자식인데 부모가 여러명일수 있다라는것.
#공중유닛을 예로 들자. 일단 유닛이니까 unit 범주에 속한다.
#드랍쉽같은 수송기 > 공격은 불가

#결국
#fly_Atk 는 어텍유닛과 플라이어블 두개를 다중 상속 받은것.

#연산자 오버라이딩

#이 경우에는 지상 유닛과 공중유닛을 구별해야한다. 이걸 스킵하기 위해 오버라이딩 하는거.

#1. unit 에 move() 함수를 정의
#2. fly_ATK 에 move() 재정의
#3. 지상 공중 moe 따로

#건물

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self,name,hp,0)
#         super().__init__(name, hp, 0) #둘이 같지만 슈퍼통해서 이닛을 할때는
#                                             #셀프값 보내주지 않아도됨
#
#         self.location=location



# 서플라이 디폿 = 건물, 1개 건물 > 8 유닛 생성가능

##함수가 완성되지 않아도 스킵처리하는것 > pass


