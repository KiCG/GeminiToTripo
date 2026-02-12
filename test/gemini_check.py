from google import genai
import config

# クライアントの初期化
client = genai.Client(api_key=config.GEMINI_API_KEY)

print("--- あなたのAPIキーで利用可能なモデル一覧 ---")

try:
    # ページング設定をしてモデルリストを取得
    for m in client.models.list(config={'page_size': 100}):
        # テキスト生成(generateContent)に対応しているモデルだけを表示
        if 'generateContent' in m.supported_actions:
            # モデルIDを表示 (例: models/gemini-2.0-flash-exp)
            print(f"ID: {m.name}")
            
except Exception as e:
    print(f"エラーが発生しました: {e}")
