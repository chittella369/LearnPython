class employee:
    def __init__(self, name, sal,dept):
        self.__name=name  # private attribute
        self.__salary=sal # private attribute

        self.__department=dept



e = employee("Bill",1000,"Physics")
e.__salary
