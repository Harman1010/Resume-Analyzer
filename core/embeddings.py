from sentence_transformers import SentenceTransformer

from config.settings import EMBEDDING_MODEL

embedding_model = SentenceTransformer(EMBEDDING_MODEL)