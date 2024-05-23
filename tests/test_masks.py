from src.masks import account_mask, card_mask


def test_card_mask():
    assert card_mask("7000792289606361") == "7000 79** **** 6361"


def test_account_mask():
    assert account_mask("73654108430135874305") == "**4305"
