from db.queries.passage_types import get_passage_id_by_name
class Passage:
    type_id: int
    def __init__(self, type: str):
        self.type_id = get_passage_id_by_name(type)