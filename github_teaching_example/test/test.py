from func import Student


def test_student():
    s1 = Student("Test", 10, 4)
    s1.passed()
    assert s1._age == 10
    assert s1._schoolclass == 5
