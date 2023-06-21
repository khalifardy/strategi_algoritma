
from strategi import greedy
from datetime import datetime


data = [
    {
        'id': 'vvip',
        'modal': 400,
        'profit': 1000
    },

    {
        'id': 'vip',
        'modal': 300,
        'profit': 750
    },

    {
        'id': '1',
        'modal': 150,
        'profit': 500
    },

    {
        'id': '2',
        'modal': 100,
        'profit': 300
    },

    {
        'id': '3',
        'modal': 50,
        'profit': 100
    }
]

modal_awal = 500

start = datetime.now().second
objek_terpilih = greedy("profit", data, modal_awal)
end = datetime.now().second

print(objek_terpilih)
print("running_time:{}".format(end-start))

profit = 0
modal = 0
print("Objek terpilih by Profit: ")
for i in objek_terpilih:

    print("ID: {} Modal: {} Profit: {}".format(
        i["id"], i["modal"], i["profit"]))
    profit += i["profit"]
    modal += i["modal"]

print("Total profit by Profit: {}  Total Modal: {}\n".format(profit, modal))

objek_terpilih = greedy("modal", data, modal_awal)
print("Objek terpilih by Modal: ")
profit = 0
modal = 0
for i in objek_terpilih:
    print("ID: {} Modal: {} Profit: {}".format(
        i["id"], i["modal"], i["profit"]))
    profit += i["profit"]
    modal += i["modal"]


print("Total profit by Modal Profit: {}  Total Modal: {}\n".format(profit, modal))


objek_terpilih = greedy("densitas", data, modal_awal)
print("Objek terpilih by Densitas: ")
profit = 0
modal = 0
for i in objek_terpilih:
    print("ID: {} Modal: {} Profit: {}".format(
        i["id"], i["modal"], i["profit"]))
    profit += i["profit"]
    modal += i["modal"]


print("Total profit by Densitas Profit: {}  Total Modal: {}\n".format(profit, modal))
