import requests


class JokeFetcher:
    """ジョークを取得するための責務を持つクラス"""

    API_URL = "https://icanhazdadjoke.com/"
    HEADERS = {"Accept": "application/json"}

    def __init__(self, http_session):
        """
        コンストラクタでHTTPセッションを受け取る
        Args:
            http_session: requests.SessionのようなHTTPクライアントオブジェクト
        """
        self.session = http_session

    def fetch(self) -> str:
        """
        APIからランダムなジョークを1つ取得します。
        """
        try:
            response = self.session.get(
                self.API_URL, headers=self.HEADERS, timeout=5)
            response.raise_for_status()  # ステータスコードが200番台以外なら例外を発生

            joke_data = response.json()
            return joke_data.get("joke", "ジョークが見つかりませんでした。")

        except requests.exceptions.RequestException as e:
            return f"エラー: ジョークを取得できませんでした。 ({e})"


def main():
    """スクリプトのメイン処理"""
    print("ジョークを一つお届けします... 🤖")
    print("---------------------------------")

    # 本番実行時は、本物のrequests.Sessionを使う
    real_session = requests.Session()
    fetcher = JokeFetcher(http_session=real_session)
    joke = fetcher.fetch()

    print(joke)
    print("---------------------------------")


if __name__ == "__main__":
    main()
