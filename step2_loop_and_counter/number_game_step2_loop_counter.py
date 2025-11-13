def main():
    attempts = 0
    MAX_TRIES = 7
    while attempts < MAX_TRIES:     # ① 繰り返しの型（p39）
        attempts += 1             # ② 状態更新（合計の発想, p26–27）
        print("ダミー実行:", attempts)

if __name__ == "__main__":
     main()

