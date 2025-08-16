class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:  # 3歳以下は0円
            return 0
        elif self.age < 20:  # 順番を入れ替え
            return 1000
        elif self.age < 65:
            return 1500
        elif self.age >= 75:  # 75歳以上は500円
            return 500
        else:
            return 1200

    def to_csv(self):  # CSV形式
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    def to_tsv(self):  # タブ区切り
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    def to_pipe(self):  # パイプ区切り
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

# 以降で各問のコードを追加していく
# C-1フルネームを取得できる
print(ken.full_name())  # "Ken Tanaka"
print(tom.full_name())  # "Tom Ford"
print(ieyasu.full_name())  # "Ieyasu Tokugawa"

# C-2年齢という概念の追加
print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力

# C-3年齢に応じた適切な入場料を計算できる
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力

# C-4単一の顧客情報をCSV形式で取得できる
print(ken.to_csv())  # Ken Tanaka,15,1000
print(tom.to_csv())  # Tom Ford,57,1500
print(ieyasu.to_csv())  # Ieyasu Tokugawa,75,1200

# C-7単一顧客の情報取得形式の追加その1

print(ken.to_tsv())  # Ken Tanaka<TAB>15<TAB>1000
print(tom.to_tsv())  # Tom Ford<TAB>57<TAB>1500
print(ieyasu.to_tsv())  # Ieyasu Tokugawa<TAB>75<TAB>500
print(michelle.to_tsv())  # Michelle Tanner<TAB>3<TAB>0


print(ken.to_pipe())  # Ken Tanaka<pipe>15<pipe>1000
print(tom.to_pipe())  # Tom Ford<pipe>57<pipe>1500
print(ieyasu.to_pipe())  # Ieyasu Tokugawa<pipe>75<pipe>500
print(michelle.to_pipe())  # Michelle Tanner<pipe>3<pipe>0
