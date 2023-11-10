# Modules

- User
- Question
- MaterialData



# Mongo Schemes

```
User: {
    id: ID,
    tg_id: int64,
    points: int,
}

Question: {
    title: str,
    answers: [str],
    correct_answers: [str],
}

EcscursionPart: {
    title: str,
    audio: File,
    materials: [Files],
    is_test: bool,
    test: [Question],
}

Ecscursion: {
    id: ID,
    author: User,
    title: str,
    description: str,
    preview_img: File,
    nead_time: int,
    distance: int,
    route_url: str,
    parts: [EcscursionPart],
}

PassEcscursion: {
    user: User,
    ecscursion: Ecscursion,
    is_finished: bool,
    start_time: datetime,
    finish_time: datetime,
    correct_answers: int,
    points: int,
}

```