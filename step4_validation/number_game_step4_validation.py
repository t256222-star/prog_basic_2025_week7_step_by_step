import random

def read_int_in_range(prompt: str, lo: int, hi: int) -> int:
    while True:  # 条件が満たされるまで反復（桁和のwhile型, p35–38）
        s = input(prompt)
        try:
            n = int(s)
            if lo <= n <= hi:
                return n
            else:
                print("1〜100の整数を入力してください。")
        except ValueError:
            print("整数を入力してください。")

def main():
    answer = random.randint(1, 100)
    attempts = 0
    MAX_TRIES = 7
    print("1〜100の数を当ててください！")

    while attempts < MAX_TRIES:
        guess = read_int_in_range("予想した数: ", 1, 100)  # ← ここだけ差し替え
        attempts += 1

        if guess == answer:
            print("正解！")
            return
        elif guess < answer:
            print("もっと大きいです。")
        else:
            print("もっと小さいです。")

    print(f"残念！正解は {answer} でした。")

if __name__ == "__main__":
    main()
