from lib.data.Passage import Passage

def test_passage():
    passage = Passage("Door")
    assert passage.type_id == 1