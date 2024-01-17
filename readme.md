Dodawanie postów +
GET http://127.0.0.1:8000/post - Lista postów z is_moderated = True
	
POST http://127.0.0.1:8000/post - Dodaje post

GET http://127.0.0.1:8000/post/1 - Szczegóły postu o id 1
	
PUT http://127.0.0.1:8000/post/1 - Edytuje post o id 1

DELETE http://127.0.0.1:8000/post/1 - Usuwa post o id 1


Komentarze do wpisów +
PUT http://127.0.0.1:8000/post/1/comment - Dodaje komentarz

Tworzenie społeczności +
GET http://127.0.0.1:8000/community/ - Lista Community

POST http://127.0.0.1:8000/community/ - Dodaje Community

GET http://127.0.0.1:8000/community/1 - Szczegóły Community o id 1

PUT http://127.0.0.1:8000/community/1 - Edytuje Community o id 1

DELETE http://127.0.0.1:8000/community/1 - Usuwa Community o id 1


Obserwowanie użytkowników +
GET http://127.0.0.1:8000/user/1 - Szczegóły Użytkownika o id 1

PUT http://127.0.0.1:8000/user/1 - Edytuje Użytkownika o id 1

PUT http://127.0.0.1:8000/user/1/follow - Użytkownik "follower" dodaje się do listy obserwujących użytkoiwnika o id 1
	{
    "follower": 3
	}


Przysyłanie wiadomości +
GET http://127.0.0.1:8000/message/1 - Szczegóły Wiadomości o id 1

PUT http://127.0.0.1:8000/message/1 - Edytuje Wiadomość o id 1

DELETE http://127.0.0.1:8000/message/1 - Usuwa Wiadomość o id 1

POST http://127.0.0.1:8000/message/add - Dodaje wiadomość


Moderacja wpisów +
GET http://127.0.0.1:8000/post/moderation - Lista postów z is_moderated = False

PUT http://127.0.0.1:8000/post/moderation/1 - Zamienia wartość is_moderated na przeciwną w postcie o id 1


Powiadomienia +
GET http://127.0.0.1:8000/notification/ - Lista nieprzeczytanych powiadomień dla zalogowanego użytkownika

GET http://127.0.0.1:8000/notification/1 - Szczegóły powiadomienia o id 1

