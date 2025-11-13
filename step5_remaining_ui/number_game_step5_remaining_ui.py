# number_game_step5_remaining_ui.py
# Step5: 残り回数を表示する数あてゲーム

import random


def read_int_in_range(prompt: str, lo: int, hi: int) -> int:
    """lo〜hi の整数だけを受け付ける入力関数"""
    while True:
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
    # 1〜100 の乱数を答えとして用意
    answer = random.randint(1, 100)

    # 試行回数のカウンタと上限
    attempts = 0
    MAX_TRIES = 7

    print("1〜100の数を当ててください！")

    # 最大 MAX_TRIES 回までチャレンジ
    while attempts < MAX_TRIES:
        # ★ Step5: 残り回数の表示（UI 強化）
        remaining = MAX_TRIES - attempts
        print(f"残り{remaining}回。")

        # 安全な入力（整数 & 範囲チェック）
        guess = read_int_in_range("予想した数: ", 1, 100)

        # 有効な入力を 1 回と数える
        attempts += 1

        # 答えとの比較とヒント
        if guess == answer:
            print("正解！")
            print(f"{attempts}回で当てました。")  # 任意の追加表示
            return
        elif guess < answer:
            print("もっと大きいです。")
        else:
            print("もっと小さいです。")

    # ここまで来たら 7 回ともハズレ
    print(f"残念！正解は {answer} でした。")


if __name__ == "__main__":
    main()
