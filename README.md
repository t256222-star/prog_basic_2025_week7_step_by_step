# Week7 学習用サンプルコード集（prog_basic_2025_week7_sample_code）

このリポジトリは **数あてゲームを段階的に完成させるための学習用サンプル集** です。  
GitHub Classroom の提出用テンプレートとは異なるため、**提出には使用しないでください**。  
理解を深めるために順番に実行し、Step1〜Step5 の「差分」を体験してください。

---

## 📁 フォルダ構成

- `step1_skeleton`  
  - 骨組みだけ（`main()` だけ動く最小プログラム）
- `step2_loop_and_counter`  
  - ループとカウンタの導入（7回の繰り返しと `attempts += 1`）
- `step3_naive_compare`  
  - 比較ロジックを導入（まだ入力は安全でない）
- `step4_validation`  
  - 入力の安全化（例外処理と範囲チェック）
- `step5_remaining_ui`  
  - 残り回数の表示を追加したバージョン

課題の穴埋めファイル　assignment3_number_game_穴埋め.py
---

## 📘 使用方法

1. このフォルダを任意の場所にコピーする（例：`C:\work\prog_basic_2025_week7_sample_code`）。
2. ターミナル（または PowerShell）で、試したい Step のフォルダに移動する：
   ```bash
   cd step3_naive_compare
   python number_game_step3_naive_compare.py
