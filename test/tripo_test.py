import requests
import config

# config.py からキーを読み込む
API_KEY = config.TRIPO_API_KEY

print(f"--- Tripo API 接続テスト ---")
print(f"使用するキー: {API_KEY[:10]}... (先頭10文字)")

# 【変更】確実にGETが許可されている「残高確認」のURLに変更
url = "https://api.tripo3d.ai/v2/openapi/user/balance"

headers = {
    # Bearerの後に半角スペースがあるか確認してください
    "Authorization": f"Bearer {API_KEY}" 
}

try:
    response = requests.get(url, headers=headers)
    
    print(f"\nステータスコード: {response.status_code}")
    print(f"レスポンス内容: {response.text}")

    if response.status_code == 200:
        data = response.json()
        if data.get('code') == 0:
            balance = data.get('data', {}).get('balance')
            print(f"\n✅ 成功！認証OKです。")
            print(f"💰 現在の残高クレジット: {balance}")
        else:
            print(f"\n⚠️ 接続できましたが、API側でエラーが返されました。")
    elif response.status_code == 401:
        print("\n❌ 認証失敗 (401): キーが間違っています。config.pyを再確認してください。")
    else:
        print(f"\n❌ エラー: 想定外のステータスコードです。")

except Exception as e:
    print(f"通信エラー: {e}")
