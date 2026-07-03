from sentence_transformers import SentenceTransformer

from keybert import KeyBERT
from config.settings import EMBEDDING_MODEL

embedding_model = SentenceTransformer(EMBEDDING_MODEL)

keybert_model = KeyBERT(model = embedding_model)