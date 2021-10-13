def citire_lista():
    l = []
    givenString = input("dati lista=")
    numberAsString = givenString.split(",")

    for x in (numberAsString):
        l.append(float(x))
    return l


def alternate_signs(l):
    '''
    verifica daca nr dntr o lista au semne alternante
    :param l: lista formata din nr intregi
    :return: true sau false
    '''

    for i in range(1, len(l)):
        if l[i] * l[i-1] > 0:
            return False
    return True


def get_longest_alternating_signs(l):
    '''
    deter cea mai lunga subsecventa cu prorpietatea ca nr au semne alternante
    :param l: lista
    :return: subsecventa maxima
    '''
    subsMax = []

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if alternate_signs(l[i:j+1]) and len(l[i:j+1]) > len(subsMax):
                subsMax = l[i:j+1]

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


def nr_cif(x):
    '''
    determina numarul de cifre dintr un numar
    :param x:un nr -> float
    :return: nr de cifre
    '''
    p = 1
    while x != int(x):
        p = p*10
        x = x*10
    return p


def all_nr_cif(l):
    '''
    verifica daca partea fractionara = partea intreaga
    :param l: lista de float uri
    :return: true sau false
    '''
    for i in l:
        if int(i) != i*nr_cif(i) - int(i)*nr_cif(i):
            return False
    return True


def get_longest_equal_int_real(l):
    '''
    determina cea mai lunga subsecventa cu proprietatea ca nr au partea frationara = partea intreaga
    :param l:lista de float uri
    :return: cea mai lunga subsecventa cu proprietatea ca nr au partea frationara = partea intreaga
    '''
    subMax=[]
    for i in range(len(l)):
        for j in range(i,len(l)):
            if all_nr_cif(l[i:j+1]) and len(l[i:j+1]) > len(subMax):
                subMax=l[i:j+1]
    return subMax


def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([12.12, 13.13, 15.15, 12.45]) == [12.12, 13.13, 15.15]
    assert get_longest_equal_int_real([12,14,16]) == []


def main():
    l = []
    test_get_longest_prime_digits()
    test_get_longest_alternating_signs()
    test_get_longest_equal_int_real()
    while True:
        print("1.Citire date:")
        print("2.cea mai lunga subsecventa cu proprietatea ca nr au semne alternante")
        print("3.cea mai lunga subsecventa cu proprietatea ca nr au toate cifrele prime")
        print("4.cea mai lunga subsecventa cu proprietatea ca nr au partea frationara = partea intreaga")
        print("5.Iesire")
        option = input("dati nr:")

        if option == "1":
            l = citire_lista()

        elif option == "2":
            print(get_longest_alternating_signs(l))

        elif option == "3":
            print(get_longest_prime_digits(l))

        elif option == "4":
            print(get_longest_equal_int_real(l))

        elif option == "5":
            break

        else:
            print("optiune gresita")


if __name__ == '__main__':
    main()
