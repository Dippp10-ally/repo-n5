from src.collection_utils import is_empty_collection


def test_none_is_empty():
    assert is_empty_collection(None)


def test_empty_list_is_empty():
    assert is_empty_collection([])


def test_non_empty_is_not_empty():
    assert not is_empty_collection([1])
