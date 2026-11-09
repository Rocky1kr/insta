# insta PJT
- 프로젝트 세팅
```
un init insta --bare --python 3.14
```

- 필요한 라이브러리 설치
```
uv add "fastapi[standard]" sqlalchemy "psycopg[binary]" alembic
```
- 데이터베이스 생성
```
psql -d postgres #macOS
psql -U postgres #Windows

CREATE DATABASE insta OWNER sd4;
\q

```
