def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            r = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            r = 0
            print("division by 0")
        except (ValueError, TypeError):
            r = 0
            print("wrong type")
        except IndexError:
            r = 0
            print("out of range")
            pass
        finally:
            new_list.append(r)

    return (new_list)
