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


def value_ub(profit, modal_awal, total_modal, densitas):

    sisa_modal = modal_awal - total_modal
    pengali = sisa_modal * densitas
    return profit + pengali


def sorted_densitas(data, key, key2):
    data1 = data.copy()
    densitas_list = []
    for i in data1:
        i["densitas"] = i[key]/i[key2]
        densitas_list.append(i)

    return sorted(densitas_list, key=lambda x: x["densitas"], reverse=True)


def branch_and_bound(data, key1, key2, modal_awal):
    densitas_list = sorted_densitas(data, key1, key2)
    total_modal = 0
    profit = 0
    ub_awal = value_ub(profit, modal_awal, total_modal,
                       densitas_list[0]['densitas'])
    object_terpilih = []
    print("mulai iterasi")
    print("ub_awal: {}".format(ub_awal))
    print("profit: {}".format(profit))
    print("modal: {}".format(total_modal))
    print("\n")
    string = ["*"]*len(densitas_list)

    for i in range(len(densitas_list)-1):

        print(string)
        ub_1 = value_ub(densitas_list[i]["profit"]+profit, modal_awal,
                        densitas_list[i]["modal"]+total_modal, densitas_list[i+1]['densitas'])
        ub_0 = value_ub(profit, modal_awal, total_modal,
                        densitas_list[i+1]['densitas'])

        print("iterasi ke-{}".format(i+1))
        string[i] = "1"
        print(",".join(string))
        print(ub_1)
        print("P:{}, M:{}\n".format(
            densitas_list[i]["profit"]+profit, densitas_list[i]["modal"]+total_modal))
        string[i] = "*"

        string[i] = "0"
        print(",".join(string))
        print(ub_0)
        print("P:{}, M:{}\n".format(profit, total_modal))
        string[i] = "*"

        if ub_1 >= ub_0 and modal_awal >= total_modal+densitas_list[i]["modal"]:
            object_terpilih.append(densitas_list[i])
            string[i] = "1"
            profit += densitas_list[i]["profit"]
            total_modal += densitas_list[i]["modal"]
        else:
            string[i] = "0"

    print("iterasi terakhir")
    string[-1] = "1"
    print(",".join(string))
    print("P:{}, M:{}\n".format(
        densitas_list[-1]["profit"]+profit, densitas_list[-1]["modal"]+total_modal))
    string[-1] = "*"

    string[-1] = "0"
    print(",".join(string))
    print("P:{}, M:{}\n".format(
        profit, total_modal))
    string[-1] = "*"

    if modal_awal >= total_modal + densitas_list[-1]["modal"]:
        object_terpilih.append(densitas_list[-1])
        string[-1] = "1"
        profit += densitas_list[i]["profit"]
        total_modal += densitas_list[i]["modal"]
    else:
        string[-1] = "0"

    print(string)

    return object_terpilih
