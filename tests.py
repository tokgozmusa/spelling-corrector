from spell import correction

def test_correction():
    assert correction("umrella") == "umbrella"
    assert correction("morning") == "morning"
    assert correction("afteronon") == "afternoon"
