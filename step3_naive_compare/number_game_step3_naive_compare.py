import random

def main():
    answer = random.randint(1, 100)
    attempts = 0
    MAX_TRIES = 7
    print("1〜100の数を当ててください！")

    while attempts < MAX_TRIES:
        s = input("予想した数: ")       # まだ“安全化”しない
        guess = int(s)                   # 非整数はここで落ちる（後で直す）
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
