import travel.thailand  # 조건 1 . 쓰려는 프로젝트가 같은 파일에 묶여있어야한다.
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# from travel import vietnam
# trip_t0 = vietnam.vietnamPackage()
# trip_t0.detail()

from travel import * # __init__ 파일에 공개범위를 설정해줘야한다.
trip_t0 = vietnam.vietnamPackage()
trip_t0.detail()

# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect #경로 찾기
from travel import *
print(inspect.getfile(thailand))

