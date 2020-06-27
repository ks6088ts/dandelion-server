# デプロイ手順

```bash
# ツールのインストール
sudo apt install -y \
    emacs24 \
    make

# リポジトリの clone
git clone https://github.com/ks6088ts/dandelion-server.git

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
make createsuperuser POETRY_RUN="" # python コンテナ内で
```

# Tips

```bash
# 開発環境に設定変更する場合は下記ファイルを修正する
emacs docker-compose.yml
emacs config/settings.py
```

# 参考リンク

* [Let's Encrypt で Nginx にSSLを設定する](https://qiita.com/HeRo/items/f9eb8d8a08d4d5b63ee9)
* [nginx 公開ディレクトリの変更](https://qiita.com/ShinyaOkazawa/items/789db336f27f0d080152)
* [ReactとNginxでリロードしても404しないSPAを作る](https://qiita.com/inatatsu_csg/items/86586a9c808479260751)
* [Docs » Get Certbot » Running with Docker](https://certbot.eff.org/docs/install.html#running-with-docker)
* [複数のdocker-compose間で通信する](https://medium.com/anti-pattern-engineering/%E8%A4%87%E6%95%B0%E3%81%AEdocker-compose%E9%96%93%E3%81%A7%E9%80%9A%E4%BF%A1%E3%81%99%E3%82%8B-4de7c6bf8bf7)
