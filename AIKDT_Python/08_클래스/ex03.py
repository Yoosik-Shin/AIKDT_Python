# 인스턴스 변수, 메소드
# 클래스 변수, 메소드

class Student:
    # 인스턴스 변수
    # name = ''
    # age = 0
    # tel = ''
    # 클래스 변수 : 객체간의 공유할 값으로 사용하는 변수
    count = 0
    student_list = []

    # 인스턴스 변수 접근 : self.변수
    # 클래스 변수 접근 : 클래스.변수

    def __init__(self, no, name, major):
      self.no = no
      self.name = name
      self.major = major
      Student.count += 1
      Student.student_list.append(self)

    # 매직 메소드
    # : 특수한 이름의 메소드, __(이름)__ 형태의 메소드
    # * 미리 정의된 이름이며, 특수한 상황에서 호출되도록 정의되어 있다.
    # __init__            : 생성자
    # __del__             : 소멸자
    # __str__             : 객체를 출력할 때 호출되는 메소드 ≒ toString?
    # __eq__              : 인스턴스가 같은지 비교하는 메소드 equals
    # __ne__              : 인스턴스가 다른지 비교하는 메소드 negative

    def __str__(self):
      return '{} / {} / {}'.format(self.no, self.name, self.major)


    # 클래스 메소드
    # @이름     : 데코레이터
    #           - 해당 클래스나 메소드의 기능/용도를 명시하는 역할

    # 클래스 메소드
    # @classmathod : 해당 메소드를 클래스 메소드로 명시
    # 클래스 메소드의 첫번째 매개변수로 클래스(cls)를 받아온다.
    # 인스턴스 메소드의 첫번째 매개변수로 인스턴스(self)를 받아온다.

    @classmethod
    def show_info(cls):
      for student in cls.student_list:
        print(str(student))


# -------------------------------------------------------------------

s1 = Student('김조은', 20, '010-1111-2222')
s2 = Student('박조은', 30, '010-2222-3333')
s3 = Student('황조은', 40, '010-3333-4444')

# 클래스 변수
print('{} 명의 학생이 참여하였습니다.'.format(Student.count))
print(s1.count)
print(s2.count)
print(s3.count)

# 클래스 메소드
Student.show_info()