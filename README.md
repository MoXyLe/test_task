## Запуск проекта

```sh
$ docker-compose up -d --build
```

Откройте [http://localhost/docs/](http://localhost/docs/) чтобы увидеть документацию по API.

## API методы

### GET /questions

Принимает опциональный параметр question_id и либо возваращет объект с указанным question_id, либо все объекты question, если question_id не указан.

Например: [http://localhost/questions?question_id=145](http://localhost/questions?question_id=145) или [http://localhost/questions](http://localhost/questions)

### POST /questions

Принимает параметр question_num и возвращает последний созданный объект question, после этого в фоновом режиме новые question добавляются в БД.

Например: [http://localhost/questions?question_num=3](http://localhost/questions?question_num=3)
