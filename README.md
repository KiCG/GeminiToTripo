# Emotional Monster Fab

**Emotional Monster Fab** は、ユーザーが入力した「感情パラメータ」に基づいて、AIがオリジナルの3Dモンスターを自動生成するPythonツールです。

「喜び」「穏やかさ」「怒り」「悲しみ」「恐怖」の5つの感情数値を入力すると、Google Gemini がその感情を視覚的な特徴（形状、色、テクスチャ）に変換し、Tripo AI がそれを3Dモデル（.glb）として具現化します。

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Gemini API](https://img.shields.io/badge/AI-Google%20Gemini-orange.svg)
![Tripo API](https://img.shields.io/badge/AI-Tripo3D-purple.svg)

## 🚀 機能

- **感情パラメータ入力**: 5つの感情（Joy, Calm, Anger, Sadness, Fear）を1〜5のスケールで指定可能。
- **動的プロンプト生成**: Google Gemini 2.0 Flash (または 1.5) を使用し、感情の組み合わせから最適な3D生成用プロンプトを作成。
- **Text-to-3D 生成**: Tripo API を使用し、プロンプトから高速に3Dモデルを生成。
- **自動ダウンロード**: 生成されたモデル（.glb形式）を自動でローカルフォルダに保存。

## 📦 必要要件

- Python 3.8 以上
- Google Cloud (Gemini) API Key
- Tripo AI API Key

## 🛠 インストールとセットアップ

### 1. リポジトリのクローン
```bash
git clone [https://github.com/あなたのユーザー名/EmotionalMonsterFab.git](https://github.com/あなたのユーザー名/EmotionalMonsterFab.git)
cd EmotionalMonsterFab
```

### ライブラリのインストール
```bash
pip install -r requirements.txt
```

### フォルダ構成
EmotionalMonsterFab/          # プロジェクトのルートディレクトリ
│
├── output/                   # 【新規】生成された3Dモデルの保存先
│   └── .gitkeep              # 空フォルダをGitに維持するためのファイル
│
├── src/                      # 【新規】ソースコードをまとめる場所
│   ├── __init__.py           # (空でOK) Pythonパッケージとして扱う印
│   ├── main.py               # メイン実行ファイル
│   ├── prompt.py             # プロンプト管理
│   └── utils.py              # (将来用) 便利な関数など
│
├── config.py                 # APIキー設定 (Gitには上げない)
├── config.example.py         # 設定のひな形 (Gitに上げる)
│
├── .gitignore                # Git除外設定
├── .gitattributes            # Git属性設定
├── requirements.txt          # 【新規】必要なライブラリ一覧
└── README.md                 # 説明書
