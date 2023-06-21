from strategi import branch_and_bound
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
start = datetime.now().second
objek_terpilih = branch_and_bound(data, "profit", "modal", 500)
end = datetime.now().second

print("running Time: {}".format(end-start))
print("\n")
print("Objek terpilih: ")
profit = 0
modal = 0
for i in objek_terpilih:
    print("ID: {} Modal: {} Profit: {}".format(
        i["id"], i["modal"], i["profit"]))
    profit += i["profit"]
    modal += i["modal"]


print("Profit: {}  Total Modal: {}\n".format(profit, modal))
