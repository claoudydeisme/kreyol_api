from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

LANG_CODE_MAP = {
    ("en", "ht"): ("eng_Latn", "hat_Latn"),
    ("ht", "en"): ("hat_Latn", "eng_Latn")
}


def neural_translate(text: str, source: str, target: str) -> str:
    src_code, tgt_code = LANG_CODE_MAP[(source, target)]

    tokenizer.src_lang = src_code
    encoded = tokenizer(text, return_tensors="pt", truncation=True)

    generated = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt_code),
        max_length=512
    )

    return tokenizer.batch_decode(generated, skip_special_tokens=True)[0]
