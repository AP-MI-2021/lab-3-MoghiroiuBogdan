def citire_lista():
    l = []
    givenString = input("dati lista=")
    numberAsString = givenString.split(",")

    for x in (numberAsString):
        l.append(int(x))
    return l


def alternate_signs(l):
    '''
    verifica daca nr dntr o lista au semne alternante
    :param l: lista formata din nr intregi
    :return: true sau false
    '''
    if l[0] > 0:
        ok = 1
    else:
        ok = 0

    for i in l[1:len(l)]:
        if ok == 1 and i > 0:
            return False
        if ok == 0 and i < 0:
            return False
        if i > 0:
            ok = 1
        else:
            ok = 0
    return True

def get_longest_alternating_signs(l):
    '''
    deter cea mai lunga subsecventa cu prorpietatea ca nr au semne alternante
    :param l: lista
    :return: subsecventa maxima
    '''
    subsMax = []

    for i in range(len(l)):
        for j in range(i, len(l)):
            if alternate_signs(l[i:j + 1]) and len(l[i:j + 1]) > len(subsMax):
                subsMax = l[i:j + 1]

    return subsMax


def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([1, -3, 5, 6, 7]) == [1, -3, 5]
    assert get_longest_alternating_signs([-4, 3, -67, 4, -1, -7]) == [-4, 3, -67, 4, -1]


def all_nr_are_prime(n):
    '''
    verifica daca nr dintr o lista sunt numere formate din cifre prime
    :param n:lista cu numere
    :return:true sau false
    '''
    for x in n:
        cop = x
        while cop != 0:
            b = cop % 10
            if b == 1 or b == 4 or b == 6 or b == 8 or b == 9:
                return False

            cop = cop // 10
    return True


def get_longest_prime_digits(lst):
    '''
    deter cea mai lunga subsecventa cu prorpietatea ca nr sunt formate din cifre prime
    :param lst: lista
    :return: subsecventa maxima
    '''
    subsecvMax = []

    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if all_nr_are_prime(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecvMax):
                subsecvMax = lst[i:j + 1]

    return subsecvMax


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([2, 3, 55, 4, 7, 11]) == [2, 3, 55]
    assert get_longest_prime_digits([4, 6, 7, 23]) == [7, 23]


def main():
    l = []
    test_get_longest_prime_digits()
    test_get_longest_alternating_signs()
    while True:
        print("1.Citire date:")
        print("2.cea mai lunga subsecventa cu proprietatea ca nr au semne alternante")
        print("3.cea mai lunga subsecventa cu proprietatea ca nr au toate cifrele prime")
        print("4.iesire")
        option = input("dati nr:")

        if option == "1":
            l = citire_lista()

        elif option == "2":
            print(get_longest_alternating_signs(l))

        elif option == "3":
            print(get_longest_prime_digits(l))

        elif option == "4":
            break

        else:
            print("optiune gresita")


if __name__ == '__main__':
    main()
