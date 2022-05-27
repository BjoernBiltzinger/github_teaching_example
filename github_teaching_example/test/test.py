from func import Student


def test_student():
    s1 = Student("Test", 10, 4)
    s1.passed()
    s1.birthday()
    assert s1._age == 11
    assert s1._schoolclass == 5
