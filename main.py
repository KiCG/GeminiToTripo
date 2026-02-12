from google import genai
import requests
import time
import os
import config 
import prompt

# --- 設定 ---
GEMINI_API_KEY = config.GEMINI_API_KEY
TRIPO_API_KEY = config.TRIPO_API_KEY

# APIのセットアップ
client = genai.Client(api_key=GEMINI_API_KEY)

# 【修正1】関数名を統一しました
def generate_monster(joy, calm, anger, sadness, fear):
    # 1. Geminiでプロンプトを生成
    formatted_prompt = prompt.base_prompt.format(
        joy=joy, calm=calm, anger=anger, sadness=sadness, fear=fear
    )
    
    print(f"--- Geminiに感情パラメータを送信中... ---")
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=formatted_prompt
        )
        tripo_prompt = response.text.strip()
        print(f"📝 生成されたプロンプト:\n>> {tripo_prompt}\n")
    except Exception as e:
        print(f"❌ Geminiエラー: {e}")
        return

    # 2. Tripo APIへタスク送信
    # 【修正2】Content-Typeを追加し、URLを v2 に変更
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TRIPO_API_KEY}"
    }
    payload = {
        "type": "text_to_model",
        "prompt": tripo_prompt
    }
    
    tripo_url = "https://api.tripo3d.ai/v2/openapi/task"
    
    try:
        req = requests.post(tripo_url, headers=headers, json=payload)
        req.raise_for_status() # エラーチェック
        task_id = req.json().get("data", {}).get("task_id")
    except Exception as e:
        print(f"❌ Tripoリクエストエラー: {e}")
        return

    if not task_id:
        print("Tripoタスクの作成に失敗しました。")
        return

    # 3. 生成完了のポーリング
    print(f"Tripoで3D生成中... (Task ID: {task_id})")
    
    while True:
        try:
            status_res = requests.get(f"{tripo_url}/{task_id}", headers=headers).json()
            status = status_res.get("data", {}).get("status")
            
            if status == "success":
                output = status_res["data"]["output"]
                result_url = output.get("model") or output.get("pbr_model")
                
                # 【修正3】存在しない変数 emotion_param を削除し、具体的なパラメータ名に変更
                # 拡張子も .glb に修正（中身がGLBのため）
                filename = f"monster_J{joy}_C{calm}_A{anger}_S{sadness}_Fe{fear}.glb"
                
                print("生成成功！ファイルをダウンロードします...")
                download_and_save(result_url, filename)
                break
            
            elif status == "failed":
                print("生成に失敗しました。")
                break
            
            elif status in ["running", "queued"]:
                print(".", end="", flush=True)
                time.sleep(5)
            else:
                print(f"Status: {status}")
                time.sleep(5)
                
        except Exception as e:
            print(f"ポーリングエラー: {e}")
            break

def download_and_save(url, filename):
    folder = "exported_models"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    filepath = os.path.join(folder, filename)
    response = requests.get(url)
    with open(filepath, "wb") as f:
        f.write(response.content)
    print(f"\n保存完了: {filepath}")

# --- 実行 ---
if __name__ == "__main__":
    print("=== Monster Fab Generator Test ===")
    print("各感情を 1〜5 の数値で入力してください")
    
    try:
        j = input("Joy (喜び): ") or "1"
        c = input("Calm (穏やか): ") or "1"
        a = input("Anger (怒り): ") or "1"
        s = input("Sadness (悲しみ): ") or "1"
        fe = input("Fear (恐怖): ") or "1"
        
        # 関数呼び出し
        generate_monster(j, c, a, s, fe)
        
    except KeyboardInterrupt:
        print("\n中止しました。")
