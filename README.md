・サーバー起動
python3 manage.py runserver

・マイグレーションの作成
python3 manage.py makemigrations モデル名

・マイグレーション実行
python3 manage.py migrate

・スーパーユーザー作成
python3 manage.py createsuperuser

・シェルの起動
python3 manage.py shell
  ・モデルのインポート
  from diaries.models import Diary
  ・全てのオブジェクトを取得
  Diary.objects.all()

・新しいアプリケーションの作成
python3 manage.py startapp blog