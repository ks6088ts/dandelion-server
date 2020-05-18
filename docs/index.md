# デプロイ手順

```bash
# ツールのインストール
sudo apt install -y \
    emacs24 \
    make

# Docker イメージのビルド
docker-compose build
docker network create shared-network

# 証明書取得
docker-compose run --rm -p 80:80 certbot

# コンテナ起動
docker-compose up -d mysql
docker-compose up -d python
docker-compose up -d nginx

# 確認
docker-compose ps # 問題があれば -d 抜きで up して調査

# スーパユーザ作成
make docker-exec SERVICE=python
make createsuperuser # python コンテナ内で
```

# Tips

```bash
# 開発環境に設定変更する場合は下記ファイルを修正する
emacs docker-compose.yml
emacs config/settings.py
```
