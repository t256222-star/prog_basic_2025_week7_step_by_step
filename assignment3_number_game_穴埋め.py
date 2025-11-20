# assignment3_number_game.py
# 課題3：数あてゲーム

import random

# 最大試行回数
MAX_TRIES = 7


def ask_int(prompt: str) -> int:
    """整数を入力させる。失敗時は再入力を求める関数

    TODO1: 文字列 s を整数に変換して n として返すように完成させよう。
           変換に失敗したときは ValueError が発生するので、except で
           「整数を入力してください。」とメッセージを出して再入力する。
    """
    while True:
        s = input(prompt)
        try:
            # TODO1-1: 文字列 s を整数に変換して n に代入する
            # ヒント: n = int(s)
            n = ...  # ← ここを書き換える

            # TODO1-2: 正しく変換できたら n を返す
            return n
        except ValueError:
            # TODO1-3: 整数に変換できなかったときのメッセージ
            # ヒント: 「整数を入力してください。」と表示する
            print("整数を入力してください。")


def play() -> None:
    """数あてゲーム本体

    TODO2〜6: 乱数で正解を作り、最大7回まで当てるゲームを完成させる。
    """

    # TODO2: 正解の数を 1〜100 の乱数で決めよう
    # ヒント: random.randint(1, 100) を使う
    answer = ...  # ← ここを書き換える

    # 試行回数カウンタ
    tries = 0

    print("1〜100の数を当ててください！")

    # TODO3: 最大 MAX_TRIES 回まで繰り返す while ループを書こう
    while tries < MAX_TRIES:
        # TODO3-1: ユーザから予想した数を整数として受け取る
        # ヒント: ask_int("予想した数: ") を使う
        guess = ...  # ← ここを書き換える

        # TODO3-2: 有効な入力が1回行われたので tries を1増やす
        # ヒント: tries += 1
        tries = ...  # ← ここを書き換える

        # TODO4: guess と answer を比較してメッセージを出す
        #  - 等しいとき  : 「正解！」＋回数を表示してゲーム終了
        #  - 小さすぎるとき: 「もっと大きいです。」と表示
        #  - 大きすぎるとき: 「もっと小さいです。」と表示

        if ...:  # TODO4-1: 正解だったときの条件（例: guess == answer）
            print(f"正解！{tries}回で当たりました！")
            return
        elif ...:  # TODO4-2: 小さすぎるときの条件（例: guess < answer）
            print("もっと大きいです。")
        else:      # TODO4-3: 上の2つ以外（大きすぎる）のとき
            print("もっと小さいです。")

    # TODO5: ここまで来たら 7 回すべて外れたことになるので、
    #        「残念！正解は ○○ でした。」というメッセージを出そう。
    # ヒント: 「残念」と正解の数字 answer の両方を含める
    print(f"残念！正解は {answer} でした。")  # ← ここはそのまま使ってよい


def main() -> None:
    """main 関数（テストや直接実行から呼び出される入口）"""
    play()


if __name__ == "__main__":
    main()
