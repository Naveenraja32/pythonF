from faker import Faker
f = Faker()

for i in range(5):
    # print(f.name())
    # print(f.emoji())
    # print(f.language_name())
    print(f.random_int(1,100))