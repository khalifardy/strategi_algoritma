def max(data, key, sisa_modal):

    result = data[0]
    value = data[0][key]
    index = 0
    count = 0

    for i in data[1:]:
        count += 1

        if value <= i[key] and sisa_modal >= i["modal"]:
            result = i
            value = i[key]
            index = count

    return result, index


def max_densitas(data, key, key2, sisa_modal):
    result = data[0]
    rho = result[key]/result[key2]
    index = 0
    count = 0

    for i in data[1:]:
        count += 1
        rho2 = i[key]/i[key2]

        if rho <= rho2 and sisa_modal >= i["modal"]:
            rho = rho2
            result = i
            index = count

    return result, index


def min(data, key, sisa_modal):

    result = data[0]
    value = data[0][key]
    index = 0
    count = 0

    for i in data[1:]:
        count += 1

        if value >= i[key] and sisa_modal >= i["modal"]:
            result = i
            value = i[key]
            index = count

    return result, index


def cek_modal(data, sisa_modal):
    hasil = False
    for i in data:
        if i["modal"] <= sisa_modal:
            hasil = True
            break

    return hasil


def greedy(by, data, modal):
    objek_terpilih = []
    sisa_modal = modal
    data1 = data.copy()
    count = 0

    if by == 'profit':

        while len(data1) > 0:
            if sisa_modal >= data1[count]["modal"]:
                obj, idx = max(data1[count:], "profit", sisa_modal)
                objek_terpilih.append(obj)
                sisa_modal -= data1[idx]["modal"]
                del data1[idx]
                count = 0
            else:
                count += 1

            if not cek_modal(data1, sisa_modal):
                break

    elif by == "modal":
        while len(data1) > 0:
            if sisa_modal >= data1[count]["modal"]:
                obj, idx = min(data1[count:], "profit", sisa_modal)
                objek_terpilih.append(obj)
                sisa_modal -= data1[idx]["modal"]
                del data1[idx]
                count = 0
            else:
                count += 1

            if not cek_modal(data1, sisa_modal):
                break

    elif by == "densitas":
        while len(data1) > 0:
            if sisa_modal >= data1[count]["modal"]:
                obj, idx = max_densitas(
                    data1[count:], "profit", "modal", sisa_modal)
                objek_terpilih.append(obj)
                sisa_modal -= data1[idx]["modal"]
                del data1[idx]
                count = 0
            else:
                count += 1

            if not cek_modal(data1, sisa_modal):
                break

    return objek_terpilih
