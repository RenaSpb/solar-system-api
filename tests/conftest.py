import pytest
from app import create_app, db
from flask import Flask


@pytest.fixture
def app():
    app = create_app(test_config=True)

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()  # ✅ 清理数据库表，避免下次卡住

@pytest.fixture
def client(app):
    return app.test_client()
