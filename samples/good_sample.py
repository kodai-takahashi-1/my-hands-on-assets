from datetime import datetime
from zoneinfo import ZoneInfo

# --- 定数定義 ---
ADULT_AGE = 20


def process_user_data(user_name: str, user_age: int, department: str) -> str:
    """ユーザーデータを処理する関数.

    Args:
        user_name (str): ユーザー名
        user_age (int): ユーザーの年齢
        department (str): 部署名
    Returns:
        str: 処理結果の文字列
    """
    output_str = f"Name:{user_name}, Age:{user_age}, Dept:{department}"
    print(output_str)

    if user_age > ADULT_AGE and department != "sales":
        temp_val = user_age * 2
        print("Temporary value:", temp_val)

    today = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")
    print("Today's date is:", today)
    return output_str


process_user_data("Alice", 25, "HR")
