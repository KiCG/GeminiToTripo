# Emotional Monster Maker

**Emotional Monster Maker** は、ユーザーが入力した「感情パラメータ」に基づいて、AIがオリジナルの3Dモンスターを自動生成するPythonツールです。

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
git clone [https://github.com/KiCG/EmotionalMonsterMaker.git](https://github.com/KiCG/EmotionalMonsterMaker.git)
cd EmotionalMonsterFab
```

### 2. ライブラリのインストール
```bash
pip install -r requirements.txt
```

### 3. APIキーの設定
```python
# config.py
GEMINI_API_KEY = "ここにGeminiのAPIキー"
TRIPO_API_KEY = "ここにTripoのAPIキー"
```

### 使い方
以下のコマンドでプログラムが実行します
```bash
python src/main.py
```

### フォルダ構成
```text
EmotionalMonsterFab/
├── exported_models/      # 生成された3Dモデルの保存先
├── src/                  # ソースコード
│   ├── __init__.py
│   ├── main.py           # メイン実行ファイル
│   └── prompt.py         # プロンプト設定
├── config.py             # 設定ファイル (Git対象外)
├── requirements.txt      # 必要なライブラリ一覧
└── README.md             # 説明書
```
