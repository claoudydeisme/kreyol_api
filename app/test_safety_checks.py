from app.safety_checks import enforce_creole_grammar, Severity


def test_french_grammar_detection():
    text = "Li ale le lopital."
    issues = enforce_creole_grammar(text)
    assert any(i["severity"] == Severity.CRITICAL for i in issues)


def test_english_leak_detection():
    text = "Mwen is going lopital."
    issues = enforce_creole_grammar(text)
    assert any(i["code"] == "ENGLISH_VERB_LEAK" for i in issues)


def test_missing_tense_marker():
    text = "Mwen ale lopital."
    issues = enforce_creole_grammar(text)
    assert any(i["code"] == "MISSING_TENSE_MARKER" for i in issues)


def test_clean_sentence():
    text = "Mwen pral ale lopital demen."
    issues = enforce_creole_grammar(text)
    assert len(issues) == 0
